#!/usr/bin/env python3
"""
OCR + chart extraction for McMillan's Options as a Strategic Investment.
Runs unattended. Writes notes.md in 20-page batches. Extracts all charts.
"""

import fitz
import os
import sys
import time
from datetime import datetime

# Fix tessdata path for tesseract OCR
os.environ['TESSDATA_PREFIX'] = '/usr/local/Cellar/tesseract/4.1.0/share/tessdata'

PDF_PATH = '/Users/alexbarnett/Desktop/Books/_OceanofPDF.com_Options_as_a_Strategic_Investment_-_Lawrence_G_McMillan.pdf'
BOOK_DIR = '/Users/alexbarnett/Documents/Code/Claude/Books/Options_As_Strategic_Investment'
CHARTS_DIR = os.path.join(BOOK_DIR, 'charts')
NOTES_PATH = os.path.join(BOOK_DIR, 'notes.md')
PROGRESS_PATH = os.path.join(BOOK_DIR, 'ocr_progress.txt')
BATCH_SIZE = 20

os.makedirs(CHARTS_DIR, exist_ok=True)

def log(msg):
    ts = datetime.now().strftime('%H:%M:%S')
    print(f'[{ts}] {msg}', flush=True)

def save_progress(page_num):
    with open(PROGRESS_PATH, 'w') as f:
        f.write(str(page_num))

def load_progress():
    if os.path.exists(PROGRESS_PATH):
        with open(PROGRESS_PATH) as f:
            return int(f.read().strip())
    return 0

def ocr_page(page):
    """OCR a single page using tesseract via PyMuPDF."""
    try:
        # Use PyMuPDF's built-in OCR (requires tesseract)
        tp = page.get_textpage_ocr(flags=0, language='eng', dpi=300, full=True)
        text = page.get_text(textpage=tp)
        return text
    except Exception as e:
        log(f'  OCR error: {e}')
        return ''

def extract_charts(doc, page_num, page):
    """Extract images from a page, skip tiny ones and covers."""
    images = page.get_images(full=True)
    extracted = []
    for idx, img in enumerate(images):
        xref = img[0]
        try:
            base_image = doc.extract_image(xref)
            w = base_image['width']
            h = base_image['height']
            # Skip tiny icons
            if w < 200 or h < 150:
                continue
            # Skip cover (page 1, first image)
            if page_num == 0 and idx == 0:
                continue
            ext = base_image['ext']
            fname = f'chart_p{page_num+1:04d}_{idx+1:02d}.{ext}'
            fpath = os.path.join(CHARTS_DIR, fname)
            if not os.path.exists(fpath):
                with open(fpath, 'wb') as f:
                    f.write(base_image['image'])
            extracted.append(fname)
        except Exception as e:
            log(f'  Chart extract error p{page_num+1}: {e}')
    return extracted

def main():
    log('Opening PDF...')
    doc = fitz.open(PDF_PATH)
    total_pages = len(doc)
    log(f'Total pages: {total_pages}')

    start_page = load_progress()
    if start_page > 0:
        log(f'Resuming from page {start_page + 1}')
    else:
        # Clear notes if starting fresh
        if os.path.exists(NOTES_PATH):
            log('Backing up existing notes...')
            os.rename(NOTES_PATH, NOTES_PATH + '.bak')

    chart_count = 0
    batch_text = ''
    batch_start = start_page

    for page_num in range(start_page, total_pages):
        page = doc[page_num]

        # OCR the page
        log(f'Page {page_num+1}/{total_pages} — OCR...')
        text = ocr_page(page)

        # Extract charts
        charts = extract_charts(doc, page_num, page)
        if charts:
            chart_count += len(charts)
            log(f'  Extracted {len(charts)} chart(s): {", ".join(charts)}')

        # Build batch text
        batch_text += f'\n\n--- PAGE {page_num+1} ---\n'
        if charts:
            for c in charts:
                batch_text += f'[CHART: {c}]\n'
        batch_text += text.strip()

        # Write batch every BATCH_SIZE pages
        if (page_num + 1) % BATCH_SIZE == 0 or page_num == total_pages - 1:
            batch_end = page_num + 1
            log(f'Writing batch pages {batch_start+1}-{batch_end} to notes.md...')
            with open(NOTES_PATH, 'a') as f:
                f.write(f'\n\n## BATCH: Pages {batch_start+1}-{batch_end}\n')
                f.write(batch_text)
            batch_text = ''
            batch_start = page_num + 1
            save_progress(page_num + 1)
            log(f'  Saved. Charts so far: {chart_count}')

    log(f'DONE. Total pages: {total_pages}, Total charts: {chart_count}')
    log(f'Notes written to: {NOTES_PATH}')

    # Extract cover from page 1
    log('Extracting cover...')
    cover_page = doc[0]
    mat = fitz.Matrix(2, 2)
    pix = cover_page.get_pixmap(matrix=mat)
    cover_path = os.path.join(BOOK_DIR, 'cover.jpg')
    pix.save(cover_path)
    log(f'Cover saved: {cover_path}')

    # Remove progress file
    if os.path.exists(PROGRESS_PATH):
        os.remove(PROGRESS_PATH)
    log('All done! Ready for HTML writing.')

if __name__ == '__main__':
    main()
