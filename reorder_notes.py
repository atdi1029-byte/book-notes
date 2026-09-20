#!/usr/bin/env python3
"""
reorder_notes.py — Put notes.md back in page order and renumber nugget IDs.

Why: bookai merges batches per wave and gap-fill appends single pages to the
END of notes.md, so the file ends up out of page order. Parallel batches also
can't know where the previous batch's [N###] numbering stopped, so IDs collide.

What it does:
  1. Splits notes.md into blocks at page markers:  <!-- pp. X-Y -->  /  <!-- p. X -->
     (anything before the first marker is kept at the top, untouched)
  2. Stable-sorts blocks by start page (ties keep original order)
  3. Renumbers every [N###] sequentially in document order (N001, N002, ...)
  4. Writes the file back only if something changed; keeps a .pre-reorder backup

Usage:
  python3 reorder_notes.py Book_Folder/notes.md
  python3 reorder_notes.py Book_Folder/notes.md --dry-run
  python3 reorder_notes.py Book_Folder/notes.md --no-renumber

Exit codes: 0 ok, 1 error.
"""

import os
import re
import shutil
import sys

MARKER_RE = re.compile(r'^\s*<!--\s*pp?\.\s*(\d+)(?:\s*-\s*(\d+))?\s*-->\s*$')
NUGGET_ID_RE = re.compile(r'\[N(\d+)\]')


def split_blocks(lines):
    """Return (preamble_lines, [ (start_page, end_page, [lines]) ])."""
    preamble = []
    blocks = []
    current = None
    for line in lines:
        m = MARKER_RE.match(line)
        if m:
            if current is not None:
                blocks.append(current)
            start = int(m.group(1))
            end = int(m.group(2)) if m.group(2) else start
            current = [start, end, [line]]
        elif current is None:
            preamble.append(line)
        else:
            current[2].append(line)
    if current is not None:
        blocks.append(current)
    return preamble, blocks


def renumber(text):
    """Renumber [N###] sequentially. Returns (new_text, count, dupes_before)."""
    ids = NUGGET_ID_RE.findall(text)
    dupes_before = len(ids) - len(set(ids))
    width = max(3, len(str(len(ids))))
    counter = [0]

    def repl(_m):
        counter[0] += 1
        return '[N%s]' % str(counter[0]).zfill(width)

    new_text = NUGGET_ID_RE.sub(repl, text)
    return new_text, counter[0], dupes_before


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = set(a for a in sys.argv[1:] if a.startswith('--'))
    if not args:
        print(__doc__)
        return 1
    path = args[0]
    dry_run = '--dry-run' in flags
    do_renumber = '--no-renumber' not in flags

    if not os.path.isfile(path):
        print(f'ERROR: {path} not found')
        return 1

    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        original = f.read()
    lines = original.splitlines(keepends=True)

    preamble, blocks = split_blocks(lines)
    if not blocks:
        print('  No page markers found — nothing to reorder')
        return 0

    # Stable sort by start page, then end page
    indexed = list(enumerate(blocks))
    ordered = sorted(indexed, key=lambda t: (t[1][0], t[1][1], t[0]))
    moved = sum(1 for new_i, (old_i, _) in enumerate(ordered) if new_i != old_i)

    out_lines = list(preamble)
    for _, (start, end, blines) in ordered:
        # Ensure each block ends with a newline so blocks don't glue together
        if blines and not blines[-1].endswith('\n'):
            blines = blines[:-1] + [blines[-1] + '\n']
        out_lines.extend(blines)
        if not (len(blines) >= 1 and blines[-1].strip() == ''):
            out_lines.append('\n')

    new_text = ''.join(out_lines)

    renumbered = 0
    dupes = 0
    if do_renumber:
        new_text, renumbered, dupes = renumber(new_text)

    pages = sorted(set(p for _, (s, e, _) in ordered for p in range(s, e + 1)))
    print(f'  Blocks: {len(blocks)}  (pages {pages[0]}-{pages[-1]}, '
          f'{len(pages)} distinct)')
    print(f'  Moved:  {moved} block(s) were out of page order')
    if do_renumber:
        print(f'  IDs:    {renumbered} nugget IDs renumbered sequentially'
              + (f' ({dupes} duplicate IDs fixed)' if dupes else ''))

    if new_text == original:
        print('  Result: already in order — file unchanged')
        return 0
    if dry_run:
        print('  Result: changes needed (dry run — file not written)')
        return 0

    backup = path + '.pre-reorder'
    if not os.path.exists(backup):
        shutil.copyfile(path, backup)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print(f'  Result: rewritten in page order (backup: {os.path.basename(backup)})')
    return 0


if __name__ == '__main__':
    sys.exit(main())
