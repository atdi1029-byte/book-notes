#!/usr/bin/env python3
"""
verify_quotes.py — Check that every quoted passage actually appears in the PDF.

Works on notes.md (> blockquotes) or index.html (<blockquote>). Pulls page text
with PyMuPDF, normalizes both sides (hyphenation, ligatures, curly quotes, case,
punctuation), then fuzzy-matches each quote against the page text using a
word n-gram anchor + sequence similarity. No third-party deps beyond PyMuPDF.

Also (with --check-ids) audits nugget IDs: duplicates, gaps, and priority tags
that have no [N###] ID.

Usage:
  # per-batch gate (bookai): only look at the pages this batch read
  python3 verify_quotes.py --pdf book.pdf --notes .batch_41_60.md --start 39 --end 60 \
      --json .batch_41_60.quotes.json --fail-ratio 0.5

  # whole-notes audit (uses each block's <!-- pp. --> marker to pick pages)
  python3 verify_quotes.py --pdf book.pdf --notes Book/notes.md --check-ids --json Book/quote_audit_notes.json

  # published HTML audit (searches the whole book)
  python3 verify_quotes.py --pdf book.pdf --notes Book/index.html --strict --json Book/quote_audit_html.json

Statuses:
  verified     similarity >= --threshold (default 0.82)
  paraphrased  similarity >= --partial   (default 0.60)  — wording drifted
  unverified   below --partial, or no anchor found     — treat as fabricated
  skipped      too short to test (< --min-words)

Exit codes:
  0  ok (or no text layer in the PDF — reported, not failed)
  1  --strict and any unverified quote, or --fail-ratio exceeded, or --check-ids found duplicate IDs
  2  usage / file error
"""

import argparse
import difflib
import html as htmllib
import json
import os
import re
import sys
import unicodedata
from collections import defaultdict

try:
    import pymupdf as fitz  # PyMuPDF >= 1.24
except ImportError:  # pragma: no cover
    try:
        import fitz  # older PyMuPDF
    except ImportError:
        fitz = None

MARKER_RE = re.compile(r'<!--\s*pp?\.\s*(\d+)(?:\s*-\s*(\d+))?\s*-->')
NUGGET_ID_RE = re.compile(r'\[N(\d+)\]')
TAG_RE = re.compile(r'\[(MUST KNOW|SHOULD KNOW|NICE TO KNOW)\]')
TAG_NO_ID_RE = re.compile(r'\[(MUST KNOW|SHOULD KNOW|NICE TO KNOW)\](?!\s*\[N\d+\])')
ELLIPSIS_RE = re.compile(r'\s*(?:\.\.\.|…|\[\.\.\.\]|\[…\])\s*')


# ── Normalization ─────────────────────────────────────────────────────────

