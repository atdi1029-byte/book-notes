#!/usr/bin/env python3
"""One-time repair of concepts.json + rebuild.

Default (no flags) makes NO Claude calls:
  - strips ```html fences / preamble from existing chapters (38 affected)
  - rebuilds all HTML pages with the fixed generator

Opt-in flags:
  --regen-broken        rewrite chapters whose stored HTML is unusable
                        (the two "API Error" entries) using their source
                        transcript.  Makes 1 Sonnet call per broken chapter.
  --retry-video <id>    un-mark a video so the bot reprocesses it next cycle
                        (e.g. hM508gcGsLk, which got 0 concepts on an error)
  --push                git push after rebuilding

  python3 repair.py
  python3 repair.py --regen-broken --push
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from finance_guide import (  # noqa: E402
    CONCEPTS_FILE, PROCESSED_FILE, TRANSCRIPTS_DIR, load_json, save_json,
    log, clean_chapter_html, write_chapter, rebuild_html, git_push,
)


def strip_fences(concepts):
    fixed, broken = 0, []
    for slug, c in concepts.items():
        raw = c.get("chapter_html", "")
        cleaned = clean_chapter_html(raw, slug)
        if cleaned is None:
            broken.append(slug)
        elif cleaned != raw:
            c["chapter_html"] = cleaned
            fixed += 1
    return fixed, broken


def regen(concepts, slugs):
    processed = load_json(PROCESSED_FILE)
    done = 0
    for slug in slugs:
        c = concepts[slug]
        vid = (c.get("sources") or [None])[0]
        txt = TRANSCRIPTS_DIR / f"{vid}.txt" if vid else None
        if not txt or not txt.exists():
            log(f"  {slug}: no cached transcript for {vid}, skipping")
            continue
        video_title = processed.get(vid, {}).get("title", vid)
        cand = dict(c, slug=slug, context=c.get("context") or c["summary"])
        log(f"  Regenerating: {c['title']}")
        html = write_chapter(cand, video_title, txt.read_text())
        if html:
            c["chapter_html"] = html
            save_json(CONCEPTS_FILE, concepts)
            done += 1
    return done


if __name__ == "__main__":
    args = sys.argv[1:]
    concepts = load_json(CONCEPTS_FILE)

    fixed, broken = strip_fences(concepts)
    log(f"Fences/preamble stripped from {fixed} chapters")
    if broken:
        log(f"Unusable chapters (still in book): {', '.join(broken)}")
    save_json(CONCEPTS_FILE, concepts)

    if "--regen-broken" in args and broken:
        n = regen(concepts, broken)
        log(f"Regenerated {n}/{len(broken)}")

    if "--retry-video" in args:
        vid = args[args.index("--retry-video") + 1]
        processed = load_json(PROCESSED_FILE)
        if vid in processed:
            processed[vid]["retry"] = True
            save_json(PROCESSED_FILE, processed)
            log(f"Marked {vid} for retry next cycle")
        else:
            log(f"{vid} not in processed list")

    rebuild_html(concepts)
    if "--push" in args:
        git_push()
    log("Repair done")
