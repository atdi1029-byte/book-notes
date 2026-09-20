#!/bin/bash
# finish-book.sh — Mechanical finish for a book after Claude has written
# summary.md, index.html, coverage_audit.json and debate_ready_report.json.
#
# Runs, in order, and records every result in Book_Folder/.run_state.json:
#   1. reorder     notes.md back into page order + sequential [N###] IDs
#   2. quotes      every > quote in notes.md verified against the PDF (report)
#   3. compaction  notes.md > 3000 lines must have been compacted (notes.md.raw)
#   4. summary     summary.md exists and isn't the template
#   5. html        index.html exists, isn't the template, and its <blockquote>s
#                  verify against the PDF (blocks on unverified quotes)
#   6. audits      coverage_audit.json + debate_ready_report.json pass
#   ── gate: anything above failing stops here, nothing below runs ──
#   7. thumb       cover.jpg / thumb.jpg (cover extracted from PDF if missing)
#   8. shelf       card inserted into index.html (To Read by default)
#   9. catalog     books.json + metadata/ regenerated
#  10. commit      git commit (and --push)
#
# Usage:
#   ./finish-book.sh "Book_Folder" [options]
#
# Options:
#   --pdf PATH              PDF to verify against (default: pdf recorded in .run_state.json)
#   --category "Name"       shelf category (default: .run_state.json, then CATEGORY_OVERRIDES)
#   --view toread|shelf     which tab the card goes in (default: toread)
#   --tier now|soon|later   To Read tier badge (default: later)
#   --allow-unverified-quotes   don't block on unverified <blockquote>s in index.html
#   --skip-audits           don't require coverage_audit.json / debate_ready_report.json
#   --no-commit             do everything except git commit
#   --push                  git push after committing
#   --dry-run               run the checks only; write nothing (no reorder, thumb, shelf, catalog, commit)
#
# Exit: 0 complete, 1 blocked (see the summary for what's missing).

set -uo pipefail

BOOKS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$BOOKS_DIR/_python.sh"
cd "$BOOKS_DIR"

if [ $# -lt 1 ]; then
  sed -n '2,36p' "$0" | sed 's/^# \{0,1\}//'
  exit 1
fi

FOLDER="$(basename "${1%/}")"; shift
DIR="$BOOKS_DIR/$FOLDER"
PDF=""; CATEGORY=""; VIEW="toread"; TIER="later"
ALLOW_UNVERIFIED=false; SKIP_AUDITS=false; NO_COMMIT=false; PUSH=false; DRY_RUN=false

while [ $# -gt 0 ]; do
  case "$1" in
    --pdf) PDF="$2"; shift 2 ;;
    --category) CATEGORY="$2"; shift 2 ;;
    --view) VIEW="$2"; shift 2 ;;
    --tier) TIER="$2"; shift 2 ;;
    --allow-unverified-quotes) ALLOW_UNVERIFIED=true; shift ;;
    --skip-audits) SKIP_AUDITS=true; shift ;;
    --no-commit) NO_COMMIT=true; shift ;;
    --push) PUSH=true; shift ;;
    --dry-run) DRY_RUN=true; shift ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

[ -d "$DIR" ] || { echo "ERROR: $DIR not found"; exit 1; }
NOTES="$DIR/notes.md"
[ -f "$NOTES" ] || { echo "ERROR: $NOTES not found — run bookai first"; exit 1; }

RS="python3 $BOOKS_DIR/run_state.py $DIR"
rs_set() { $DRY_RUN || $RS set "$1" "$2"; }
rs_get() { $RS get "$1"; }

# Resolve PDF / category from run state when not given
[ -n "$PDF" ] || PDF="$(rs_get pdf)"
[ -n "$CATEGORY" ] || CATEGORY="$(rs_get shelf_update.category)"
STATE_TIER="$(rs_get shelf_update.tier)"; [ "$TIER" = "later" ] && [ -n "$STATE_TIER" ] && TIER="$STATE_TIER"
STATE_VIEW="$(rs_get shelf_update.view)"; [ "$VIEW" = "toread" ] && [ -n "$STATE_VIEW" ] && VIEW="$STATE_VIEW"

