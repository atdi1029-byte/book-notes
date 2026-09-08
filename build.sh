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
# Typical flow for one book:
#   ./build.sh process "/path/to/book.pdf" "My_Book"       # bookai: extraction + gates + audits
#   (Claude writes summary.md, index.html, coverage_audit.json, debate_ready_report.json)
#   ./build.sh finish "My_Book" --category "Investing" --tier now --push
#
# Examples:
#   ./build.sh scaffold "The Intelligent Investor" "Benjamin Graham" "1949" "640" "investing" "/path/to/book.pdf"
#   ./build.sh add-shelf "The_Intelligent_Investor" --category "Investing" --tier now

BOOKS_DIR="$(cd "$(dirname "$0")" && pwd)"

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
  local BM_KEY=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/ /_/g; s/[^a-z0-9_]//g')

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

  # Create summary.md from template
  if [ ! -f "$DIR/summary.md" ]; then
    sed "s/\[BOOK TITLE\]/$TITLE/g; s/\[AUTHOR\]/$AUTHOR/g; s/\[YEAR\]/$YEAR/g; s/\[PAGE COUNT\]/$PAGES/g" \
      "$BOOKS_DIR/summary-template.md" > "$DIR/summary.md"
    echo "  Created summary.md"
  else
    echo "  summary.md already exists — skipping"
  fi

  # Create notes.md from template
  if [ ! -f "$DIR/notes.md" ]; then
    sed "s/\[BOOK TITLE\]/$TITLE/g" \
      "$BOOKS_DIR/notes-template.md" > "$DIR/notes.md"
    echo "  Created notes.md"
  else
    echo "  notes.md already exists — skipping"
  fi

  # Create index.html from template
  if [ ! -f "$DIR/index.html" ]; then
    sed "s/BOOK_TITLE/$TITLE/g; s/BOOK_AUTHOR/$AUTHOR/g; s/BOOK_YEAR/$YEAR/g; s/BOOK_PAGES/$PAGES/g; s/BOOK_KEY/$BM_KEY/g" \
      "$BOOKS_DIR/template.html" > "$DIR/index.html"
    echo "  Created index.html (template — fill in content)"
  else
    echo "  index.html already exists — skipping"
  fi

  echo ""
  echo "Done! Next steps:"
  echo "  1. Extract notes:  ./build.sh process \"$PDF\" \"$FOLDER\""
  echo "  2. Fill in $DIR/summary.md and build the HTML content in $DIR/index.html"
  echo "  3. Write coverage_audit.json and debate_ready_report.json"
  echo "  4. Finish:         ./build.sh finish \"$FOLDER\" --category \"$CATEGORY\""
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
