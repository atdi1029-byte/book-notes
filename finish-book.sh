#!/bin/bash
# finish-book.sh — the only way a finished book goes on the shelf.
#
# Run after Claude has written summary.md and index.html and the independent
# grader has run (./grade_coverage.py Book_Folder). Checks everything, and
# only if all checks pass does it add the shelf card, rebuild the catalog and
# commit. Results are recorded in Book_Folder/.run_state.json.
#
#   1. extraction  bookai finished every page (.run_state.json extraction.status)
#   2. notes       notes.md in page order with unique [N###] IDs (not rewritten here)
#   3. quotes      every > quote in notes.md checked against the PDF (report)
#   4. compaction  notes.md > 3000 lines must be compacted; every MUST/SHOULD ID
#                  in notes.md.raw must survive in notes.md
#   5. summary     summary.md exists and isn't the template
#   6. html        index.html passes check_html.py (layout rules) and its
#                  <blockquote>s verify against the PDF
#   7. audits      coverage_audit.json + debate_ready_report.json from
#                  grade_coverage.py, matching the current notes.md/index.html
#   ── gate: anything above failing stops here, nothing below runs ──
#   8. thumb       cover.jpg / thumb.jpg (cover extracted from PDF if missing)
#   9. shelf       card inserted into index.html (To Read by default)
#  10. catalog     books.json + metadata.json + metadata/ regenerated
#  11. commit      only the files the site needs (pages, images they use,
#                  notes, summary, cover, thumb) — pipeline files stay local
#
# Usage:
#   ./finish-book.sh "Book_Folder" [options]
#
# Options:
#   --pdf PATH                  PDF to verify against (default: pdf recorded in .run_state.json)
#   --category "Name"           shelf category (default: .run_state.json, then CATEGORY_OVERRIDES)
#   --view toread|shelf         which tab the card goes in (default: toread)
#   --tier now|soon|later       To Read tier badge (default: later)
#   --accept-gaps "reason"      publish although extraction is INCOMPLETE (reason is recorded)
#   --allow-unverified-quotes   don't block on unverified <blockquote>s in index.html
#   --skip-audits "reason"      publish without the grader's audits (reason is recorded)
#   --no-commit                 do everything except git commit
#   --push                      git push after committing
#   --dry-run                   run the checks only; write nothing
#
# Exit: 0 complete, 1 blocked (see the summary for what's missing).

set -uo pipefail

BOOKS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$BOOKS_DIR/_python.sh"
cd "$BOOKS_DIR"

if [ $# -lt 1 ]; then
  sed -n '2,42p' "$0" | sed 's/^# \{0,1\}//'
  exit 1
fi

FOLDER="$(basename "${1%/}")"; shift
DIR="$BOOKS_DIR/$FOLDER"
PDF=""; CATEGORY=""; VIEW="toread"; TIER="later"; ACCEPT_GAPS=""; SKIP_AUDITS=""
ALLOW_UNVERIFIED=false; NO_COMMIT=false; PUSH=false; DRY_RUN=false

while [ $# -gt 0 ]; do
  case "$1" in
    --pdf) PDF="$2"; shift 2 ;;
    --category) CATEGORY="$2"; shift 2 ;;
    --view) VIEW="$2"; shift 2 ;;
    --tier) TIER="$2"; shift 2 ;;
    --accept-gaps) ACCEPT_GAPS="${2:?--accept-gaps needs a reason}"; shift 2 ;;
    --allow-unverified-quotes) ALLOW_UNVERIFIED=true; shift ;;
    --skip-audits) SKIP_AUDITS="${2:?--skip-audits needs a reason}"; shift 2 ;;
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
json_get() { python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['summary'].get('unverified',0))" "$1" 2>/dev/null || echo 0; }

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

# ── 1. Extraction ─────────────────────────────────────────────────────────
echo "[1/11] Extraction"
EXT="$(rs_get extraction.status)"
case "$EXT" in
  PASSED) ok "every page extracted" ;;
  DEGRADED) warn "pages written by haiku: $(rs_get extraction.haiku_ranges) — spot-check them" ;;
  INCOMPLETE)
    if [ -n "$ACCEPT_GAPS" ]; then
      warn "extraction INCOMPLETE (missing: $(rs_get extraction.missing_pages)) — accepted: $ACCEPT_GAPS"
      rs_set extraction.accepted_gaps "$ACCEPT_GAPS"
    else
      fail "extraction INCOMPLETE — missing pages $(rs_get extraction.missing_pages). Re-run bookai (it only redoes the gaps) or pass --accept-gaps \"reason\""
    fi ;;
  "") warn "no extraction record (notes not made by bookai?)" ;;
  *) warn "extraction status: $EXT" ;;
esac
echo

