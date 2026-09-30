#!/usr/bin/env python3
"""
bookai_lib.py — helpers for bookai (called as subcommands; no state of its own).

  pages PDF READ_START REAL_START END OUTDIR [--charts DIR] [--all-images]
      Write OUTDIR/pages.txt (page text, "=== PAGE N ===" headers) and
      OUTDIR/pages.json (per page: chars, figure, image). Pages that have a
      figure, or almost no text layer, get a PNG in OUTDIR (copied from
      --charts when it has one, rendered otherwise). --all-images gives every
      page an image (chart/visual book types).

  plan DONE_FILE START END BATCH OVERLAP
      Print the batches still to do, one per line: "READ_START REAL_START END".
      Pages already listed in DONE_FILE are skipped, so a re-run only fills gaps.

  missing DONE_FILE START END
      Print the pages not in DONE_FILE as compact ranges ("121-130 145").

  result CLI_JSON
      Parse `claude -p --output-format json` output. Prints four lines:
      status (ok|rate_limit|usage_limit|content_filter|max_turns|error),
      cost in USD, number of turns, and a one-line message.

  gate NOTES REAL_START END PAGES_JSON TYPE
      Quality gate for one batch. Prints "OK <pages-acked>" or "FAIL <reason>".

  acks NOTES REAL_START END
      Print the pages in [REAL_START, END] that NOTES acknowledges.

  state STATE_JSON key=value ...
      Merge values into the run state (dotted keys; JSON values allowed) and
      write it back. Never drops keys it wasn't given.

  publish BOOK_DIR FOLDER
      Print the files finish-book commits for a book: the pages, notes,
      summary, cover, thumb, and every image the pages actually use.

Exit status is 0 unless the arguments are unusable.
"""

import json
import os
import re
import shutil
import sys

ACK_RE = re.compile(r'<!--\s*page\s+(\d+)\s*:\s*(.*?)-->', re.S)
TAG_RE = re.compile(r'\[(MUST KNOW|SHOULD KNOW|NICE TO KNOW)\]')
IMG_REF_RE = re.compile(r'\[(?:PAGE IMAGE|IMAGE NOT AVAILABLE):')
EMPTY_ACK_RE = re.compile(r'no content|blank|copyright|index page|bibliography|no substantive', re.I)


def fitz():
    try:
        import pymupdf as m
    except ImportError:
        import fitz as m
    return m


# ── pages ─────────────────────────────────────────────────────────────────

def page_text(page):
    parts = []
    for b in page.get_text('blocks', sort=True):
        if len(b) > 6 and b[6] != 0:          # image block
            continue
        t = b[4]
        t = re.sub(r'(\w)-\n(\w)', r'\1\2', t)  # re-join hyphenated line breaks
        t = re.sub(r'\s*\n\s*', ' ', t).strip()
        if t:
            parts.append(t)
    return '\n\n'.join(parts)


def has_figure(page):
    area = abs(page.rect) or 1
    try:
        for info in page.get_image_info():
            x0, y0, x1, y1 = info.get('bbox', (0, 0, 0, 0))
            if (x1 - x0) * (y1 - y0) > 0.05 * area:
                return True
    except Exception:
        pass
    try:
        if len(page.get_drawings()) > 40:
            return True
    except Exception:
        pass
    return False


