#!/usr/bin/env python3
"""
add_to_shelf.py — Actually insert a book card into index.html (no more copy/paste).

Finds the view (To Read or Shelf), finds the category section (creates it if
missing), and appends a card in the same format as the existing ones.
Idempotent: if the folder already has a card, nothing changes.

Usage:
  python3 add_to_shelf.py Book_Folder --category "Options & Derivatives"
  python3 add_to_shelf.py Book_Folder --category "..." --view toread --tier now
  python3 add_to_shelf.py Book_Folder --category "..." --view shelf
  python3 add_to_shelf.py Book_Folder --category "..." --title "T" --author "A"
  python3 add_to_shelf.py Book_Folder --category "..." --dry-run

Category may be omitted if generate_books_json.py's CATEGORY_OVERRIDES knows the folder.
Prints the assigned data-book id and bmkey on success.
"""

import argparse
import html
import os
import re
import sys

BOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
SHELF_PATH = os.path.join(BOOKS_DIR, 'index.html')

sys.path.insert(0, BOOKS_DIR)
try:
    import generate_books_json as gbj
except Exception:  # pragma: no cover
    gbj = None

VIEW_END = {
    'shelf': '  </div><!-- end shelfView -->',
    'toread': '  </div><!-- end toReadView -->',
}
VIEW_START = {
    'shelf': '<div id="shelfView">',
    'toread': '<div id="toReadView"',
}
CHECK_SVG = ('<svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 '
             '1.41L9 19 21 7l-1.41-1.41z"/></svg>')


def card_html(folder, book_id, bmkey, title, author, cover, view, tier):
    t = html.escape(title, quote=False)
    a = html.escape(author, quote=False)
    tier_line = ''
    if view == 'toread' and tier:
        tier_line = f'        <span class="tier-badge tier-{tier}">{tier.capitalize()}</span>\n'
    return (
        f'    <a class="book" href="{folder}/index.html"\n'
        f'      data-book="{book_id}"\n'
        f'      data-bmkey="{bmkey}">\n'
        f'      <div class="cover-wrap">\n'
        f'        <img class="book-cover" loading="lazy"\n'
        f'          src="{folder}/{cover}"\n'
        f'          alt="{html.escape(title)}">\n'
        f'{tier_line}'
        f'        <button class="mark-read"\n'
        f'          onclick="toggleRead(event,\'{book_id}\')"\n'
        f'          title="Mark as read"></button>\n'
        f'        <button class="read-badge"\n'
        f'          onclick="toggleRead(event,\'{book_id}\')"\n'
        f'          title="Read! Click to unmark">\n'
        f'          {CHECK_SVG}\n'
        f'        </button>\n'
        f'      </div>\n'
        f'      <div class="book-title">{t}</div>\n'
        f'      <div class="book-author">{a}</div>\n'
        f'    </a>\n'
    )


def find_view(doc, view):
    s = doc.find(VIEW_START[view])
    e = doc.find(VIEW_END[view])
    if s < 0 or e < 0:
        raise SystemExit(f'ERROR: could not locate {view} view markers in index.html')
    return s, e


