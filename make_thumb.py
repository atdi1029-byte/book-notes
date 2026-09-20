#!/usr/bin/env python3
"""
make_thumb.py — Make the shelf thumbnail for a book folder.

  cover.jpg  (full-size, extracted from PDF page 1)  ->  thumb.jpg  (600px wide, ~40-80 KB)

If cover.jpg is missing and --pdf is given, page 1 is rendered first.
Uses Pillow; falls back to macOS `sips` if Pillow isn't installed.

Usage:
  python3 make_thumb.py Book_Folder                  # cover.jpg -> thumb.jpg
  python3 make_thumb.py Book_Folder --pdf book.pdf   # also extract cover if missing
  python3 make_thumb.py Book_Folder --force          # overwrite existing thumb
  python3 make_thumb.py --all                        # backfill every folder with cover.jpg but no thumb.jpg

Exit codes: 0 ok, 1 nothing to do / error.
"""

import os
import subprocess
import sys

BOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
THUMB_WIDTH = 600
JPEG_QUALITY = 82


def extract_cover(pdf, out_path, dpi=150):
    try:
        import pymupdf as fitz
    except ImportError:
        import fitz
    doc = fitz.open(pdf)
    if len(doc) == 0:
        return False
    pix = doc[0].get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
    pix.save(out_path)
    return True


def make_thumb(cover, thumb):
    try:
        from PIL import Image
    except ImportError:
        Image = None
    if Image is not None:
        im = Image.open(cover)
        if im.mode not in ('RGB', 'L'):
            im = im.convert('RGB')
        w, h = im.size
        if w > THUMB_WIDTH:
            im = im.resize((THUMB_WIDTH, round(h * THUMB_WIDTH / w)), Image.LANCZOS)
        im.save(thumb, 'JPEG', quality=JPEG_QUALITY, optimize=True, progressive=True)
        return True
    # macOS fallback
    if subprocess.call(['which', 'sips'], stdout=subprocess.DEVNULL) == 0:
        r = subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', str(JPEG_QUALITY),
                            '--resampleWidth', str(THUMB_WIDTH), cover, '--out', thumb],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return r.returncode == 0 and os.path.isfile(thumb)
    print('ERROR: neither Pillow nor sips available (pip install pillow)')
    return False


def process_dir(folder, pdf=None, force=False):
    d = folder if os.path.isabs(folder) else os.path.join(BOOKS_DIR, folder)
    if not os.path.isdir(d):
        print(f'ERROR: folder not found: {d}')
        return False
    cover = os.path.join(d, 'cover.jpg')
    thumb = os.path.join(d, 'thumb.jpg')
    name = os.path.basename(d.rstrip('/'))

    if not os.path.isfile(cover):
        if pdf and os.path.isfile(pdf):
            if extract_cover(pdf, cover):
                print(f'  {name}: extracted cover.jpg from PDF page 1')
        if not os.path.isfile(cover):
            print(f'  {name}: no cover.jpg (pass --pdf to extract one)')
            return False

    if os.path.isfile(thumb) and not force:
        print(f'  {name}: thumb.jpg already exists')
        return True
    if make_thumb(cover, thumb):
        kb = os.path.getsize(thumb) // 1024
        print(f'  {name}: thumb.jpg written ({kb} KB)')
        return True
    return False


def main():
    argv = sys.argv[1:]
    if not argv or '-h' in argv or '--help' in argv:
        print(__doc__)
        return 1
    force = '--force' in argv
    pdf = None
    if '--pdf' in argv:
        i = argv.index('--pdf')
        pdf = argv[i + 1]
        del argv[i:i + 2]
    positional = [a for a in argv if not a.startswith('--')]

    if '--all' in argv:
        done = missing = 0
        for d in sorted(os.listdir(BOOKS_DIR)):
            full = os.path.join(BOOKS_DIR, d)
            if not os.path.isdir(full) or d.startswith('.') or d == 'metadata':
                continue
            if not os.path.isfile(os.path.join(full, 'index.html')):
                continue
            if os.path.isfile(os.path.join(full, 'thumb.jpg')) and not force:
                continue
            if os.path.isfile(os.path.join(full, 'cover.jpg')):
                if process_dir(full, force=force):
                    done += 1
            elif not os.path.isfile(os.path.join(full, 'cover.svg')):
                print(f'  {d}: no cover.jpg / cover.svg — needs a cover')
                missing += 1
        print(f'Thumbs written: {done}; books still without a cover: {missing}')
        return 0

    if not positional:
        print(__doc__)
        return 1
    return 0 if process_dir(positional[0], pdf=pdf, force=force) else 1


if __name__ == '__main__':
    sys.exit(main())
