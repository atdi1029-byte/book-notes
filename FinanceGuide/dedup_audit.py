#!/usr/bin/env python3
"""One-time dedup audit over the existing concepts.json.

  python3 dedup_audit.py              # fuzzy pass only, prints suspect pairs
  python3 dedup_audit.py --judge      # run EVERY concept past the Haiku judge
                                      # (~1 cheap call per concept); reports
                                      # each one it thinks duplicates another
  python3 dedup_audit.py --merge keep_slug:drop_slug [...]
                                      # merge drop into keep (after you approve)

Nothing is modified unless --merge is given.  Merged entries are archived to
merged_concepts.json (chapter included) so nothing is lost, then the HTML is
rebuilt.  Push separately (or pass --push).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from finance_guide import (  # noqa: E402
    BASE_DIR, CONCEPTS_FILE, load_json, save_json, log, _similarity,
    judge_duplicate, merge_into, rebuild_html, git_push,
    FUZZY_DUP_RATIO, FUZZY_DUP_JACCARD,
)

SUSPECT_RATIO = 0.70      # lower bar for the report than the live bot uses
SUSPECT_JACCARD = 0.40
ARCHIVE_FILE = BASE_DIR / "merged_concepts.json"


def fuzzy_pairs(concepts):
    slugs = list(concepts)
    pairs = []
    for i, a in enumerate(slugs):
        for b in slugs[i + 1:]:
            r, j = _similarity(concepts[a]["title"], concepts[b]["title"])
            if r >= SUSPECT_RATIO or j >= SUSPECT_JACCARD:
                auto = r >= FUZZY_DUP_RATIO or j >= FUZZY_DUP_JACCARD
                pairs.append((r, j, auto, a, b))
    pairs.sort(reverse=True)
    return pairs


def report(concepts):
    """Fuzzy-only report: title-similar pairs.  Weak signal — see notes."""
    pairs = fuzzy_pairs(concepts)
    print(f"{len(concepts)} concepts, {len(pairs)} title-similar pairs "
          f"(fuzzy only — run --judge for the real pass)\n")
    out = []
    for r, j, auto, a, b in pairs:
        out.append({
            "a": a, "b": b, "ratio": round(r, 2), "jaccard": round(j, 2),
            "would_auto_merge": auto,
            "a_title": concepts[a]["title"], "b_title": concepts[b]["title"],
        })
        flag = "AUTO " if auto else "     "
        print(f"{flag}{r:.2f}/{j:.2f}  {a}  <->  {b}")
        print(f"        {concepts[a]['title']}")
        print(f"        {concepts[b]['title']}\n")
    (BASE_DIR / "dedup_report.json").write_text(json.dumps(out, indent=2))
    print("Report written: dedup_report.json")


def judge_report(concepts):
    """Run every concept past the judge as if it were a new candidate
    against the rest of the book.  Prints suggested merges as
    keep:drop pairs you can feed straight back to --merge."""
    suggestions = []
    failed = 0
    slugs = list(concepts)
    for i, slug in enumerate(slugs, 1):
        c = concepts[slug]
        rest = {k: v for k, v in concepts.items() if k != slug}
        verdict = judge_duplicate(
            {"title": c["title"], "summary": c.get("summary", ""),
             "category": c.get("category")}, rest)
        if verdict is None:
            failed += 1
            print(f"[{i}/{len(slugs)}] {slug}: judge call FAILED")
            continue
        if verdict["verdict"] != "new":
            keep, drop = verdict["match_slug"], slug
            # Avoid reporting both directions of the same pair
            if any(s["keep"] == drop and s["drop"] == keep for s in suggestions):
                continue
            suggestions.append({
                "keep": keep, "drop": drop, "verdict": verdict["verdict"],
                "keep_title": concepts[keep]["title"], "drop_title": c["title"],
            })
            print(f"[{i}/{len(slugs)}] {verdict['verdict'].upper():8} "
                  f"{drop}  ->  {keep}")
            print(f"           '{c['title']}'  ->  '{concepts[keep]['title']}'")
        else:
            print(f"[{i}/{len(slugs)}] new       {slug}")
    (BASE_DIR / "dedup_report.json").write_text(
        json.dumps(suggestions, indent=2))
    print(f"\n{len(suggestions)} suggested merge(s), {failed} failed call(s).")
    print("Report written: dedup_report.json")
    if suggestions:
        print("\nTo apply the ones you agree with:")
        print("  python3 dedup_audit.py --merge "
              + " ".join(f"{s['keep']}:{s['drop']}" for s in suggestions))


def merge(concepts, keep, drop):
    if keep not in concepts or drop not in concepts:
        print(f"  skip {keep}:{drop} — unknown slug")
        return False
    archive = load_json(ARCHIVE_FILE) or {}
    archive[drop] = dict(concepts[drop], merged_into=keep)
    for vid in concepts[drop].get("sources", []):
        merge_into(keep, None, vid, concepts)
    merge_into(keep, concepts[drop]["title"], None, concepts)
    for alias in concepts[drop].get("aliases", []):
        merge_into(keep, alias, None, concepts)
    del concepts[drop]
    save_json(ARCHIVE_FILE, archive)
    log(f"  Merged {drop} -> {keep}")
    return True


if __name__ == "__main__":
    args = sys.argv[1:]
    concepts = load_json(CONCEPTS_FILE)
    if "--merge" in args:
        specs = [a for a in args if ":" in a and not a.startswith("--")]
        done = sum(merge(concepts, *spec.split(":", 1)) for spec in specs)
        if done:
            save_json(CONCEPTS_FILE, concepts)
            rebuild_html(concepts)
            if "--push" in args:
                git_push()
        print(f"{done} merge(s) applied")
    elif "--judge" in args:
        judge_report(concepts)
    else:
        report(concepts)
