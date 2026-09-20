#!/usr/bin/env python3
"""
run_state.py — get/set values in a book folder's .run_state.json (dotted keys).

  python3 run_state.py Book_Folder get extraction.status        -> prints value ('' if absent)
  python3 run_state.py Book_Folder set html.status PASSED
  python3 run_state.py Book_Folder set complete true            -> true/false/null/numbers are typed
  python3 run_state.py Book_Folder set shelf_update.tier now
  python3 run_state.py Book_Folder show                         -> pretty-print the file
"""

import json
import os
import sys
from datetime import datetime


def load(path):
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def coerce(v):
    if v in ('true', 'false'):
        return v == 'true'
    if v == 'null':
        return None
    try:
        if v.strip().lstrip('-').isdigit():
            return int(v)
        return float(v)
    except ValueError:
        return v


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    folder, op = sys.argv[1], sys.argv[2]
    path = os.path.join(folder, '.run_state.json')
    st = load(path)

    if op == 'show':
        print(json.dumps(st, indent=2))
        return 0
    if op == 'get':
        cur = st
        for k in sys.argv[3].split('.'):
            if not isinstance(cur, dict) or k not in cur:
                print('')
                return 0
            cur = cur[k]
        print(cur if not isinstance(cur, (dict, list)) else json.dumps(cur))
        return 0
    if op == 'set':
        keys = sys.argv[3].split('.')
        val = coerce(sys.argv[4]) if len(sys.argv) > 4 else None
        cur = st
        for k in keys[:-1]:
            cur = cur.setdefault(k, {})
        cur[keys[-1]] = val
        st['updated'] = datetime.now().isoformat(timespec='seconds')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(st, f, indent=2)
        return 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main())