# ── 2. Notes order + IDs ──────────────────────────────────────────────────
echo "[2/11] notes.md order and nugget IDs"
NOTES_CHECK=$(python3 "$BOOKS_DIR/reorder_notes.py" "$NOTES" --check 2>/dev/null || true)
case "$NOTES_CHECK" in
  ok)    ok "in page order, IDs unique" ;;
  order) fail "notes.md is out of page order — run ./reorder_notes.py $FOLDER/notes.md, then re-run ./grade_coverage.py $FOLDER" ;;
  dupe)  fail "notes.md has duplicate nugget IDs — run ./reorder_notes.py $FOLDER/notes.md, then re-run ./grade_coverage.py $FOLDER" ;;
  noid)  fail "MUST/SHOULD nuggets without [N###] IDs — run ./reorder_notes.py $FOLDER/notes.md --add-ids, then ./grade_coverage.py $FOLDER" ;;
  *)     fail "could not read notes.md" ;;
esac
echo

# ── 3. Quote audit on notes.md ────────────────────────────────────────────
echo "[3/11] Quotes in notes.md vs PDF"
if $HAVE_PDF; then
  QN="$DIR/quote_audit_notes.json"
  python3 "$BOOKS_DIR/verify_quotes.py" --pdf "$PDF" --notes "$NOTES" --check-ids --json "$QN" > /dev/null
  UNV=$(json_get "$QN")
  [ "${UNV:-0}" -gt 0 ] && warn "$UNV unverified quote(s) in notes.md — see quote_audit_notes.json" || ok "notes quotes verified"
  rs_set quote_audit.notes_unverified "${UNV:-0}"
else
  warn "skipped (no PDF)"
fi
echo

# ── 4. Compaction ─────────────────────────────────────────────────────────
echo "[4/11] Compaction"
LINES=$(wc -l < "$NOTES" | tr -d ' ')
if [ "$LINES" -gt 3000 ] && [ ! -f "$DIR/notes.md.raw" ]; then
  fail "notes.md is $LINES lines (> 3000) and has not been compacted (no notes.md.raw)"
  rs_set compaction.status FAILED
elif [ -f "$DIR/notes.md.raw" ]; then
  LOST=$(python3 - "$DIR/notes.md.raw" "$NOTES" <<'IDS_EOF'
import re, sys
pat = re.compile(r'\[(?:MUST KNOW|SHOULD KNOW)\]\s*\[N(\d+)\]')
raw = set(pat.findall(open(sys.argv[1], errors='replace').read()))
now = set(re.findall(r'\[N(\d+)\]', open(sys.argv[2], errors='replace').read()))
lost = sorted(raw - now, key=int)
print(' '.join('N' + x for x in lost[:20]) + (f' (+{len(lost) - 20} more)' if len(lost) > 20 else '') if lost else '')
IDS_EOF
)
  if [ -n "$LOST" ]; then
    fail "compaction dropped MUST/SHOULD nuggets (IDs in notes.md.raw but not notes.md): $LOST"
    rs_set compaction.status FAILED
  else
    ok "compacted ($LINES lines); every MUST/SHOULD ID kept"
    rs_set compaction.status PASSED
  fi
else
  ok "not needed ($LINES lines)"; rs_set compaction.status SKIPPED
fi
echo

# ── 5. summary.md ─────────────────────────────────────────────────────────
echo "[5/11] summary.md"
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

# ── 6. index.html ─────────────────────────────────────────────────────────
echo "[6/11] index.html"
HTML="$DIR/index.html"
HTML_OK=true
if [ ! -f "$HTML" ]; then
  fail "index.html missing"; HTML_OK=false
else
  if python3 "$BOOKS_DIR/check_html.py" "$FOLDER" > "$DIR/.check_html.txt" 2>&1; then
    ok "layout rules pass ($(grep -c '⚠' "$DIR/.check_html.txt" || true) warning(s))"
  else
    HTML_OK=false
    fail "index.html breaks layout rules — run ./check_html.py $FOLDER:"
    grep '  ✗ ' "$DIR/.check_html.txt" | head -12 | sed 's/^/    /'
  fi
  rm -f "$DIR/.check_html.txt"
  if [ -f "$DIR/plain.html" ] && ! python3 "$BOOKS_DIR/check_html.py" "$FOLDER" --page plain.html --progress > /dev/null 2>&1; then
    warn "plain.html has layout problems — ./check_html.py $FOLDER --page plain.html --progress"
  fi
  if $HAVE_PDF; then
    QH="$DIR/quote_audit_html.json"
    if $ALLOW_UNVERIFIED; then
      python3 "$BOOKS_DIR/verify_quotes.py" --pdf "$PDF" --notes "$HTML" --json "$QH" > /dev/null
      HUNV=$(json_get "$QH")
      [ "${HUNV:-0}" -gt 0 ] && warn "$HUNV unverified blockquote(s) in index.html (allowed by flag)" || ok "html quotes verified"
    elif python3 "$BOOKS_DIR/verify_quotes.py" --pdf "$PDF" --notes "$HTML" --json "$QH" --strict > /dev/null; then
      ok "html quotes verified"
    else
      HTML_OK=false
      fail "index.html has unverified <blockquote>s — fix them or pass --allow-unverified-quotes (details: quote_audit_html.json)"
    fi
    rs_set quote_audit.html_unverified "$(json_get "$QH")"
  else
    warn "html quotes not checked (no PDF)"
  fi