def normalize(text):
    """Lowercase alnum words only; fix hyphenation/ligatures/curly quotes."""
    text = text.replace('\u00ad', '')                 # soft hyphen
    text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)  # hyphen-ated line breaks
    text = text.replace('\n', ' ')
    text = unicodedata.normalize('NFKD', text)        # ﬁ -> fi, é -> e + accent
    text = ''.join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[’'`]", '', text)                 # don't -> dont (both sides)
    text = re.sub(r'[^a-z0-9]+', ' ', text)
    return text.split()


# ── Quote extraction ──────────────────────────────────────────────────────

def clean_quote(q):
    q = htmllib.unescape(q)
    q = re.sub(r'\s+', ' ', q).strip()
    q = q.strip('"“”„\'‘’«» ')
    # drop trailing "(p. 12)" / "(Chapter 4)"
    q = re.sub(r'\s*\((?:p|pp|ch|chapter|loc)\b[^)]*\)\s*$', '', q, flags=re.I)
    # drop trailing attribution after a dash: "— Keynes", "– p. 44", "-- Chapter 3"
    for sep in (' — ', ' – ', ' -- ', ' —', '—'):
        if sep in q:
            head, tail = q.rsplit(sep, 1)
            tail = tail.strip()
            if head.strip() and len(tail.split()) <= 12 and (
                tail[:1].isupper() or len(tail.split()) <= 3
                or re.match(r'(p|pp|ch|chapter|loc)\b', tail, re.I)
                or re.search(r'\b(p|pp)\.?\s*\d', tail)
            ):
                q = head.strip()
                break
    q = q.strip('"“”„\'‘’«» ')
    return q


def extract_md_quotes(text):
    """Return list of (quote, page_start, page_end, line_no). Consecutive '>' lines join."""
    quotes = []
    cur_range = (None, None)
    buf, buf_line = [], None
    for i, line in enumerate(text.splitlines(), 1):
        m = MARKER_RE.search(line)
        if m:
            s = int(m.group(1))
            e = int(m.group(2)) if m.group(2) else s
            cur_range = (s, e)
        if line.lstrip().startswith('>'):
            body = line.lstrip()[1:].strip()
            if body.startswith('[!'):       # > [!NOTE] admonitions
                continue
            # A new quoted passage on the very next '>' line (no blank line
            # between): a line that opens with a quote mark starts a new quote.
            if buf and body[:1] in '"“„':
                quotes.append((clean_quote(' '.join(buf)), cur_range[0], cur_range[1], buf_line))
                buf, buf_line = [], None
            if buf_line is None:
                buf_line = i
            buf.append(body)
        else:
            if buf:
                quotes.append((clean_quote(' '.join(buf)), cur_range[0], cur_range[1], buf_line))
                buf, buf_line = [], None
    if buf:
        quotes.append((clean_quote(' '.join(buf)), cur_range[0], cur_range[1], buf_line))
    return quotes


def extract_html_quotes(text):
    quotes = []
    for m in re.finditer(r'<blockquote\b[^>]*>(.*?)</blockquote>', text, re.S | re.I):
        inner = m.group(1)
        inner = re.sub(r'<(cite|footer)\b[^>]*>.*?</\1>', ' ', inner, flags=re.S | re.I)
        inner = re.sub(r'<br\s*/?>', ' ', inner, flags=re.I)
        inner = re.sub(r'</p>', ' ', inner, flags=re.I)
        inner = re.sub(r'<[^>]+>', '', inner)
        line_no = text.count('\n', 0, m.start()) + 1
        quotes.append((clean_quote(inner), None, None, line_no))
    return quotes


# ── PDF text + n-gram index ───────────────────────────────────────────────

class BookText:
    def __init__(self, pdf_path, page_start=None, page_end=None):
        doc = fitz.open(pdf_path)
        self.page_count = len(doc)
        lo = max(1, page_start or 1)
        hi = min(self.page_count, page_end or self.page_count)
        self.words = []       # normalized words
        self.word_page = []   # page number per word (1-based)
        self.pages_scanned = 0
        for pno in range(lo, hi + 1):
            w = normalize(doc[pno - 1].get_text('text'))
            self.words.extend(w)
            self.word_page.extend([pno] * len(w))
            self.pages_scanned += 1
        self.text_layer = self.pages_scanned > 0 and (len(self.words) / self.pages_scanned) >= 15
        self._index = {}

    def index(self, g):
        if g not in self._index:
            idx = defaultdict(list)
            w = self.words
            for i in range(len(w) - g + 1):
                idx[tuple(w[i:i + g])].append(i)
            self._index[g] = idx
        return self._index[g]

    def best_match(self, qwords, page_lo=None, page_hi=None):
        """Return (score, page, snippet) for the best window in the text."""
        n = len(qwords)
        if n == 0 or not self.words:
            return 0.0, None, ''
        # Candidate start positions via n-gram anchors (4, then 3, then 2)
        cands = None
        for g in (4, 3, 2):
            if n < g:
                continue
            idx = self.index(g)
            votes = defaultdict(int)
            for k in range(n - g + 1):
                for pos in idx.get(tuple(qwords[k:k + g]), ()):
                    votes[pos - k] += 1
            if votes:
                cands = votes
                break
        if not cands:
            return 0.0, None, ''
        # Restrict to page range when known
        if page_lo is not None:
            ranged = {s: v for s, v in cands.items()
                      if s >= 0 and page_lo <= self.word_page[min(max(s, 0), len(self.word_page) - 1)] <= page_hi}
            if ranged:
                cands = ranged
        top = sorted(cands.items(), key=lambda t: -t[1])[:8]
        qstr = ' '.join(qwords)
        best = (0.0, None, '')
        for s, _v in top:
            for shift in range(-3, 4):
                for extra in (0, -1, 1, -2, 2, 3):
                    a = s + shift
                    b = a + n + extra
                    if a < 0 or b > len(self.words) or b <= a:
                        continue
                    win = self.words[a:b]
                    score = difflib.SequenceMatcher(None, ' '.join(win), qstr, autojunk=False).ratio()
                    if score > best[0]:
                        best = (score, self.word_page[a], ' '.join(win))
                        if score >= 0.995:
                            return best
        return best


# ── ID checks ─────────────────────────────────────────────────────────────

def check_ids(text):
    ids = [int(x) for x in NUGGET_ID_RE.findall(text)]
    seen, dupes = set(), []
    for i in ids:
        if i in seen and i not in dupes:
            dupes.append(i)
        seen.add(i)
    gaps = []
    if ids:
        expected = set(range(1, max(ids) + 1))
        gaps = sorted(expected - set(ids))
    tags_total = len(TAG_RE.findall(text))
    tags_no_id = len(TAG_NO_ID_RE.findall(text))
    sequential = ids == sorted(set(ids)) and not gaps and not dupes
    return {
        'total_ids': len(ids),
        'unique_ids': len(set(ids)),
        'duplicates': dupes[:50],
        'gaps': gaps[:50],
        'tags_total': tags_total,
        'tags_without_id': tags_no_id,
        'sequential': sequential,
    }


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pdf', required=True)
    ap.add_argument('--notes', required=True, help='notes.md, a batch .md, or index.html')
    ap.add_argument('--start', type=int, help='first PDF page to search (default: from markers / whole book)')
    ap.add_argument('--end', type=int, help='last PDF page to search')
    ap.add_argument('--margin', type=int, default=2, help='pages of slack around a block marker (default 2)')
    ap.add_argument('--threshold', type=float, default=0.82)
    ap.add_argument('--partial', type=float, default=0.60)
    ap.add_argument('--min-words', type=int, default=4)
    ap.add_argument('--check-ids', action='store_true')
    ap.add_argument('--strict', action='store_true', help='exit 1 if any quote is unverified')
    ap.add_argument('--fail-ratio', type=float, help='exit 1 if unverified/tested > R (and >= 2 unverified)')
    ap.add_argument('--json', help='write full report here')
    ap.add_argument('--quiet', action='store_true')
    args = ap.parse_args()

    if fitz is None:
        print('ERROR: PyMuPDF not installed (pip install pymupdf)')
        return 2
    if not os.path.isfile(args.pdf):
        print(f'ERROR: PDF not found: {args.pdf}')
        return 2
    if not os.path.isfile(args.notes):
        print(f'ERROR: notes not found: {args.notes}')
        return 2

    with open(args.notes, 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()
    is_html = args.notes.lower().endswith(('.html', '.htm'))
    raw_quotes = extract_html_quotes(text) if is_html else extract_md_quotes(text)

    # Decide which pages to load: explicit range, else marker range (+margin), else whole book
    if args.start or args.end:
        load_lo, load_hi = args.start, args.end
    else:
        load_lo = load_hi = None
    book = BookText(args.pdf, load_lo, load_hi)

    report = {
        'pdf': os.path.basename(args.pdf),
        'notes': os.path.basename(args.notes),
        'pages_scanned': book.pages_scanned,
        'text_layer': book.text_layer,
        'threshold': args.threshold,
        'partial': args.partial,
        'quotes': [],
        'summary': {},
    }

    counts = {'verified': 0, 'paraphrased': 0, 'unverified': 0, 'skipped': 0}

    if not book.text_layer:
        report['summary'] = {'note': 'PDF has no usable text layer — quote check skipped', **counts}
        if not args.quiet:
            print('  QUOTE CHECK SKIPPED — PDF has no usable text layer '
                  f'({len(book.words)} words over {book.pages_scanned} pages)')
    else:
        for q, ps, pe, line_no in raw_quotes:
            entry = {'line': line_no, 'quote': q[:200], 'status': None, 'score': 0.0, 'page': None}
            if ps is not None:
                entry['marker_pages'] = [ps, pe]
            parts = [p for p in ELLIPSIS_RE.split(q) if p and len(normalize(p)) >= 3]
            if not parts or len(normalize(q)) < args.min_words:
                entry['status'] = 'skipped'
                counts['skipped'] += 1
                report['quotes'].append(entry)
                continue
            # page window for this quote
            if args.start or args.end:
                lo, hi = args.start or 1, args.end or book.page_count
            elif ps is not None:
                lo, hi = max(1, ps - args.margin), pe + args.margin
            else:
                lo = hi = None
            scores, pages, snippets = [], [], []
            for part in parts:
                qw = normalize(part)
                sc, pg, snip = book.best_match(qw, lo, hi)
                # If ranged search failed, try the whole scanned text once
                if sc < args.partial and lo is not None:
                    sc2, pg2, snip2 = book.best_match(qw, None, None)
                    if sc2 > sc:
                        sc, pg, snip = sc2, pg2, snip2
                        entry['found_outside_marker'] = True
                scores.append(sc)
                pages.append(pg)
                snippets.append(snip)
            score = min(scores)
            entry['score'] = round(score, 3)
            entry['page'] = next((p for p in pages if p), None)
            if score >= args.threshold:
                entry['status'] = 'verified'
            elif score >= args.partial:
                entry['status'] = 'paraphrased'
                entry['closest'] = ' '.join(snippets)[:200]
            else:
                entry['status'] = 'unverified'
                if score > 0:
                    entry['closest'] = ' '.join(snippets)[:200]
            counts[entry['status']] += 1
            report['quotes'].append(entry)
        report['summary'] = dict(counts)
        report['summary']['tested'] = counts['verified'] + counts['paraphrased'] + counts['unverified']

    id_fail = False
    if args.check_ids and not is_html:
        ids = check_ids(text)
        report['ids'] = ids
        id_fail = bool(ids['duplicates'])

    if args.json:
        with open(args.json, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)

    tested = report['summary'].get('tested', 0)
    if not args.quiet and book.text_layer:
        print(f"  Quotes: {tested} tested — {counts['verified']} verified, "
              f"{counts['paraphrased']} paraphrased, {counts['unverified']} unverified"
              + (f", {counts['skipped']} skipped (too short)" if counts['skipped'] else ''))
        for e in report['quotes']:
            if e['status'] in ('unverified', 'paraphrased'):
                where = f"line {e['line']}"
                if e.get('marker_pages'):
                    where += f", pp. {e['marker_pages'][0]}-{e['marker_pages'][1]}"
                print(f"    {e['status'].upper():11} ({e['score']:.2f}) {where}: \"{e['quote'][:90]}\"")
                if e.get('closest'):
                    print(f"                closest: \"{e['closest'][:90]}\"")
    if args.check_ids and not is_html and not args.quiet:
        ids = report['ids']
        print(f"  IDs: {ids['unique_ids']} unique of {ids['total_ids']}"
              + (f" — DUPLICATES: {ids['duplicates'][:10]}" if ids['duplicates'] else '')
              + (f" — gaps: {ids['gaps'][:10]}" if ids['gaps'] else '')
              + (f" — {ids['tags_without_id']} priority tags without an ID" if ids['tags_without_id'] else '')
              + ('' if ids['sequential'] else ' — NOT sequential'))

    # Exit status
    unv = counts['unverified']
    if id_fail:
        return 1
    if args.strict and unv > 0:
        return 1
    if args.fail_ratio is not None and tested > 0 and unv >= 2 and (unv / tested) > args.fail_ratio:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
