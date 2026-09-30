#!/usr/bin/python3
"""bookai end-to-end tests with a fake `claude` (no API calls, ~1 min).

Runs a copy of the pipeline scripts in a temp folder against a generated
30-page PDF:  clean run · re-run does nothing · resume fills only gaps ·
failing batch is split and only the small bad range goes to Haiku ·
content filter · rate limit backoff · usage limit stops and resumes ·
folder lock · Ctrl-C stops every worker · claude runs outside the home
folder with only Read/Write.

  /usr/bin/python3 tests/bookai_test.py
"""
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
BOOKS = os.path.dirname(HERE)
FAKE = os.path.join(HERE, 'fake_claude.py')
SCRIPTS = ['bookai', 'bookai_lib.py', '_python.sh', 'verify_quotes.py', 'reorder_notes.py', 'run_state.py']

failures = 0


def check(name, ok, detail=None):
    global failures
    print(('  PASS ' if ok else '  FAIL ') + name + ('' if ok or detail is None else '  → ' + str(detail)[:300]))
    if not ok:
        failures += 1


def make_pdf(path, pages=30):
    import pymupdf as fitz
    doc = fitz.open()
    for p in range(1, pages + 1):
        page = doc.new_page()
        if p == 12:
            continue                                   # blank page
        lines = [f'Page {p} opens with the claim that idea number {p} changes how markets behave.',
                 f'The author supports idea {p} with a detailed historical example from year {1900 + p}.',
                 f'A caveat follows: idea {p} fails when liquidity disappears during a panic.']
        y = 72
        for ln in lines:
            page.insert_text((72, y), ln, fontsize=11)
            y += 18
        if p == 20:
            pix = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 200, 150), 0)
            pix.set_rect(pix.irect, (120, 160, 220))
            page.insert_image(fitz.Rect(72, 200, 472, 500), pixmap=pix)
    doc.save(path)


class Env:
    def __init__(self):
        self.root = tempfile.mkdtemp(prefix='bookai-test-')
        for s in SCRIPTS:
            shutil.copy2(os.path.join(BOOKS, s), os.path.join(self.root, s))
        self.pdf = os.path.join(self.root, 'test book.pdf')
        make_pdf(self.pdf)
        self.rules = os.path.join(self.root, 'rules.json')
        self.log = os.path.join(self.root, 'calls.jsonl')
        self.rule()

    def rule(self, **kw):
        json.dump(kw, open(self.rules, 'w'))
        open(self.log, 'w').close()

    def env(self):
        e = dict(os.environ, BOOKAI_CLAUDE=FAKE, BOOKAI_BACKOFF='0',
                 FAKE_CLAUDE_RULES=self.rules, FAKE_CLAUDE_LOG=self.log)
        return e

    def run(self, folder, *extra, timeout=240):
        cmd = [os.path.join(self.root, 'bookai'), self.pdf, folder, '1', '0', '10', '0', '2', '--type=analytical', *extra]
        return subprocess.run(cmd, env=self.env(), capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL)

    def calls(self):
        return [json.loads(l) for l in open(self.log) if l.strip()]

    def notes(self, folder):
        return open(os.path.join(self.root, folder, 'notes.md')).read()

    def state(self, folder):
        return json.load(open(os.path.join(self.root, folder, '.run_state.json')))

    def pages_in_notes(self, folder):
        acks = re.findall(r'<!--\s*page\s+(\d+):', self.notes(folder))
        return [int(a) for a in acks]


