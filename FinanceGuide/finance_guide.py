#!/usr/bin/env python3
"""
Finance Guide Bot — pulls YouTube transcripts, extracts finance concepts,
builds a living book on the Books shelf.

Runs like rhythm_bot: nohup python3 finance_guide.py &
Checks channels every 6 hours for new videos.
"""

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

# Ensure tools are in PATH (nohup doesn't load shell profile)
for p in ["/usr/local/bin", "/opt/homebrew/bin", os.path.expanduser("~/.local/bin")]:
    if p not in os.environ.get("PATH", ""):
        os.environ["PATH"] = p + ":" + os.environ.get("PATH", "")

# === CONFIG ===
BASE_DIR = Path(__file__).parent
TRANSCRIPTS_DIR = BASE_DIR / "transcripts"
CHANNELS_FILE = BASE_DIR / "channels.json"
CONCEPTS_FILE = BASE_DIR / "concepts.json"
PROCESSED_FILE = BASE_DIR / "processed_videos.json"
HTML_FILE = BASE_DIR / "index.html"
LOG_FILE = BASE_DIR / "bot.log"

CHECK_INTERVAL = 6 * 3600  # 6 hours between checks
MAX_VIDEOS_PER_RUN = 1     # process 1 video per check cycle
BOOKS_DIR = BASE_DIR.parent

TRANSCRIPTS_DIR.mkdir(exist_ok=True)


def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {} if path.suffix == ".json" else []


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


# === STEP 1: Pull new video IDs from channels ===
def get_channel_videos(channel_url, limit=30):
    """Pull recent video IDs and titles from a YouTube channel."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "--print", "id", "--print", "title",
             "--playlist-end", str(limit), channel_url],
            capture_output=True, text=True, timeout=60
        )
        lines = result.stdout.strip().split("\n")
        videos = []
        for i in range(0, len(lines) - 1, 2):
            vid_id = lines[i].strip()
            title = lines[i + 1].strip()
            if vid_id and title:
                videos.append({"id": vid_id, "title": title})
        return videos
    except Exception as e:
        log(f"  ERROR pulling channel: {e}")
        return []


def find_new_videos():
    """Check all channels, return videos not yet processed."""
    channels = load_json(CHANNELS_FILE)
    if isinstance(channels, dict):
        channels = []
    processed = load_json(PROCESSED_FILE)

    new_videos = []
    for channel in channels:
        log(f"  Checking: {channel['name']}")
        videos = get_channel_videos(channel["url"])
        for v in videos:
            if v["id"] not in processed:
                v["channel"] = channel["name"]
                new_videos.append(v)
        log(f"  Found {len(videos)} total, "
            f"{sum(1 for v in videos if v['id'] not in processed)} new")

    return new_videos[:MAX_VIDEOS_PER_RUN]


# === STEP 2: Download transcript ===
def download_transcript(video_id):
    """Download auto-captions and clean to plain text."""
    srt_path = TRANSCRIPTS_DIR / f"{video_id}.en.srt"
    txt_path = TRANSCRIPTS_DIR / f"{video_id}.txt"

    if txt_path.exists():
        return txt_path.read_text()

    try:
        subprocess.run(
            ["yt-dlp", "--write-auto-subs", "--sub-langs", "en",
             "--skip-download", "--convert-subs", "srt",
             "-o", str(TRANSCRIPTS_DIR / f"{video_id}"),
             f"https://www.youtube.com/watch?v={video_id}"],
            capture_output=True, text=True, timeout=60
        )
    except Exception as e:
        log(f"  ERROR downloading subs for {video_id}: {e}")
        return None

    # Find the SRT file (yt-dlp adds .en.srt)
    if not srt_path.exists():
        # Try alternate naming
        for f in TRANSCRIPTS_DIR.glob(f"{video_id}*.srt"):
            srt_path = f
            break

    if not srt_path.exists():
        log(f"  No subtitles found for {video_id}")
        return None

    # Clean SRT to plain text
    content = srt_path.read_text()
    lines = []
    for line in content.split("\n"):
        line = line.strip()
        if not line:
            continue
        if re.match(r"^\d+$", line):
            continue
        if re.match(r"\d{2}:\d{2}:\d{2}", line):
            continue
        if line not in lines[-1:]:  # dedup consecutive
            lines.append(line)

    text = " ".join(lines)
    text = re.sub(r"\s+", " ", text).strip()

    txt_path.write_text(text)
    srt_path.unlink()  # clean up SRT
    return text


# === STEP 3: Extract concepts via Claude CLI ===
def extract_concepts(video_id, title, transcript, existing_concepts):
    """Call Claude to read transcript and extract finance concepts."""

    concept_list = "\n".join(
        f"- {c['title']} ({c['category']})"
        for c in existing_concepts.values()
    )

    prompt = f"""You are building a living finance education guide. Read this YouTube video transcript
