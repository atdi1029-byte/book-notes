#!/usr/bin/env python3
"""
check_html.py — check a book page against the layout rules (book_rules.json).

  ./check_html.py Book_Folder              full check (before finish-book)
  ./check_html.py Book_Folder --progress   while writing: per-chapter table and
                                           depth trend for the chapters written
                                           so far; missing end sections are fine
  ./check_html.py Book_Folder --json       machine-readable result
  ./check_html.py Book_Folder --page plain.html

Errors are PIPELINE.md "must" rules (section order, 8+ paragraphs per chapter,
no cover image, bookmarks, table formats, ...); warnings are "should" rules.
Exit: 0 no errors, 1 errors, 2 usage/file problem.
"""

import html as htmllib
import json
import os
import re
import sys

BOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
RULES = json.load(open(os.path.join(BOOKS_DIR, 'book_rules.json'), encoding='utf-8'))
TAG_RE = re.compile(r'<[^>]+>')


def text_of(fragment):
    return re.sub(r'\s+', ' ', htmllib.unescape(TAG_RE.sub(' ', fragment))).strip()


def words(fragment):
    return len(text_of(fragment).split())


def paragraphs(fragment):
    out = []
    for m in re.finditer(r'<p\b([^>]*)>(.*?)</p>', fragment, re.S | re.I):
        attrs, body = m.group(1), m.group(2)
        if 'subtitle' in attrs or 'caption' in attrs:
            continue
        if words(body) == 0:
            continue
        out.append(body)
    return out


def sentences(fragment):
    t = text_of(fragment)
    return len(re.findall(r'[.!?]["”’)]?(\s|$)', t))


def split_sections(doc):
    """[(title, id, html_after_heading, start_offset)] for every <h2>."""
    heads = list(re.finditer(r'<h2\b([^>]*)>(.*?)</h2>', doc, re.S | re.I))
    out = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(doc)
        idm = re.search(r'\bid\s*=\s*["\']([^"\']+)', m.group(1))
        in_nav = doc.rfind('<nav', 0, m.start()) > doc.rfind('</nav>', 0, m.start())
        out.append({'title': text_of(m.group(2)).replace('\U0001F516', '').strip(), 'id': idm.group(1) if idm else None,
                    'html': doc[m.end():end], 'toc': in_nav, 'offset': m.start()})
    return out


def classify(title, sid):
    """Section key for an <h2>, or None for a chapter. Titles are matched at
    their start (after numbering/emoji), so a chapter called "Jason Shapiro:
    The Contrarian" is still a chapter."""
    if sid == 'glossary':
        return 'glossary'
    t = re.sub(r'^[^A-Za-z]+', '', title).strip()
    for s in RULES['section_order']:
        if s['key'] == 'chapters' or not s['match']:
            continue
        if re.search(s['match'], t, re.I):
            return s['key']
    return None


def table_shape(fragment):
    """(columns, data_rows) of the first table in fragment, or None."""
    m = re.search(r'<table\b.*?</table>', fragment, re.S | re.I)
    if not m:
        return None
    rows = re.findall(r'<tr\b.*?</tr>', m.group(0), re.S | re.I)
    if not rows:
        return None
    cols = max(len(re.findall(r'<t[hd]\b', r, re.I)) for r in rows)
    data = [r for r in rows if re.search(r'<td\b', r, re.I)]
    return cols, len(data)


