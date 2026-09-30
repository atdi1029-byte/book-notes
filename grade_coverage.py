#!/usr/bin/env python3
"""
grade_coverage.py — independent coverage audit + debate-ready test for a book.

The writer never grades its own page. For each chapter of index.html a fresh
`claude -p` call (no tools, no memory, no CLAUDE.md) gets that chapter's text
and the MUST/SHOULD KNOW nuggets from notes.md that belong to it, and says for
each nugget COVERED / PARTIAL / MISSING, quoting the sentence that covers it.
Every quoted sentence is checked against the page. Nuggets not found in their
own chapter get a second look against the whole page. The same call judges
whether the chapter is debate-ready (claim, reasoning, evidence, caveats,
objection).

Writes coverage_audit.json and debate_ready_report.json (with hashes of
notes.md and index.html, so finish-book can tell they belong to the current
files).

  ./grade_coverage.py Book_Folder                 grade every chapter
  ./grade_coverage.py Book_Folder --chapters 3,7  re-grade some chapters (after fixes)
  ./grade_coverage.py Book_Folder --dry-run       show the chapter mapping and size, no calls
  ./grade_coverage.py Book_Folder --model opus

Exit: 0 both pass, 1 something to fix (listed per chapter), 2 usage/setup problem.
Test hook: GRADER_CLAUDE=/path/to/fake-claude.
"""

import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

BOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BOOKS_DIR)
from check_html import split_sections, classify, text_of  # noqa: E402
from verify_quotes import normalize  # noqa: E402

CLAUDE = os.environ.get('GRADER_CLAUDE', 'claude')
TAG_ID_RE = re.compile(r'\[(MUST KNOW|SHOULD KNOW)\]\s*\[N(\d+)\]')
TAG_NO_ID_RE = re.compile(r'\[(MUST KNOW|SHOULD KNOW)\](?!\s*\[N\d+\])')
WORDNUM = {w: i for i, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen '
                                      'fourteen fifteen sixteen seventeen eighteen nineteen twenty'.split())}
ROMAN = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100}
FRONT_BACK = ('prologue', 'preface', 'foreword', 'introduction', 'epilogue', 'afterword', 'conclusion', 'appendix')


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def roman(s):
    total, prev = 0, 0
    for ch in reversed(s.lower()):
        v = ROMAN.get(ch, 0)
        total = total - v if v < prev else total + v
        prev = max(prev, v)
    return total


def chapter_no(title):
    m = re.search(r'\b(?:chapter|ch\.?)\s+(\d+|[ivxlc]+\b|[a-z]+)', title, re.I)
    if not m:
        m = re.match(r'\s*(\d+)[.:)]\s', title)
        return int(m.group(1)) if m else None
    tok = m.group(1).lower()
    if tok.isdigit():
        return int(tok)
    if tok in WORDNUM:
        return WORDNUM[tok]
    if re.fullmatch(r'[ivxlc]+', tok):
        return roman(tok)
    return None


def norm_title(t):
    t = re.sub(r'\b(?:chapter|ch\.?)\s+\S+\s*[:.\-—–]?', ' ', t, flags=re.I)
    t = re.sub(r'\(.*?\)', ' ', t)
    return ' '.join(normalize(t))


# ── notes ────────────────────────────────────────────────────────────────

def notes_nuggets(notes_text):
    """[(section_title, [nugget dicts])] in notes order."""
    sections = [['(before first heading)', []]]
    lines = notes_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('## '):
            sections.append([line[3:].strip(), []])
        m = TAG_ID_RE.search(line)
        if m:
            body = [line.strip()]
            j = i + 1
            while j < len(lines) and lines[j].startswith((' ', '\t')) and lines[j].strip() and not TAG_ID_RE.search(lines[j]):
                body.append(lines[j].strip())
                j += 1
            text = re.sub(r'\s+', ' ', ' '.join(body))
            text = re.sub(r'^-\s*', '', text)
            sections[-1][1].append({'id': 'N' + m.group(2), 'tag': m.group(1), 'text': text[:1500]})
            i = j
            continue
        i += 1
    return [(t, n) for t, n in sections if n]


# ── page ─────────────────────────────────────────────────────────────────

class PageText:
    """Normalized word index of the page, for checking quoted evidence."""

    def __init__(self, text):
        self.words = normalize(text)
        self.idx = {}
        for k in range(len(self.words) - 3):
            self.idx.setdefault(tuple(self.words[k:k + 4]), []).append(k)

    def contains(self, sentence, threshold=0.8):
        q = normalize(sentence)
        if not q:
            return False
        if len(q) < 5:                      # short quote: must appear word for word
            return (' ' + ' '.join(q) + ' ') in (' ' + ' '.join(self.words) + ' ')
        starts = set()
        for k in range(len(q) - 3):
            for pos in self.idx.get(tuple(q[k:k + 4]), ()):
                starts.add(max(0, pos - k))
        qs = ' '.join(q)
        for s in list(starts)[:40]:
            window = ' '.join(self.words[s:s + len(q)])
            if difflib.SequenceMatcher(None, qs, window).ratio() >= threshold:
                return True
        return False


