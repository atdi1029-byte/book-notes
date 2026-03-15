#!/bin/bash
# verify-book.sh — Verify book notes have no gaps, and optionally fill them
#
# Checks .pages_done tracking file and scans notes.md for page markers.
# Reports any missing pages and can auto-rerun them.
#
# Usage:
#   ./verify-book.sh "Book_Folder" [start_page] [end_page]           # Report only
#   ./verify-book.sh "Book_Folder" [start_page] [end_page] --fix     # Report + fill gaps
#   ./verify-book.sh "Book_Folder" [start_page] [end_page] --fix "/path/to/book.pdf"
#
# Examples:
#   ./verify-book.sh "Antifragile" 1 650
#   ./verify-book.sh "Asset_Allocation" 16 320 --fix "/Users/alexbarnett/Desktop/Books/Asset Allocation.pdf"

set -euo pipefail

BOOKS_DIR="$(cd "$(dirname "$0")" && pwd)"

FOLDER="$1"
START="${2:-1}"
END_PAGE="${3:-0}"
FIX_MODE="${4:---report}"
PDF="${5:-}"

DIR="$BOOKS_DIR/$FOLDER"
NOTES="$DIR/notes.md"
LOG="$DIR/process.log"
PAGES_DONE="$DIR/.pages_done"

if [ ! -f "$NOTES" ]; then
  echo "ERROR: $NOTES not found"
  exit 1
fi

echo "========================================"
echo "Book Verification — $FOLDER"
echo "Expected range: pages $START–$END_PAGE"
echo "========================================"
echo ""

# === CHECK 1: .pages_done tracking file ===
echo "--- Check 1: Pages Done Tracking File ---"
if [ -f "$PAGES_DONE" ]; then
  DONE_COUNT=$(wc -l < "$PAGES_DONE" | tr -d ' ')
  EXPECTED=$((END_PAGE - START + 1))
  echo "  Tracked: $DONE_COUNT / $EXPECTED pages"

  MISSING_TRACKED=""
  for ((P=START; P<=END_PAGE; P++)); do
    if ! grep -qx "$P" "$PAGES_DONE" 2>/dev/null; then
      MISSING_TRACKED="$MISSING_TRACKED $P"
    fi
  done

  if [ -z "$MISSING_TRACKED" ]; then
    echo "  Status: ALL PAGES TRACKED"
  else
    MISS_T_COUNT=$(echo "$MISSING_TRACKED" | wc -w | tr -d ' ')
    echo "  Status: $MISS_T_COUNT PAGES MISSING"
    # Group consecutive pages into ranges for readability
    echo "  Missing pages:"
    echo "$MISSING_TRACKED" | tr ' ' '\n' | grep -v '^$' | awk '
      NR==1 { start=$1; prev=$1; next }
      $1 != prev+1 { if (start==prev) printf "    - Page %d\n", start; else printf "    - Pages %d-%d\n", start, prev; start=$1 }
      { prev=$1 }
      END { if (start==prev) printf "    - Page %d\n", start; else printf "    - Pages %d-%d\n", start, prev }
    '
  fi
else
  echo "  No .pages_done file found (older run without tracking)"
  MISSING_TRACKED="all"
fi

echo ""

# === CHECK 2: Page markers in notes.md ===
echo "--- Check 2: Page Markers in Notes ---"
# Look for <!-- pp. X-Y --> and <!-- p. X --> markers
MARKERS=$(grep -oP '<!-- pp?\. \K[0-9]+(-[0-9]+)?' "$NOTES" 2>/dev/null || true)

if [ -z "$MARKERS" ]; then
  echo "  No page markers found in notes.md (older format without markers)"