fi
rs_set html.status "$($HTML_OK && echo PASSED || echo FAILED)"
echo

# ── 7. Audit artifacts ────────────────────────────────────────────────────
echo "[7/11] Coverage audit + debate-ready report (independent grader)"
if [ -n "$SKIP_AUDITS" ]; then
  warn "skipped: $SKIP_AUDITS"
  rs_set coverage_audit.status SKIPPED; rs_set debate_ready.status SKIPPED
  rs_set coverage_audit.skipped_reason "$SKIP_AUDITS"
else
  python3 "$BOOKS_DIR/audit_check.py" "$DIR"
  CRC=$?
  if [ $CRC -eq 0 ]; then
    rs_set coverage_audit.status PASSED; rs_set debate_ready.status PASSED
  elif [ $CRC -eq 2 ]; then
    fail "audits missing — run ./grade_coverage.py $FOLDER"
    rs_set coverage_audit.status MISSING; rs_set debate_ready.status MISSING
  else
    fail "audits don't pass — fix the chapters listed above, then ./grade_coverage.py $FOLDER --chapters N"
    rs_set coverage_audit.status FAILED; rs_set debate_ready.status FAILED
  fi
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

# ── 8. Thumb ──────────────────────────────────────────────────────────────
echo "[8/11] Cover / thumb"
HAD_COVER=false
[ -f "$DIR/cover.jpg" ] || [ -f "$DIR/cover.png" ] || [ -f "$DIR/cover.svg" ] && HAD_COVER=true
if $HAVE_PDF; then python3 "$BOOKS_DIR/make_thumb.py" "$DIR" --pdf "$PDF"; else python3 "$BOOKS_DIR/make_thumb.py" "$DIR"; fi
if [ -f "$DIR/thumb.jpg" ] || [ -f "$DIR/cover.jpg" ] || [ -f "$DIR/cover.svg" ]; then
  if $HAD_COVER; then
    rs_set cover.status PASSED
  else
    warn "cover taken from PDF page 1 — look at $FOLDER/cover.jpg; if it's an ebook/publisher page, replace it (the thumb follows)"
    rs_set cover.status NEEDS_REVIEW
  fi
else
  warn "no cover — shelf card will show a broken image until one is added"
  rs_set cover.status MISSING
fi
echo

# ── 9. Shelf ──────────────────────────────────────────────────────────────
echo "[9/11] Shelf card"
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

# ── 10. Catalog ───────────────────────────────────────────────────────────
echo "[10/11] books.json + metadata"
if [ ${#FAILS[@]} -eq 0 ]; then
  CAT_OK=true
  python3 "$BOOKS_DIR/generate_books_json.py" | tail -n 6 || { warn "generate_books_json.py failed"; CAT_OK=false; }
  python3 "$BOOKS_DIR/build_metadata.py" > /dev/null 2>&1 && ok "metadata rebuilt" || { warn "build_metadata.py failed (Book Universe data may be stale)"; CAT_OK=false; }
  rs_set catalog.status "$($CAT_OK && echo PASSED || echo FAILED)"
else
  warn "skipped — shelf step failed"
fi
echo

# ── 11. Commit ────────────────────────────────────────────────────────────
echo "[11/11] Commit"
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
  # Only what the site needs. Chart renders, raw notes, logs and run state stay
  # on this Mac (.gitignore); referenced images are force-added.
  PUBLISH=()
  while IFS= read -r f; do PUBLISH+=("$f"); done < <(python3 "$BOOKS_DIR/bookai_lib.py" publish "$DIR" "$FOLDER")
  git -C "$BOOKS_DIR" add -f -- "${PUBLISH[@]}"
  git -C "$BOOKS_DIR" add -- index.html books.json metadata.json metadata 2>/dev/null
  if git -C "$BOOKS_DIR" diff --cached --quiet; then
    echo "  nothing new to commit"
  else
    git -C "$BOOKS_DIR" commit -q -m "Add book: $TITLE" && ok "committed \"Add book: $TITLE\" (${#PUBLISH[@]} files from $FOLDER)"
    if $PUSH; then git -C "$BOOKS_DIR" push -q && ok "pushed"; fi
  fi
fi
echo
echo "═══ DONE — $TITLE is finished ═══"
[ ${#WARNS[@]} -gt 0 ] && { echo "Warnings:"; for w in "${WARNS[@]}"; do echo "  ⚠ $w"; done; }
exit 0