def page_sections(doc):
    out = []
    for s in split_sections(doc):
        if s['toc']:
            continue
        key = classify(s['title'], s['id']) or 'chapters'
        out.append({'title': s['title'], 'key': key, 'text': text_of(s['html'])})
    return out


def map_sections(note_secs, chapters):
    """note section index -> chapter index (or None)."""
    mapping = {}
    by_no = {}
    for ci, c in enumerate(chapters):
        n = chapter_no(c['title'])
        if n is not None:
            by_no.setdefault(n, ci)
    for ni, (title, _) in enumerate(note_secs):
        n = chapter_no(title)
        if n is not None and n in by_no:
            mapping[ni] = by_no[n]
            continue
        nt = norm_title(title)
        best, best_ci = 0.0, None
        for ci, c in enumerate(chapters):
            r = difflib.SequenceMatcher(None, nt, norm_title(c['title'])).ratio()
            if r > best:
                best, best_ci = r, ci
        low = title.lower()
        for word in FRONT_BACK:
            if word in low:
                for ci, c in enumerate(chapters):
                    if word in c['title'].lower():
                        best, best_ci = 1.0, ci
                        break
        mapping[ni] = best_ci if best >= 0.45 else None
    # A notes section with no heading match that sits between two sections
    # mapped to the same chapter belongs to that chapter too (continued notes).
    for ni in range(len(note_secs)):
        if mapping.get(ni) is None:
            prev = next((mapping[k] for k in range(ni - 1, -1, -1) if mapping.get(k) is not None), None)
            nxt = next((mapping[k] for k in range(ni + 1, len(note_secs)) if mapping.get(k) is not None), None)
            if prev is not None and prev == nxt:
                mapping[ni] = prev
    return mapping


# ── grader calls ─────────────────────────────────────────────────────────

PROMPT = """You are auditing a book summary page for coverage. Below is the text of {scope}, then the key points
("nuggets") from the source notes that it must preserve.

For each nugget decide:
- COVERED: a reader of this text could explain the point — the claim AND its reasoning or supporting
  evidence are there (the wording may differ).
- PARTIAL: the topic is there but the reasoning, the evidence, or an essential detail or number is missing.
- MISSING: not there.
For COVERED and PARTIAL copy the single best supporting sentence from the text EXACTLY, word for word
(8-40 words), as "evidence". For PARTIAL and MISSING say in a few words what is missing.
{debate}
Reply with ONLY a JSON object, no commentary:
{shape}

TEXT:
<<<
{text}
>>>

NUGGETS:
{nuggets}
"""

DEBATE = """
Then judge the chapter as a whole: could someone who read ONLY this text state the chapter's main claim,
why the author believes it, the key evidence, the main caveats or limits, and an obvious objection with
the author's answer? List whichever of those five are missing ("claim", "reasoning", "evidence",
"caveats", "objection").
"""