and extract every distinct finance/economics/market concept mentioned.

VIDEO: "{title}"
TRANSCRIPT:
{transcript}

ALREADY COVERED CONCEPTS (do NOT re-extract these — skip them):
{concept_list if concept_list else "(none yet)"}

For each NEW concept not in the list above, output a JSON array of objects:
[
  {{
    "slug": "yield_curve_inversion",
    "title": "Yield Curve Inversion",
    "category": "macro|technicals|credit_bonds|derivatives|market_structure|sentiment_flows|fiscal_policy|monetary_policy|commodities|crypto|real_estate|labor_economics",
    "summary": "One sentence explaining what this concept is",
    "context": "How the video discussed it — what claim was made, what evidence given"
  }}
]

Rules:
- Extract CONCEPTS, not news events. "Fed raised rates" is news; "Federal Funds Rate" is a concept.
- Be specific: "Credit Default Swaps" not just "derivatives"
- If the video mentions a concept already covered, SKIP IT entirely
- If no new concepts, return an empty array: []
- Output ONLY the JSON array, nothing else
"""

    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", "sonnet"],
            capture_output=True, text=True, timeout=120
        )
        output = result.stdout.strip()

        # Extract JSON from output
        match = re.search(r"\[.*\]", output, re.DOTALL)
        if match:
            return json.loads(match.group())
        return []
    except Exception as e:
        log(f"  ERROR extracting concepts: {e}")
        return []


# === STEP 4: Write chapter for a concept via Claude CLI ===
def write_chapter(concept, video_title, transcript_excerpt):
    """Call Claude to write a bookai-depth chapter for one concept."""

    prompt = f"""You are writing a chapter for a personal finance education guide.
Write a thorough, clear explanation of this concept that would help someone
truly understand it — not a summary, but real teaching.

CONCEPT: {concept['title']}
CATEGORY: {concept['category']}
CONTEXT FROM VIDEO: {concept['context']}
VIDEO: "{video_title}"

RELEVANT TRANSCRIPT EXCERPT:
{transcript_excerpt[:3000]}

Write the chapter in HTML format (just the content, no <html>/<body> tags).
Structure:
- <h4 id="{concept['slug']}">{concept['title']}</h4>
- 8+ paragraphs minimum, each 100-120 words, explaining:
  1. What is this concept? Define it clearly for someone new to finance.
  2. Why does it matter? What does it affect in the real economy/markets?
  3. How does it work mechanically? The actual mechanism step by step.
  4. A real-world example — use specific numbers, dates, or events from the video.
  5. How do traders/investors use it? Practical application and signals.
  6. What are the gotchas/nuances? Common misconceptions.
  7. What happens when it breaks or fails? Edge cases and risks.
  8. Connection to other concepts (if relevant).
  The goal is COMPLETE understanding — someone reading this should be able
  to discuss this concept confidently in a conversation about markets.
