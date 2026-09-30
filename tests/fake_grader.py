#!/usr/bin/python3
"""Stand-in for the grader's `claude -p` call (GRADER_CLAUDE=this file).

Marks a nugget COVERED when the text contains the nugget's key phrase (the
words after "KEY:" in the nugget), quoting the sentence that holds it; nugget
text containing "FAKE-EVIDENCE" gets a made-up quote so the page check can
catch it. A chapter fails the debate test when its text contains "NO-CAVEATS".
"""
import json
import re
import sys

args = sys.argv[1:]
prompt = args[args.index('-p') + 1]
text = prompt.split('TEXT:\n<<<', 1)[1].split('>>>', 1)[0]
nugget_block = prompt.split('NUGGETS:\n', 1)[1]
sentences = re.split(r'(?<=[.!?])\s+', ' '.join(text.split()))
out = []
for line in nugget_block.strip().splitlines():
    m = re.match(r'(N\d+) \[(MUST KNOW|SHOULD KNOW)\] (.*)', line)
    if not m:
        continue
    nid, _, body = m.groups()
    key = re.search(r'KEY:\s*([a-z ]+)', body)
    phrase = key.group(1).strip() if key else '@@none@@'
    hit = next((s for s in sentences if phrase in s.lower()), None)
    if 'FAKE-EVIDENCE' in body:
        out.append({'id': nid, 'status': 'COVERED', 'evidence': 'This sentence was never written anywhere on the page at all.', 'missing': ''})
    elif hit:
        out.append({'id': nid, 'status': 'COVERED', 'evidence': hit, 'missing': ''})
    else:
        out.append({'id': nid, 'status': 'MISSING', 'evidence': '', 'missing': 'not discussed'})
res = {'nuggets': out}
if 'Then judge the chapter' in prompt:
    res['debate'] = {'missing': ['caveats'] if 'NO-CAVEATS' in text else []}
print(json.dumps({'type': 'result', 'subtype': 'success', 'is_error': False,
                  'result': '```json\n' + json.dumps(res) + '\n```', 'total_cost_usd': 0.02, 'num_turns': 1}))
