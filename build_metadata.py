#!/usr/bin/env python3
"""
Build metadata for the Book Universe explorer.

Outputs:
  metadata.json     — lightweight index (~15-20 KB)
                      categories, book stubs, adjacency,
                      mostConnected, precomputed sorts
  metadata/<id>.json — per-book detail (~2-4 KB each)
                       references, connections with shared
                       thinkers, keywords

The browser loads metadata.json once, then lazy-fetches
per-book files only when someone clicks into a book.
"""

import json
import os
import re
from collections import Counter

BOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
SHELF_PATH = os.path.join(BOOKS_DIR, 'index.html')
OUT_INDEX = os.path.join(BOOKS_DIR, 'metadata.json')
OUT_DIR = os.path.join(BOOKS_DIR, 'metadata')

# ── Keyword extraction ──

# Domain-specific keywords to tag books with
KEYWORD_DICT = {
    'macro': ['macro', 'macroeconom', 'gdp', 'fiscal',
        'monetary policy', 'central bank', 'fed ',
        'federal reserve', 'treasury', 'inflation',
        'deflation', 'stimulus'],
    'cycles': ['cycle', 'turning', 'secular', 'wave',
        'seasonal', 'timing', 'rhythm', 'periodicity',
        'oscillat'],
    'debt': ['debt', 'credit', 'leverage', 'default',
        'sovereign', 'deleveraging', 'bond',
        'interest rate', 'yield'],
    'money': ['money', 'currency', 'gold', 'silver',
        'fiat', 'banking', 'monetary', 'mint',
        'coinage'],
    'risk': ['risk', 'volatility', 'drawdown', 'hedge',
        'tail risk', 'black swan', 'antifragil',
        'position siz', 'kelly criterion'],
    'psychology': ['psycholog', 'bias', 'heuristic',
        'cognitive', 'behavior', 'emotion', 'fear',
        'greed', 'overconfiden', 'habit'],
    'history': ['history', 'historical', 'century',
        'empire', 'civiliz', 'ancient', 'medieval',
        'war ', 'revolution', 'dynasty'],
    'investing': ['invest', 'portfolio', 'asset allocat',
        'diversif', 'rebalance', 'compound',
        'dividend', 'valuation', 'stock',
        'equity', 'index fund'],
    'trading': ['trading', 'trader', 'technical analysis',
        'chart', 'momentum', 'trend', 'signal',
        'backtest', 'systematic'],
    'economics': ['econom', 'supply', 'demand', 'market',
        'capitalism', 'socialism', 'free market',
        'price', 'marginal', 'scarcity'],
    'geopolitics': ['geopolit', 'power', 'hegemony',
        'empire', 'nation', 'institution',
        'governance', 'democra', 'authorit'],
    'probability': ['probability', 'statistic', 'random',
        'stochastic', 'expected value', 'variance',
        'distribut', 'monte carlo', 'regression'],
    'options': ['option', 'derivative', 'call ', 'put ',
        'strike', 'expir', 'volatility', 'greek',
        'premium'],
    'commodities': ['commodity', 'oil', 'gold', 'silver',
        'copper', 'wheat', 'energy', 'crude',
        'natural gas'],
    'quant': ['quant', 'algorithm', 'model', 'formula',
        'mathematical', 'computation', 'simulat',
        'optimize'],
    'habits': ['habit', 'routine', 'discipline',
        'consistency', 'compound', 'identity',
        'cue', 'reward', 'behavior change'],
    'wealth': ['wealth', 'rich', 'millionaire',
        'financial independence', 'retire', 'saving',
        'frugal', 'net worth', 'income'],
    'forex': ['forex', 'currency', 'exchange rate',
        'dollar', 'euro', 'yen', 'yuan',
        'devaluat', 'peg'],
}


