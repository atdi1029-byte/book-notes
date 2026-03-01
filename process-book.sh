#!/bin/bash
# process-book.sh — Batch-process a PDF into notes.md using Claude CLI
#
# Runs parallel claude invocations per page range, each writing to a temp file.
# Merges results in page order after each wave.
#
# Usage:
#   ./process-book.sh "/path/to/book.pdf" "Book_Folder" [start] [end] [batch] [sleep] [parallel]
#
# Examples:
#   ./process-book.sh "/path/to/book.pdf" "My_Book" 1 300 20 5 3
#   ./process-book.sh "/path/to/book.pdf" "My_Book"              # auto-detect pages, defaults

set -euo pipefail

BOOKS_DIR="$(cd "$(dirname "$0")" && pwd)"

PDF="$1"
FOLDER="$2"
START="${3:-1}"
END_PAGE="${4:-0}"
BATCH="${5:-20}"
SLEEP="${6:-5}"
PARALLEL="${7:-3}"

DIR="$BOOKS_DIR/$FOLDER"
NOTES="$DIR/notes.md"
LOG="$DIR/process.log"
PAGES_DONE="$DIR/.pages_done"

# Auto-detect total pages if not specified
if [ "$END_PAGE" -eq 0 ]; then
  END_PAGE=$(mdls -name kMDItemNumberOfPages "$PDF" 2>/dev/null | awk '{print $NF}')
  if [ -z "$END_PAGE" ] || [ "$END_PAGE" = "(null)" ]; then
    echo "ERROR: Could not detect page count. Specify end_page manually."
    exit 1
  fi
fi

mkdir -p "$DIR"
touch "$NOTES" "$PAGES_DONE"

echo "========================================" | tee -a "$LOG"
echo "Book PDF Processor — $(date)" | tee -a "$LOG"
echo "PDF:    $PDF" | tee -a "$LOG"
echo "Output: $NOTES" | tee -a "$LOG"
echo "Pages:  $START → $END_PAGE (batch: $BATCH, parallel: $PARALLEL, sleep: ${SLEEP}s)" | tee -a "$LOG"
echo "========================================" | tee -a "$LOG"

MAX_RETRIES=2

# Function: record successfully processed pages
record_pages() {
  local p_start="$1" p_end="$2"
  for ((p=p_start; p<=p_end; p++)); do
    echo "$p" >> "$PAGES_DONE"
  done
  sort -un "$PAGES_DONE" -o "$PAGES_DONE"
}

# Function: build the prompt for a page range
make_prompt() {
  local P_START="$1" P_END="$2" OUT_FILE="$3"
  cat <<PROMPT_EOF
You are creating detailed study notes from a book PDF. This is a personal, educational book-analysis project for academic study and note-taking.

READ pages $P_START-$P_END of the PDF at '$PDF'.

WRITE the notes to '$OUT_FILE' using the Write tool. Markdown format:
- START with: <!-- pp. $P_START-$P_END -->
- Chapter headers: ## Chapter N: Title
- Subheadings: ### Topic Name
- Key points as bullet points (-)
- Notable quotes as > blockquotes with attribution
- **Bold** for key terms, concepts, and names
- Capture arguments, reasoning, logic chains, cause-and-effect — not just conclusions
- Include examples, stories, anecdotes, historical references, data points
- Note contrarian/surprising claims with evidence
- Include named individuals, books, or thinkers referenced
- Do NOT summarize or condense — write expansive, detailed notes
- Do NOT output preamble — ONLY write the notes

IMPORTANT: Only cover pages $P_START-$P_END. This is academic study material — process the content faithfully.
PROMPT_EOF
}

