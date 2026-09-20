#!/usr/bin/env python3
"""
audit_check.py — Mechanically verify the audit artifacts Claude writes in stages 7–8.

  python3 audit_check.py Book_Folder/coverage_audit.json
      PASS unless any MUST/SHOULD nugget is marked MISSING or PARTIAL.
      Understands both a per-nugget list (status/coverage/result + priority/tag)
      and a summary block (missing/partial counts). Falls back to counting
      "MISSING"/"PARTIAL" string values anywhere in the file.

  python3 audit_check.py Book_Folder/debate_ready_report.json
      PASS unless a status/verdict/pass/result/ready field says FAIL / false /
      NOT READY / INCOMPLETE, or an "issues"/"gaps"/"missing" list is non-empty.

Exit: 0 pass, 1 fail, 2 file missing / unreadable.
"""

import json
import os
import sys

BAD_STATUSES = {'MISSING', 'PARTIAL', 'FAIL', 'FAILED', 'NOT READY', 'NOT_READY',
                'INCOMPLETE', 'NO', 'FALSE'}
STATUS_KEYS = {'status', 'coverage', 'result', 'verdict', 'state', 'covered', 'ready', 'pass', 'passed'}
PRIORITY_KEYS = {'priority', 'tag', 'importance', 'level', 'tier', 'type'}
LIST_KEYS = {'issues', 'gaps', 'missing', 'missing_nuggets', 'partial', 'partial_nuggets', 'blockers', 'problems'}


def walk(node, parent=None):
    """Yield (dict, parent_key) for every dict in the tree."""
    if isinstance(node, dict):
        yield node, parent
        for k, v in node.items():
            yield from walk(v, k)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v, parent)


def bad_value(v):
    if isinstance(v, bool):
        return v is False
    if isinstance(v, str):
        return v.strip().upper() in BAD_STATUSES
    return False


def is_must_or_should(d):
    for k, v in d.items():
        if k.lower() in PRIORITY_KEYS and isinstance(v, str):
            u = v.upper()
            if 'MUST' in u or 'SHOULD' in u:
                return True
            if 'NICE' in u:
                return False
    # Also accept nugget text that carries the tag inline
    for v in d.values():
        if isinstance(v, str) and ('[MUST KNOW]' in v or '[SHOULD KNOW]' in v):
            return True
    return None  # unknown priority -> treat as counting


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    path = sys.argv[1]
    name = os.path.basename(path)
    if not os.path.isfile(path):
        print(f'  {name}: MISSING')
        return 2
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f'  {name}: unreadable ({e})')
        return 2

    problems = []
    nice_only = 0
    for d, parent in walk(data):
        # summary-style counts: {"missing": 3, "partial": 1}
        for k, v in d.items():
            kl = k.lower()
            if kl in ('missing', 'partial', 'missing_count', 'partial_count', 'unresolved') and isinstance(v, int) and v > 0:
                problems.append(f'{k}={v}')
            if kl in LIST_KEYS and isinstance(v, list) and v:
                problems.append(f'{k}: {len(v)} item(s)')
        # per-item statuses
        for k, v in d.items():
            if k.lower() in STATUS_KEYS and bad_value(v):
                pri = is_must_or_should(d)
                if pri is False:
                    nice_only += 1
                    continue
                label = d.get('id') or d.get('nugget') or d.get('nugget_id') or d.get('name') or d.get('title') or parent or '?'
                problems.append(f'{label}: {k}={v}')

    if not problems:
        # last resort: raw string scan (only if nothing structured was found)
        raw = json.dumps(data).upper()
        hits = raw.count('"MISSING"') + raw.count('"PARTIAL"') + raw.count('"NOT READY"')
        if hits and nice_only == 0:
            problems.append(f'{hits} MISSING/PARTIAL value(s) found (unstructured)')

    if problems:
        print(f'  {name}: FAIL — {len(problems)} problem(s)')
        for p in problems[:15]:
            print(f'      - {p}')
        if len(problems) > 15:
            print(f'      ... and {len(problems) - 15} more')
        return 1
    extra = f' ({nice_only} NICE-TO-KNOW gaps ignored)' if nice_only else ''
    print(f'  {name}: PASS{extra}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
