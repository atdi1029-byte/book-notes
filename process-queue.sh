#!/bin/bash
# process-queue.sh — Process all PDFs in a folder, one after another
#
# Scans a PDF directory, scaffolds any missing book folders, and runs
# bookai on each unfinished book. bookai skips pages it already has, so a
# re-run only fills gaps; a book whose .run_state.json says the extraction
# PASSED is skipped.
#
# Usage:
#   ./process-queue.sh [pdf_dir] [batch_size] [sleep_secs] [parallel] [--type=TYPE]
#
# batch/sleep/parallel are optional — when omitted, bookai picks type-aware
# defaults (technical 10/5/1, textbook 12/5/2, analytical 20/5/3, ...).
# --type applies to every PDF in the queue; omit it to auto-detect per book.
#
# Examples:
#   ./process-queue.sh                                        # defaults, auto-detect types
#   ./process-queue.sh "/path/to/pdfs"                        # custom dir
#   ./process-queue.sh "/path/to/pdfs" 20 5 3 --type=analytical

set -euo pipefail

BOOKS_DIR="$(cd "$(dirname "$0")" && pwd)"
. "$BOOKS_DIR/_python.sh"

# Separate --type flag from positionals
TYPE_FLAG=""
POS=()
for arg in "$@"; do
  case "$arg" in
    --type=*) TYPE_FLAG="$arg" ;;
    *) POS+=("$arg") ;;
  esac
done
PDF_DIR="${POS[0]:-$HOME/Desktop/Books}"
BATCH="${POS[1]:-}"
SLEEP="${POS[2]:-}"
PARALLEL="${POS[3]:-}"
QUEUE_LOG="$BOOKS_DIR/queue.log"

page_count() {
  # PyMuPDF everywhere; mdls fallback on macOS
  local N
  N=$(python3 -c "import sys
try:
    import pymupdf as fitz
except ImportError:
    import fitz
print(len(fitz.open(sys.argv[1])))" "$1" 2>/dev/null || true)
  if ! [[ "$N" =~ ^[0-9]+$ ]] && command -v mdls >/dev/null 2>&1; then
    N=$(mdls -name kMDItemNumberOfPages "$1" 2>/dev/null | awk '{print $NF}')
  fi
  [[ "$N" =~ ^[0-9]+$ ]] && echo "$N" || echo ""
}

echo "========================================" | tee -a "$QUEUE_LOG"
echo "Book Queue Processor — $(date)" | tee -a "$QUEUE_LOG"
echo "PDF dir:  $PDF_DIR" | tee -a "$QUEUE_LOG"
echo "Books dir: $BOOKS_DIR" | tee -a "$QUEUE_LOG"
echo "Settings: batch=${BATCH:-auto}, sleep=${SLEEP:-auto}, parallel=${PARALLEL:-auto}, type=${TYPE_FLAG:-auto-detect}" | tee -a "$QUEUE_LOG"
echo "========================================" | tee -a "$QUEUE_LOG"

PROCESSED=0
SKIPPED=0
FAILED=0

extraction_status() {
  python3 "$BOOKS_DIR/run_state.py" "$1" get extraction.status 2>/dev/null || true
}

for PDF in "$PDF_DIR"/*.pdf; do
  [ ! -f "$PDF" ] && continue

  # Folder name from the file name, without the download-site prefix and the
  # " - Author" tail ("_OceanofPDF.com_Cant_We_Just_Print_More_Money_-_Rupal_Patel"
  # → "Cant_We_Just_Print_More_Money"), so it matches hand-named folders.
  BASENAME=$(basename "$PDF" .pdf)
  FOLDER=$(echo "$BASENAME" | sed -E 's/^_*OceanofPDF(\.com)?_+//I; s/(_| )-(_| ).*$//; s/ /_/g; s/[^A-Za-z0-9_]//g; s/_+$//')
  DIR="$BOOKS_DIR/$FOLDER"

  # Get page count
  PAGES=$(page_count "$PDF")
  if [ -z "$PAGES" ]; then
    echo "  SKIP: $BASENAME — could not detect page count" | tee -a "$QUEUE_LOG"
    FAILED=$((FAILED + 1))
    continue
  fi

  echo "" | tee -a "$QUEUE_LOG"
  echo ">>> $BASENAME → $FOLDER ($PAGES pages)" | tee -a "$QUEUE_LOG"

  # Scaffold (folder + cover) if the folder doesn't exist yet
  if [ ! -d "$DIR" ]; then
    echo "  Scaffolding $FOLDER..." | tee -a "$QUEUE_LOG"
    "$BOOKS_DIR/build.sh" scaffold "$FOLDER" "Unknown Author" "Unknown" "$PAGES" "Uncategorized" "$PDF" >> "$QUEUE_LOG" 2>&1 \
      || echo "  (scaffold had a problem — continuing)" | tee -a "$QUEUE_LOG"
  fi

  STATUS=$(extraction_status "$DIR")
  if [ "$STATUS" = "PASSED" ] || [ "$STATUS" = "DEGRADED" ]; then
    echo "  COMPLETE — extraction $STATUS" | tee -a "$QUEUE_LOG"
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  # bookai only extracts the pages that aren't done yet.
  BOOKAI_ARGS=("$PDF" "$FOLDER" 1 0)
  if [ -n "$BATCH$SLEEP$PARALLEL" ]; then BOOKAI_ARGS+=("$BATCH" "$SLEEP" "$PARALLEL"); fi
  [ -n "$TYPE_FLAG" ] && BOOKAI_ARGS+=("$TYPE_FLAG")
  "$BOOKS_DIR/bookai" "${BOOKAI_ARGS[@]}" < /dev/null >> "$QUEUE_LOG" 2>&1 || true
  STATUS=$(extraction_status "$DIR")
  case "$STATUS" in
    PASSED)   echo "  DONE: $BASENAME" | tee -a "$QUEUE_LOG"; PROCESSED=$((PROCESSED + 1)) ;;
    DEGRADED) echo "  DONE (some pages by haiku — see .run_state.json): $BASENAME" | tee -a "$QUEUE_LOG"; PROCESSED=$((PROCESSED + 1)) ;;
    *)        echo "  INCOMPLETE ($STATUS): $BASENAME — re-run the queue to fill the gaps" | tee -a "$QUEUE_LOG"; FAILED=$((FAILED + 1)) ;;
  esac

  sleep 5
done

echo "" | tee -a "$QUEUE_LOG"
echo "========================================" | tee -a "$QUEUE_LOG"
echo "QUEUE DONE — $(date)" | tee -a "$QUEUE_LOG"
echo "Processed: $PROCESSED | Skipped: $SKIPPED | Failed: $FAILED" | tee -a "$QUEUE_LOG"
echo "========================================" | tee -a "$QUEUE_LOG"