def extract_keywords(book):
    """Extract keywords from title, references, and category."""
    text = ' '.join([
        book['title'].lower(),
        book['author'].lower(),
        book['category'].lower(),
        book.get('superCategory', '').lower(),
    ])
    # Add reference names and descriptions
    for ref in book.get('references', []):
        text += ' ' + ref['name'].lower()
        text += ' ' + ref.get('desc', '').lower()
        text += ' ' + ref.get('connection', '').lower()

    keywords = set()
    for kw, patterns in KEYWORD_DICT.items():
        for pat in patterns:
            if pat in text:
                keywords.add(kw)
                break

    return sorted(keywords)


# ── Parse shelf HTML ──

def parse_shelf_with_regex(html):
    """Parse shelf HTML using regex — handles multi-line attrs."""
    books = []
    seen_ids = set()

    shelf_end = html.find('id="toReadView"')
    if shelf_end == -1:
        shelf_end = len(html)

    section_pattern = re.compile(
        r'<h2\s+class="section-title"[^>]*>(.*?)</h2>',
        re.DOTALL
    )

    book_pattern = re.compile(
        r'<a\s+class="book"\s+href="([^"]+)"[^>]*'
        r'data-book="([^"]+)"[^>]*>.*?'
        r'<div\s+class="book-title">(.*?)</div>\s*'
        r'<div\s+class="book-author">(.*?)</div>',
        re.DOTALL
    )

    sections = []
    for m in section_pattern.finditer(html):
        cat_text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        cat_text = cat_text.replace('&amp;', '&')
        sections.append((m.start(), cat_text))

    def get_category(pos):
        cat = ''
        for s_pos, s_cat in sections:
            if s_pos <= pos:
                cat = s_cat
            else:
                break
        return cat

    for m in book_pattern.finditer(html):
        href = m.group(1)
        book_id = m.group(2)
        title = re.sub(r'<[^>]+>', '', m.group(3)).strip()
        title = (title.replace('&amp;', '&')
                      .replace('&mdash;', '—'))
        author = re.sub(r'<[^>]+>', '', m.group(4)).strip()
        author = author.replace('&amp;', '&')

        if 'plain.html' in href:
            continue
        if book_id in seen_ids:
            continue
        seen_ids.add(book_id)

        category = get_category(m.start())
        if category in ('Guides', 'To Read', ''):
            continue
        if 'Recently Added' in category:
            continue

        book_dir = href.split('/')[0] if '/' in href else href
        is_read = m.start() < shelf_end

        books.append({
            'id': book_id,
            'dir': book_dir,
            'href': href,
            'title': title,
            'author': author,
            'category': category,
            'isRead': is_read,
        })

    categories = list(dict.fromkeys(
        b['category'] for b in books))
    return books, categories


# ── Parse referenced works ──

def parse_references(book_dir):
    """Extract referenced works table from a book's HTML."""
    path = os.path.join(BOOKS_DIR, book_dir, 'index.html')
    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    ref_start = None
    for m in re.finditer(
        r'<h2[^>]*>[^<]*Referenced[^<]*</h2>',
        html, re.IGNORECASE
    ):
        ref_start = m.end()
    if ref_start is None:
        for m in re.finditer(
            r'<h2[^>]*>[^<]*&amp;[^<]*Referenced[^<]*</h2>',
            html, re.IGNORECASE
        ):
            ref_start = m.end()
    if ref_start is None:
        return []

    next_h2 = re.search(r'<h2', html[ref_start:])
    end = (ref_start + next_h2.start()
           if next_h2 else len(html))
    section = html[ref_start:end]

    rows = []
    for tr in re.finditer(
        r'<tr[^>]*>(.*?)</tr>', section, re.DOTALL
    ):
        tds = re.findall(
            r'<td[^>]*>(.*?)</td>', tr.group(1), re.DOTALL)
        if len(tds) >= 1:
            name = re.sub(r'<[^>]+>', '', tds[0]).strip()
            name = re.sub(r'\s*\(.*\)\s*$', '', name).strip()
            name = (name.replace('\u201c', '')
                        .replace('\u201d', '')
                        .replace('"', '')
                        .replace('\u2018', '')
                        .replace('\u2019', ''))
            desc = ''
            if len(tds) >= 2:
                desc = re.sub(r'<[^>]+>', '', tds[1]).strip()
            connection = ''
            if len(tds) >= 3:
                connection = re.sub(
                    r'<[^>]+>', '', tds[2]).strip()
            if name and len(name) > 1:
                rows.append({
                    'name': name,
                    'desc': desc,
                    'connection': connection,
                })
    return rows


