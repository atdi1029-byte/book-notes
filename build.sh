#!/bin/bash
# Book Notes — Build Script
# Usage:
#   ./build.sh scaffold "Book Title" "Author Name" "YEAR" "PAGE_COUNT" "category" "source.pdf"
#   ./build.sh add-shelf "Book Title" "Author Name" "folder_name" "category" "data-book-id"
#
# Examples:
#   ./build.sh scaffold "The Intelligent Investor" "Benjamin Graham" "1949" "640" "investing" "/path/to/book.pdf"
#   ./build.sh add-shelf "The Intelligent Investor" "Benjamin Graham" "The_Intelligent_Investor" "Investing" "intelligent-investor"

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

  # Extract cover from PDF if provided
  if [ -n "$PDF" ] && [ -f "$PDF" ]; then
    echo "  Extracting cover from PDF..."
    pdftoppm -jpeg -f 1 -l 1 -r 300 "$PDF" "$DIR/cover"
    # Rename pdftoppm output (it adds -01 suffix)
    if [ -f "$DIR/cover-01.jpg" ]; then
      mv "$DIR/cover-01.jpg" "$DIR/cover.jpg"
    elif [ -f "$DIR/cover-1.jpg" ]; then
      mv "$DIR/cover-1.jpg" "$DIR/cover.jpg"
    fi
    echo "  Cover extracted: $DIR/cover.jpg"
  else
    echo "  No PDF provided — add cover.jpg manually"
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
  echo "  1. Fill in $DIR/summary.md with key takeaways"
  echo "  2. Fill in $DIR/notes.md with chapter notes"
  echo "  3. Build the HTML content in $DIR/index.html"
  echo "  4. Run: ./build.sh add-shelf \"$TITLE\" \"$AUTHOR\" \"$FOLDER\" \"$CATEGORY\" \"$BM_KEY\""
}

add_shelf() {
  local TITLE="$1"
  local AUTHOR="$2"
  local FOLDER="$3"
  local CATEGORY="$4"
  local DATA_BOOK="$5"
  local SHELF="$BOOKS_DIR/index.html"

  # HTML for the new book card
  local CARD="    <a class=\"book\" href=\"${FOLDER}/index.html\" data-book=\"${DATA_BOOK}\">
      <div class=\"cover-wrap\">
        <img class=\"book-cover\" src=\"${FOLDER}/cover.jpg\" alt=\"${TITLE}\">
        <button class=\"mark-read\" onclick=\"toggleRead(event,'${DATA_BOOK}')\" title=\"Mark as read\"></button>
        <button class=\"read-badge\" onclick=\"toggleRead(event,'${DATA_BOOK}')\" title=\"Read! Click to unmark\">
          <svg viewBox=\"0 0 24 24\"><path d=\"M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z\"/></svg>
        </button>
      </div>
      <div class=\"book-title\">${TITLE}</div>
      <div class=\"book-author\">${AUTHOR}</div>
    </a>"

  echo "Card HTML for $TITLE:"
  echo ""
  echo "$CARD"
  echo ""
  echo "Add this card inside the appropriate <div class=\"shelf\"> section in index.html"
  echo "If category '$CATEGORY' doesn't exist, add a new section:"
  echo "  <h2 class=\"section-title\">$CATEGORY</h2>"
  echo "  <div class=\"shelf\">"
  echo "    [paste card here]"
  echo "  </div>"
}

process() {
  local PDF="$1"
  local FOLDER="$2"
  local START="${3:-1}"
  local END="${4:-0}"
  local BATCH="${5:-50}"
  local SLEEP="${6:-5}"
  local PARALLEL="${7:-3}"

  "$BOOKS_DIR/process-book.sh" "$PDF" "$FOLDER" "$START" "$END" "$BATCH" "$SLEEP" "$PARALLEL"
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
  *)
    echo "Usage:"
    echo "  ./build.sh scaffold \"Title\" \"Author\" \"Year\" \"Pages\" \"category\" \"source.pdf\""
    echo "  ./build.sh add-shelf \"Title\" \"Author\" \"folder\" \"category\" \"data-book-id\""
    echo "  ./build.sh process  \"/path/to/book.pdf\" \"Folder\" [start] [end] [batch] [sleep] [parallel]"
    echo "  ./build.sh queue    [\"/path/to/pdf/folder\"] [batch] [sleep] [parallel]"
    ;;
esac
