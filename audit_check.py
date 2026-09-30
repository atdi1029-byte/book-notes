#!/usr/bin/env python3
"""
audit_check.py — check the coverage audit and debate-ready report for a book.

  python3 audit_check.py Book_Folder

Both files must come from grade_coverage.py (the independent grader, not the
writer) and belong to the current notes.md and index.html (their SHA-256 is
recorded when grading, so editing the page after grading makes the audit
stale). Coverage passes only when every [MUST KNOW]/[SHOULD KNOW] ID in
notes.md is in the audit and marked COVERED (or MERGED into another ID that is
covered). The debate report passes only when every graded chapter passed.

Exit: 0 pass, 1 fail or stale, 2 a file is missing / unreadable.
"""

import hashlib
import json
import os
import re
import sys

TAG_ID_RE = re.compile(r'\[(MUST KNOW|SHOULD KNOW)\]\s*\[N(\d+)\]')


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def load(path):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except Exception as e:
        return {'_error': str(e)}


def provenance(data, name, d):
    probs = []
    if data.get('grader') != 'grade_coverage.py':
        probs.append(f'{name} was not written by grade_coverage.py (the writer must not grade its own page)')
    if data.get('notes_sha256') != sha(os.path.join(d, 'notes.md')):
        probs.append(f'{name} is stale: notes.md changed after grading — re-run grade_coverage.py')
    if data.get('html_sha256') != sha(os.path.join(d, 'index.html')):
        probs.append(f'{name} is stale: index.html changed after grading — re-run grade_coverage.py')
    return probs


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    arg = sys.argv[1].rstrip('/')
    d = os.path.dirname(arg) if arg.endswith('.json') else arg
    if not os.path.isabs(d):
        d = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.basename(d)) \
            if not os.path.isdir(d) else os.path.abspath(d)
    for f in ('notes.md', 'index.html'):
        if not os.path.isfile(os.path.join(d, f)):
            print(f'  {f} missing in {d}')
            return 2

    audit = load(os.path.join(d, 'coverage_audit.json'))
    debate = load(os.path.join(d, 'debate_ready_report.json'))
    missing = [n for n, v in (('coverage_audit.json', audit), ('debate_ready_report.json', debate)) if v is None]
    if missing:
        print('  MISSING: ' + ', '.join(missing) + ' — run ./grade_coverage.py ' + os.path.basename(d))
        return 2
    for n, v in (('coverage_audit.json', audit), ('debate_ready_report.json', debate)):
        if '_error' in v:
            print(f'  {n}: unreadable ({v["_error"]})')
            return 2

    problems = provenance(audit, 'coverage_audit.json', d) + provenance(debate, 'debate_ready_report.json', d)

    notes = open(os.path.join(d, 'notes.md'), encoding='utf-8', errors='replace').read()
    required = {'N' + m.group(2): m.group(1) for m in TAG_ID_RE.finditer(notes)}
    rows = {}
    for n in audit.get('nuggets', []):
        if n.get('id') in rows:
            problems.append(f'{n.get("id")} is listed twice in the audit')
        rows[n.get('id')] = n
    absent = sorted(set(required) - set(rows))
    if absent:
        problems.append(f'{len(absent)} MUST/SHOULD nugget(s) not in the audit: ' + ', '.join(absent[:12]))
    not_covered = []
    for nid in required:
        n = rows.get(nid)
        if not n:
            continue
        st = str(n.get('status', '')).upper()
        if st == 'MERGED':
            target = rows.get(n.get('merged_into'))
            if not target or str(target.get('status', '')).upper() != 'COVERED':
                not_covered.append(f'{nid} MERGED into a nugget that is not covered')
        elif st != 'COVERED':
            not_covered.append(f'{nid} {st}: {str(n.get("issue", ""))[:80]}')
    if not_covered:
        problems.append(f'{len(not_covered)} nugget(s) not covered:')
        problems.extend('    ' + x for x in not_covered[:15])
        if len(not_covered) > 15:
            problems.append(f'    … and {len(not_covered) - 15} more')

    if not debate.get('chapters_tested'):
        problems.append('debate report tested no chapters')
    if debate.get('chapters_failed') or debate.get('failures') or debate.get('pass') is not True:
        problems.append(f'debate-ready: {debate.get("chapters_failed", "?")} chapter(s) failed:')
        for f in (debate.get('failures') or [])[:10]:
            problems.append(f'    {str(f.get("chapter", "?"))[:50]} — missing {", ".join(f.get("missing", []))}')

    if problems:
        print(f'  audits: FAIL — {os.path.basename(d)}')
        for p in problems:
            print('    ' + p if not p.startswith('    ') else p)
        return 1
    print(f'  audits: PASS — {len(required)} nuggets covered, {debate.get("chapters_tested")} chapters debate-ready')
    return 0


if __name__ == '__main__':
    sys.exit(main())