# ── Cross-references ──

def get_surnames(author_str):
    parts = re.split(r'[,&]+', author_str)
    surnames = []
    for part in parts:
        words = part.strip().split()
        if words:
            surname = words[-1]
            if len(surname) >= 3:
                surnames.append(surname)
    return surnames


def compute_cross_refs(books):
    edges = []
    edge_set = set()

    for i, book_a in enumerate(books):
        if not book_a.get('references'):
            continue
        for j, book_b in enumerate(books):
            if i == j:
                continue
            surnames = get_surnames(book_b['author'])
            if not surnames:
                continue

            matches = []
            for ref in book_a['references']:
                ref_lower = ref['name'].lower()
                for sn in surnames:
                    if sn.lower() in ref_lower:
                        matches.append(ref['name'])
                        break
                title_lower = book_b['title'].lower()
                full = (ref_lower + ' '
                        + ref.get('desc', '').lower())
                if title_lower in full:
                    if ref['name'] not in matches:
                        matches.append(ref['name'])

            if matches:
                key = tuple(sorted(
                    [book_a['id'], book_b['id']]))
                if key not in edge_set:
                    edge_set.add(key)
                    edges.append({
                        'source': book_a['id'],
                        'target': book_b['id'],
                        'shared': list(set(matches)),
                    })
                else:
                    for e in edges:
                        k = tuple(sorted(
                            [e['source'], e['target']]))
                        if k == key:
                            existing = set(
                                e.get('shared', []))
                            existing.update(matches)
                            e['shared'] = list(existing)
                            e['bidirectional'] = True
                            break

    return edges


# ── Super-categories ──

SUPER_CATEGORIES = {
    'Finance & Investing': [
        'Personal Finance Basics',
        'Investing Fundamentals',
        'Portfolio Management & Asset Allocation',
        'Fixed Income & Bonds',
        'Options & Derivatives',
    ],
    'Economics': [
        'Economics Fundamentals',
        'Free Markets & Political Economy',
        'Monetary Policy & Central Banking',
    ],
    'Markets & Trading': [
        'Technical Analysis',
        'Risk Management & Position Sizing',
        'Cycles & Market Timing',
        'Commodities & Energy',
        'Forex & Currencies',
    ],
    'History & Crises': [
        'Economic History & Financial Crises',
        'Wall Street Stories & Biographies',
    ],
    'Macro & Geopolitics': [
        'Macro Investing & Geopolitics',
        'Geopolitics, Sociology & Power',
    ],
    'Mind & Behavior': [
        'Behavioral Finance & Psychology',
        'Self-Development & Mindset',
    ],
    'Other': [
        'Language Guides',
        'Training & Nutrition',
    ],
}


def get_supercategory(category):
    for sc, subcats in SUPER_CATEGORIES.items():
        if category in subcats:
            return sc
    return 'Other'


# ── Main ──