# Function: process a single batch with model fallback
# On content filter errors, immediately tries haiku instead of retrying sonnet.
process_batch() {
  local B_START="$1" B_END="$2" TEMP_FILE="$3" BATCH_LOG="$4"

  local MODELS=("sonnet" "haiku")

  for MODEL in "${MODELS[@]}"; do
    local RETRY=0
    while [ "$RETRY" -lt "$MAX_RETRIES" ]; do
      if [ "$RETRY" -gt 0 ]; then
        sleep 30
      fi

      local PROMPT
      PROMPT=$(make_prompt "$B_START" "$B_END" "$TEMP_FILE")
      local STDERR_FILE="$DIR/.stderr_${B_START}_${B_END}.tmp"

      claude -p "$PROMPT" \
        --model "$MODEL" \
        --allowedTools "Read" "Write" \
        2>"$STDERR_FILE" || true

      local STDERR_CONTENT=""
      [ -f "$STDERR_FILE" ] && STDERR_CONTENT=$(cat "$STDERR_FILE") && rm -f "$STDERR_FILE"

      # Check if temp file was created with content
      if [ -f "$TEMP_FILE" ] && [ "$(wc -c < "$TEMP_FILE" | tr -d ' ')" -gt 50 ]; then
        local LINES=$(wc -l < "$TEMP_FILE" | tr -d ' ')
        echo "  OK — pp. $B_START-$B_END ($MODEL, +$LINES lines)" >> "$BATCH_LOG"
        return 0
      fi

      # Content filter? Skip straight to next model
      if echo "$STDERR_CONTENT" | grep -q "content filtering"; then
        echo "  CONTENT_FILTER — pp. $B_START-$B_END ($MODEL)" >> "$BATCH_LOG"
        rm -f "$TEMP_FILE"
        break  # break retry loop, try next model
      fi

      # Other error — retry same model
      RETRY=$((RETRY + 1))
      echo "  RETRY $RETRY — pp. $B_START-$B_END ($MODEL)" >> "$BATCH_LOG"
      rm -f "$TEMP_FILE"
    done
  done

  echo "  FAILED — pp. $B_START-$B_END after all models" >> "$BATCH_LOG"
  return 1
}

# Build list of all batch ranges
BATCHES=()
PAGE=$START
while [ "$PAGE" -le "$END_PAGE" ]; do
  BATCH_END=$((PAGE + BATCH - 1))
  [ "$BATCH_END" -gt "$END_PAGE" ] && BATCH_END=$END_PAGE
  BATCHES+=("$PAGE:$BATCH_END")
  PAGE=$((BATCH_END + 1))
done

