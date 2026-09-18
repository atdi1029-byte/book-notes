#!/usr/bin/env python3
"""
One-off repair for concepts.json — run it once from the FinanceGuide folder.

  1. Flags the concepts that predate the star/plain/deep system (143 as of
     Sept 18) so the site's "star" filter stops missing Federal Funds Rate,
     CPI, Forward Guidance and friends.  Asks Claude in batches of 40 using
     the same rubric the extractor uses; nothing else on the concept changes.
  2. Rewrites chapters that are stubs (under 300 words — two of them) using
     the bot's own chapter writer and the source video's transcript.
  3. Rebuilds the site and pushes.

  python3 backfill_flags.py            # do it
  python3 backfill_flags.py --dry-run  # show what would change, write nothing
  python3 backfill_flags.py --no-push  # fix and rebuild, but don't git push

A backup of concepts.json is written next to it before anything is changed.
Safe to re-run: already-flagged concepts and full-length chapters are skipped.
"""

import json
import re
import shutil
import sys
from datetime import datetime

import finance_guide as fg

DRY = "--dry-run" in sys.argv
PUSH = "--no-push" not in sys.argv
BATCH = 40
STUB_WORDS = 300


def flag_batch(items):
    """items: list of (slug, concept). Returns {slug: flag} or None on failure."""
    listing = "\n".join(
        f"- {slug}: {c['title']} — {c.get('summary', '')}  ({fg.concept_category(c)})"
        for slug, c in items
    )
    prompt = f"""You maintain a finance education guide. Assign each concept below an importance flag.

FLAG:
- "star": must-know — you cannot follow a markets conversation without it
  (Federal Funds Rate, Term Premium, Yield Curve, CPI).
- "plain": standard working knowledge for someone actively trading or investing.
- "deep": deep cut — sector plumbing, single-country or single-industry mechanics,
  a curiosity (fertilizer pricing, farm loan-loss provisions, COMEX inventories).

Be selective with "star": roughly one in five at most. Reserve it for the ideas a
newcomer must learn first.

CONCEPTS:
{listing}

Output ONLY a JSON object mapping every slug above to its flag, e.g.
{{"federal_funds_rate": "star", "pawn_receivables_economic_indicator": "deep"}}
"""
    out = fg.run_claude(prompt, timeout=180)
    if out is None:
        return None
    m = re.search(r"\{.*\}", out, re.DOTALL)
    if not m:
        fg.log(f"  ERROR flag output not JSON: {out[:150]}")
        return None
    try:
        data = json.loads(m.group())
    except json.JSONDecodeError:
        fg.log(f"  ERROR flag bad JSON: {out[:150]}")
        return None
    return {s: str(f).lower() for s, f in data.items()}


def chapter_words(c):
    return len(re.sub(r"<[^>]+>", " ", c.get("chapter_html", "")).split())


def main():
    concepts = fg.load_json(fg.CONCEPTS_FILE)
    processed = fg.load_json(fg.PROCESSED_FILE)
    if not concepts:
        print(f"No concepts found at {fg.CONCEPTS_FILE}")
        sys.exit(1)

    unflagged = [(s, c) for s, c in concepts.items() if c.get("flag") not in fg.FLAGS]
    stubs = [(s, c) for s, c in concepts.items() if chapter_words(c) < STUB_WORDS]
    print(f"{len(concepts)} concepts: {len(unflagged)} unflagged, {len(stubs)} stub chapters")
    if DRY:
        for s, c in stubs:
            print(f"  stub: {c['title']} ({chapter_words(c)} words, sources {c.get('sources')})")
        print("Dry run — nothing written.")
        return
    if not unflagged and not stubs:
        print("Nothing to do.")
        return

    backup = fg.CONCEPTS_FILE.with_name(
        f"concepts.backup-{datetime.now().strftime('%Y%m%d-%H%M')}.json")
    shutil.copy(fg.CONCEPTS_FILE, backup)
    print(f"Backup: {backup.name}")

    # ---- 1. flags ----
    flagged = 0
    for i in range(0, len(unflagged), BATCH):
        batch = unflagged[i:i + BATCH]
        print(f"Flagging {i + 1}-{i + len(batch)} of {len(unflagged)}...")
        result = flag_batch(batch)
        if result is None:
            print("  batch failed — re-run the script later to finish")
            continue
        for slug, _ in batch:
            f = result.get(slug)
            if f in fg.FLAGS:
                concepts[slug]["flag"] = f
                flagged += 1
            else:
                concepts[slug]["flag"] = "plain"
                print(f"  no verdict for {slug}; set to plain")
                flagged += 1
        fg.save_json(fg.CONCEPTS_FILE, concepts)   # save after each batch
    if unflagged:
        counts = {f: sum(1 for c in concepts.values() if c.get("flag") == f) for f in fg.FLAGS}
        print(f"Flagged {flagged}. Book is now {counts}")

    # ---- 2. stub chapters ----
    rewritten = 0
    for slug, c in stubs:
        print(f"Rewriting stub: {c['title']}")
        vid = next((v for v in c.get("sources", []) if v in processed), None)
        if not vid:
            print("  no source video on record — skipping")
            continue
        try:
            transcript = fg.download_transcript(vid)
        except fg.NetworkError as e:
            print(f"  network error fetching transcript: {e} — skipping")
            continue
        if not transcript:
            print(f"  no transcript for {vid} — skipping")
            continue
        c.setdefault("slug", slug)
        html = fg.write_chapter(dict(c, slug=slug), processed[vid].get("title", ""), transcript)
        if html:
            concepts[slug]["chapter_html"] = html
            fg.save_json(fg.CONCEPTS_FILE, concepts)
            rewritten += 1
            print(f"  done ({chapter_words(concepts[slug])} words)")
        else:
            print("  writer returned nothing usable — left as is")

    # ---- 3. rebuild + push ----
    if flagged or rewritten:
        print("Rebuilding site...")
        fg.rebuild_html(concepts)
        if PUSH:
            fg.git_push()
        else:
            print("Skipped push (--no-push)")
    print(f"Done: {flagged} flagged, {rewritten} chapters rewritten.")


if __name__ == "__main__":
    main()
