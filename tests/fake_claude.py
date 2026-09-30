#!/usr/bin/python3
"""Stand-in for `claude -p` in bookai tests (BOOKAI_CLAUDE=this file).

Reads pages.txt from its working directory, writes notes.md the way a good
model would (acks, tagged bullets, one verbatim quote per page), and prints
the same JSON shape as `claude -p --output-format json`.

Behaviour switches come from the JSON file in $FAKE_CLAUDE_RULES:
  fail_pages:            pages that make a Sonnet batch write nothing
  filter_pages:          pages that trigger a content-filter error on Sonnet
  rate_limit_first:      first call answers 429
  usage_limit_at_call:   that call (1-based) answers "usage limit reached"
  sleep:                 seconds to sleep before answering (interrupt tests)
Every call is appended to $FAKE_CLAUDE_LOG as one JSON line.
"""
import json
import os
import re
import sys
import time

args = sys.argv[1:]
prompt = args[args.index('-p') + 1] if '-p' in args else ''
model = args[args.index('--model') + 1] if '--model' in args else '?'
rules_path = os.environ.get('FAKE_CLAUDE_RULES', '')
rules = json.load(open(rules_path)) if rules_path and os.path.exists(rules_path) else {}
log_path = os.environ.get('FAKE_CLAUDE_LOG', '/dev/null')

m = re.search(r'For EVERY page in the range (\d+)-(\d+)', prompt)
s, e = (int(m.group(1)), int(m.group(2))) if m else (0, -1)
calls = 0
if log_path != '/dev/null' and os.path.exists(log_path):
    calls = sum(1 for _ in open(log_path))
calls += 1
with open(log_path, 'a') as f:
    f.write(json.dumps({'call': calls, 'model': model, 'range': [s, e], 'cwd': os.getcwd(), 'args': args[2:],
                        'rejected_before': 'REJECTED because' in prompt}) + '\n')


def answer(result='Notes written.', is_error=False, subtype='success', api=None):
    out = {'type': 'result', 'subtype': subtype, 'is_error': is_error, 'result': result,
           'total_cost_usd': 0.01, 'num_turns': 3}
    if api:
        out['api_error_status'] = api
    print(json.dumps(out))
    sys.exit(0)


time.sleep(float(rules.get('sleep', 0)))
pages = set(range(s, e + 1))
if rules.get('rate_limit_first') and calls == 1:
    answer('Rate limit exceeded', True, 'error_during_execution', 429)
if rules.get('usage_limit_at_call') == calls:
    answer('Claude usage limit reached. Your limit will reset at 5pm.', True, 'error_during_execution')
if model == 'sonnet' and pages & set(rules.get('filter_pages', [])):
    answer('Output blocked by content filtering policy', True, 'error_during_execution')
if model == 'sonnet' and pages & set(rules.get('fail_pages', [])):
    answer('I could not finish.')      # no notes.md → the gate rejects the batch

text = open('pages.txt', encoding='utf-8').read()
chunks = re.split(r'(?m)^=== PAGE (\d+) ===.*$', text)
page_text = {int(chunks[i]): chunks[i + 1] for i in range(1, len(chunks) - 1, 2)}
out = ['## Chapter %d: Test chapter' % (s // 10 + 1)]
n = 1
for p in range(s, e + 1):
    body = page_text.get(p, '')
    sentences = re.findall(r'[A-Z][^.]{25,}\.', body)
    if not sentences:
        out.append('<!-- page %d: no content -->' % p)
        continue
    out.append('### Page %d' % p)
    out.append('- [MUST KNOW][N%03d] %s' % (n, sentences[0]))
    n += 1
    if len(sentences) > 1:
        out.append('- [SHOULD KNOW][N%03d] %s' % (n, sentences[1]))
        n += 1
    out.append('- Detail for page %d, with enough words to count as real notes about the argument.' % p)
    out.append('> "%s" — Author' % sentences[0].rstrip('.'))
    out.append('<!-- page %d: 2 nuggets -->' % p)
open('notes.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
answer()