def section_titles(doc, s, e):
    """Yield (match_start, match_end, category_text) for h2.section-title in [s, e)."""
    for m in re.finditer(r'<h2\s+class="section-title"[^>]*>(.*?)</h2>', doc[s:e], re.S):
        cat = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()
        yield s + m.start(), s + m.end(), cat


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('folder')
    ap.add_argument('--category')
    ap.add_argument('--view', choices=['shelf', 'toread'], default='toread')
    ap.add_argument('--tier', choices=['now', 'soon', 'later'])
    ap.add_argument('--title')
    ap.add_argument('--author')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    folder = os.path.basename(args.folder.rstrip('/'))
    book_dir = os.path.join(BOOKS_DIR, folder)
    if not os.path.isfile(os.path.join(book_dir, 'index.html')):
        print(f'ERROR: {folder}/index.html not found — build the book first')
        return 1
    if not os.path.isfile(SHELF_PATH):
        print('ERROR: index.html (shelf) not found')
        return 1

    with open(SHELF_PATH, 'r', encoding='utf-8') as f:
        doc = f.read()

    # Idempotence
    m = re.search(r'<a class="book" href="' + re.escape(folder) + r'/index\.html"[^>]*?data-book="([^"]+)"[^>]*?data-bmkey="([^"]+)"', doc, re.S)
    if m:
        where = 'toread' if doc.find(VIEW_START['toread']) < m.start() else 'shelf'
        print(f'  Already on shelf ({where}) — id={m.group(1)} bmkey={m.group(2)}')
        print(f'ID={m.group(1)}\nBMKEY={m.group(2)}\nVIEW={where}')
        return 0

    # Title / author
    title, author = args.title, args.author
    if (not title or not author) and gbj is not None:
        t2, a2 = gbj.extract_title_author(folder)
        title = title or t2
        author = author or a2
    title = title or folder.replace('_', ' ')
    author = author or 'Unknown'

    # Category
    category = args.category
    if not category and gbj is not None:
        category = gbj.CATEGORY_OVERRIDES.get(folder)
    if not category:
        cats = sorted({c for _, _, c in section_titles(doc, 0, len(doc))} - {'To Read', 'Recently Added from To Read'})
        print('ERROR: --category required. Existing categories:')
        for c in cats:
            print(f'    {c}')
        return 1

    # IDs — keep books.json's id if it already knows this folder
    book_id = bmkey = None
    bj = os.path.join(BOOKS_DIR, 'books.json')
    if os.path.isfile(bj):
        try:
            import json
            for b in json.load(open(bj))['books']:
                if b.get('folder') == folder:
                    book_id, bmkey = b.get('id'), b.get('bmkey')
                    break
        except Exception:
            pass
    if not book_id:
        book_id = re.sub(r'[^a-z0-9]+', '-', folder.lower()).strip('-')
    if not bmkey:
        bmkey = 'bm_' + book_id.replace('-', '_')
    if re.search(r'data-book="' + re.escape(book_id) + '"', doc):
        book_id += '-2'
        bmkey += '_2'

    # Cover
    cover = next((c for c in ('thumb.jpg', 'cover.jpg', 'cover.svg')
                  if os.path.isfile(os.path.join(book_dir, c))), 'thumb.jpg')

    card = card_html(folder, book_id, bmkey, title, author, cover, args.view, args.tier)

    vs, ve = find_view(doc, args.view)
    titles = list(section_titles(doc, vs, ve))
    target = next(((ms, me) for ms, me, c in titles if c == category), None)

    if target:
        # Region: from this section's h2 to the next h2 (or view end)
        idx = [t[0] for t in titles].index(target[0])
        region_end = titles[idx + 1][0] if idx + 1 < len(titles) else ve
        region = doc[target[1]:region_end]
        last_a = region.rfind('</a>')
        if last_a >= 0:
            ins = target[1] + last_a + len('</a>')
            # include the trailing newline
            if doc[ins:ins + 1] == '\n':
                ins += 1
            new_doc = doc[:ins] + card + doc[ins:]
        else:
            open_div = region.find('<div class="shelf">')
            if open_div < 0:
                print(f'ERROR: section "{category}" has no <div class="shelf">')
                return 1
            ins = target[1] + open_div + len('<div class="shelf">')
            if doc[ins:ins + 1] == '\n':
                ins += 1
            new_doc = doc[:ins] + card + doc[ins:]
        action = f'appended to existing section "{category}"'
    else:
        cat_html = html.escape(category, quote=False)
        section = (f'    <h2 class="section-title">{cat_html}</h2>\n'
                   f'    <div class="shelf">\n{card}    </div>\n\n')
        if args.view == 'shelf':
            # keep "Guides" last
            guides = next(((ms, me) for ms, me, c in titles if c == 'Guides'), None)
            ins = guides[0] if guides else ve
            # back up to the start of that line
            ins = doc.rfind('\n', 0, ins) + 1
        else:
            ins = doc.rfind('\n', 0, ve) + 1
        new_doc = doc[:ins] + section + doc[ins:]
        action = f'created new section "{category}"'

    print(f'  {title} — {author}')
    print(f'  view={args.view} tier={args.tier or "-"} cover={cover} {action}')
    if args.dry_run:
        print('  (dry run — index.html not written)')
    else:
        with open(SHELF_PATH, 'w', encoding='utf-8') as f:
            f.write(new_doc)
        print('  index.html updated')
    print(f'ID={book_id}\nBMKEY={bmkey}\nVIEW={args.view}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
