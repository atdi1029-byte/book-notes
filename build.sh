#!/bin/bash
# Book Notes — Build Script
# Usage:
#   ./build.sh scaffold  "Book Title" "Author Name" "YEAR" "PAGE_COUNT" "category" "source.pdf"
#   ./build.sh process   "/path/to/book.pdf" "Folder" [start] [end] [batch] [sleep] [parallel] [--type=TYPE]
#   ./build.sh queue     ["/path/to/pdf/folder"] [batch] [sleep] [parallel] [--type=TYPE]
#   ./build.sh add-shelf "Folder" --category "Category" [--view toread|shelf] [--tier now|soon|later]
#   ./build.sh thumbs    [--force]        # backfill thumb.jpg for every book that has cover.jpg
#   ./build.sh finish    "Folder" [finish-book.sh options]
#
# Typical flow for one book (full rules: PIPELINE.md):
#   ./build.sh process "/path/to/book.pdf" "My_Book"       # bookai: extraction + gates
#   (Claude writes summary.md and index.html; ./check_html.py My_Book --progress while writing)
#   ./grade_coverage.py My_Book                            # independent coverage + debate grader
#   ./build.sh finish "My_Book" --category "Investing" --tier now --push
#
# Examples:
#   ./build.sh scaffold "The Intelligent Investor" "Benjamin Graham" "1949" "640" "investing" "/path/to/book.pdf"
#   ./build.sh add-shelf "The_Intelligent_Investor" --category "Investing" --tier now

BOOKS_DIR="$(cd "$(dirname "$0")" && pwd)"
. "$BOOKS_DIR/_python.sh"

scaffold() {
  local TITLE="$1"
  local AUTHOR="$2"
  local YEAR="$3"
  local PAGES="$4"
  local CATEGORY="$5"
  local PDF="$6"

  # Create folder name from title (spaces → underscores, remove special chars)
  local FOLDER=$(echo "$TITLE" | sed 's/ /_/g; s/[^A-Za-z0-9_]//g')
  local DIR="$BOOKS_DIR/$FOLDER"

  echo "Creating book: $TITLE"
  echo "  Folder: $DIR"

  # Create directory
  mkdir -p "$DIR"

  # Extract cover from PDF page 1 and make the shelf thumbnail (thumb.jpg)
  if [ -n "$PDF" ] && [ -f "$PDF" ]; then
    echo "  Extracting cover + thumb from PDF..."
    python3 "$BOOKS_DIR/make_thumb.py" "$DIR" --pdf "$PDF"
  else
    echo "  No PDF provided — add cover.jpg then run: ./build.sh thumbs"
  fi

  # No notes.md / summary.md / index.html from templates: bookai writes the
  # notes, and a template index.html made the folder look finished.

  echo ""
  echo "Done! Next steps (PIPELINE.md):"
  echo "  1. Extract notes:  ./build.sh process \"$PDF\" \"$FOLDER\""
  echo "  2. Write summary.md and index.html (check as you go: ./check_html.py \"$FOLDER\" --progress)"
  echo "  3. Grade:          ./grade_coverage.py \"$FOLDER\""
  echo "  4. Finish:         ./build.sh finish \"$FOLDER\" --category \"$CATEGORY\" --push"
}

add_shelf() {
  # Inserts the card into index.html (creates the category section if needed).
  # Legacy 5-arg form (title author folder category id) still works — only the folder is used.
  if [ $# -ge 5 ] && [[ "$2" != --* ]] && [[ "$3" != --* ]]; then
    local FOLDER="$3" CATEGORY="$4"
    python3 "$BOOKS_DIR/add_to_shelf.py" "$FOLDER" --category "$CATEGORY" --view shelf
  else
    python3 "$BOOKS_DIR/add_to_shelf.py" "$@"
  fi
}

process() {
  # Everything goes straight to bookai: it applies type-aware batch/parallel
  # defaults when the numeric args are omitted, and accepts --type=TYPE anywhere.
  "$BOOKS_DIR/bookai" "$@"
}

case "$1" in
  scaffold)
    shift
    scaffold "$@"
    ;;
  add-shelf)
    shift
    add_shelf "$@"
    ;;
  process)
    shift
    process "$@"
    ;;
  queue)
    shift
    "$BOOKS_DIR/process-queue.sh" "$@"
    ;;
  thumbs)
    shift
    python3 "$BOOKS_DIR/make_thumb.py" --all "$@"
    ;;
  finish)
    shift
    "$BOOKS_DIR/finish-book.sh" "$@"
    ;;
  *)
    sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
    ;;
esac
