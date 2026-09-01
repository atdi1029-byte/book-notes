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


# === STEP 5: Rebuild HTML (multi-page drill-down) ===

# Shared CSS for all pages
PAGE_CSS = '''
.nav-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1rem; margin: 1.5rem 0;
}
.nav-card {
  background: #e8e0d0; border-radius: 10px;
  padding: 1.5rem; text-decoration: none; color: #3a2a1a;
  border: 1px solid #d4c8b0;
  transition: all 0.2s; position: relative;
}
.nav-card:hover {
  border-color: #a08060; background: #ded4c0;
  transform: translateY(-2px);
}
.nav-card h3 { margin: 0 0 0.3rem; color: #d4a574; font-size: 1.3rem; }
.nav-card .card-sub { font-size: 0.85rem; color: #a08060; }
.nav-card .card-count {
  font-size: 0.75rem; color: #a08060;
  margin-top: 0.5rem;
}
.nav-card.done { opacity: 0.25; }
body.hide-done .nav-card.done { display: none; }
.back-link {
  display: inline-block; margin-bottom: 1rem;
  color: #a08060; text-decoration: none; font-size: 0.9rem;
}
.back-link:hover { color: #d4a574; }
.concept-section { position: relative; transition: opacity 0.3s; }
.concept-section.completed { opacity: 0.3; }
body.hide-done .concept-section.completed { display: none; }
.concept-done {
  display: inline-flex; align-items: center; gap: 0.4rem;
  background: none; border: 1px solid #d4c8b0;
  border-radius: 4px; padding: 0.3rem 0.8rem;
  cursor: pointer; font-size: 0.8rem; color: #a08060;
  transition: all 0.2s; margin-top: 1rem;
}
.concept-done:hover { border-color: #4ade80; color: #4ade80; }
.concept-section.completed .concept-done {
  border-color: #4ade80; background: #4ade80; color: #1a1008;
}
.filter-bar {
  display: flex; gap: 1rem; align-items: center;
  margin: 0 0 1.5rem; padding: 0.7rem 1rem;
  background: #e8e0d0; border-radius: 8px;
  border: 1px solid #d4c8b0; font-size: 0.85rem;
}
.filter-btn {
  background: none; border: 1px solid #d4c8b0;
  color: #3a2a1a; padding: 0.3rem 0.8rem;
  border-radius: 4px; cursor: pointer;
  font-size: 0.8rem; transition: all 0.2s;
}
.filter-btn:hover { border-color: #a08060; }
.filter-btn.active {
  background: #a08060; color: #f4efe8; border-color: #a08060;
}
.filter-count { color: #a08060; margin-left: auto; }
.stats-bar {
  display: flex; gap: 1.5rem; flex-wrap: wrap;
  margin: 1rem 0 2rem; padding: 1rem;
  background: #e8e0d0; border: 1px solid #d4c8b0; border-radius: 8px;
  font-size: 0.9rem;
}
.stats-bar .stat {
  display: flex; flex-direction: column; align-items: center;
}
.stats-bar .stat-num {
  font-size: 1.4rem; font-weight: bold; color: #d4a574;
}
'''

# Shared JS for completion tracking (cascading hide)
PAGE_JS = '''
<script>
(function() {
  var KEY = 'fg_done';
  var done = JSON.parse(localStorage.getItem(KEY) || '{}');

  function apply() {
    // Mark completed concepts
    document.querySelectorAll('.concept-section').forEach(function(s) {
      if (done[s.dataset.slug]) s.classList.add('completed');
      else s.classList.remove('completed');
    });
    // Mark completed nav cards (all children done)
    document.querySelectorAll('.nav-card[data-slugs]').forEach(function(card) {
      var slugs = card.dataset.slugs.split(',');
      var allDone = slugs.length > 0 && slugs.every(function(s) { return done[s]; });
      if (allDone) card.classList.add('done');
      else card.classList.remove('done');
    });
    updateCount();
  }

  function updateCount() {
    var concepts = document.querySelectorAll('.concept-section');
    var cards = document.querySelectorAll('.nav-card[data-slugs]');
    var total = concepts.length || cards.length;
    var read = concepts.length
      ? [].filter.call(concepts, function(s) { return done[s.dataset.slug]; }).length
      : [].filter.call(cards, function(c) { return c.classList.contains('done'); }).length;
    var el = document.getElementById('filterCount');
    if (el) el.textContent = read + '/' + total + ' completed';
  }

  window.toggleDone = function(slug) {
    if (done[slug]) delete done[slug];
    else done[slug] = true;
    localStorage.setItem(KEY, JSON.stringify(done));
    apply();
  };

  window.toggleFilter = function() {
    document.body.classList.toggle('hide-done');
    var btn = document.getElementById('filterBtn');
    if (document.body.classList.contains('hide-done')) {
      btn.textContent = 'Show All';
      btn.classList.add('active');
    } else {
      btn.textContent = 'Hide Completed';
      btn.classList.remove('active');
    }
  };

  window.markAllDone = function() {
    document.querySelectorAll('.concept-section').forEach(function(s) {
      done[s.dataset.slug] = true;
    });
    localStorage.setItem(KEY, JSON.stringify(done));
    apply();
  };

  apply();
})();
</script>
'''