else
  # Expand ranges and collect all marked pages
  MARKED_PAGES=""
  while IFS= read -r M; do
    if echo "$M" | grep -q '-'; then
      M_START=$(echo "$M" | cut -d- -f1)
      M_END=$(echo "$M" | cut -d- -f2)
      for ((MP=M_START; MP<=M_END; MP++)); do
        MARKED_PAGES="$MARKED_PAGES $MP"
      done
    else
      MARKED_PAGES="$MARKED_PAGES $M"
    fi
  done <<< "$MARKERS"

  MARKED_SORTED=$(echo "$MARKED_PAGES" | tr ' ' '\n' | grep -v '^$' | sort -un)
  MARK_COUNT=$(echo "$MARKED_SORTED" | wc -l | tr -d ' ')
  EXPECTED=$((END_PAGE - START + 1))
  echo "  Found markers for $MARK_COUNT unique pages"

  MISSING_MARKED=""
  for ((P=START; P<=END_PAGE; P++)); do
    if ! echo "$MARKED_SORTED" | grep -qx "$P"; then
      MISSING_MARKED="$MISSING_MARKED $P"
    fi
  done

  if [ -z "$MISSING_MARKED" ]; then
    echo "  Status: ALL PAGES HAVE MARKERS"
  else
    MISS_M_COUNT=$(echo "$MISSING_MARKED" | wc -w | tr -d ' ')
    echo "  Status: $MISS_M_COUNT PAGES WITHOUT MARKERS"
  fi
fi

echo ""

# === CHECK 3: Chapter coverage ===
echo "--- Check 3: Chapter Coverage ---"
CHAPTERS=$(grep -c '^## Chapter' "$NOTES" 2>/dev/null || true)
INTRO=$(grep -c '^## Introduction' "$NOTES" 2>/dev/null || true)
CONCLUSION=$(grep -c '^## Conclusion' "$NOTES" 2>/dev/null || true)
TOTAL_LINES=$(wc -l < "$NOTES" | tr -d ' ')
echo "  Chapter headings found: $CHAPTERS"
echo "  Introduction: $([ "$INTRO" -gt 0 ] && echo 'Yes' || echo 'No')"
echo "  Conclusion: $([ "$CONCLUSION" -gt 0 ] && echo 'Yes' || echo 'No')"
echo "  Total lines: $TOTAL_LINES"

# List all chapter headings
echo "  Chapters:"
grep '^## ' "$NOTES" | while IFS= read -r line; do
  echo "    $line"
done

echo ""

# === CHECK 4: Lines per chapter ===
echo "--- Check 4: Lines Per Chapter ---"
# Get line numbers for each chapter heading, then compute gaps
grep -n '^## ' "$NOTES" | while IFS=: read -r LNUM HEADING; do
  echo "    L$LNUM: $HEADING"
done

echo ""

# === CHECK 5: Process log summary ===
echo "--- Check 5: Process Log Summary ---"
if [ -f "$LOG" ]; then
  OK_COUNT=$(grep -c '  OK —' "$LOG" 2>/dev/null || true)
  FAIL_COUNT=$(grep -c 'FAILED' "$LOG" 2>/dev/null || true)
  GAVE_UP=$(grep -c 'GIVING UP' "$LOG" 2>/dev/null || true)
  SILENT=$(grep -c 'SILENT FAILURE' "$LOG" 2>/dev/null || true)
  echo "  Successful batches: $OK_COUNT"
  echo "  Failed attempts: $FAIL_COUNT"
  echo "  Gave up entirely: $GAVE_UP"
  echo "  Silent failures (0 lines): $SILENT"
else
  echo "  No process.log found"
fi

echo ""
echo "========================================"

# === Combine all missing pages ===
ALL_MISSING=""
if [ "$MISSING_TRACKED" = "all" ]; then
  # No tracking file — rely on markers if available
  ALL_MISSING="$MISSING_MARKED"
elif [ -n "$MISSING_TRACKED" ]; then
  ALL_MISSING="$MISSING_TRACKED"
fi

ALL_MISSING=$(echo "$ALL_MISSING" | tr ' ' '\n' | grep -v '^$' | sort -un)
TOTAL_MISSING=$(echo "$ALL_MISSING" | grep -c . 2>/dev/null || true)

if [ "$TOTAL_MISSING" -eq 0 ]; then
  echo "RESULT: COMPLETE — no gaps detected"
  echo "========================================"
  exit 0
fi

echo "RESULT: $TOTAL_MISSING PAGES MISSING"
echo ""
echo "Missing pages:"
echo "$ALL_MISSING" | awk '
  NR==1 { start=$1; prev=$1; next }
  $1 != prev+1 { if (start==prev) printf "  - Page %d\n", start; else printf "  - Pages %d-%d\n", start, prev; start=$1 }
  { prev=$1 }
  END { if (start==prev) printf "  - Page %d\n", start; else printf "  - Pages %d-%d\n", start, prev }