def main():
    env = Env()
    try:
        print('Clean run')
        r = env.run('Clean')
        st = env.state('Clean')
        acks = env.pages_in_notes('Clean')
        check('exit 0', r.returncode == 0, r.stdout[-800:] + r.stderr[-400:])
        check('extraction PASSED', st['extraction']['status'] == 'PASSED', st['extraction'])
        check('every page acknowledged exactly once', sorted(acks) == list(range(1, 31)), acks)
        ids = re.findall(r'\[N(\d+)\]', env.notes('Clean'))
        check('nugget IDs unique and sequential', ids == ['%03d' % i for i in range(1, len(ids) + 1)])
        check('blank page acknowledged as no content', '<!-- page 12: no content -->' in env.notes('Clean'))
        calls = env.calls()
        home = os.path.expanduser('~')
        check('claude runs outside the home folder', all(not c['cwd'].startswith(home) for c in calls), [c['cwd'] for c in calls][:2])
        check('claude gets only Read/Write and no MCP', all('--tools' in c['args'] and 'Read,Write' in c['args'] and '--strict-mcp-config' in c['args'] for c in calls))
        check('cost recorded', st['extraction']['cost_usd'] > 0, st['extraction'].get('cost_usd'))
        pagestxt_fig = False
        check('no leftover temp or lock files', not [f for f in os.listdir(os.path.join(env.root, 'Clean')) if f.startswith(('.leaf_', '.bookai.lock'))])

        print('Re-run does nothing')
        before = env.notes('Clean')
        env.rule()
        r = env.run('Clean')
        check('no claude calls', len(env.calls()) == 0, env.calls())
        check('notes unchanged', env.notes('Clean') == before)

        print('Resume fills only the gap')
        folder = os.path.join(env.root, 'Clean')
        done = [l for l in open(os.path.join(folder, '.pages_done')) if l.strip() and not (14 <= int(l) <= 16)]
        open(os.path.join(folder, '.pages_done'), 'w').writelines(done)
        env.rule()
        r = env.run('Clean')
        ranges = [c['range'] for c in env.calls()]
        check('only pages 14-16 re-extracted', ranges == [[14, 16]], ranges)
        check('extraction PASSED again', env.state('Clean')['extraction']['status'] == 'PASSED')

        print('A failing batch is split; only the small bad range goes to Haiku')
        env.rule(fail_pages=[7])
        r = env.run('Split')
        calls = env.calls()
        st = env.state('Split')
        haiku = [c['range'] for c in calls if c['model'] == 'haiku']
        check('haiku used only for a small range around page 7', haiku and all(a <= 7 <= b and b - a < 4 for a, b in haiku), haiku)
        check('retry told the model why it was rejected', any(c['rejected_before'] for c in calls if c['range'] == [1, 10]))
        check('all pages extracted', sorted(env.pages_in_notes('Split')) == list(range(1, 31)))
        check('status DEGRADED with the haiku range recorded', st['extraction']['status'] == 'DEGRADED' and st['extraction']['haiku_ranges'], st['extraction'])

        print('Content filter goes straight to splitting')
        env.rule(filter_pages=[23])
        env.run('Filter')
        calls = env.calls()
        first = [c for c in calls if c['range'] == [21, 30]]
        check('filtered batch not retried on the same range', len(first) == 1, len(first))
        check('pages still all extracted', sorted(env.pages_in_notes('Filter')) == list(range(1, 31)))

        print('Rate limit: wait and retry')
        env.rule(rate_limit_first=True)
        r = env.run('Rate')
        check('run completes after a 429', env.state('Rate')['extraction']['status'] == 'PASSED', r.stdout[-400:])

        print('Usage limit: stop early, resume later')
        env.rule(usage_limit_at_call=2)
        r = env.run('Usage')
        st = env.state('Usage')
        check('stops with INCOMPLETE and stopped_early', st['extraction']['status'] == 'INCOMPLETE' and st['extraction']['stopped_early'], st['extraction'])
        check('non-zero exit', r.returncode != 0)
        n_calls = len(env.calls())
        check('no batches launched after the limit', n_calls <= 3, n_calls)
        env.rule()
        r = env.run('Usage')
        check('re-run finishes the book', env.state('Usage')['extraction']['status'] == 'PASSED' and sorted(env.pages_in_notes('Usage')) == list(range(1, 31)))

        print('Folder lock')
        lock = os.path.join(env.root, 'Locked', '.bookai.lock')
        os.makedirs(lock)
        open(os.path.join(lock, 'pid'), 'w').write(str(os.getpid()))
        env.rule()
        r = env.run('Locked')
        check('second run refused while the first is alive', r.returncode != 0 and 'already working' in r.stdout, r.stdout[-300:])
        open(os.path.join(lock, 'pid'), 'w').write('999999')
        r = env.run('Locked')
        check('stale lock removed and run completes', env.state('Locked')['extraction']['status'] == 'PASSED', r.stdout[-300:])

        print('Ctrl-C stops everything')
        env.rule(sleep=30)
        p = subprocess.Popen([os.path.join(env.root, 'bookai'), env.pdf, 'Interrupt', '1', '0', '10', '0', '2', '--type=analytical'],
                             env=env.env(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                             start_new_session=True)
        time.sleep(4)
        os.killpg(p.pid, signal.SIGINT)
        try:
            p.wait(timeout=20)
            stopped = True
        except subprocess.TimeoutExpired:
            stopped = False
            os.killpg(p.pid, signal.SIGKILL)
        time.sleep(1)
        leftovers = subprocess.run(['pgrep', '-f', FAKE], capture_output=True, text=True).stdout.split()
        check('bookai exits promptly', stopped and p.returncode in (130, -2), p.returncode)
        check('no fake claude processes left running', not leftovers, leftovers)
        check('lock released', not os.path.exists(os.path.join(env.root, 'Interrupt', '.bookai.lock')))
    finally:
        subprocess.run(['pkill', '-f', FAKE])
        shutil.rmtree(env.root, ignore_errors=True)
    print(f'\n{failures} FAILED' if failures else '\nALL PASSED')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