def _page_wrap(title, body, css_path="../book.css", back_href=None,
               back_label=None, bm_key=None, extra_js=""):
    """Wrap content in a full HTML page."""
    back = ""
    if back_href:
        back = (f'<a class="back-link" href="{back_href}">'
                f'&larr; {back_label or "Back"}</a>')
    bm = ""
    if bm_key:
        bm = f'<script>var BM_KEY = \'{bm_key}\';</script>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="theme-color" content="#f4efe8">
<title>{title} - Finance Guide</title>
<link rel="stylesheet" href="{css_path}">
<style>{PAGE_CSS}</style>
</head>
<body class="hide-done">
<div class="progress-bar" id="progressBar"></div>
<div class="bookmark-bar" id="bookmarkBar" style="display:none"
 onclick="jumpToBookmark()">
  <span class="bm-label" id="bmLabel"></span>
  <button class="bm-clear"
   onclick="event.stopPropagation();clearBookmark()">Clear</button>
</div>
<div class="bm-toast" id="bmToast"></div>
{back}
{body}
{bm}
<script src="{css_path.replace('book.css','book.js')}"></script>
{extra_js}
</body>
</html>'''


def rebuild_html(concepts):
    """Rebuild multi-page drill-down: index → year → month → week pages."""

    # Group concepts into hierarchy
    hierarchy = {}  # year → month → week_key → [concepts]
    for slug, c in concepts.items():
        added = c.get("added", "2026-01-01")
        dt = datetime.strptime(added, "%Y-%m-%d")
        year = dt.strftime("%Y")
        month_key = dt.strftime("%m")
        month_name = dt.strftime("%B")
        week_start = dt - timedelta(days=dt.weekday())
        week_key = week_start.strftime("%m-%d")
        week_label = f"Week of {week_start.strftime('%B %d')}"

        if year not in hierarchy:
            hierarchy[year] = {}
        if month_key not in hierarchy[year]:
            hierarchy[year][month_key] = {
                "name": month_name, "weeks": {}
            }
        if week_key not in hierarchy[year][month_key]["weeks"]:
            hierarchy[year][month_key]["weeks"][week_key] = {
                "label": week_label, "concepts": []
            }
        hierarchy[year][month_key]["weeks"][week_key][
            "concepts"].append((slug, c))

    total = len(concepts)
    videos = len(load_json(PROCESSED_FILE))

    # === MAIN INDEX (years) ===
    cards = []
    for year in sorted(hierarchy.keys(), reverse=True):
        months = hierarchy[year]
        concept_count = sum(
            len(w["concepts"])
            for m in months.values()
            for w in m["weeks"].values()
        )
        all_slugs = ",".join(
            slug for m in months.values()
            for w in m["weeks"].values()
            for slug, _ in w["concepts"]
        )
        cards.append(
            f'<a class="nav-card" href="{year}/index.html"'
            f' data-slugs="{all_slugs}">'
            f'<h3>{year}</h3>'
            f'<div class="card-sub">'
            f'{len(months)} month{"s" if len(months) != 1 else ""}</div>'
            f'<div class="card-count">'
            f'{concept_count} concepts</div></a>'
        )

    body = f'''
<h1>Finance Guide</h1>
<p class="subtitle">A living book &middot; {total} concepts
 &middot; {videos} videos processed</p>
<div class="filter-bar">
  <button class="filter-btn" id="filterBtn"
   onclick="toggleFilter()" class="active">Show All</button>
  <span class="filter-count" id="filterCount"></span>