def call_grader(prompt, model):
    work = tempfile.mkdtemp(prefix='grader-')
    try:
        r = subprocess.run([CLAUDE, '-p', prompt, '--model', model, '--max-turns', '1', '--tools', '',
                            '--strict-mcp-config', '--no-session-persistence', '--output-format', 'json'],
                           cwd=work, capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired:
        return None, 0.0, 'timed out'
    finally:
        try:
            os.rmdir(work)
        except OSError:
            pass
    try:
        d = json.loads(r.stdout[r.stdout.index('{'):])
    except Exception:
        return None, 0.0, (r.stderr or r.stdout or 'no output')[:200]
    cost = float(d.get('total_cost_usd') or 0)
    text = str(d.get('result') or '')
    if d.get('is_error'):
        return None, cost, text[:200]
    try:
        return json.loads(text[text.index('{'):text.rindex('}') + 1]), cost, ''
    except Exception:
        return None, cost, 'unreadable answer: ' + text[:120]


def grade(prompt, model, expect_ids):
    """Call the grader (one retry) and return (dict, cost, error)."""
    total = 0.0
    err = ''
    for _ in range(2):
        res, cost, err = call_grader(prompt, model)
        total += cost
        if res and isinstance(res.get('nuggets'), list):
            got = {str(n.get('id', '')).strip() for n in res['nuggets']}
            if expect_ids <= got:
                return res, total, ''
            err = 'answer skipped nuggets: ' + ', '.join(sorted(expect_ids - got)[:8])
    return None, total, err


def fmt_nuggets(nugs):
    return '\n'.join(f"{n['id']} [{n['tag']}] {n['text']}" for n in nugs)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__)
        return 2
    folder = os.path.basename(args[0].rstrip('/'))
    d = os.path.join(BOOKS_DIR, folder)
    notes_p, html_p = os.path.join(d, 'notes.md'), os.path.join(d, 'index.html')
    for p in (notes_p, html_p):
        if not os.path.isfile(p):
            print(f'missing {p}')
            return 2
    model = sys.argv[sys.argv.index('--model') + 1] if '--model' in sys.argv else 'sonnet'
    if model in args:
        args.remove(model)
    only = None
    if '--chapters' in sys.argv:
        only = {int(x) for x in sys.argv[sys.argv.index('--chapters') + 1].split(',') if x.strip()}
    dry = '--dry-run' in sys.argv

    notes = open(notes_p, encoding='utf-8', errors='replace').read()
    untagged = TAG_NO_ID_RE.findall(notes)
    if untagged:
        print(f'{len(untagged)} MUST/SHOULD tags in notes.md have no [N###] ID — run: '
              f'./reorder_notes.py {folder}/notes.md --add-ids')
        return 2
    note_secs = notes_nuggets(notes)
    all_nugs = [n for _, ns in note_secs for n in ns]
    if not all_nugs:
        print('notes.md has no [MUST KNOW]/[SHOULD KNOW] nuggets with IDs — nothing to grade')
        return 2
    doc = open(html_p, encoding='utf-8', errors='replace').read()
    secs = page_sections(doc)
    chapters = [s for s in secs if s['key'] == 'chapters']
    page_text = '\n\n'.join(f"## {s['title']}\n{s['text']}" for s in secs)
    index = PageText(page_text)
    mapping = map_sections(note_secs, chapters)

    groups = {}          # chapter index (or None) -> nuggets
    for ni, (_, nugs) in enumerate(note_secs):
        groups.setdefault(mapping.get(ni), []).extend(nugs)

    print(f'═══ grade_coverage: {folder} — {len(all_nugs)} MUST/SHOULD nuggets, {len(chapters)} chapters ═══')
    for ci, c in enumerate(chapters, 1):
        n = len(groups.get(ci - 1, []))
        print(f'  {ci:>3}. {c["title"][:60]:<60} {n:>3} nuggets, {len(c["text"].split()):>6} words')
    if groups.get(None):
        print(f'   ?  (notes sections with no matching chapter: graded against the whole page) {len(groups[None])} nuggets')
    if dry:
        return 0

    audit_p = os.path.join(d, 'coverage_audit.json')
    debate_p = os.path.join(d, 'debate_ready_report.json')
    prev = {}
    prev_debate = {}
    if only and os.path.isfile(audit_p):
        prev = {n['id']: n for n in json.load(open(audit_p)).get('nuggets', [])}
        if os.path.isfile(debate_p):
            prev_debate = {c['chapter']: c for c in json.load(open(debate_p)).get('chapters', [])}

    results = {}
    debate = {}
    cost = 0.0
    problems = []
    for ci, c in enumerate(chapters):
        nugs = groups.get(ci, [])
        num = ci + 1
        if only and num not in only:
            for n in nugs:
                if n['id'] in prev:
                    results[n['id']] = prev[n['id']]
            if c['title'] in prev_debate:
                debate[c['title']] = prev_debate[c['title']]
            continue
        if not nugs:
            continue
        print(f'  grading {num}. {c["title"][:60]} …', flush=True)
        prompt = PROMPT.format(scope='ONE chapter section of the summary', debate=DEBATE,
                               shape='{"nuggets":[{"id":"N001","status":"COVERED","evidence":"...","missing":""}],'
                                     '"debate":{"missing":[]}}',
                               text=f"{c['title']}\n{c['text']}", nuggets=fmt_nuggets(nugs))
        res, spent, err = grade(prompt, model, {n['id'] for n in nugs})
        cost += spent
        if not res:
            problems.append(f'chapter {num}: grader failed ({err})')
            for n in nugs:
                results[n['id']] = {'id': n['id'], 'tag': n['tag'], 'status': 'UNGRADED', 'location': c['title'], 'issue': err}
            continue
        answers = {str(a.get('id')).strip(): a for a in res['nuggets']}
        for n in nugs:
            a = answers.get(n['id'], {})
            results[n['id']] = {'id': n['id'], 'tag': n['tag'], 'status': str(a.get('status', 'MISSING')).upper(),
                                'location': c['title'], 'evidence': a.get('evidence', ''), 'issue': a.get('missing', '')}
        missing = [m for m in (res.get('debate') or {}).get('missing', []) if m]
        debate[c['title']] = {'chapter': c['title'], 'number': num, 'pass': not missing, 'missing': missing}

    # Nuggets from unmatched notes sections and the ones not found in their own
    # chapter get one look at the whole page.
    second = [n for n in groups.get(None, [])] + [
        n for n in all_nugs if results.get(n['id'], {}).get('status') in ('PARTIAL', 'MISSING')]
    second = [n for n in second if not only or n['id'] not in prev or n['id'] in results]
    if second:
        print(f'  second look at {len(second)} nugget(s) against the whole page …', flush=True)
        for k in range(0, len(second), 40):
            chunk = second[k:k + 40]
            prompt = PROMPT.format(scope='the WHOLE summary page (every section)', debate='',
                                   shape='{"nuggets":[{"id":"N001","status":"COVERED","evidence":"...","missing":""}]}',
                                   text=page_text, nuggets=fmt_nuggets(chunk))
            res, spent, err = grade(prompt, model, {n['id'] for n in chunk})
            cost += spent
            if not res:
                problems.append(f'second look failed ({err})')
                for n in chunk:
                    results.setdefault(n['id'], {'id': n['id'], 'tag': n['tag'], 'status': 'UNGRADED', 'issue': err})
                continue
            answers = {str(a.get('id')).strip(): a for a in res['nuggets']}
            for n in chunk:
                a = answers.get(n['id'], {})
                st = str(a.get('status', 'MISSING')).upper()
                old = results.get(n['id'], {'status': 'MISSING'})
                rank = {'MISSING': 0, 'UNGRADED': 0, 'PARTIAL': 1, 'COVERED': 2}
                if rank.get(st, 0) > rank.get(old['status'], 0) or n['id'] not in results:
                    results[n['id']] = {'id': n['id'], 'tag': n['tag'], 'status': st, 'location': 'elsewhere on the page',
                                        'evidence': a.get('evidence', ''), 'issue': a.get('missing', '')}

    # Evidence must really be on the page.
    for r in results.values():
        if r['status'] in ('COVERED', 'PARTIAL') and not index.contains(r.get('evidence', '')):
            if r['status'] == 'COVERED':
                r['status'] = 'PARTIAL'
                r['issue'] = 'the quoted evidence is not on the page'
            r['evidence_verified'] = False
        elif r['status'] in ('COVERED', 'PARTIAL'):
            r['evidence_verified'] = True

    nuggets = [results.get(n['id'], {'id': n['id'], 'tag': n['tag'], 'status': 'UNGRADED'}) for n in all_nugs]
    count = lambda st: sum(1 for n in nuggets if n['status'] == st)
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    stamp = {'grader': 'grade_coverage.py', 'model': model, 'timestamp': now,
             'notes_sha256': sha(notes_p), 'html_sha256': sha(html_p)}
    audit = dict(stamp, total_must_know=sum(1 for n in all_nugs if n['tag'] == 'MUST KNOW'),
                 total_should_know=sum(1 for n in all_nugs if n['tag'] == 'SHOULD KNOW'),
                 covered=count('COVERED'), partial=count('PARTIAL'), missing=count('MISSING'),
                 ungraded=count('UNGRADED'), merged=0,
                 **{'pass': all(n['status'] == 'COVERED' for n in nuggets)}, nuggets=nuggets)
    chapter_list = [debate[c['title']] for c in chapters if c['title'] in debate]
    failures = [c for c in chapter_list if not c['pass']]
    report = dict(stamp, chapters_tested=len(chapter_list), chapters_passed=len(chapter_list) - len(failures),
                  chapters_failed=len(failures), **{'pass': not failures and bool(chapter_list)},
                  failures=[{'chapter': c['chapter'], 'missing': c['missing']} for c in failures],
                  chapters=chapter_list)
    json.dump(audit, open(audit_p, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
    json.dump(report, open(debate_p, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

    print(f'\n  Coverage: {audit["covered"]} covered, {audit["partial"]} partial, {audit["missing"]} missing'
          + (f', {audit["ungraded"]} ungraded' if audit['ungraded'] else '')
          + f' of {len(nuggets)}  →  {"PASS" if audit["pass"] else "FAIL"}')
    print(f'  Debate-ready: {report["chapters_passed"]}/{report["chapters_tested"]} chapters  →  {"PASS" if report["pass"] else "FAIL"}')
    print(f'  Grader cost: ${cost:.2f}')
    todo = [n for n in nuggets if n['status'] != 'COVERED']
    if todo:
        print('\n  Fix these in the chapter prose, then re-run with --chapters N:')
        for n in todo[:60]:
            print(f"    {n['id']} [{n['tag']}] {n['status']} — {n.get('location', '?')[:40]}: {n.get('issue', '')[:100]}")
    for f in failures:
        print(f"    debate: {f['chapter'][:50]} — missing {', '.join(f['missing'])}")
    for p in problems:
        print('    ! ' + p)
    return 0 if audit['pass'] and report['pass'] else 1


if __name__ == '__main__':
    sys.exit(main())
