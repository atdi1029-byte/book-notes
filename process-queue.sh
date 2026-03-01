#!/bin/bash
# process-queue.sh — Process all PDFs in a folder, one after another
#
# Scans a PDF directory, scaffolds any missing book folders, and runs
# process-book.sh on each unfinished book. Uses page markers and .pages_done
# for accurate resume (not line-count guessing).
#
# Usage:
#   ./process-queue.sh [pdf_dir] [batch_size] [sleep_secs] [parallel]
#
# Examples:
#   ./process-queue.sh                                        # defaults
#   ./process-queue.sh "/path/to/pdfs" 50 5 3                 # custom settings

set -euo pipefail

BOOKS_DIR="$(cd "$(dirname "$0")" && pwd)"
PDF_DIR="${1:-$HOME/Desktop/Books}"
BATCH="${2:-50}"
SLEEP="${3:-5}"
PARALLEL="${4:-3}"
QUEUE_LOG="$BOOKS_DIR/queue.log"

echo "========================================" | tee -a "$QUEUE_LOG"
echo "Book Queue Processor — $(date)" | tee -a "$QUEUE_LOG"
echo "PDF dir:  $PDF_DIR" | tee -a "$QUEUE_LOG"
echo "Books dir: $BOOKS_DIR" | tee -a "$QUEUE_LOG"
echo "Settings: batch=$BATCH, sleep=$SLEEP, parallel=$PARALLEL" | tee -a "$QUEUE_LOG"
echo "========================================" | tee -a "$QUEUE_LOG"

PROCESSED=0
SKIPPED=0
FAILED=0

# Function: find how many pages are done and the first missing page
# Outputs two values: DONE_COUNT and FIRST_MISSING (0 if all done)
find_resume_info() {
  local DIR="$1" NOTES="$2" TOTAL_PAGES="$3" PAGES_DONE="$DIR/.pages_done"

  # Rebuild .pages_done from markers if it's sparse/empty
  local TRACKED=0
  if [ -f "$PAGES_DONE" ]; then
    TRACKED=$(wc -l < "$PAGES_DONE" | tr -d ' ')
  fi

  # If tracking file has less than 50% of pages, try rebuilding from markers
  local HALF=$((TOTAL_PAGES / 2))
  if [ "$TRACKED" -lt "$HALF" ] && [ -f "$NOTES" ]; then
    rebuild_pages_done "$DIR" "$NOTES"
    if [ -f "$PAGES_DONE" ]; then
      TRACKED=$(wc -l < "$PAGES_DONE" | tr -d ' ')
    fi
  fi

  # Find the first missing page
  local FIRST_MISSING=0
  for ((P=1; P<=TOTAL_PAGES; P++)); do
    if ! grep -qx "$P" "$PAGES_DONE" 2>/dev/null; then
      FIRST_MISSING=$P
      break
    fi
  done

  echo "$TRACKED $FIRST_MISSING"
}

# Function: rebuild .pages_done from page markers in notes.md
rebuild_pages_done() {
  local DIR="$1" NOTES="$2" PAGES_DONE="$DIR/.pages_done"
  local MARKERS=$(grep -oP '<!-- pp?\. \K[0-9]+(-[0-9]+)?' "$NOTES" 2>/dev/null || true)

  if [ -n "$MARKERS" ]; then
    > "$PAGES_DONE"  # clear
    while IFS= read -r M; do
      if echo "$M" | grep -q '-'; then
        local M_START=$(echo "$M" | cut -d- -f1)
        local M_END=$(echo "$M" | cut -d- -f2)
        for ((P=M_START; P<=M_END; P++)); do
          echo "$P" >> "$PAGES_DONE"
        done
      else
        echo "$M" >> "$PAGES_DONE"
      fi
    done <<< "$MARKERS"
    sort -un "$PAGES_DONE" -o "$PAGES_DONE"
  fi
}

for PDF in "$PDF_DIR"/*.pdf; do
  [ ! -f "$PDF" ] && continue

  # Derive folder name from PDF filename
  BASENAME=$(basename "$PDF" .pdf)
  FOLDER=$(echo "$BASENAME" | sed 's/ /_/g; s/[^A-Za-z0-9_]//g')
  DIR="$BOOKS_DIR/$FOLDER"
  NOTES="$DIR/notes.md"

  # Get page count
  PAGES=$(mdls -name kMDItemNumberOfPages "$PDF" 2>/dev/null | awk '{print $NF}')
  if [ -z "$PAGES" ] || [ "$PAGES" = "(null)" ]; then
    echo "  SKIP: $BASENAME — could not detect page count" | tee -a "$QUEUE_LOG"
    FAILED=$((FAILED + 1))
    continue
  fi

  echo "" | tee -a "$QUEUE_LOG"
  echo ">>> $BASENAME ($PAGES pages)" | tee -a "$QUEUE_LOG"

  # Scaffold if folder doesn't exist yet
  if [ ! -d "$DIR" ]; then
    echo "  Scaffolding $FOLDER..." | tee -a "$QUEUE_LOG"
    "$BOOKS_DIR/build.sh" scaffold "$BASENAME" "Unknown Author" "Unknown" "$PAGES" "Uncategorized" "$PDF" >> "$QUEUE_LOG" 2>&1
  fi

  # Find where to resume from
  RESUME_INFO=$(find_resume_info "$DIR" "$NOTES" "$PAGES")
  DONE_COUNT=$(echo "$RESUME_INFO" | awk '{print $1}')
  FIRST_MISSING=$(echo "$RESUME_INFO" | awk '{print $2}')

  if [ "$FIRST_MISSING" -eq 0 ]; then
    echo "  COMPLETE — all $PAGES pages tracked" | tee -a "$QUEUE_LOG"
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  echo "  Progress: $DONE_COUNT/$PAGES pages done, resuming from page $FIRST_MISSING" | tee -a "$QUEUE_LOG"
  START=$FIRST_MISSING

  # Process the book
  if "$BOOKS_DIR/process-book.sh" "$PDF" "$FOLDER" "$START" "$PAGES" "$BATCH" "$SLEEP" "$PARALLEL" >> "$QUEUE_LOG" 2>&1; then
    # Check verification verdict from process log
    PROCESS_LOG="$DIR/process.log"
    if grep -q "VERDICT: COMPLETE" "$PROCESS_LOG" 2>/dev/null; then
      echo "  DONE (verified): $BASENAME" | tee -a "$QUEUE_LOG"
      PROCESSED=$((PROCESSED + 1))
    else
      echo "  PROCESSED but INCOMPLETE: $BASENAME — check verification output" | tee -a "$QUEUE_LOG"
      FAILED=$((FAILED + 1))
    fi
  else
    echo "  FAILED: $BASENAME" | tee -a "$QUEUE_LOG"
    FAILED=$((FAILED + 1))
  fi

  sleep 5
done

echo "" | tee -a "$QUEUE_LOG"
echo "========================================" | tee -a "$QUEUE_LOG"
echo "QUEUE DONE — $(date)" | tee -a "$QUEUE_LOG"
echo "Processed: $PROCESSED | Skipped: $SKIPPED | Failed: $FAILED" | tee -a "$QUEUE_LOG"
echo "========================================" | tee -a "$QUEUE_LOG"