'
echo "========================================"

# === FIX MODE: Auto-fill gaps ===
if [ "$FIX_MODE" = "--fix" ]; then
  echo ""
  echo "=== AUTO-FIX MODE — filling $TOTAL_MISSING missing pages ==="

  if [ -z "$PDF" ]; then
    echo "ERROR: --fix requires PDF path as 5th argument"
    echo "Usage: ./verify-book.sh \"$FOLDER\" $START $END_PAGE --fix \"/path/to/book.pdf\""
    exit 1
  fi

  if [ ! -f "$PDF" ]; then
    echo "ERROR: PDF not found at: $PDF"
    exit 1
  fi

  FIXED=0
  STILL_FAILED=0
  MAX_RETRIES=3
  MODELS=("sonnet" "haiku")

  for FP in $ALL_MISSING; do
    echo ""
    echo "  Fixing page $FP ($(date '+%H:%M:%S'))"
    GP_BEFORE=$(wc -l < "$NOTES" | tr -d ' ')

    FIX_PROMPT="You are a deeply analytical reader creating comprehensive study notes from a book PDF. This is a purely educational and academic book analysis project for personal study and note-taking purposes.

READ page $FP of the PDF at '$PDF'.

Then APPEND the notes to the end of '$NOTES' using the Edit tool (match the last line and add after it). Use this markdown style:
- START with: <!-- p. $FP -->
- Chapter headers: ## Chapter N: Title
- Subheadings: ### Topic Name
- Key points as bullet points (-)
- Notable quotes as > blockquotes with attribution
- **Bold** for key terms, concepts, and names
- Capture the author's arguments and reasoning — not just conclusions
- Include specific examples, stories, anecdotes, and data points
- Do NOT summarize or condense — write expansive, detailed notes
- Do NOT output any preamble or explanation — ONLY append the chapter notes

IMPORTANT: Only cover page $FP. This is an academic study notes project — please process the content faithfully."

    PAGE_OK=false
    for MODEL in "${MODELS[@]}"; do
      if [ "$PAGE_OK" = true ]; then break; fi

      RETRY=0
      while [ "$RETRY" -lt "$MAX_RETRIES" ] && [ "$PAGE_OK" = false ]; do
        if [ "$RETRY" -gt 0 ]; then
          echo "    Retry $RETRY/$MAX_RETRIES ($MODEL) — waiting 60s..."
          sleep 10
        fi

        FIX_OUT=$(claude -p "$FIX_PROMPT" \
          --model "$MODEL" \
          --allowedTools "Read" "Edit" "Write" \
          2>/dev/null) || true

        GP_AFTER=$(wc -l < "$NOTES" | tr -d ' ')
        if ! echo "$FIX_OUT" | grep -q "API Error" && [ $((GP_AFTER - GP_BEFORE)) -gt 0 ]; then
          PAGE_OK=true
          echo "    OK — page $FP filled ($MODEL, +$((GP_AFTER - GP_BEFORE)) lines)"
          FIXED=$((FIXED + 1))
          echo "$FP" >> "$PAGES_DONE"
          sort -un "$PAGES_DONE" -o "$PAGES_DONE"
        else
          RETRY=$((RETRY + 1))
          GP_BEFORE=$(wc -l < "$NOTES" | tr -d ' ')
        fi
      done

      if [ "$PAGE_OK" = false ] && [ "$MODEL" != "${MODELS[-1]}" ]; then
        echo "    Trying next model for page $FP..."
      fi
    done

    if [ "$PAGE_OK" = false ]; then
      echo "    STILL FAILED — page $FP (all models exhausted)"
      STILL_FAILED=$((STILL_FAILED + 1))
    fi
    sleep 5
  done

  echo ""
  echo "========================================"
  echo "Fix complete: $FIXED filled, $STILL_FAILED still failed"
  if [ "$STILL_FAILED" -eq 0 ]; then
    echo "ALL GAPS FILLED — book is complete!"
  else
    echo "Remaining gaps:"
    for ((P=START; P<=END_PAGE; P++)); do
      if ! grep -qx "$P" "$PAGES_DONE" 2>/dev/null; then
        echo "  - Page $P"
      fi
    done
  fi
  echo "========================================"
fi