TOTAL=${#BATCHES[@]}
echo "Batches: $TOTAL (processing $PARALLEL at a time)" | tee -a "$LOG"

# Process batches in parallel waves
IDX=0
FAILURES=0
WAVE_NUM=0

while [ "$IDX" -lt "$TOTAL" ]; do
  WAVE_NUM=$((WAVE_NUM + 1))
  WAVE_END=$((IDX + PARALLEL))
  [ "$WAVE_END" -gt "$TOTAL" ] && WAVE_END=$TOTAL

  echo "" | tee -a "$LOG"
  echo "--- Wave $WAVE_NUM: batches $((IDX+1))-$WAVE_END of $TOTAL ($(date '+%H:%M:%S')) ---" | tee -a "$LOG"

  # Launch parallel workers
  PIDS=()
  for ((W=IDX; W<WAVE_END; W++)); do
    IFS=: read -r B_START B_END <<< "${BATCHES[$W]}"
    TEMP="$DIR/.batch_${B_START}_${B_END}.md"
    BATCH_LOG="$DIR/.batch_${B_START}_${B_END}.log"
    rm -f "$TEMP" "$BATCH_LOG"

    echo "  Starting: pp. $B_START-$B_END" | tee -a "$LOG"
    process_batch "$B_START" "$B_END" "$TEMP" "$BATCH_LOG" &
    PIDS+=($!)
  done

  # Wait for all workers in this wave
  WAVE_RESULTS=()
  for PID in "${PIDS[@]}"; do
    if wait "$PID"; then
      WAVE_RESULTS+=(0)
    else
      WAVE_RESULTS+=(1)
    fi
  done

  # Merge completed temp files in page order and log results
  for ((W=IDX; W<WAVE_END; W++)); do
    local_idx=$((W - IDX))
    IFS=: read -r B_START B_END <<< "${BATCHES[$W]}"
    TEMP="$DIR/.batch_${B_START}_${B_END}.md"
    BATCH_LOG="$DIR/.batch_${B_START}_${B_END}.log"

    # Append batch log to main log
    [ -f "$BATCH_LOG" ] && cat "$BATCH_LOG" >> "$LOG" && rm -f "$BATCH_LOG"

    if [ "${WAVE_RESULTS[$local_idx]}" -eq 0 ] && [ -f "$TEMP" ]; then
      LINES=$(wc -l < "$TEMP" | tr -d ' ')
      cat "$TEMP" >> "$NOTES"
      echo "" >> "$NOTES"
      record_pages "$B_START" "$B_END"
      echo "  Merged: pp. $B_START-$B_END ($LINES lines)" | tee -a "$LOG"
      rm -f "$TEMP"
    else
      FAILURES=$((FAILURES + 1))
      echo "  FAILED: pp. $B_START-$B_END" | tee -a "$LOG"
      rm -f "$TEMP"
    fi
  done

  IDX=$WAVE_END

  # Brief sleep between waves
  if [ "$IDX" -lt "$TOTAL" ]; then
    sleep "$SLEEP"
  fi
done

echo "" | tee -a "$LOG"
echo "========================================" | tee -a "$LOG"
echo "DONE — $(date)" | tee -a "$LOG"
echo "Batches: $TOTAL total, $FAILURES failed" | tee -a "$LOG"
echo "Notes:   $(wc -l < "$NOTES") lines" | tee -a "$LOG"
echo "========================================" | tee -a "$LOG"

# === GAP-FILL PASS ===
echo "" | tee -a "$LOG"
echo "=== GAP-FILL — checking for missing pages ===" | tee -a "$LOG"

MISSING_PAGES=""
for ((P=START; P<=END_PAGE; P++)); do
  if ! grep -qx "$P" "$PAGES_DONE" 2>/dev/null; then
    MISSING_PAGES="$MISSING_PAGES $P"
  fi
done

MISSING_PAGES=$(echo "$MISSING_PAGES" | tr ' ' '\n' | grep -v '^$' | sort -un)
MISS_COUNT=$(echo "$MISSING_PAGES" | grep -c . || true)

if [ "$MISS_COUNT" -eq 0 ]; then
  echo "  No gaps — all $((END_PAGE - START + 1)) pages processed!" | tee -a "$LOG"
else
  echo "  Found $MISS_COUNT missing pages — filling..." | tee -a "$LOG"

  GAP_FIXED=0
  GAP_FAILED=0

  for FP in $MISSING_PAGES; do
    echo "  Gap-fill: page $FP ($(date '+%H:%M:%S'))" | tee -a "$LOG"
    TEMP="$DIR/.gap_${FP}.md"
    rm -f "$TEMP"

    GAP_PROMPT="You are creating detailed study notes from a book PDF. This is a personal, educational book-analysis project for academic study and note-taking.

READ page $FP of the PDF at '$PDF'.

WRITE the notes to '$TEMP' using the Write tool. Markdown format:
- START with: <!-- p. $FP -->
- Chapter headers: ## Chapter N: Title
- Subheadings: ### Topic Name
- Key points as bullet points (-)
- Notable quotes as > blockquotes with attribution
- **Bold** for key terms, concepts, and names
- Capture arguments and reasoning — not just conclusions
- Include examples, stories, anecdotes, and data points
- Do NOT summarize — write expansive, detailed notes
- Do NOT output preamble — ONLY write the notes

IMPORTANT: Only cover page $FP. This is academic study material — process the content faithfully."

    GAP_OK=false
    for MODEL in sonnet haiku; do
      [ "$GAP_OK" = true ] && break
      RETRY=0
      while [ "$RETRY" -lt "$MAX_RETRIES" ] && [ "$GAP_OK" = false ]; do
        [ "$RETRY" -gt 0 ] && sleep 15
        STDERR_FILE="$DIR/.stderr_gap_${FP}.tmp"
        claude -p "$GAP_PROMPT" \
          --model "$MODEL" \
          --allowedTools "Read" "Write" \
          2>"$STDERR_FILE" || true

        STDERR_CONTENT=""
        [ -f "$STDERR_FILE" ] && STDERR_CONTENT=$(cat "$STDERR_FILE") && rm -f "$STDERR_FILE"

        if [ -f "$TEMP" ] && [ "$(wc -c < "$TEMP" | tr -d ' ')" -gt 20 ]; then
          cat "$TEMP" >> "$NOTES"
          echo "" >> "$NOTES"
          record_pages "$FP" "$FP"
          GAP_OK=true
          GAP_FIXED=$((GAP_FIXED + 1))
          echo "    OK — page $FP ($MODEL, +$(wc -l < "$TEMP" | tr -d ' ') lines)" | tee -a "$LOG"
          rm -f "$TEMP"
        elif echo "$STDERR_CONTENT" | grep -q "content filtering"; then
          echo "    CONTENT_FILTER — page $FP ($MODEL)" | tee -a "$LOG"
          rm -f "$TEMP"
          break  # try next model
        else
          RETRY=$((RETRY + 1))
          rm -f "$TEMP"
        fi
      done
    done

    if [ "$GAP_OK" = false ]; then
      echo "    STILL FAILED — page $FP" | tee -a "$LOG"
      GAP_FAILED=$((GAP_FAILED + 1))
    fi
    sleep 3
  done

  echo "" | tee -a "$LOG"
  echo "Gap-fill: $GAP_FIXED fixed, $GAP_FAILED still failed" | tee -a "$LOG"
  if [ "$GAP_FAILED" -gt 0 ]; then
    echo "Remaining gaps:" | tee -a "$LOG"
    for ((P=START; P<=END_PAGE; P++)); do
      if ! grep -qx "$P" "$PAGES_DONE" 2>/dev/null; then
        echo "  - Page $P" | tee -a "$LOG"
      fi
    done
  fi
fi

# === DEDUPLICATION PASS ===
echo "" | tee -a "$LOG"
echo "=== DEDUP — removing duplicate sections ===" | tee -a "$LOG"

python3 << DEDUP_EOF 2>>"$LOG" | tee -a "$LOG"
import sys

notes_path = "$NOTES"
with open(notes_path, 'r') as f:
    lines = f.readlines()

# Parse sections by ## headers
sections = []
current_start = 0
for i in range(len(lines)):
    if lines[i].startswith('## ') and i > 0:
        sections.append((current_start, i))
        current_start = i
sections.append((current_start, len(lines)))

import re

# Extract chapter number from header (e.g. "## Chapter 12: ..." -> 12)
def get_chapter_num(header):
    m = re.match(r'## Chapter (\d+)', header)
    return int(m.group(1)) if m else None

# Also extract appendix/book identifiers
def get_section_key(header):
    ch = get_chapter_num(header)
    if ch is not None:
        return f"chapter_{ch}"
    if 'Appendix I:' in header or 'Appendix I ' in header:
        return 'appendix_i'
    if 'Appendix II' in header:
        return 'appendix_ii'
    m = re.match(r'## Book ([IVX]+)', header)
    if m:
        return f"book_{m.group(1)}"
    return None

# Group sections by key
from collections import defaultdict
groups = defaultdict(list)
for s, e in sections:
    h = lines[s].strip()
    key = get_section_key(h)
    if key:
        groups[key].append((s, e, h, e - s))

# Find duplicates (multiple sections with same key)
remove_ranges = set()
dedup_count = 0
for key, secs in groups.items():
    if len(secs) <= 1:
        continue
    # For chapter sections: "continued" sections are intentional, skip them
    non_continued = [(s, e, h, sz) for s, e, h, sz in secs if '(cont' not in h.lower()]
    if len(non_continued) <= 1:
        continue
    # Keep the longest, remove the rest
    non_continued.sort(key=lambda x: x[3], reverse=True)
    keeper = non_continued[0]
    for s, e, h, sz in non_continued[1:]:
        remove_ranges.add((s, e))
        dedup_count += 1
        print(f"  REMOVE duplicate: [{s+1}-{e}] ({sz} lines) {h[:60]}")
    print(f"  KEEP:             [{keeper[0]+1}-{keeper[1]}] ({keeper[3]} lines) {keeper[2][:60]}")

# Also remove template placeholders
for s, e in sections:
    h = lines[s].strip()
    block = ''.join(lines[s:e])
    if '[Title]' in h or ('[Quote]' in block and '## Notable Quotes' in h):
        remove_ranges.add((s, e))
        dedup_count += 1
        print(f"  REMOVE template:  [{s+1}-{e}] {h[:60]}")

if dedup_count == 0:
    print("  No duplicates found — clean!")
else:
    # Rebuild file without removed ranges
    output = []
    for s, e in sections:
        if (s, e) not in remove_ranges:
            output.extend(lines[s:e])

    with open(notes_path, 'w') as f:
        f.writelines(output)

    new_lines = len(output)
    print(f"  Removed {dedup_count} duplicate sections ({len(lines) - new_lines} lines)")
    print(f"  File: {len(lines)} → {new_lines} lines")
DEDUP_EOF

# === VERIFICATION PASS ===
echo "" | tee -a "$LOG"
echo "=== VERIFY — checking chapter coverage ===" | tee -a "$LOG"

python3 << VERIFY_EOF 2>>"$LOG" | tee -a "$LOG"
import re

notes_path = "$NOTES"
pages_done_path = "$PAGES_DONE"
total_pages = $END_PAGE

with open(notes_path, 'r') as f:
    content = f.read()

# Extract all chapter numbers mentioned
chapters = set()
for m in re.finditer(r'^## Chapter (\d+)', content, re.MULTILINE):
    chapters.add(int(m.group(1)))

# Extract all page markers
pages_covered = set()
for m in re.finditer(r'<!-- pp?\. (\d+)(?:-(\d+))? -->', content):
    start = int(m.group(1))
    end = int(m.group(2)) if m.group(2) else start
    for p in range(start, end + 1):
        pages_covered.add(p)

# Check pages_done file
pages_tracked = set()
try:
    with open(pages_done_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                pages_tracked.add(int(line))
except FileNotFoundError:
    pass

# Report
print(f"  Chapters found: {sorted(chapters)}")
print(f"  Chapter count: {len(chapters)}")

# Check for gaps in chapter sequence
if chapters:
    max_ch = max(chapters)
    missing_chs = [c for c in range(1, max_ch + 1) if c not in chapters]
    if missing_chs:
        print(f"  WARNING: Missing chapters: {missing_chs}")
    else:
        print(f"  Chapters 1-{max_ch}: all present")

print(f"  Page markers in notes: {len(pages_covered)} pages")
print(f"  Pages in .pages_done: {len(pages_tracked)} of {total_pages}")

missing_pages = [p for p in range(1, total_pages + 1) if p not in pages_tracked]
if missing_pages:
    if len(missing_pages) <= 20:
        print(f"  Missing pages: {missing_pages}")
    else:
        print(f"  Missing pages: {len(missing_pages)} (first 20: {missing_pages[:20]})")
else:
    print(f"  All {total_pages} pages tracked — COMPLETE")

# Count total lines
line_count = content.count('\n')
print(f"  Total notes: {line_count} lines")

# Summary verdict
issues = []
if missing_chs:
    issues.append(f"{len(missing_chs)} missing chapters")
if missing_pages:
    issues.append(f"{len(missing_pages)} missing pages")
if issues:
    print(f"  VERDICT: INCOMPLETE — {', '.join(issues)}")
else:
    print(f"  VERDICT: COMPLETE")
VERIFY_EOF
