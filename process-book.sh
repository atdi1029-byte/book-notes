#!/bin/bash
# process-book.sh — Batch-process a PDF into notes.md using Claude CLI
#
# Runs independent claude invocations per page range so each gets fresh context.
# Sleeps between batches to avoid rate limits. Can run unattended overnight.
#
# Usage:
#   ./process-book.sh "/path/to/book.pdf" "Book_Folder" [start_page] [end_page] [batch_size] [sleep_secs]
#
# Examples:
#   ./process-book.sh "/Users/alexbarnett/Desktop/Books/Atomic Habits.pdf" "Atomic_Habits" 161 256 20 120
#   ./process-book.sh "/path/to/new-book.pdf" "New_Book" 1 300 20 120
#
# Prerequisites:
#   - claude CLI installed and authenticated
#   - Run with: claude --dangerously-skip-permissions (for unattended mode)
#   - Or configure allowed tools in ~/.claude/settings.json

set -euo pipefail

BOOKS_DIR="$(cd "$(dirname "$0")" && pwd)"

PDF="$1"
FOLDER="$2"
START="${3:-1}"
END_PAGE="${4:-0}"        # 0 = auto-detect from PDF metadata
BATCH="${5:-20}"
SLEEP="${6:-120}"

DIR="$BOOKS_DIR/$FOLDER"
NOTES="$DIR/notes.md"
LOG="$DIR/process.log"

# Auto-detect total pages if not specified
if [ "$END_PAGE" -eq 0 ]; then
  END_PAGE=$(mdls -name kMDItemNumberOfPages "$PDF" 2>/dev/null | awk '{print $NF}')
  if [ -z "$END_PAGE" ] || [ "$END_PAGE" = "(null)" ]; then
    echo "ERROR: Could not detect page count. Specify end_page manually."
    exit 1
  fi
fi

echo "========================================" | tee -a "$LOG"
echo "Book PDF Processor — $(date)" | tee -a "$LOG"
echo "PDF:    $PDF" | tee -a "$LOG"
echo "Output: $NOTES" | tee -a "$LOG"
echo "Pages:  $START → $END_PAGE (batch size: $BATCH, sleep: ${SLEEP}s)" | tee -a "$LOG"
echo "========================================" | tee -a "$LOG"

# Ensure output directory and notes file exist
mkdir -p "$DIR"
touch "$NOTES"

PAGE=$START
BATCH_NUM=0
FAILURES=0
MAX_RETRIES=3

while [ "$PAGE" -le "$END_PAGE" ]; do
  BATCH_END=$((PAGE + BATCH - 1))
  [ "$BATCH_END" -gt "$END_PAGE" ] && BATCH_END=$END_PAGE
  BATCH_NUM=$((BATCH_NUM + 1))

  echo "" | tee -a "$LOG"
  echo "--- Batch $BATCH_NUM: pages $PAGE-$BATCH_END ($(date '+%H:%M:%S')) ---" | tee -a "$LOG"

  # Build the prompt for this batch
  PROMPT="You are processing a book PDF into detailed chapter notes in markdown format.

READ pages $PAGE-$BATCH_END of the PDF at '$PDF'.

Then APPEND the notes to the end of '$NOTES' using the Edit tool (match the last line and add after it). Use this markdown style:
- Chapter headers: ## Chapter N: Title
- Subheadings: ### Topic Name
- Key points as bullet points (-)
- Notable quotes as > blockquotes
- **Bold** for key terms and concepts
- Include ALL important ideas, examples, stories, and data points from these pages
- Be thorough - do NOT skip or summarize content
- Do NOT output any preamble or explanation - ONLY append the chapter notes

IMPORTANT: Only cover pages $PAGE-$BATCH_END. Do not go beyond these pages."

  # Run claude with retries
  RETRY=0
  SUCCESS=false
  while [ "$RETRY" -lt "$MAX_RETRIES" ] && [ "$SUCCESS" = false ]; do
    if [ "$RETRY" -gt 0 ]; then
      WAIT=$((SLEEP * RETRY))
      echo "  Retry $RETRY/$MAX_RETRIES — waiting ${WAIT}s..." | tee -a "$LOG"
      sleep "$WAIT"
    fi

    # Run claude in print mode (non-interactive, fresh context each time)
    # --model opus: handles book content without content filtering issues
    # --fallback-model sonnet: auto-fallback if opus is overloaded/rate-limited
    # --allowedTools: pre-approve Read/Edit/Write so no prompts needed
    CLAUDE_OUTPUT=$(claude -p "$PROMPT" \
      --model opus \
      --fallback-model sonnet \
      --allowedTools "Read" "Edit" "Write" \
      2>>"$LOG") || true
    CLAUDE_EXIT=$?

    # Check for both exit code and API errors in output
    if [ $CLAUDE_EXIT -eq 0 ] && ! echo "$CLAUDE_OUTPUT" | grep -q "API Error"; then
      SUCCESS=true
      echo "  OK — batch $BATCH_NUM complete" | tee -a "$LOG"
    else
      RETRY=$((RETRY + 1))
      echo "  FAILED — attempt $RETRY (output: $(echo "$CLAUDE_OUTPUT" | head -1))" | tee -a "$LOG"
    fi
  done

  if [ "$SUCCESS" = false ]; then
    FAILURES=$((FAILURES + 1))
    echo "  GIVING UP on batch $BATCH_NUM (pages $PAGE-$BATCH_END) after $MAX_RETRIES retries" | tee -a "$LOG"
    echo "  Resume later with: ./process-book.sh \"$PDF\" \"$FOLDER\" $PAGE $END_PAGE $BATCH $SLEEP" | tee -a "$LOG"

    # Continue to next batch instead of stopping entirely
    # Uncomment the next line to stop on failure instead:
    # exit 1
  fi

  # Advance to next batch
  PAGE=$((BATCH_END + 1))

  # Sleep between batches (skip after last batch)
  if [ "$PAGE" -le "$END_PAGE" ]; then
    echo "  Sleeping ${SLEEP}s..." | tee -a "$LOG"
    sleep "$SLEEP"
  fi
done

echo "" | tee -a "$LOG"
echo "========================================" | tee -a "$LOG"
echo "DONE — $(date)" | tee -a "$LOG"
echo "Batches: $BATCH_NUM total, $FAILURES failed" | tee -a "$LOG"
echo "Notes:   $(wc -l < "$NOTES") lines in $NOTES" | tee -a "$LOG"
echo "========================================" | tee -a "$LOG"

if [ "$FAILURES" -gt 0 ]; then
  echo ""
  echo "Some batches failed. Check $LOG for details."
  echo "You can resume from a specific page with:"
  echo "  ./process-book.sh \"$PDF\" \"$FOLDER\" <start_page> $END_PAGE $BATCH $SLEEP"
fi
