#!/usr/bin/env python3
"""Backfill outline category + flag for concepts that predate the outline.

  python3 backfill_outline.py            # file everything not yet filed
  python3 backfill_outline.py --all      # re-file everything (overwrites)
  python3 backfill_outline.py --dry      # show what would be sent, no calls

Batches ~40 concepts per Sonnet call (title + summary in, slug -> category/flag
out).  Saves after every batch.  Concepts the model skips or mis-names keep
their legacy mapping and are listed at the end so you can fix them by hand.
Rebuilds the HTML at the end; push separately (or --push).
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from finance_guide import (  # noqa: E402
    CONCEPTS_FILE, CATEGORIES, FILEABLE, FLAGS, load_json, save_json, log,
    run_claude, category_rubric, rebuild_html, git_push, concept_category,
)

BATCH = 40


def prompt_for(batch):
    listing = "\n".join(
        f'- {slug}: "{c["title"]}" — {c.get("summary", "")}' for slug, c in batch
    )
    return f"""You are filing entries of a finance glossary into a reading-list outline.

CATEGORIES (use the exact name):
{category_rubric()}

FLAG:
- "star": must-know — you cannot follow a markets conversation without it.
- "plain": standard working knowledge for someone actively trading or investing.
- "deep": deep cut — sector plumbing, single-country or single-industry mechanics,
  a curiosity (fertilizer pricing, farm loan-loss provisions, exchange inventories).
Aim for roughly a third star, a third plain, a third deep across a typical batch;
be strict about "star".

CONCEPTS:
{listing}

Output ONLY a JSON object mapping every slug above to its filing:
{{"slug_here": {{"category": "<exact category name>", "flag": "star|plain|deep"}}, ...}}
"""


def backfill(concepts, redo=False, dry=False):
    todo = [(s, c) for s, c in concepts.items()
            if redo or c.get("category") not in CATEGORIES or c.get("flag") not in FLAGS]
    log(f"{len(todo)} concepts to file")
    unresolved = []
    for i in range(0, len(todo), BATCH):
        batch = todo[i:i + BATCH]
        log(f"  Batch {i // BATCH + 1}: {len(batch)} concepts")
        if dry:
            print(prompt_for(batch)[:1500] + "\n...\n")
            continue
        out = run_claude(prompt_for(batch), timeout=300)
        m = re.search(r"\{.*\}", out or "", re.DOTALL)
        data = None
        if m:
            try:
                data = json.loads(m.group())
            except json.JSONDecodeError:
                pass
        if not isinstance(data, dict):
            log("  Batch FAILED — leaving these on legacy mapping")
            unresolved += [s for s, _ in batch]
            continue
        for slug, c in batch:
            f = data.get(slug) or {}
            cat, flag = f.get("category"), f.get("flag")
            if cat in FILEABLE and flag in FLAGS:
                c["category"], c["flag"] = cat, flag
            else:
                c["category"] = concept_category(c)
                c.setdefault("flag", "plain")
                unresolved.append(slug)
        save_json(CONCEPTS_FILE, concepts)
    return unresolved


if __name__ == "__main__":
    args = sys.argv[1:]
    concepts = load_json(CONCEPTS_FILE)
    left = backfill(concepts, redo="--all" in args, dry="--dry" in args)
    if "--dry" in args:
        sys.exit()
    if left:
        log(f"{len(left)} left on legacy mapping (fix by hand in concepts.json): "
            + ", ".join(left))
    rebuild_html(concepts)
    if "--push" in args:
        git_push()
    log("Backfill done")