def cmd_pages(args):
    pdf, rs, s, e, outdir = args[0], int(args[1]), int(args[2]), int(args[3]), args[4]
    charts = None
    all_images = '--all-images' in args
    if '--charts' in args:
        charts = args[args.index('--charts') + 1]
    m = fitz()
    doc = m.open(pdf)
    e = min(e, len(doc))
    os.makedirs(outdir, exist_ok=True)
    info = {}
    out = []
    for p in range(rs, e + 1):
        page = doc[p - 1]
        text = page_text(page)
        fig = has_figure(page)
        sparse = len(text) < 200
        img = None
        if all_images or fig or sparse:
            img = 'page_%03d.png' % p
            src = os.path.join(charts, img) if charts else None
            if src and os.path.isfile(src):
                shutil.copyfile(src, os.path.join(outdir, img))
            else:
                page.get_pixmap(matrix=m.Matrix(2, 2)).save(os.path.join(outdir, img))
        head = '=== PAGE %d ===' % p
        if p < s:
            head += '  (overlap from the previous batch: context only)'
        notes = []
        if fig and img:
            notes.append('[FIGURE on this page: open %s with the Read tool before describing it]' % img)
        if sparse and img:
            notes.append('[little or no text layer: read %s instead]' % img)
        elif img and all_images and not fig:
            notes.append('[page image: %s]' % img)
        out.append('\n'.join([head] + notes + [text or '(no text)']))
        info[p] = {'chars': len(text), 'figure': fig, 'image': img}
    with open(os.path.join(outdir, 'pages.txt'), 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(out) + '\n')
    with open(os.path.join(outdir, 'pages.json'), 'w', encoding='utf-8') as f:
        json.dump(info, f)
    return 0


# ── planning ──────────────────────────────────────────────────────────────

def read_done(path):
    done = set()
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line.isdigit():
                    done.add(int(line))
    except FileNotFoundError:
        pass
    return done


def runs(pages):
    out = []
    for p in sorted(pages):
        if out and p == out[-1][1] + 1:
            out[-1][1] = p
        else:
            out.append([p, p])
    return out


def compact(pages):
    return ' '.join(str(a) if a == b else '%d-%d' % (a, b) for a, b in runs(pages))


def cmd_plan(args):
    done = read_done(args[0])
    start, end, batch, overlap = (int(x) for x in args[1:5])
    todo = [p for p in range(start, end + 1) if p not in done]
    for a, b in runs(todo):
        s = a
        while s <= b:
            e = min(b, s + batch - 1)
            rs = max(1, s - overlap) if s > 1 else s
            print(rs, s, e)
            s = e + 1
    return 0


def cmd_missing(args):
    done = read_done(args[0])
    start, end = int(args[1]), int(args[2])
    print(compact(p for p in range(start, end + 1) if p not in done))
    return 0


# ── claude CLI result ─────────────────────────────────────────────────────

def cmd_result(args):
    status, cost, turns, msg = 'error', 0.0, 0, 'no output from claude'
    try:
        with open(args[0], encoding='utf-8', errors='replace') as f:
            raw = f.read().strip()
        d = json.loads(raw[raw.index('{'):]) if raw else {}
    except Exception:
        d = {}
        if raw:
            msg = raw.replace('\n', ' ')[:200]
    if d:
        cost = float(d.get('total_cost_usd') or 0)
        turns = int(d.get('num_turns') or 0)
        text = str(d.get('result') or '')
        sub = str(d.get('subtype') or '')
        api = str(d.get('api_error_status') or '')
        msg = (text or sub).replace('\n', ' ')[:200]
        blob = (text + ' ' + api).lower()
        if not d.get('is_error') and sub == 'success':
            status = 'ok'                      # the notes file itself is judged by the gate
        elif re.search(r'usage limit|limit reached|out of (credits|usage)|billing|credit balance', blob):
            status = 'usage_limit'
        elif api in ('429', '529') or re.search(r'rate.?limit|overloaded|too many requests', blob):
            status = 'rate_limit'
        elif re.search(r'content (filter|policy)|unable to process|violat', blob):
            status = 'content_filter'
        elif sub == 'error_max_turns':
            status = 'max_turns'
        else:
            status = 'error'
    print(status)
    print('%.4f' % cost)
    print(turns)
    print(msg or '-')
    return 0


# ── quality gate ──────────────────────────────────────────────────────────

def acked(text, s, e):
    got = {}
    for m in ACK_RE.finditer(text):
        p = int(m.group(1))
        if s <= p <= e:
            got[p] = m.group(2).strip()
    return got


def cmd_acks(args):
    with open(args[0], encoding='utf-8', errors='replace') as f:
        text = f.read()
    print(' '.join(str(p) for p in sorted(acked(text, int(args[1]), int(args[2])))))
    return 0