- Use <strong> for key terms (first mention)
- Use <blockquote> for any memorable quotes from the video
- Write in direct, clear prose — not academic, not dumbed down
- Output ONLY the HTML content, nothing else
"""

    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", "sonnet"],
            capture_output=True, text=True, timeout=180
        )
        return result.stdout.strip()
    except Exception as e:
        log(f"  ERROR writing chapter for {concept['title']}: {e}")
        return None


# === STEP 5: Rebuild HTML ===
def rebuild_html(concepts):
    """Rebuild index.html with all concepts organized by year/month/week."""

    # Group concepts by week
    by_week = {}
    for slug, c in sorted(concepts.items(),
                           key=lambda x: x[1].get("added", ""),
                           reverse=True):
        added = c.get("added", "2026-01-01")
        dt = datetime.strptime(added, "%Y-%m-%d")
        year = dt.strftime("%Y")
        month = dt.strftime("%B %Y")
        # Week start (Monday)
        week_start = dt - timedelta(days=dt.weekday())
        week_key = week_start.strftime("%Y-%m-%d")
        week_label = f"Week of {week_start.strftime('%B %d')}"

        if year not in by_week:
            by_week[year] = {}
        if month not in by_week[year]:
            by_week[year][month] = {}
        if week_key not in by_week[year][month]:
            by_week[year][month][week_key] = {
                "label": week_label, "concepts": []
            }
        by_week[year][month][week_key]["concepts"].append((slug, c))

    # Group concepts by category for index
    by_category = {}
    for slug, c in concepts.items():
        cat = c.get("category", "uncategorized")
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append((slug, c))

    category_labels = {
        "macro": "Macro Economics",
        "technicals": "Technical Analysis",
        "credit_bonds": "Credit & Bonds",
        "derivatives": "Derivatives",
        "market_structure": "Market Structure",
        "sentiment_flows": "Sentiment & Flows",
        "fiscal_policy": "Fiscal Policy",
        "monetary_policy": "Monetary Policy",
        "commodities": "Commodities",
        "crypto": "Crypto",
        "real_estate": "Real Estate",
        "labor_economics": "Labor Economics",
    }

    # Build TOC
    toc_items = []
    for year in sorted(by_week.keys(), reverse=True):
        for month in by_week[year]:
            for week_key in sorted(by_week[year][month].keys(),
                                    reverse=True):
                week = by_week[year][month][week_key]
                for slug, c in week["concepts"]:
                    toc_items.append(
                        f'  <li><a href="#{slug}">'
                        f'{c["title"]}</a>'
                        f' <span class="toc-cat">[{c.get("category", "")}]'
                        f'</span></li>'
                    )

    # Build chapter content
    chapters_html = []
    for year in sorted(by_week.keys(), reverse=True):
        chapters_html.append(f'<h2 id="y{year}">{year}</h2>')
        for month in by_week[year]:
            chapters_html.append(f'<h3 id="m{month.replace(" ", "")}">'
                                  f'{month}</h3>')
            for week_key in sorted(by_week[year][month].keys(),
                                    reverse=True):
                week = by_week[year][month][week_key]
                chapters_html.append(
                    f'<div class="week-header">{week["label"]}</div>'
                )
                for slug, c in week["concepts"]:
                    chapter_html = c.get("chapter_html", "")
                    if chapter_html:
                        chapters_html.append(chapter_html)
                    else:
                        chapters_html.append(
                            f'<h4 id="{slug}">{c["title"]}</h4>\n'
                            f'<p>{c.get("summary", "")}</p>'
                        )

    # Build category index
    cat_index = ['<h2 id="categories">Browse by Category</h2>',
                 '<div class="cat-grid">']
    for cat_key, cat_label in sorted(category_labels.items()):
        items = by_category.get(cat_key, [])
        if items:
            cat_index.append(f'<div class="cat-card">')
            cat_index.append(f'<h4>{cat_label}</h4>')
            cat_index.append(f'<span class="cat-count">'
                              f'{len(items)} concepts</span>')
            cat_index.append('<ul>')
            for slug, c in sorted(items, key=lambda x: x[1]["title"]):
                cat_index.append(
                    f'<li><a href="#{slug}">{c["title"]}</a></li>'
                )
            cat_index.append('</ul></div>')
    cat_index.append('</div>')

    # Count stats
    total = len(concepts)
    newest = ""
    if concepts:
        latest = max(concepts.values(),
                      key=lambda x: x.get("added", ""))
        newest = latest.get("added", "")

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport"
 content="width=device-width, initial-scale=1.0">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style"
 content="black-translucent">
<meta name="theme-color" content="#f4efe8">
<title>Finance Guide - Living Book</title>
<link rel="stylesheet" href="../book.css?v=8">
<style>
.stats-bar {{
  display: flex; gap: 1.5rem; flex-wrap: wrap;
  margin: 1rem 0 2rem; padding: 1rem;
  background: rgba(0,0,0,0.15); border-radius: 8px;
  font-size: 0.9rem;
}}
.stats-bar .stat {{
  display: flex; flex-direction: column;
  align-items: center;
}}
.stats-bar .stat-num {{
  font-size: 1.4rem; font-weight: bold;
  color: #d4a574;
}}
.week-header {{
  font-size: 0.85rem; text-transform: uppercase;
  letter-spacing: 0.1em; color: #a08060;
  margin: 2rem 0 0.5rem;
  padding-bottom: 0.3rem;
  border-bottom: 1px solid rgba(160,128,96,0.3);
}}
.toc-cat {{
  font-size: 0.75rem; color: #a08060;
  margin-left: 0.3rem;
}}
.cat-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem; margin: 1rem 0 2rem;
}}
.cat-card {{
  background: rgba(0,0,0,0.15);
  border-radius: 8px; padding: 1rem;
}}
.cat-card h4 {{
  margin: 0 0 0.3rem; color: #d4a574;
}}
.cat-count {{
  font-size: 0.8rem; color: #a08060;
}}
.cat-card ul {{
  list-style: none; padding: 0;
  margin: 0.5rem 0 0;
}}
.cat-card li {{
  font-size: 0.85rem; padding: 0.15rem 0;
}}
.cat-card a {{
  color: inherit; text-decoration: none;
  border-bottom: 1px dotted rgba(160,128,96,0.4);
}}
.cat-card a:hover {{
  color: #d4a574;
}}
.new-badge {{
  display: inline-block; font-size: 0.65rem;
  background: #d4a574; color: #1a1008;
  padding: 0.1rem 0.4rem; border-radius: 3px;
  margin-left: 0.4rem; vertical-align: middle;
  font-weight: bold;
}}
</style>
</head>
<body>

<div class="progress-bar" id="progressBar"></div>
<div class="bookmark-bar" id="bookmarkBar"
 style="display:none" onclick="jumpToBookmark()">
  <span class="bm-label" id="bmLabel"></span>
  <button class="bm-clear"
   onclick="event.stopPropagation();clearBookmark()">
    Clear</button>
</div>
<div class="bm-toast" id="bmToast"></div>

<h1>Finance Guide</h1>
<p class="subtitle">A living book &middot;
 {total} concepts &middot;
 Built from YouTube &middot;
 Last updated {newest}</p>

<div class="stats-bar">
  <div class="stat">
    <span class="stat-num">{total}</span>
    Concepts
  </div>
  <div class="stat">
    <span class="stat-num">
      {len(by_category)}</span>
    Categories
  </div>
  <div class="stat">
    <span class="stat-num">
      {len(load_json(PROCESSED_FILE))}</span>
    Videos Processed
  </div>
</div>

<nav class="toc">
<h2>Contents</h2>
<ol>
  <li><a href="#categories">Browse by Category</a></li>
{chr(10).join(toc_items)}
</ol>
</nav>

{chr(10).join(cat_index)}

{chr(10).join(chapters_html)}

<script>var BM_KEY = 'finance_guide';</script>
<script src="../book.js"></script>
</body>
</html>'''

    HTML_FILE.write_text(html)
    log(f"  HTML rebuilt: {total} concepts, {len(html)} chars")


# === STEP 6: Git push ===
def git_push():
    """Push changes to GitHub."""
    git_cmd = ('GIT_SSH_COMMAND="ssh -p 443 -o HostName=ssh.github.com" '
               f'git -C {BOOKS_DIR} ')
    try:
        subprocess.run(
            f'{git_cmd} add FinanceGuide/',
            shell=True, capture_output=True, timeout=30
        )
        subprocess.run(
            f'{git_cmd} commit -m "finance guide: auto-update '
            f'{datetime.now().strftime("%Y-%m-%d %H:%M")}"',
            shell=True, capture_output=True, timeout=30
        )
        result = subprocess.run(
            f'{git_cmd} push',
            shell=True, capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            log("  Pushed to GitHub")
        else:
            log(f"  Push failed: {result.stderr[:200]}")
    except Exception as e:
        log(f"  Git error: {e}")


# === MAIN LOOP ===
def run_once():
    """Single check-and-process cycle."""
    log("=== Finance Guide check ===")

    # Find new videos
    new_videos = find_new_videos()
    if not new_videos:
        log("  No new videos found")
        return

    log(f"  Processing {len(new_videos)} new videos")

    concepts = load_json(CONCEPTS_FILE)
    processed = load_json(PROCESSED_FILE)
    new_concept_count = 0

    for video in new_videos:
        vid_id = video["id"]
        title = video["title"]
        channel = video.get("channel", "unknown")
        log(f"  Video: {title}")

        # Download transcript
        transcript = download_transcript(vid_id)
        if not transcript:
            log(f"    Skipped (no transcript)")
            continue

        log(f"    Transcript: {len(transcript)} chars")

        # Extract concepts
        new_concepts = extract_concepts(
            vid_id, title, transcript, concepts
        )
        log(f"    Extracted: {len(new_concepts)} new concepts")

        # Write chapters for each new concept
        for concept in new_concepts:
            slug = concept["slug"]
            if slug in concepts:
                log(f"    Skip (exists): {concept['title']}")
                continue

            log(f"    Writing: {concept['title']}")
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
                new_concept_count += 1
                # Save after each concept (crash safety)
                save_json(CONCEPTS_FILE, concepts)

        # Mark video as processed
        processed[vid_id] = {
            "title": title,
            "channel": channel,
            "processed": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "concepts_extracted": len(new_concepts),
        }
        save_json(PROCESSED_FILE, processed)

    if new_concept_count > 0:
        log(f"  Total new concepts: {new_concept_count}")
        rebuild_html(concepts)
        git_push()
    else:
        log("  No new concepts to add")

    log("=== Done ===\n")


def main():
    # Lock file — prevent duplicate instances
    lock_file = BASE_DIR / ".bot.lock"
    if lock_file.exists():
        try:
            pid = int(lock_file.read_text().strip())
            # Check if process is still running
            os.kill(pid, 0)
            print(f"Bot already running (PID {pid}). Exiting.")
            sys.exit(1)
        except (ProcessLookupError, ValueError):
            pass  # stale lock, take over

    lock_file.write_text(str(os.getpid()))

    log("Finance Guide Bot starting")
    log(f"Check interval: {CHECK_INTERVAL // 3600}h")
    log(f"Channels: {CHANNELS_FILE}")

    try:
        while True:
            try:
                run_once()
            except Exception as e:
                log(f"ERROR in run_once: {e}")
            log(f"Sleeping {CHECK_INTERVAL // 3600}h until next check...")
            time.sleep(CHECK_INTERVAL)
    finally:
        lock_file.unlink(missing_ok=True)


if __name__ == "__main__":
    if "--once" in sys.argv:
        run_once()
    else:
        main()