HAVE_PDF=false
if [ -n "$PDF" ] && [ -f "$PDF" ]; then HAVE_PDF=true; fi

FAILS=()
WARNS=()
fail() { FAILS+=("$1"); echo "  ✗ $1"; }
warn() { WARNS+=("$1"); echo "  ⚠ $1"; }
ok()   { echo "  ✓ $1"; }

echo "═══ finish-book: $FOLDER ═══"
$DRY_RUN && echo "(dry run — no files will be written)"
$HAVE_PDF && echo "PDF: $PDF" || echo "PDF: (none — quote verification will be skipped)"
echo

# ── 1. Reorder ────────────────────────────────────────────────────────────
echo "[1/10] Reorder notes.md by page + renumber IDs"
if $DRY_RUN; then
  python3 "$BOOKS_DIR/reorder_notes.py" "$NOTES" --dry-run
else
  python3 "$BOOKS_DIR/reorder_notes.py" "$NOTES" && rs_set extraction.reordered true || fail "reorder pass failed"
fi
echo

# ── 2. Quote audit on notes.md ────────────────────────────────────────────
echo "[2/10] Quotes in notes.md vs PDF"
if $HAVE_PDF; then
  QN="$DIR/quote_audit_notes.json"
  python3 "$BOOKS_DIR/verify_quotes.py" --pdf "$PDF" --notes "$NOTES" --check-ids --json "$QN"
  QRC=$?
  if [ $QRC -eq 1 ]; then
    # only exit 1 here means duplicate IDs (not strict on quotes for notes)
    fail "notes.md has duplicate nugget IDs (run reorder without --dry-run)"
  fi
  UNV=$(python3 -c "import json;print(json.load(open('$QN'))['summary'].get('unverified',0))" 2>/dev/null || echo 0)
  [ "${UNV:-0}" -gt 0 ] && warn "$UNV unverified quote(s) in notes.md — see quote_audit_notes.json" || ok "notes quotes verified"
  rs_set quote_audit.notes_unverified "${UNV:-0}"
else
  warn "skipped (no PDF)"
fi
echo

# ── 3. Compaction ─────────────────────────────────────────────────────────
echo "[3/10] Compaction"
LINES=$(wc -l < "$NOTES" | tr -d ' ')
if [ "$LINES" -gt 3000 ] && [ ! -f "$DIR/notes.md.raw" ]; then
  fail "notes.md is $LINES lines (> 3000) and has not been compacted (no notes.md.raw)"
  rs_set compaction.status FAILED
else
  if [ -f "$DIR/notes.md.raw" ]; then ok "compacted ($LINES lines; raw kept in notes.md.raw)"; else ok "not needed ($LINES lines)"; fi
  rs_set compaction.status PASSED
fi
echo

# ── 4. summary.md ─────────────────────────────────────────────────────────
echo "[4/10] summary.md"
SUM="$DIR/summary.md"
if [ ! -f "$SUM" ]; then
  fail "summary.md missing"; rs_set summary.status FAILED
elif grep -q '\[Takeaway title\]\|\[AUTHOR\]\|\[BOOK TITLE\]\|\[Concept\]' "$SUM"; then
  fail "summary.md still contains template placeholders"; rs_set summary.status FAILED
elif [ "$(wc -l < "$SUM" | tr -d ' ')" -lt 25 ]; then
  fail "summary.md is only $(wc -l < "$SUM" | tr -d ' ') lines"; rs_set summary.status FAILED
else
  ok "summary.md present ($(wc -l < "$SUM" | tr -d ' ') lines)"; rs_set summary.status PASSED
fi
echo

# ── 5. index.html ─────────────────────────────────────────────────────────
echo "[5/10] index.html"
HTML="$DIR/index.html"
HTML_OK=true
if [ ! -f "$HTML" ]; then
  fail "index.html missing"; HTML_OK=false
