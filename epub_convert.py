#!/usr/bin/env python3
"""Convert a book's index.html into an EPUB file."""

import sys
import os
import re
from html.parser import HTMLParser
from ebooklib import epub

# ── Stripped CSS for e-readers (no bg images, no bookmark UI) ──
EPUB_CSS = """
body {
  font-family: Georgia, serif;
  line-height: 1.7;
  color: #3a2e1e;
}
h1 { font-size: 2em; color: #5a3e1a; margin-bottom: 0.25em; }
h2 { font-size: 1.5em; color: #5a3e1a; margin-top: 2em;
     border-bottom: 2px solid #c5a55a; padding-bottom: 0.3em; }
h3 { font-size: 1.2em; color: #6b8f8b; margin-top: 1.5em; }
h4 { font-size: 1.05em; color: #7a6530; margin-top: 1.2em; }
p { margin-bottom: 0.8em; }
strong { color: #5a3e1a; }
ol, ul { margin: 0.5em 0 1em 1.5em; }
li { margin-bottom: 0.4em; }
hr { border: none; border-top: 1px solid #d4c8b0; margin: 2em 0; }
blockquote {
  border-left: 3px solid #c5a55a;
  margin: 1em 0; padding: 0.5em 1em;
  font-style: italic; color: #5a4a30;
}
table { width: 100%; border-collapse: collapse; font-size: 0.95em; }
th { background: #6b8f8b; color: #fff; text-align: left;
     padding: 0.5em 0.6em; }
td { padding: 0.4em 0.6em; border-bottom: 1px solid #d4c8b0; }
.subtitle { color: #8a7a60; font-style: italic; margin-bottom: 2em; }
.toc { margin: 1em 0 2em; }
.toc a { color: #4a7872; text-decoration: none; }
a { color: #4a7872; }
.summary-section {
  border-left: 4px solid #c5a55a;
  padding: 1em; margin: 1em 0;
}
cite { font-style: normal; font-size: 0.9em; color: #8a7a60; }
"""


def clean_html(raw_html: str) -> str:
    """Strip interactive elements, scripts, and bookmark UI."""
    # Remove script tags
    html = re.sub(r'<script[^>]*>.*?</script>', '', raw_html,
                  flags=re.DOTALL)

    # Remove bookmark bar, toast, progress bar divs
    html = re.sub(
        r'<div\s+class="(progress-bar|bookmark-bar|bm-toast)"'
        r'[^>]*>.*?</div>',
        '', html, flags=re.DOTALL)

    # Remove bookmark buttons
    html = re.sub(r'<span\s+class="bm-btn[^"]*"[^>]*>.*?</span>',
                  '', html, flags=re.DOTALL)

    # Remove SVG diagrams (they render badly on e-ink)
    html = re.sub(r'<div\s+class="diagram"[^>]*>.*?</div>',
                  '', html, flags=re.DOTALL)

    # Remove link to book.css and book.js
    html = re.sub(r'<link[^>]*book\.css[^>]*>', '', html)
    html = re.sub(r'<script[^>]*book\.js[^>]*>.*?</script>', '',
                  html, flags=re.DOTALL)

    # Remove meta tags for PWA
    html = re.sub(
        r'<meta\s+name="apple-mobile-web-app[^>]*>', '', html)

    # Remove onclick attributes
    html = re.sub(r'\s+onclick="[^"]*"', '', html)

    return html


def extract_title_author(html: str):
    """Pull title and author from the HTML."""
    title_m = re.search(r'<h1>(.*?)</h1>', html, re.DOTALL)
    title = title_m.group(1).strip() if title_m else 'Unknown'
    title = re.sub(r'<[^>]+>', '', title)

    sub_m = re.search(r'class="subtitle"[^>]*>(.*?)</p>',
                      html, re.DOTALL)
    author = 'Unknown'
    if sub_m:
        # Extract "By Author Name" from subtitle
        sub = re.sub(r'<[^>]+>', '', sub_m.group(1))
        a_m = re.search(r'By\s+(.+?)(?:\s*[·&]|$)', sub)
        if a_m:
            author = a_m.group(1).strip()

    return title, author


def extract_body(html: str) -> str:
    """Extract content between <body> tags."""
    m = re.search(r'<body[^>]*>(.*)</body>',
                  html, re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else html


def convert(book_dir: str):
    html_path = os.path.join(book_dir, 'index.html')
    cover_path = os.path.join(book_dir, 'cover.jpg')

    if not os.path.exists(html_path):
        print(f"No index.html in {book_dir}")
        return False

    with open(html_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    title, author = extract_title_author(raw)
    cleaned = clean_html(raw)
    body = extract_body(cleaned)

    # Build EPUB
    book = epub.EpubBook()
    book.set_identifier(
        'bookshelf-' + os.path.basename(book_dir).lower())
    book.set_title(title)
    book.set_language('en')
    book.add_author(author)

    # Add CSS
    css = epub.EpubItem(
        uid='style', file_name='style/book.css',
        media_type='text/css', content=EPUB_CSS.encode())
    book.add_item(css)

    # Add cover image if exists
    if os.path.exists(cover_path):
        with open(cover_path, 'rb') as f:
            cover_data = f.read()
        book.set_cover('cover.jpg', cover_data)

    # Single chapter with all content
    ch = epub.EpubHtml(
        title=title, file_name='content.xhtml',
        lang='en')
    ch.content = (
        f'<html><body>{body}</body></html>'
    ).encode('utf-8')
    ch.add_item(css)
    book.add_item(ch)

    # Table of contents + spine
    book.toc = [ch]
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ['nav', ch]

    out_path = os.path.join(book_dir, 'book.epub')
    epub.write_epub(out_path, book, {})
    size_kb = os.path.getsize(out_path) / 1024
    print(f"Created: {out_path} ({size_kb:.0f} KB)")
    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 epub_convert.py <book_dir>")
        print("       python3 epub_convert.py --all")
        sys.exit(1)

    books_root = os.path.dirname(os.path.abspath(__file__))

    if sys.argv[1] == '--all':
        count = 0
        for d in sorted(os.listdir(books_root)):
            full = os.path.join(books_root, d)
            if (os.path.isdir(full)
                    and os.path.exists(
                        os.path.join(full, 'index.html'))):
                if convert(full):
                    count += 1
        print(f"\nConverted {count} books.")
    else:
        book_dir = sys.argv[1]
        if not os.path.isabs(book_dir):
            book_dir = os.path.join(books_root, book_dir)
        convert(book_dir)
