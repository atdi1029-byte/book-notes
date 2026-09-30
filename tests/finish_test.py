#!/usr/bin/python3
"""finish-book.sh gate tests in a throwaway copy of the repo (no API calls).

  /usr/bin/python3 tests/finish_test.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BOOKS = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from grader_test import book_html, NOTES  # noqa: E402

SCRIPTS = ['finish-book.sh', '_python.sh', 'bookai_lib.py', 'run_state.py', 'reorder_notes.py', 'verify_quotes.py', 'check_html.py',
           'book_rules.json', 'audit_check.py', 'grade_coverage.py', 'make_thumb.py', 'add_to_shelf.py',
           'generate_books_json.py', 'build_metadata.py', 'index.html', 'books.json', 'metadata.json', '.gitignore']
failures = 0


def check(name, ok, detail=None):
    global failures
    print(('  PASS ' if ok else '  FAIL ') + name + ('' if ok or detail is None else '  → ' + str(detail)[-700:]))
    if not ok:
        failures += 1


def sh(cmd, cwd, env=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=dict(os.environ, **(env or {})), timeout=300)


def main():
    root = tempfile.mkdtemp(prefix='finish-test-')
    try:
        for s in SCRIPTS:
            shutil.copy2(os.path.join(BOOKS, s), root)
        os.makedirs(os.path.join(root, 'metadata'), exist_ok=True)
        sh(['git', 'init', '-q'], root)
        sh(['git', '-c', 'user.email=t@t', '-c', 'user.name=t', 'add', '-A'], root)
        sh(['git', '-c', 'user.email=t@t', '-c', 'user.name=t', 'commit', '-qm', 'base'], root)

        book = os.path.join(root, 'Test_Book')
        os.makedirs(os.path.join(book, 'charts'))
        fig = '<p>See the figure.</p><img src="charts/fig_p0001.png" alt="figure">'
        extra = '<p>The book explains that reserves are not lent out to customers, contrary to the textbook story told for decades.</p>'
        open(os.path.join(book, 'index.html'), 'w').write(book_html(ch1_extra=fig, ch2_extra=extra))
        open(os.path.join(book, 'notes.md'), 'w').write(NOTES)
        open(os.path.join(book, 'notes.md.raw'), 'w').write(NOTES + '\n- [NICE TO KNOW][N006] dropped in compaction\n')
        open(os.path.join(book, 'summary.md'), 'w').write('\n'.join(f'- takeaway {i}' for i in range(30)))
        open(os.path.join(book, 'process.log'), 'w').write('log\n')
        import pymupdf as fitz
        pix = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 60, 90), 0)
        pix.save(os.path.join(book, 'cover.jpg'))
        pix.save(os.path.join(book, 'charts', 'fig_p0001.png'))
        pix.save(os.path.join(book, 'charts', 'page_001.png'))
        state = os.path.join(book, '.run_state.json')
        json.dump({'book': 'Test_Book', 'type': 'analytical', 'extraction': {'status': 'INCOMPLETE', 'missing_pages': '12-14'}},
                  open(state, 'w'))
        run = lambda *a: sh(['bash', os.path.join(root, 'finish-book.sh'), 'Test_Book', '--category', 'Economics Fundamentals', *a], root)

        print('Blocks until everything passes')
        r = run('--no-commit')
        check('blocked: extraction incomplete', r.returncode == 1 and 'extraction INCOMPLETE' in r.stdout, r.stdout)
        check('blocked: no audits', 'audits missing' in r.stdout, r.stdout)
        st = json.load(open(state))
        check('complete stays false', st.get('complete') is False)

        st['extraction']['status'] = 'PASSED'
        json.dump(st, open(state, 'w'))
        env = {'GRADER_CLAUDE': os.path.join(HERE, 'fake_grader.py')}
        g = sh(['/usr/bin/python3', os.path.join(root, 'grade_coverage.py'), 'Test_Book'], root, env)
        check('grader passes on this page', g.returncode == 0, g.stdout)
        with open(os.path.join(book, 'index.html'), 'a') as f:
            f.write('\n<!-- edit after grading -->\n')
        r = run('--no-commit')
        check('blocked: page edited after grading (stale audit)', r.returncode == 1 and 'stale' in r.stdout, r.stdout)
        g = sh(['/usr/bin/python3', os.path.join(root, 'grade_coverage.py'), 'Test_Book'], root, env)

        print('Compaction must keep every MUST/SHOULD ID')
        open(os.path.join(book, 'notes.md.raw'), 'a').write('- [MUST KNOW][N099] only in raw\n')
        r = run('--no-commit')
        check('blocked: nugget lost in compaction', r.returncode == 1 and 'N099' in r.stdout, r.stdout)
        open(os.path.join(book, 'notes.md.raw'), 'w').write(NOTES)

        print('Publishes only what the site needs')
        r = run()
        committed = sh(['git', 'show', '--name-only', '--format=', 'HEAD'], root).stdout.split()
        check('finish succeeds', r.returncode == 0, r.stdout)
        check('page, notes, summary, cover committed', all(f'Test_Book/{f}' in committed for f in ('index.html', 'notes.md', 'summary.md', 'cover.jpg')), committed)
        check('the figure the page uses is committed', 'Test_Book/charts/fig_p0001.png' in committed, committed)
        check('page renders, raw notes, logs, run state stay local',
              not any(x in committed for x in ('Test_Book/charts/page_001.png', 'Test_Book/notes.md.raw', 'Test_Book/process.log', 'Test_Book/.run_state.json')), committed)
        check('shelf card added', 'index.html' in committed and 'Test_Book/index.html' in open(os.path.join(root, 'index.html')).read())
        st = json.load(open(state))
        check('complete true, cover needs no review (it was already there)', st.get('complete') is True and st['cover']['status'] == 'PASSED', st.get('cover'))
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print(f'\n{failures} FAILED' if failures else '\nALL PASSED')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