else
  HL=$(wc -l < "$HTML" | tr -d ' ')
  if grep -q 'BOOK_TITLE\|<!-- TAKEAWAYS -->\|<!-- CONTENT -->\|<!-- TOC -->' "$HTML"; then
    fail "index.html still contains template placeholders"; HTML_OK=false
  elif [ "$HL" -lt 300 ]; then
    fail "index.html is only $HL lines — looks unfinished (target 1200-1500)"; HTML_OK=false
  elif ! grep -q '<h2' "$HTML"; then
    fail "index.html has no <h2> sections"; HTML_OK=false
  elif ! grep -q 'book\.js' "$HTML"; then
    fail "index.html does not load book.js (reading tracker / bookmarks won't work)"; HTML_OK=false
  else
    ok "index.html present ($HL lines)"
  fi
  if $HTML_OK && $HAVE_PDF; then
    QH="$DIR/quote_audit_html.json"
    if $ALLOW_UNVERIFIED; then
      python3 "$BOOKS_DIR/verify_quotes.py" --pdf "$PDF" --notes "$HTML" --json "$QH"
      HUNV=$(python3 -c "import json;print(json.load(open('$QH'))['summary'].get('unverified',0))" 2>/dev/null || echo 0)
      [ "${HUNV:-0}" -gt 0 ] && warn "$HUNV unverified blockquote(s) in index.html (allowed by flag)" || ok "html quotes verified"
    else
      python3 "$BOOKS_DIR/verify_quotes.py" --pdf "$PDF" --notes "$HTML" --json "$QH" --strict
      if [ $? -ne 0 ]; then
        HTML_OK=false
        fail "index.html has unverified <blockquote>s — fix them or pass --allow-unverified-quotes (details: quote_audit_html.json)"
      else
        ok "html quotes verified"
      fi
    fi
    HUNV=$(python3 -c "import json;print(json.load(open('$QH'))['summary'].get('unverified',0))" 2>/dev/null || echo 0)
    rs_set quote_audit.html_unverified "${HUNV:-0}"
  elif $HTML_OK; then
    warn "html quotes not checked (no PDF)"
  fi
fi
rs_set html.status "$($HTML_OK && echo PASSED || echo FAILED)"
echo

# ── 6. Audit artifacts ────────────────────────────────────────────────────
echo "[6/10] Coverage audit + debate-ready report"
if $SKIP_AUDITS; then
  warn "skipped (--skip-audits)"
  rs_set coverage_audit.status SKIPPED; rs_set debate_ready.status SKIPPED
else
  python3 "$BOOKS_DIR/audit_check.py" "$DIR/coverage_audit.json"
  CRC=$?
  if [ $CRC -eq 0 ]; then rs_set coverage_audit.status PASSED
  elif [ $CRC -eq 2 ]; then fail "coverage_audit.json missing — Claude must run the coverage audit (every MUST/SHOULD nugget in the HTML)"; rs_set coverage_audit.status MISSING
  else fail "coverage_audit.json reports MISSING/PARTIAL nuggets — fix index.html and re-audit"; rs_set coverage_audit.status FAILED; fi
  python3 "$BOOKS_DIR/audit_check.py" "$DIR/debate_ready_report.json"
  DRC=$?
  if [ $DRC -eq 0 ]; then rs_set debate_ready.status PASSED
  elif [ $DRC -eq 2 ]; then fail "debate_ready_report.json missing — Claude must write the debate-ready report"; rs_set debate_ready.status MISSING
  else fail "debate_ready_report.json reports problems"; rs_set debate_ready.status FAILED; fi
fi
echo