def main():
    with open(SHELF_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    books, categories = parse_shelf_with_regex(html)
    print(f"Found {len(books)} books in "
          f"{len(categories)} categories")

    # Parse references
    for book in books:
        refs = parse_references(book['dir'])
        book['references'] = refs
        book['superCategory'] = get_supercategory(
            book['category'])
        book['keywords'] = extract_keywords(book)
        print(f"  {book['title']}: {len(refs)} refs, "
              f"kw={book['keywords']}")

    # Cross-references
    edges = compute_cross_refs(books)
    print(f"Found {len(edges)} cross-references")

    # Connection counts
    conn_count = Counter()
    for e in edges:
        conn_count[e['source']] += 1
        conn_count[e['target']] += 1

    # Adjacency list (precomputed)
    adjacency = {}
    for e in edges:
        if e['source'] not in adjacency:
            adjacency[e['source']] = []
        if e['target'] not in adjacency:
            adjacency[e['target']] = []
        adjacency[e['source']].append(e['target'])
        adjacency[e['target']].append(e['source'])

    # ── Build per-book detail files ──
    os.makedirs(OUT_DIR, exist_ok=True)

    book_by_id = {b['id']: b for b in books}

    for b in books:
        neighbors = adjacency.get(b['id'], [])
        # Build connections with shared thinkers
        conns = []
        for e in edges:
            if e['source'] == b['id']:
                other_id = e['target']
            elif e['target'] == b['id']:
                other_id = e['source']
            else:
                continue
            other = book_by_id.get(other_id)
            if not other:
                continue
            conns.append({
                'id': other_id,
                'title': other['title'],
                'author': other['author'],
                'dir': other['dir'],
                'category': other['category'],
                'superCategory': other['superCategory'],
                'shared': e['shared'],
            })
        # Sort: most shared first
        conns.sort(key=lambda c: -len(c['shared']))

        detail = {
            'id': b['id'],
            'references': b['references'],
            'connections': conns,
            'keywords': b['keywords'],
        }

        detail_path = os.path.join(OUT_DIR, b['id'] + '.json')
        with open(detail_path, 'w', encoding='utf-8') as f:
            json.dump(detail, f, ensure_ascii=False)

    # ── Build lightweight index ──

    # Category data (precomputed, sorted)
    cat_data = {}
    for sc_name in SUPER_CATEGORIES:
        sc_books = [b for b in books
                    if b['superCategory'] == sc_name]
        subcats = {}
        for sb in sc_books:
            if sb['category'] not in subcats:
                subcats[sb['category']] = 0
            subcats[sb['category']] += 1

        # Sort books: most connected first, then alpha
        sc_books.sort(
            key=lambda x: (-conn_count[x['id']],
                           x['title']))

        cat_data[sc_name] = {
            'count': len(sc_books),
            'subcategories': subcats,
            'books': [b['id'] for b in sc_books],
        }

    # Most connected (top 12)
    most_connected = sorted(
        books,
        key=lambda x: -conn_count[x['id']]
    )[:12]

    # Book stubs (lightweight — no references)
    stubs = []
    for b in books:
        stubs.append({
            'id': b['id'],
            'dir': b['dir'],
            'title': b['title'],
            'author': b['author'],
            'category': b['category'],
            'sc': b['superCategory'],
            'read': b.get('isRead', False),
            'refs': len(b.get('references', [])),
            'conn': conn_count[b['id']],
            'kw': b['keywords'],
        })

    index = {
        'generated': __import__('datetime')
            .datetime.now().isoformat(),
        'totalBooks': len(books),
        'totalEdges': len(edges),
        'categories': cat_data,
        'mostConnected': [b['id'] for b in most_connected],
        'adjacency': adjacency,
        'books': stubs,
    }

    with open(OUT_INDEX, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False)

    # Stats
    idx_size = os.path.getsize(OUT_INDEX)
    detail_sizes = []
    for b in books:
        p = os.path.join(OUT_DIR, b['id'] + '.json')
        if os.path.exists(p):
            detail_sizes.append(os.path.getsize(p))

    print(f"\nOutput:")
    print(f"  metadata.json: {idx_size/1024:.1f} KB")
    print(f"  metadata/*.json: {len(detail_sizes)} files, "
          f"avg {sum(detail_sizes)/len(detail_sizes)/1024:.1f} KB, "
          f"total {sum(detail_sizes)/1024:.1f} KB")


if __name__ == '__main__':
    main()
