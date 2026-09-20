#!/usr/bin/env python3
"""
detect_type.py — Suggest a bookai book type for a PDF with one cheap model call.

Looks at the front matter / table of contents (first ~30 pages) plus a
text-vs-image density sample across the whole book, asks Claude (haiku) for
one word, and validates it. Falls back to a density heuristic if the CLI is
unavailable or times out.

Prints exactly one of: analytical narrative technical textbook practical
(diagnostics go to stderr).

Usage:
  python3 detect_type.py book.pdf            -> type
  python3 detect_type.py book.pdf --explain  -> type + reasoning on stderr
"""

import re
import shutil
import subprocess
import sys

try:
    import pymupdf as fitz
except ImportError:
    import fitz

TYPES = ('analytical', 'narrative', 'technical', 'textbook', 'practical')

TYPE_GUIDE = """
analytical  — argument-driven non-fiction: ideas, frameworks, evidence, essays,
              economics/finance/philosophy books, investing theory. Mostly prose.
narrative   — story-driven: biography, memoir, history told as narrative, journalism.
technical   — chart/diagram-heavy trading or technical-analysis books, pattern manuals,
              anything where the figures carry the meaning.
textbook    — structured course material: numbered chapters/sections, definitions,
              worked examples, exercises, formulas, end-of-chapter problems.
practical   — how-to / step-by-step guides, workbooks, checklists, recipes-for-doing,
              manuals with procedures.
"""


def sample(doc, max_front=30, spread=24):
    n = len(doc)
    front = []
    for i in range(min(max_front, n)):
        t = doc[i].get_text('text')
        if t.strip():
            front.append(t)
    front_text = '\n'.join(front)
    front_text = re.sub(r'\n{3,}', '\n\n', front_text)[:9000]

    idxs = sorted(set(int(k * (n - 1) / max(1, spread - 1)) for k in range(spread))) if n > 1 else [0]
    words = imgs = drawings = 0
    for i in idxs:
        p = doc[i]
        words += len(p.get_text('text').split())
        imgs += len(p.get_images(full=False))
        try:
            drawings += 1 if len(p.get_drawings()) > 40 else 0
        except Exception:
            pass
    k = max(1, len(idxs))
    return front_text, n, words / k, imgs / k, drawings / k


def heuristic(words_pp, imgs_pp, draw_pp):
    if imgs_pp >= 1.0 or draw_pp >= 0.5:
        return 'technical' if words_pp < 300 else 'textbook'
    return 'analytical'


def ask_claude(prompt, model='haiku', timeout=120):
    if not shutil.which('claude'):
        return None, 'claude CLI not found'
    try:
        r = subprocess.run(['claude', '-p', prompt, '--model', model, '--max-turns', '1'],
                           capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, 'claude timed out'
    out = (r.stdout or '').strip().lower()
    for t in TYPES:
        if re.search(r'\b' + t + r'\b', out):
            return t, out[:200]
    return None, f'unrecognized answer: {out[:120]!r}'


def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    pdf = sys.argv[1]
    explain = '--explain' in sys.argv
    try:
        doc = fitz.open(pdf)
    except Exception as e:
        print(f'cannot open PDF: {e}', file=sys.stderr)
        print('analytical')
        return 0

    front, n, wpp, ipp, dpp = sample(doc)
    fallback = heuristic(wpp, ipp, dpp)
    if len(front.split()) < 80:
        # scanned / no text layer — can't read the TOC; rely on density
        print(f'no usable text layer; heuristic -> {fallback}', file=sys.stderr)
        print(fallback)
        return 0

    prompt = f"""Classify this book into exactly ONE of five types for a note-extraction pipeline.
{TYPE_GUIDE}
Book stats: {n} pages; average {wpp:.0f} words/page, {ipp:.2f} images/page, {dpp*100:.0f}% of sampled pages are drawing-heavy (charts/diagrams).

Front matter and table of contents (first pages):
---
{front}
---
Reply with exactly one word — one of: analytical, narrative, technical, textbook, practical. No explanation."""

    ans, why = ask_claude(prompt)
    if ans is None:
        print(f'{why}; heuristic -> {fallback}', file=sys.stderr)
        print(fallback)
        return 0
    if explain:
        print(f'claude -> {ans} ({why}); density heuristic -> {fallback}', file=sys.stderr)
    print(ans)
    return 0


if __name__ == '__main__':
    sys.exit(main())