# ── Gate ──────────────────────────────────────────────────────────────────
if [ ${#FAILS[@]} -gt 0 ]; then
  echo "═══ BLOCKED — $FOLDER is not finished ═══"
  for f in "${FAILS[@]}"; do echo "  ✗ $f"; done
  rs_set complete false
  echo
  echo "Fix the above and re-run: ./finish-book.sh \"$FOLDER\""
  exit 1
fi
if $DRY_RUN; then
  echo "═══ DRY RUN — all checks pass; re-run without --dry-run to finish ═══"
  [ ${#WARNS[@]} -gt 0 ] && for w in "${WARNS[@]}"; do echo "  ⚠ $w"; done
  exit 0
fi

# ── 7. Thumb ──────────────────────────────────────────────────────────────
echo "[7/10] Cover / thumb"
if $HAVE_PDF; then python3 "$BOOKS_DIR/make_thumb.py" "$DIR" --pdf "$PDF"; else python3 "$BOOKS_DIR/make_thumb.py" "$DIR"; fi
if [ -f "$DIR/thumb.jpg" ] || [ -f "$DIR/cover.jpg" ] || [ -f "$DIR/cover.svg" ]; then
  rs_set cover.status PASSED
else
  warn "no cover — shelf card will show a broken image until one is added"
  rs_set cover.status MISSING
fi
echo

# ── 8. Shelf ──────────────────────────────────────────────────────────────
echo "[8/10] Shelf card"
SHELF_ARGS=("$FOLDER" --view "$VIEW" --tier "$TIER")
[ -n "$CATEGORY" ] && SHELF_ARGS+=(--category "$CATEGORY")
SHELF_OUT=$(python3 "$BOOKS_DIR/add_to_shelf.py" "${SHELF_ARGS[@]}")
SRC=$?
echo "$SHELF_OUT" | grep -v '^ID=\|^BMKEY=\|^VIEW='
if [ $SRC -ne 0 ]; then
  fail "could not add to shelf (pass --category \"...\")"
  rs_set shelf_update.status FAILED
else
  rs_set shelf_update.status PASSED
  rs_set shelf_update.view "$(echo "$SHELF_OUT" | sed -n 's/^VIEW=//p')"
  rs_set shelf_update.tier "$TIER"
  [ -n "$CATEGORY" ] && rs_set shelf_update.category "$CATEGORY"
  rs_set shelf_update.id "$(echo "$SHELF_OUT" | sed -n 's/^ID=//p')"
fi
echo

# ── 9. Catalog ────────────────────────────────────────────────────────────
echo "[9/10] books.json + metadata"
if [ ${#FAILS[@]} -eq 0 ]; then
  python3 "$BOOKS_DIR/generate_books_json.py" | tail -n 6 || fail "generate_books_json.py failed"
  python3 "$BOOKS_DIR/build_metadata.py" > /dev/null 2>&1 && ok "metadata/ rebuilt" || warn "build_metadata.py failed (Book Universe data may be stale)"
  rs_set catalog.status PASSED
else
  warn "skipped — shelf step failed"
fi
echo

# ── 10. Commit ────────────────────────────────────────────────────────────
echo "[10/10] Commit"
if [ ${#FAILS[@]} -gt 0 ]; then
  rs_set complete false
  echo "═══ BLOCKED ═══"; for f in "${FAILS[@]}"; do echo "  ✗ $f"; done
  exit 1
fi
rs_set complete true
TITLE=$(sed -n 's/.*<title>\(.*\)<\/title>.*/\1/p' "$HTML" | head -1 | sed 's/ *[—|-] *Book Notes.*//')
[ -n "$TITLE" ] || TITLE="$FOLDER"
if $NO_COMMIT; then
  echo "  (skipped — --no-commit)"
elif ! git -C "$BOOKS_DIR" rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  warn "not a git repo — nothing committed"
else
  git -C "$BOOKS_DIR" add -A "$FOLDER" index.html books.json metadata 2>/dev/null
  if git -C "$BOOKS_DIR" diff --cached --quiet; then
    echo "  nothing new to commit"
  else
    git -C "$BOOKS_DIR" commit -q -m "Add book: $TITLE" && ok "committed \"Add book: $TITLE\""
    if $PUSH; then git -C "$BOOKS_DIR" push && ok "pushed"; fi
  fi
fi
echo
echo "═══ DONE — $TITLE is finished ═══"
[ ${#WARNS[@]} -gt 0 ] && { echo "Warnings:"; for w in "${WARNS[@]}"; do echo "  ⚠ $w"; done; }
exit 0