</div>
<div class="nav-grid">
{"".join(cards)}
</div>'''

    index_html = _page_wrap("Finance Guide", body,
                             css_path="../book.css",
                             bm_key="finance_guide",
                             extra_js=PAGE_JS)
    HTML_FILE.write_text(index_html)

    # === YEAR PAGES (months) ===
    for year in hierarchy:
        year_dir = BASE_DIR / year
        year_dir.mkdir(exist_ok=True)
        months = hierarchy[year]

        cards = []
        for mk in sorted(months.keys(), reverse=True):
            m = months[mk]
            concept_count = sum(
                len(w["concepts"]) for w in m["weeks"].values()
            )
            all_slugs = ",".join(
                slug for w in m["weeks"].values()
                for slug, _ in w["concepts"]
            )
            cards.append(
                f'<a class="nav-card" href="{mk}.html"'
                f' data-slugs="{all_slugs}">'
                f'<h3>{m["name"]}</h3>'
                f'<div class="card-sub">'
                f'{len(m["weeks"])} week'
                f'{"s" if len(m["weeks"]) != 1 else ""}</div>'
                f'<div class="card-count">'
                f'{concept_count} concepts</div></a>'
            )

        body = f'''
<h1>{year}</h1>
<div class="filter-bar">
  <button class="filter-btn" id="filterBtn"
   onclick="toggleFilter()" class="active">Show All</button>
  <span class="filter-count" id="filterCount"></span>
</div>
<div class="nav-grid">
{"".join(cards)}
</div>'''

        year_html = _page_wrap(year, body,
                                css_path="../../book.css",
                                back_href="../index.html",
                                back_label="Finance Guide",
                                bm_key=f"fg_{year}",
                                extra_js=PAGE_JS)
        (year_dir / "index.html").write_text(year_html)

        # === MONTH PAGES (weeks) ===
        for mk in months:
            m = months[mk]
            cards = []
            for wk in sorted(m["weeks"].keys(), reverse=True):
                w = m["weeks"][wk]
                all_slugs = ",".join(
                    slug for slug, _ in w["concepts"]
                )
                cards.append(
                    f'<a class="nav-card" href="{mk}-{wk}.html"'
                    f' data-slugs="{all_slugs}">'
                    f'<h3>{w["label"]}</h3>'
                    f'<div class="card-count">'
                    f'{len(w["concepts"])} concepts</div></a>'
                )

            body = f'''
<h1>{m["name"]} {year}</h1>
<div class="filter-bar">
  <button class="filter-btn" id="filterBtn"
   onclick="toggleFilter()" class="active">Show All</button>
  <span class="filter-count" id="filterCount"></span>
</div>
<div class="nav-grid">
{"".join(cards)}
</div>'''

            month_html = _page_wrap(
                f'{m["name"]} {year}', body,
                css_path="../../book.css",
                back_href="index.html",
                back_label=year,
                bm_key=f"fg_{year}_{mk}",
                extra_js=PAGE_JS)
            (year_dir / f"{mk}.html").write_text(month_html)

            # === WEEK PAGES (concepts) ===
            for wk in m["weeks"]:
                w = m["weeks"][wk]
                sections = []
                for slug, c in w["concepts"]:
                    ch = c.get("chapter_html", "")
                    if not ch:
                        ch = (f'<h4 id="{slug}">{c["title"]}</h4>'
                              f'\n<p>{c.get("summary", "")}</p>')
                    sections.append(
                        f'<section class="concept-section"'
                        f' data-slug="{slug}">'
                        f'{ch}'
                        f'<button class="concept-done"'
                        f' onclick="toggleDone(\'{slug}\')"'
                        f' title="Mark as understood">'
                        f'&#x2713; Mark Complete</button>'
                        f'</section>'
                    )

                body = f'''
<h1>{w["label"]}</h1>
<p class="subtitle">{m["name"]} {year}
 &middot; {len(w["concepts"])} concepts</p>
<div class="filter-bar">
  <button class="filter-btn" id="filterBtn"
   onclick="toggleFilter()" class="active">Show All</button>
  <button class="filter-btn"
   onclick="markAllDone()">Mark All Done</button>
  <span class="filter-count" id="filterCount"></span>
</div>
{"".join(sections)}'''

                week_html = _page_wrap(
                    w["label"], body,
                    css_path="../../book.css",
                    back_href=f"{mk}.html",
                    back_label=f"{m['name']} {year}",
                    bm_key=f"fg_{year}_{mk}_{wk}",
                    extra_js=PAGE_JS)
                (year_dir / f"{mk}-{wk}.html").write_text(
                    week_html)

    log(f"  HTML rebuilt: {total} concepts, "
        f"{len(hierarchy)} years, multi-page")


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