def cmd_gate(args):
    path, s, e, pages_json, btype = args[0], int(args[1]), int(args[2]), args[3], args[4]
    if not os.path.isfile(path) or os.path.getsize(path) < 50:
        print('FAIL no notes file was written')
        return 0
    with open(path, encoding='utf-8', errors='replace') as f:
        text = f.read()
    acks = acked(text, s, e)
    if not acks:
        print('FAIL no <!-- page N: … --> acknowledgments for pages %d-%d' % (s, e))
        return 0
    content_pages = [p for p, why in acks.items() if not EMPTY_ACK_RE.search(why)]
    if not content_pages:
        print('OK %d' % len(acks))           # front/back matter, honestly acknowledged
        return 0
    n = len(content_pages)
    visual = btype in ('technical', 'practical', 'textbook')
    min_words = min(300 if visual else 200, 35 * n)
    min_bullets = min(5 if visual else 4, max(1, (n + 2) // 3))
    words = len(text.split())
    bullets = len(re.findall(r'^\s*- ', text, re.M))
    tags = len(TAG_RE.findall(text))
    problems = []
    if words < min_words:
        problems.append('only %d words for %d content pages (need %d)' % (words, n, min_words))
    if bullets < min_bullets:
        problems.append('only %d bullet points (need %d)' % (bullets, min_bullets))
    if n >= 2 and tags == 0:
        problems.append('no [MUST KNOW]/[SHOULD KNOW]/[NICE TO KNOW] tags')
    try:
        with open(pages_json) as f:
            info = json.load(f)
    except Exception:
        info = {}
    fig_pages = [int(p) for p, v in info.items() if s <= int(p) <= e and v.get('figure') and v.get('image')]
    if visual and len(fig_pages) > 3 and not IMG_REF_RE.search(text):
        problems.append('%d pages have figures but there are no [PAGE IMAGE: …] descriptions' % len(fig_pages))
    if problems:
        print('FAIL ' + '; '.join(problems))
    else:
        print('OK %d' % len(acks))
    return 0


# ── run state ─────────────────────────────────────────────────────────────

def cmd_state(args):
    path = args[0]
    try:
        with open(path, encoding='utf-8') as f:
            st = json.load(f)
    except Exception:
        st = {}
    for kv in args[1:]:
        k, _, v = kv.partition('=')
        try:
            val = json.loads(v)
        except Exception:
            val = v
        cur = st
        keys = k.split('.')
        for key in keys[:-1]:
            if not isinstance(cur.get(key), dict):
                cur[key] = {}
            cur = cur[key]
        cur[keys[-1]] = val
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(st, f, indent=2)
    os.replace(tmp, path)
    return 0


def cmd_publish(args):
    d, folder = args[0], args[1]
    files = set()
    for name in ('index.html', 'plain.html', 'summary.md', 'notes.md', 'cover.jpg', 'cover.png', 'cover.svg', 'thumb.jpg'):
        if os.path.isfile(os.path.join(d, name)):
            files.add(name)
    for page in ('index.html', 'plain.html'):
        p = os.path.join(d, page)
        if not os.path.isfile(p):
            continue
        html = open(p, encoding='utf-8', errors='replace').read()
        for ref in re.findall(r'["\'(]([^"\'()\s<>]+\.(?:png|jpe?g|gif|webp|svg|mp4))', html, re.I):
            if ref.startswith(('http:', 'https:', 'data:', '/')):
                continue
            path = os.path.normpath(ref.split('?')[0].split('#')[0])
            if not path.startswith('..') and os.path.isfile(os.path.join(d, path)):
                files.add(path)
    for f in sorted(files):
        print(f'{folder}/{f}')
    return 0


COMMANDS = {'publish': cmd_publish, 'pages': cmd_pages, 'plan': cmd_plan, 'missing': cmd_missing, 'result': cmd_result,
            'gate': cmd_gate, 'acks': cmd_acks, 'state': cmd_state}

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(__doc__)
        sys.exit(2)
    sys.exit(COMMANDS[sys.argv[1]](sys.argv[2:]))
