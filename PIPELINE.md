# BookAI pipeline — the one rules file

This is the single source of truth for turning a book into its notes page.
`/Users/alexbarnett/CLAUDE.md`, the `bookai` skill and the memory notes all point
here. **If anything else disagrees with this file, this file wins.** The page
layout rules also live in `book_rules.json`, which `check_html.py` enforces.
(Consolidated Sep 30 2026; the conflicts that were resolved are listed at the end.)

## The standard

A person who reads only the page should be able to confidently discuss and
debate the book with someone who read all of it.

- **Never skip pages.** Every page is read. A book isn't done until every page
  is extracted: bookai reports `INCOMPLETE` and finish-book refuses it.
- **Signal over noise:** read 100% of the book, keep 100% of the important
  ideas, deliver 10-20% of the reading time. Space goes by importance, not by
  chapter length.
- Notes capture every distinct useful idea: claims, reasoning, mechanisms,
  evidence, caveats, exceptions, counterarguments, and examples that teach
  something different. Two examples are redundant only when they teach the same
  thing. Remove repetition, not information.
- Nuggets are tagged `[MUST KNOW]`, `[SHOULD KNOW]`, `[NICE TO KNOW]` with IDs
  (`[MUST KNOW][N042]`). The IDs follow a nugget from notes to the finished page.
- No fixed line target for notes: length follows information density.
- **The HTML is original writing, not reformatted notes.** Read the notes, close
  them, write from understanding; return to the notes only to check facts,
  quotes and numbers. No "the author argues X, then the author argues Y", no bold
  topic headers carried over from the notes. State ideas directly, tell the
  stories, build the arguments as flowing prose. The good books (Big Debt Crises,
  How an Economy Grows, Talking to My Daughter) were written this way.
- Each book folder holds `notes.md`, `summary.md`, `index.html`, `cover.jpg`
  (+ `thumb.jpg`, and `plain.html` when asked for).

## The flow

| Step | Who | Command / output |
|---|---|---|
| 1. Extract | script | `./bookai "/path/book.pdf" Book_Folder` → `notes.md` |
| 2. Compact (if notes > 3000 lines) | Claude + 2 agents | `notes.md.raw` kept; `notes.md` compacted |
| 3. Summary | Claude | `summary.md` |
| 4. Write the page | Claude, main session | `index.html`, checked with `./check_html.py Book_Folder --progress` after each chapter |
| 5. Grade | script (fresh Claude calls) | `./grade_coverage.py Book_Folder` → `coverage_audit.json`, `debate_ready_report.json` |
| 6. Publish | script | `./finish-book.sh Book_Folder --category "…" --push` |
| 7. Remember | Claude | add the book to `books.md` and its type guide in memory |

### 1. Extract — `bookai`

```
./bookai "/path/to/book.pdf" "Book_Folder" [start] [end] [batch] [sleep] [parallel] [--type=TYPE]
```

