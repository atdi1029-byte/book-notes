#!/usr/bin/python3
"""check_html.py / grade_coverage.py / audit_check.py tests (no API calls).

  /usr/bin/python3 tests/grader_test.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BOOKS = os.path.dirname(HERE)
SCRIPTS = ['check_html.py', 'book_rules.json', 'grade_coverage.py', 'audit_check.py', 'verify_quotes.py']
failures = 0


def check(name, ok, detail=None):
    global failures
    print(('  PASS ' if ok else '  FAIL ') + name + ('' if ok or detail is None else '  → ' + str(detail)[:400]))
    if not ok:
        failures += 1


def para(topic, n=8):
    words = ('The argument about ' + topic + ' rests on a long chain of reasoning that the author develops '
             'with examples, numbers and a few caveats that the reader should keep in mind when applying it. ') * 4
    return '\n'.join(f'<p>{words}Paragraph {i + 1} about {topic}.</p>' for i in range(n))


def book_html(ch1_extra='', ch2_extra='', cover=False):
    sec = lambda sid, title, body: f'<h2 id="{sid}">{title}</h2>\n{body}\n'
    lessons = ''.join(f'<h3>Lesson {i}</h3><p>Lesson text {i}.</p>' for i in range(5))
    skipped = ''.join(f'<h3>Skip {i}</h3><p>Why {i}.</p>' for i in range(4))
    rows = ''.join(f'<tr><td>Ref {i}</td><td>Idea {i}</td></tr>' for i in range(12))
    refs = ''.join(f'<tr><td>Name {i}</td><td>Work</td><td>Link</td></tr>' for i in range(5))
    fit = ''.join(f'<h3>Story {i}</h3><p>One. Two. Three. Four. Five. Six.</p>' for i in range(2))
    quotes = ''.join(f'<blockquote>Quote {i}<cite>Author</cite></blockquote>' for i in range(8))
    strong = ' '.join(f'<strong>term{i}</strong>' for i in range(40))
    return f'''<!DOCTYPE html><html><head><title>Test Book</title></head><body>
<h1>Test Book</h1>
{'<img src="cover.jpg">' if cover else ''}
<nav class="toc"><h2>Contents</h2><ol><li>x</li></ol></nav>
{sec('ten', 'If You Only Remember 10 Things', '<ol>' + '<li>x</li>' * 10 + '</ol>')}
{sec('ch1', 'Chapter 1: Money', para('money') + ch1_extra + quotes)}
{sec('ch2', 'Chapter 2: Banks', para('banks') + ch2_extra)}
{sec('skip', 'What Can Be Safely Skipped', skipped)}
{sec('trading', 'Trading & Investing Lessons', lessons)}
{sec('take', 'Key Takeaways', f'<h3>A</h3><p>{strong}</p>')}
{sec('contra', 'Contrarian Ideas', '<h3>B</h3><p>x</p>')}
{sec('quotes', 'Notable Quotes', '<p>q</p>')}
{sec('alleg', 'Allegories &amp; Cultural References', '<table role="presentation">' + rows + '</table>')}
{sec('refs', 'Referenced Works', '<table role="presentation">' + refs + '</table>')}
{sec('fit', "What Didn't Fit", fit)}
<footer>Author, 2020</footer>
{sec('author', 'About the Author', '<p>Bio one.</p><p>Bio two.</p>')}
<script>var BM_KEY = 'bm_test';</script>
<script src="../book.js"></script>
</body></html>'''


NOTES = '''<!-- pp. 1-10 -->
## Chapter 1: Money
- [MUST KNOW][N001] Money is a claim. KEY: argument about money
- [SHOULD KNOW][N002] Supply matters. KEY: paragraph 3 about money
- [NICE TO KNOW][N003] Trivia, never graded.
<!-- pp. 11-20 -->
## Chapter 2: Banks
- [MUST KNOW][N004] Banks create deposits. KEY: argument about banks
- [MUST KNOW][N005] Reserves are not lent out. KEY: reserves are not lent
'''


def run(root, *cmd, env=None):
    return subprocess.run(['/usr/bin/python3', os.path.join(root, cmd[0]), *cmd[1:]], capture_output=True, text=True,
                          env=dict(os.environ, **(env or {})), timeout=120)


def main():
    root = tempfile.mkdtemp(prefix='grader-test-')
    try:
        for s in SCRIPTS:
            shutil.copy2(os.path.join(BOOKS, s), root)
        book = os.path.join(root, 'Test_Book')
        os.makedirs(book)

        print('check_html')
        open(os.path.join(book, 'index.html'), 'w').write(book_html())
        r = run(root, 'check_html.py', 'Test_Book')
        check('a page that follows the rules passes', r.returncode == 0, r.stdout[-900:])
        open(os.path.join(book, 'index.html'), 'w').write(book_html(cover=True))
        r = run(root, 'check_html.py', 'Test_Book')
        check('cover image inside the page is an error', r.returncode == 1 and 'cover image' in r.stdout)
        open(os.path.join(book, 'index.html'), 'w').write(book_html().replace(para('banks'), para('banks', 5)))
        r = run(root, 'check_html.py', 'Test_Book')
        check('a 5-paragraph chapter is an error', r.returncode == 1 and '5 paragraphs' in r.stdout, r.stdout[-400:])
        r = run(root, 'check_html.py', 'Test_Book', '--progress')
        check('--progress still flags the thin chapter', r.returncode == 1)

        print('grade_coverage + audit_check')
        env = {'GRADER_CLAUDE': os.path.join(HERE, 'fake_grader.py')}
        open(os.path.join(book, 'notes.md'), 'w').write(NOTES)
        open(os.path.join(book, 'index.html'), 'w').write(book_html())
        r = run(root, 'grade_coverage.py', 'Test_Book', env=env)
        audit = json.load(open(os.path.join(book, 'coverage_audit.json')))
        st = {n['id']: n['status'] for n in audit['nuggets']}
        check('covered nuggets found with evidence', st.get('N001') == 'COVERED' and st.get('N004') == 'COVERED', st)
        check('NICE TO KNOW not graded', 'N003' not in st)
        check('nugget absent from the page is MISSING', st.get('N005') == 'MISSING', st)
        check('grader exits 1 when something is missing', r.returncode == 1, r.stdout[-300:])
        r = run(root, 'audit_check.py', 'Test_Book')
        check('audit_check fails on the missing nugget', r.returncode == 1 and 'N005' in r.stdout, r.stdout)

        extra = '<p>The book explains that reserves are not lent out to customers, contrary to the textbook story told for decades.</p>'
        open(os.path.join(book, 'index.html'), 'w').write(book_html(ch2_extra=extra))
        r = run(root, 'grade_coverage.py', 'Test_Book', env=env)
        check('after the fix everything passes', r.returncode == 0, r.stdout[-400:])
        r = run(root, 'audit_check.py', 'Test_Book')
        check('audit_check passes', r.returncode == 0, r.stdout)
        with open(os.path.join(book, 'index.html'), 'a') as f:
            f.write('\n<!-- edited after grading -->\n')
        r = run(root, 'audit_check.py', 'Test_Book')
        check('editing the page after grading makes the audit stale', r.returncode == 1 and 'stale' in r.stdout, r.stdout)

        audit = json.load(open(os.path.join(book, 'coverage_audit.json')))
        audit['grader'] = 'me'
        json.dump(audit, open(os.path.join(book, 'coverage_audit.json'), 'w'))
        r = run(root, 'audit_check.py', 'Test_Book')
        check('a hand-written audit is rejected', r.returncode == 1 and 'not written by grade_coverage' in r.stdout)

        open(os.path.join(book, 'notes.md'), 'w').write(NOTES.replace('Money is a claim.', 'Money is a claim. FAKE-EVIDENCE'))
        open(os.path.join(book, 'index.html'), 'w').write(book_html(ch2_extra=extra))
        r = run(root, 'grade_coverage.py', 'Test_Book', env=env)
        audit = json.load(open(os.path.join(book, 'coverage_audit.json')))
        n1 = next(n for n in audit['nuggets'] if n['id'] == 'N001')
        check('a quote that is not on the page is caught', n1['status'] == 'PARTIAL' and not n1.get('evidence_verified'), n1)

        open(os.path.join(book, 'notes.md'), 'w').write(NOTES)
        open(os.path.join(book, 'index.html'), 'w').write(book_html(ch2_extra=extra + '<p>NO-CAVEATS here.</p>'))
        r = run(root, 'grade_coverage.py', 'Test_Book', env=env)
        rep = json.load(open(os.path.join(book, 'debate_ready_report.json')))
        check('a chapter missing caveats fails the debate test', rep['chapters_failed'] == 1 and not rep['pass'], rep.get('failures'))

        open(os.path.join(book, 'notes.md'), 'w').write(NOTES.replace('[MUST KNOW][N001]', '[MUST KNOW]'))
        r = run(root, 'grade_coverage.py', 'Test_Book', env=env)
        check('notes without IDs are refused with the fix', r.returncode == 2 and '--add-ids' in r.stdout, r.stdout)
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print(f'\n{failures} FAILED' if failures else '\nALL PASSED')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