def check(folder, page='index.html', progress=False):
    path = os.path.join(BOOKS_DIR, folder, page)
    if not os.path.isfile(path):
        return None
    doc = open(path, encoding='utf-8', errors='replace').read()
    book_type = ''
    try:
        book_type = json.load(open(os.path.join(BOOKS_DIR, folder, '.run_state.json'))).get('type', '')
    except Exception:
        pass
    errors, warnings = [], []
    E, W = errors.append, warnings.append
    B, C = RULES['book'], RULES['chapter']

    sections = [s for s in split_sections(doc) if not s['toc']]
    order_keys = [s['key'] for s in RULES['section_order']]
    rank = {k: i for i, k in enumerate(order_keys)}

    # Every <h2> is either a named section or a chapter.
    for s in sections:
        s['key'] = classify(s['title'], s['id']) or 'chapters'
    chapters = [s for s in sections if s['key'] == 'chapters']
    present = {}
    for s in sections:
        present.setdefault(s['key'], s)

    # ── section presence and order ──
    if not progress:
        for spec in RULES['section_order']:
            k, req = spec['key'], spec['required']
            if req == 'for_types':
                req = book_type in spec.get('types', [])
            if req and k not in present:
                E(f'missing section: {spec["title"]}')
        last, last_title, misplaced = -1, '', []
        for s in sections:
            r = rank[s['key']]
            if r < last:
                misplaced.append(f'"{s["title"][:50]}" comes after "{last_title[:50]}"')
            else:
                last, last_title = r, s['title']
        if misplaced:
            more = f' (+{len(misplaced) - 1} more)' if len(misplaced) > 1 else ''
            E('sections out of order: ' + misplaced[0] + more +
              ' — order is ' + ', '.join(x['title'] for x in RULES['section_order'] if x['key'] != 'footer'))

    # ── page-wide rules ──
    if re.search(r'<img\b[^>]*src=["\'][^"\']*cover\.(jpe?g|png)', doc, re.I):
        E('cover image inside the page (covers go on the shelf only)')
    bm = re.search(r'\b(var|let|const)\s+BM_KEY\s*=', doc)
    js = re.search(r'<script[^>]+src=["\'][^"\']*book\.js', doc)
    if not bm or not js:
        E('BM_KEY and book.js must both be present (bookmarks/progress)')
    elif bm.start() > js.start():
        E('BM_KEY must be set before book.js loads')
    elif bm.group(1) != 'var':
        W('use `var BM_KEY` (not let/const)')
    if not re.search(r'<nav\b[^>]*class=["\'][^"\']*\btoc\b', doc):
        E('no <nav class="toc"> table of contents')
    for s in sections:
        if not s['id']:
            E(f'<h2> without an id (no bookmark): "{s["title"][:50]}"')
    for m in re.finditer(r'<table\b([^>]*)>', doc, re.I):
        if 'role="presentation"' not in m.group(1) and "role='presentation'" not in m.group(1):
            E('a <table> without role="presentation" (text-to-speech reads it as a grid)')
            break
    strongs = len(re.findall(r'<strong\b', doc, re.I))
    quotes = re.findall(r'<blockquote\b.*?</blockquote>', doc, re.S | re.I)
    if not progress:
        if strongs < B['min_strong']:
            E(f'only {strongs} <strong> key terms (need {B["min_strong"]}+)')
        if len(quotes) < B['min_blockquotes']:
            E(f'only {len(quotes)} inline <blockquote>s (need {B["min_blockquotes"]}+)')
    no_cite = sum(1 for q in quotes if '<cite' not in q.lower())
    if no_cite:
        W(f'{no_cite} <blockquote>(s) without a <cite>')

    # ── chapters ──
    rows = []
    for s in chapters:
        title = s['title']
        ps = paragraphs(s['html'])
        n = len(ps)
        avg = round(sum(words(p) for p in ps) / n) if n else 0
        bq = len(re.findall(r'<blockquote\b', s['html'], re.I))
        part = bool(re.search(C['part_header_match'], title, re.I)) and n < C['min_paragraphs']
        rows.append({'title': title, 'paragraphs': n, 'avg_words': avg, 'blockquotes': bq, 'part_header': part})
        if re.search(C['combined_heading_match'], title, re.I):
            E(f'combined chapters in one heading: "{title[:60]}" (every chapter gets its own <h2>)')
        if part:
            continue
        if n < C['min_paragraphs']:
            E(f'"{title[:60]}": {n} paragraphs (need {C["min_paragraphs"]}+)')
        elif avg < C['min_avg_words']:
            E(f'"{title[:60]}": paragraphs average {avg} words (need {C["min_avg_words"]}+, aim {C["target_avg_words"]}-120)')
        elif avg < C['target_avg_words']:
            W(f'"{title[:60]}": paragraphs average {avg} words (aim {C["target_avg_words"]}-120)')
    real = [r for r in rows if not r['part_header']]
    no_quote = [r for r in real if r['blockquotes'] == 0]
    if no_quote and real:
        W(f'{len(no_quote)} of {len(real)} chapters have no inline blockquote')
    if len(real) >= 6:
        third = max(2, len(real) // 3)
        first = sum(r['paragraphs'] for r in real[:third]) / third
        last_ = sum(r['paragraphs'] for r in real[-third:]) / third
        if first and last_ / first < C['depth_drop_ratio']:
            E(f'later chapters are thinner: last third averages {last_:.1f} paragraphs vs {first:.1f} in the first third')
    if not chapters:
        E('no chapter sections found')

    # ── end sections ──
    def sub_count(key, tag='h3'):
        s = present.get(key)
        return len(re.findall(rf'<{tag}\b', s['html'], re.I)) if s else 0

    if 'ten_things' in present:
        items = len(re.findall(r'<li\b', present['ten_things']['html'], re.I))
        if items != B['ten_things_items']:
            W(f'"If You Only Remember 10 Things" has {items} items')
    if 'skipped' in present:
        n = sub_count('skipped')
        if n < B['skipped_min_entries']:
            E(f'"What Can Be Safely Skipped" has {n} <h3> entries (need {B["skipped_min_entries"]}-{B["skipped_max_entries"]})')
        elif n > B['skipped_max_entries']:
            W(f'"What Can Be Safely Skipped" has {n} entries (aim {B["skipped_min_entries"]}-{B["skipped_max_entries"]})')
    if 'trading' in present and sub_count('trading') < B['trading_min_lessons']:
        E(f'"Trading & Investing Lessons" has {sub_count("trading")} <h3> lessons (need {B["trading_min_lessons"]}+)')
    for key in B['subheaded_sections']:
        s = present.get(key)
        if s and sub_count(key) == 0 and re.search(r'<p>\s*<strong>', s['html'], re.I):
            E(f'"{s["title"]}" uses <p><strong> items — use <h3> so each gets a bookmark')
    if 'allegories' in present:
        shape = table_shape(present['allegories']['html'])
        if not shape:
            E('Allegories & Cultural References must be a table (Reference | Concept Illustrated)')
        else:
            cols, n = shape
            if cols != B['allegories_columns']:
                E(f'Allegories table has {cols} columns (must be {B["allegories_columns"]})')
            if n < B['allegories_min_rows']:
                E(f'Allegories table has {n} rows (need {B["allegories_min_rows"]}+)')
    if 'references' in present:
        shape = table_shape(present['references']['html'])
        if shape and shape[0] != B['references_columns']:
            E(f'Referenced Works table has {shape[0]} columns (must be {B["references_columns"]}: Name | Work/Role | Connection)')
        elif not shape:
            W('Referenced Works is not a table (Name | Work/Role | Connection)')
    if 'didnt_fit' in present:
        parts = re.split(r'<h3\b', present['didnt_fit']['html'], flags=re.I)[1:]
        short = sum(1 for p in parts if sentences(p) < B['didnt_fit_min_sentences'])
        if not parts:
            W('"What Didn\'t Fit" has no <h3> sub-sections')
        elif short:
            W(f'{short} "What Didn\'t Fit" sub-section(s) under {B["didnt_fit_min_sentences"]} sentences')
    if 'about_author' in present:
        n = len(paragraphs(present['about_author']['html']))
        if n < B['about_author_min_paragraphs']:
            E(f'"About the Author" has {n} paragraph(s) (need 2-3)')
    if 'glossary' in present:
        g = present['glossary']['html']
        terms = len(re.findall(r'<(p|li|br)\b[^>]*>\s*<strong>', g, re.I))
        if terms < B['glossary_min_terms']:
            W(f'glossary has {terms} terms (20-40 for lighter books, 50-70 for dense ones)')
    if 'footer' not in present and not re.search(r'<footer\b|class=["\'][^"\']*footer', doc, re.I) and not progress:
        W('no footer (author, year, pages, summary blurb)')

    # ── length and wrapping (soft) ──
    lines = doc.split('\n')
    long_share = sum(1 for l in lines if len(l) > B['long_line_chars']) / max(1, len(lines))
    if long_share > B['long_line_share_warn']:
        W(f'{long_share:.0%} of lines are over {B["long_line_chars"]} characters (wrap prose at ~70)')

    return {'folder': folder, 'page': page, 'type': book_type, 'lines': len(lines), 'strong': strongs,
            'blockquotes': len(quotes), 'chapters': rows, 'sections': [s['key'] for s in sections],
            'errors': errors, 'warnings': warnings}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = [a for a in sys.argv[1:] if a.startswith('--')]
    if not args:
        print(__doc__)
        return 2
    folder = os.path.basename(args[0].rstrip('/'))
    page = 'index.html'
    if '--page' in sys.argv:
        page = sys.argv[sys.argv.index('--page') + 1]
        if page in args:
            args.remove(page)
    progress = '--progress' in flags
    res = check(folder, page, progress)
    if res is None:
        print(f'{folder}/{page} not found')
        return 2
    if '--json' in flags:
        print(json.dumps(res, indent=2))
        return 1 if res['errors'] else 0

    print(f'═══ check_html: {folder}/{page} ({res["lines"]} lines, {res["strong"]} <strong>, {res["blockquotes"]} blockquotes) ═══')
    print(f'{"#":>3}  {"paras":>5}  {"avg w":>5}  {"quotes":>6}  chapter')
    for i, r in enumerate(res['chapters'], 1):
        flag = ''
        if r['part_header']:
            flag = '  (part header)'
        elif r['paragraphs'] < RULES['chapter']['min_paragraphs'] or r['avg_words'] < RULES['chapter']['min_avg_words']:
            flag = '  ✗'
        print(f'{i:>3}  {r["paragraphs"]:>5}  {r["avg_words"]:>5}  {r["blockquotes"]:>6}  {r["title"][:60]}{flag}')
    if res['errors']:
        print(f'\nERRORS ({len(res["errors"])}):')
        for e in res['errors']:
            print('  ✗ ' + e)
    if res['warnings']:
        print(f'\nWarnings ({len(res["warnings"])}):')
        for w in res['warnings']:
            print('  ⚠ ' + w)
    print('\n' + ('FAIL' if res['errors'] else 'PASS') + (' (progress check — end sections not required yet)' if progress else ''))
    return 1 if res['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