- Always use bookai for PDFs (don't read a PDF by hand in batches). bookai
  takes a PDF; `epub_convert.py` goes the other way (finished page → EPUB for
  an e-reader).
- Types: `analytical` (default), `narrative`, `technical`, `textbook`,
  `practical`. Omit `--type` to auto-detect. Defaults per type: technical
  10-page batches, 1 at a time; practical 10/2; textbook 12/2; others 20/3.
- Each batch is one `claude -p` call from an empty temp folder with only
  Read/Write (no CLAUDE.md, memory or MCP, about 70% less fixed prompt). The
  model gets the page text (PyMuPDF) plus page images for pages with figures
  or no text layer. Chart book types also keep every page as `charts/page_NNN.png`
  for the HTML stage.
- Gates per batch: every page acknowledged, enough content for the pages that
  have content, priority tags, figure descriptions for chart books, and every
  `> quote` found in the PDF text. A rejected batch is retried on Sonnet with
  the reason, then split in half down to 4 pages, and only then tried on Haiku.
  Haiku pages are listed in `.run_state.json` (`extraction.haiku_ranges`,
  status `DEGRADED`) — spot-check or re-run them.
- Re-running is safe: finished pages are skipped, so a re-run only fills gaps.
  One run per folder (`.bookai.lock`); Ctrl-C stops every worker and keeps
  finished batches. A usage/credit limit stops the run cleanly; re-run later.
- Nothing is deleted from the notes. Pages covered twice are listed in
  `notes.duplicates-report.md`.
- `extraction.status` is `PASSED` only when every page is in.
- Everything runs on the Claude subscription: the "≈$" figures in the logs
  (and `extraction.cost_usd`) are what the calls would cost at pay-per-use
  prices, shown as a measure of plan usage — nothing is charged.

### 2. Compact — only when notes.md > 3000 lines

- Back up first: `cp notes.md notes.md.raw`. Two agents in parallel (first half,
  second half), then merge.
- Soft target about 2× the page count in lines (650 pages → ~1,300). **Keeping
  every [MUST KNOW] and [SHOULD KNOW] nugget overrides the target**; only
  [NICE TO KNOW] items and true duplicates may go. Keep the nugget IDs exactly
  as they are — finish-book blocks if any MUST/SHOULD ID from `notes.md.raw` is
  missing from `notes.md`. When in doubt, keep the nugget.
- Technical books (TA, options, quantitative): optimize for compressed
  understanding, not shrinking. Never reduce `concept → structure → reasoning →
  conclusion` to `conclusion + example`. For every [MUST KNOW] concept keep:
  definition, construction, recognition criteria, reasoning, use case, worked
  example, confirmation/invalidation, failure modes. Safe to cut: repeated
  examples that add nothing, duplicated explanations, excess history, filler,
  repeated warnings. Full rules: memory `ta-books.md`.

### 3. Summary — `summary.md`

Key takeaways and thematic breakdown, written after the notes are final.

### 4. Write the page — `index.html`

- **Write it yourself in the main session. Never delegate the HTML to an
  agent** (they consistently write about a third of what's needed).
- Pick the style template first (memory): `narrative-books.md`,
  `analytical-books.md`, `conversational-books.md`, `practical-finance-books.md`,
  `textbook-books.md`, `ta-books.md`, `fitness-books.md`. Read it and open the
  closest finished book of that type as the reference. If none fits, say so.
- Copy the head/body skeleton from a recent book: shared `../book.css`,
  progress bar + bookmark bar + toast divs, and at the end
  `<script>var BM_KEY = 'bm_…';</script>` then `<script src="../book.js"></script>`
  (BM_KEY first, `var` not `const`).
- Extract the charts/figures you'll show before writing, and place them
  inline or as `[view]` lightbox links as you write.
- Write chapter by chapter. After each chapter run
  `./check_html.py Book_Folder --progress`: it prints every chapter's paragraph
  count and average words and fails when later chapters get thinner than the
  first ones. Fix a thin chapter right away; don't rewrite what is already good.
- Wrap prose at ~70 characters, one sentence per line.
- Plain-English companion `plain.html`: only when Alex asks for it (dense or
  technical books: bonds, options, macro finance, quantitative) — don't suggest
  or assume it. Same chapter structure, title + "(Plain English)", its own
  `BM_KEY`, its own card on the shelf. No length limit (a math/quant book may
  need 1,500-2,500+ lines): 8+ paragraphs per chapter with everyday worked
  examples and real explanations of the math (not just "there's a formula").
  Inline SVG diagrams wherever they help (flow charts, timelines, feedback
  loops, comparisons) in `.diagram` divs with optional `.diagram-caption`,
  light strokes that work on dark backgrounds. No synthesis sections.

### 5. Grade — `grade_coverage.py`

The writer never grades its own page. For each chapter a fresh Claude call
(no tools, no memory) compares that chapter's MUST/SHOULD nuggets with the
chapter text and quotes the sentence that covers each one; quotes are checked
against the page; nuggets not found get a second look against the whole page;
the same call checks the chapter is debate-ready (claim, reasoning, evidence,
caveats, objection + answer).

- Fix what it lists in the existing chapter prose (don't add a new section),
  then `./grade_coverage.py Book_Folder --chapters 3,7` to re-grade those.
- `--dry-run` shows how notes sections map to chapters.
- The audit files carry hashes of `notes.md` and `index.html`; editing either
  afterwards makes them stale, and finish-book asks for a re-grade.

### 6. Publish — `finish-book.sh`

`./finish-book.sh Book_Folder --category "Section" [--tier now|soon|later] --push`
is the only way a book goes on the shelf. It checks, in order: extraction
complete, notes in order with IDs, notes quotes, compaction kept every
MUST/SHOULD ID, summary, `check_html.py`, `<blockquote>`s found in the PDF,
the grader's audits. Anything failing blocks. Then it makes the thumb, adds the
card (To Read by default — don't ask which section; Alex moves books with
"→ Shelf"), rebuilds `books.json` / `metadata.json` / `metadata/`, and commits
only what the site needs. Escape hatches need a reason that gets recorded:
`--accept-gaps "…"`, `--skip-audits "…"`.

The cover comes from PDF page 1. finish-book marks it `NEEDS_REVIEW`: look at
it, and if it's an ebook/publisher page, find the real cover (Goodreads) and
save it as `cover.jpg`; the thumb rebuilds itself.

## Page layout (enforced by check_html.py via book_rules.json)

Order of the page:

0. **Glossary** — right after the table of contents, before chapter 1.
   Required for textbook, technical, practical and fitness books; for others
   use judgment (jargon-heavy finance: yes; narrative/conversational: usually
   no). 20-40 terms for lighter books, 50-70 for dense ones, grouped under
   `<h4>` categories. Each term: `<p><strong>Term:</strong> definition with a
   concrete example</p>` (or `<li>`; several terms in one `<p>` must be
   separated by `<br>`) — that's the format the tap-for-definition tooltips
   read. Economics 101's glossary is the model. Gets `<h2 id="glossary">`.
1. **If You Only Remember 10 Things** — ten items, 1-2 sentences each, no preamble.
2. **Chapters** — thorough prose, not bullet dumps. Every chapter, prologue,
   introduction and epilogue gets its own `<h2>`; never combine chapters
   ("Chapters 10–11"). **8+ paragraphs each,
   averaging 100-120 words (never under 80)**, with at least one specific
   example, anecdote or episode. No chapter gets reduced coverage; later
   chapters are as deep as early ones.
3. **What Can Be Safely Skipped** — 4-8 `<h3>` entries: what repeats, what
   defends one study at length, what's interesting but non-essential, and what
   the reader would miss.
4. **Trading & Investing Lessons** — every book, 4-6+ lessons, each an `<h3>`
   plus a real paragraph connecting the book's idea to trading/investing
   (e.g. extractive institutions as value traps, creative destruction as
   innovation investing, vicious circles as negative momentum, critical
   junctures as regime changes). Fitness books use **Programming Takeaways**
   here instead (memory `fitness-books.md`).
5. **Key Takeaways** — never capped; each item an `<h3>` (not `<p><strong>`),
   full paragraphs with specific examples and reasoning, not 2-sentence stubs.
6. **Contrarian Ideas** — each an `<h3>`, full paragraphs.
7. **Notable Quotes**.
8. **Allegories & Cultural References** — a 2-column table
   (Reference | Concept Illustrated), 12+ rows, never h3 + paragraphs: a short
   reference name, then a one-sentence explanation. Dig through the notes for
   every metaphor, analogy, historical parallel and cultural reference.
   Antifragile (15 rows) is the model.
9. **Proposals/Frameworks** — when the author lays out models or recommendations.
10. **Referenced Works** — 3-column table (Name | Work/Role | Connection),
    the notable ones.
11. **What Didn't Fit** — the good stories, stats and examples from the notes
    that didn't make it into chapter prose, as `<h3>` sub-sections of 5-8+
    sentences each (context, specifics, why it matters; not filler). Compare
    notes with the page after writing.
12. **Footer** — author, year, page count, summary blurb.
13. **About the Author** — 2-3 paragraphs (not counted in length targets).
14. **Why This Book Matters** — 2-3 paragraphs, for important books.

Everywhere:

- **Table of contents:** `<nav class="toc"><h2>Contents</h2><ol>…</ol></nav>`.
  Flat list; when the book is divided into Parts, nest each Part's chapters in
  an `<ol>` inside the Part's `<li>` (Economics 101 style).
- **No cover image inside the page** (`index.html` or `plain.html`); the cover
  is on the shelf card only.
- Every `<h2>` has an `id`. Sub-items use `<h3>` so each gets a bookmark
  (book.js adds bookmark buttons to headings and every `<p>`).
- **40-70+ `<strong>`** key terms: people (full name on first mention),
  institutions, concepts, famous phrases — while writing, not as a later pass.
- **8-15+ inline `<blockquote>`s with `<cite>`** inside chapter prose (close the
  `</p>`, add the blockquote, open a new `<p>`; no empty `<p></p>`). Every one is
  checked against the PDF text by finish-book.
- Every `<table>` has `role="presentation"` (so "Listen to page" reads it as text).
- Textbooks need 10+ tables and 4+ inline SVG diagrams from the first draft.
- Length follows the book (soft, not gated): light/repetitive ~800-1,000 lines,
  standard ~1,200-1,500, dense/technical ~1,500-2,000, textbooks ~3,000-5,000.

## Files: what's published and what stays on this Mac

The repo is the public site. Committed per book: `index.html`, `plain.html`,
`summary.md`, `notes.md`, `cover.jpg`, `thumb.jpg`, and the images the pages
actually use. Pipeline files stay local (`.gitignore`): `charts/` renders
(referenced images are force-added by finish-book), `notes.md.raw` and other
note backups, logs, `.pages_done`, `.run_state.json`, quote/coverage audits.
Never `git add -A` a book folder; use finish-book.

## Decisions that settled old conflicts (Sep 30 2026)

| Topic | Old conflict | Rule now |
|---|---|---|
| Cover in the page | skill: put it before `<h1>`; CLAUDE.md/memory: never | never |
| Table of contents | flat vs nested by Part | flat; nested only when the book has Parts |
| Section order | skill had no glossary; books.md had no 10 Things / Safely Skipped; template.html put Key Takeaways first | the list above |
| Paragraphs per chapter | 8+ vs "7-8" vs 6-8 vs 5-8 | 8+, averaging 100-120 words (80 minimum) |
| Page length | several line targets, some "hard gates" | soft guidance; depth is checked per chapter |
| Compaction | "HARD LIMIT: X lines" vs soft target | soft target; every MUST/SHOULD ID must survive (checked) |
| Reading PDFs | 50-80-page manual batches vs bookai | always bookai, type defaults |
| Which shelf section | ask Alex vs don't ask | To Read by default, no asking |
| Who marks a book complete | Claude set `complete: true` | only finish-book writes it |
| Coverage audit | written by the same session that wrote the page | `grade_coverage.py` (independent); hand-written audits are rejected |
| Rewrite vs patch | "if it's thin, rewrite from scratch" | fix the thin chapters the checks name; don't redo good work |
| Blockquotes | 8-15 per book vs 1+ per chapter | 8+ per book, spread through the chapters |
| Referenced Works | columns unspecified vs 3 columns | 3 columns |
| Pushing | "always push" vs "never push without review" | finish-book `--push` after all checks pass |
