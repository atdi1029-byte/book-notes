#!/bin/bash
# process-queue.sh — Process all PDFs in a folder, one after another
#
# Scans a PDF directory, scaffolds any missing book folders, and runs
# process-book.sh on each unfinished book. Skips books with >100 lines
# of notes (considered complete).
#
# Usage:
#   ./process-queue.sh [pdf_dir] [batch_size] [sleep_secs]
#
# Examples:
#   ./process-queue.sh                                          # defaults: ~/Desktop/Books, batch 20, sleep 120
#   ./process-queue.sh "/path/to/pdfs"                          # custom PDF directory
#   ./process-queue.sh "/path/to/pdfs" 20 120                   # custom batch + sleep

set -euo pipefail

BOOKS_DIR="$(cd "$(dirname "$0")" && pwd)"
PDF_DIR="${1:-$HOME/Desktop/Books}"
BATCH="${2:-20}"
SLEEP="${3:-120}"
QUEUE_LOG="$BOOKS_DIR/queue.log"
MIN_LINES=100  # notes.md lines threshold to consider "complete"

echo "========================================" | tee -a "$QUEUE_LOG"
echo "Book Queue Processor — $(date)" | tee -a "$QUEUE_LOG"
echo "PDF dir:  $PDF_DIR" | tee -a "$QUEUE_LOG"
echo "Books dir: $BOOKS_DIR" | tee -a "$QUEUE_LOG"
echo "========================================" | tee -a "$QUEUE_LOG"

PROCESSED=0
SKIPPED=0
FAILED=0

for PDF in "$PDF_DIR"/*.pdf; do
  [ ! -f "$PDF" ] && continue

  # Derive folder name from PDF filename (strip .pdf, spaces -> underscores, remove special chars)
  BASENAME=$(basename "$PDF" .pdf)
  FOLDER=$(echo "$BASENAME" | sed 's/ /_/g; s/[^A-Za-z0-9_]//g')
  DIR="$BOOKS_DIR/$FOLDER"
  NOTES="$DIR/notes.md"

  # Check if already complete
  if [ -f "$NOTES" ]; then
    LINES=$(wc -l < "$NOTES" 2>/dev/null || echo "0")
    if [ "$LINES" -gt "$MIN_LINES" ]; then
      echo "SKIP: $BASENAME ($LINES lines — already complete)" | tee -a "$QUEUE_LOG"
      SKIPPED=$((SKIPPED + 1))
      continue
    fi
  fi

  echo "" | tee -a "$QUEUE_LOG"
  echo ">>> PROCESSING: $BASENAME" | tee -a "$QUEUE_LOG"

  # Get page count
  PAGES=$(mdls -name kMDItemNumberOfPages "$PDF" 2>/dev/null | awk '{print $NF}')
  if [ -z "$PAGES" ] || [ "$PAGES" = "(null)" ]; then
    echo "  ERROR: Could not detect page count — skipping" | tee -a "$QUEUE_LOG"
    FAILED=$((FAILED + 1))
    continue
  fi

  echo "  Pages: $PAGES" | tee -a "$QUEUE_LOG"

  # Scaffold if folder doesn't exist or notes is template-only
  if [ ! -d "$DIR" ] || [ ! -f "$NOTES" ] || [ "$(wc -l < "$NOTES" 2>/dev/null || echo 0)" -lt "$MIN_LINES" ]; then
    # Only scaffold if folder doesn't exist yet
    if [ ! -d "$DIR" ]; then
      echo "  Scaffolding $FOLDER..." | tee -a "$QUEUE_LOG"
      "$BOOKS_DIR/build.sh" scaffold "$BASENAME" "Unknown Author" "Unknown" "$PAGES" "Uncategorized" "$PDF" >> "$QUEUE_LOG" 2>&1
    fi

    # Determine start page (check if partially processed)
    START=1
    if [ -f "$NOTES" ]; then
      EXISTING_LINES=$(wc -l < "$NOTES")
      if [ "$EXISTING_LINES" -gt 40 ]; then
        # Estimate where we left off (~5 lines per page on average)
        APPROX_PAGE=$(( EXISTING_LINES / 5 ))
        # Round down to nearest batch boundary
        START=$(( (APPROX_PAGE / BATCH) * BATCH + 1 ))
        echo "  Resuming from page $START (notes has $EXISTING_LINES lines)" | tee -a "$QUEUE_LOG"
      fi
    fi

    # Process the book
    echo "  Running process-book.sh (pages $START-$PAGES)..." | tee -a "$QUEUE_LOG"
    if "$BOOKS_DIR/process-book.sh" "$PDF" "$FOLDER" "$START" "$PAGES" "$BATCH" "$SLEEP" >> "$QUEUE_LOG" 2>&1; then
      echo "  DONE: $BASENAME" | tee -a "$QUEUE_LOG"
      PROCESSED=$((PROCESSED + 1))
    else
      echo "  FAILED: $BASENAME" | tee -a "$QUEUE_LOG"
      FAILED=$((FAILED + 1))
    fi
  fi

  # Brief pause between books
  echo "  Pausing 60s before next book..." | tee -a "$QUEUE_LOG"
  sleep 60
done

echo "" | tee -a "$QUEUE_LOG"
echo "========================================" | tee -a "$QUEUE_LOG"
echo "QUEUE DONE — $(date)" | tee -a "$QUEUE_LOG"
echo "Processed: $PROCESSED | Skipped: $SKIPPED | Failed: $FAILED" | tee -a "$QUEUE_LOG"
echo "========================================" | tee -a "$QUEUE_LOG"
