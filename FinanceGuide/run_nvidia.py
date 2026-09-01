#!/usr/bin/env python3
"""One-shot: finish Nvidia 10-Q video, then clear backlog marks so bot picks up new videos."""
import json
import sys
import os

# Ensure tools are in PATH
for p in ["/usr/local/bin", "/opt/homebrew/bin", os.path.expanduser("~/.local/bin")]:
    if p not in os.environ.get("PATH", ""):
        os.environ["PATH"] = p + ":" + os.environ.get("PATH", "")

sys.path.insert(0, os.path.dirname(__file__))
from finance_guide import *

vid_id = "k2_HNo_L_rw"
title = "I Forensically Audited Nvidia\u2019s 10-Q. The $420B Gamble Hidden Inside."

log("=== Resuming Nvidia 10-Q video ===")

# Download transcript (cached)
transcript = download_transcript(vid_id)
if not transcript:
    log("No transcript found")
    sys.exit(1)

log(f"Transcript: {len(transcript)} chars")

# Extract concepts
concepts = load_json(CONCEPTS_FILE)
new_concepts = extract_concepts(vid_id, title, transcript, concepts)
log(f"Extracted: {len(new_concepts)} new concepts")

# Write chapters for ones not already saved
written = 0
for concept in new_concepts:
    slug = concept["slug"]
    if slug in concepts:
        log(f"  Skip (exists): {concept['title']}")
        continue
    log(f"  Writing: {concept['title']}")
    chapter_html = write_chapter(concept, title, transcript)
    if chapter_html:
        concepts[slug] = {
            "title": concept["title"],
            "category": concept["category"],
            "summary": concept["summary"],
            "sources": [vid_id],
            "added": datetime.now().strftime("%Y-%m-%d"),
            "chapter_html": chapter_html,
        }
        written += 1
        save_json(CONCEPTS_FILE, concepts)

log(f"Wrote {written} new chapters")

# Mark this video processed
processed = load_json(PROCESSED_FILE)
processed[vid_id] = {
    "title": title,
    "channel": "BigBankTheory",
    "processed": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "concepts_extracted": len(new_concepts),
}

# Clear ALL backlog_marked entries so the bot processes them fresh
cleared = 0
for k in list(processed.keys()):
    if processed[k].get("skipped") == "backlog_marked":
        del processed[k]
        cleared += 1

save_json(PROCESSED_FILE, processed)
log(f"Cleared {cleared} backlog-marked videos from processed list")

# Rebuild HTML and push
rebuild_html(concepts)
git_push()
log("=== Done ===")
