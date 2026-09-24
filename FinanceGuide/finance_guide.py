#!/usr/bin/env python3
"""
Finance Guide Bot — pulls YouTube transcripts, extracts finance concepts,
builds a living book on the Books shelf.

Preferred: run under launchd so it starts at login and is restarted if it
dies (see install_launchd.sh).  Manual: nohup python3 finance_guide.py &
Checks channels every 6 hours, and whenever the Mac wakes from sleep
(after waiting for Wi-Fi to come back).  A failed check is retried in
10 minutes instead of 6 hours.

  python3 finance_guide.py --status   # is it alive? what did it last do?
  python3 finance_guide.py --once     # one check-and-process cycle, then exit
"""

import fcntl
import json
import os
import re
import signal
import socket
import subprocess
import sys
import time
import traceback
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
WAKE_GAP = 5 * 60          # a 60s nap that takes >5 min wall-clock = machine slept -> check now
RETRY_INTERVAL = 10 * 60   # after a check that failed (network, yt-dlp, claude), try again
                           # this soon; doubles on each further failure, capped at CHECK_INTERVAL
NETWORK_WAIT = 3 * 60      # after login/wake, wait up to this long for Wi-Fi before checking
CAPTION_RETRY = 60 * 60    # a new video is up but has no captions yet: check again this soon
MAX_VIDEOS_PER_RUN = 0     # 0 = no limit, process all new videos
BOOKS_DIR = BASE_DIR.parent

TRANSCRIPTS_DIR.mkdir(exist_ok=True)


# === OUTLINE: borrowed from the Master Investment Reading List ===
# The guide files every concept into one of these categories and lays the
# pages out tier -> category -> concept.  Snapshot of the list as of
# Sept 2026; update by hand if the list's outline changes.  The list itself
# is never modified by this bot.
OUTLINE = [
    {"tier": 1, "name": "Tier 1 \u2014 Foundations",
     "desc": "Build the base. Learn how money, economies, and markets actually work.",
     "cats": [
        {"slug": "personal-finance-basics", "name": "Personal Finance Basics",
         "stars": ["I Will Teach You To Be Rich — Ramit Sethi", "The Simple Path To Wealth — JL Collins", "The Total Money Makeover — Dave Ramsey", "Your Money or Your Life — Vicki Robin", "The Millionaire Next Door — Thomas Stanley", "The Millionaire Mind — Thomas Stanley"]},
        {"slug": "economics-fundamentals", "name": "Economics Fundamentals",
         "stars": ["Basic Economics, Vol 1 & 2 — Thomas Sowell", "Economics in One Lesson — Henry Hazlitt", "The 6 Lessons — Ludwig von Mises", "Talking to My Daughter About the Economy — Yanis Varoufakis", "The Wealth of Nations — Adam Smith", "Naked Economics — Charles Wheelan"]},
        {"slug": "investing-fundamentals", "name": "Investing Fundamentals",
         "stars": ["Winning the Loser's Game — Charles D. Ellis", "A Random Walk Down Wall Street — Burton Malkiel", "The Four Pillars of Investing — William Bernstein", "The Little Book of Common Sense Investing — John Bogle", "Common Sense on Mutual Funds — John Bogle", "Just Keep Buying — Nick Maggiulli"]},
        {"slug": "free-markets-political-economy", "name": "Free Markets & Political Economy",
         "stars": ["Free To Choose — Milton Friedman", "Capitalism And Freedom — Milton Friedman", "The Road To Serfdom — F.A. Hayek", "Capital in the Twenty-First Century — Thomas Piketty"]},
     ]},
    {"tier": 2, "name": "Tier 2 \u2014 Core Knowledge",
     "desc": "Understand how money is created, why markets crash, and why humans are terrible with money.",
     "cats": [
        {"slug": "monetary-policy-central-banking", "name": "Monetary Policy & Central Banking",
         "stars": ["The Price of Time: The Real Story of Interest — Edward Chancellor", "A History of Interest Rates — Sidney Homer & Richard Sylla", "The Creature From Jekyll Island — G. Edward Griffin", "When Money Dies — Adam Fergusson", "A Monetary History of the United States, 1867-1960 — Friedman & Schwartz"]},
        {"slug": "economic-history-financial-crises", "name": "Economic History & Financial Crises",
         "stars": ["Big Debt Crises — Ray Dalio", "Against the Gods: The Remarkable Story of Risk — Peter Bernstein", "Manias, Panics, and Crashes — Charles Kindleberger", "This Time Is Different: Eight Centuries of Financial Folly — Reinhart & Rogoff", "The Lessons of History — Will & Ariel Durant", "Extraordinary Popular Delusions And The Madness Of Crowds — Charles Mackay", "Debt: The First 5,000 Years — David Graeber", "Alexander Hamilton — Ron Chernow"]},
        {"slug": "behavioral-finance-psychology", "name": "Behavioral Finance & Psychology",
         "stars": ["Thinking, Fast and Slow — Daniel Kahneman", "The Psychology of Money — Morgan Housel", "Fooled By Randomness — Nassim Taleb", "The Black Swan — Nassim Taleb", "Antifragile — Nassim Taleb", "Misbehaving — Richard Thaler"]},
        {"slug": "portfolio-management-asset-allocation", "name": "Portfolio Management & Asset Allocation",
         "stars": ["The Most Important Thing — Howard Marks", "Pioneering Portfolio Management — David Swensen", "Expected Returns — Antti Ilmanen", "Portfolio Selection: Efficient Diversification of Investments — Harry Markowitz"]},
        {"slug": "accounting-financial-statements", "name": "Accounting & Financial Statements",
         "stars": ["The Interpretation of Financial Statements — Benjamin Graham", "Financial Statements: A Step-by-Step Guide — Thomas Ittelson"]},
     ]},
    {"tier": 3, "name": "Tier 3 \u2014 Asset Classes",
     "desc": "Deep dives into each major asset class \u2014 stocks, bonds, real estate, commodities, currencies, and derivatives.",
     "cats": [
        {"slug": "value-investing-equities", "name": "Value Investing & Equities",
         "stars": ["The Intelligent Investor — Benjamin Graham", "Security Analysis — Benjamin Graham & David Dodd", "The Essays of Warren Buffett — Buffett & Cunningham", "One Up on Wall Street — Peter Lynch", "Common Stocks and Uncommon Profits — Philip Fisher", "Common Stocks as Long Term Investments — Edgar Lawrence Smith", "Margin of Safety — Seth Klarman", "Stocks For The Long Run — Jeremy Siegel", "The Dhandho Investor — Mohnish Pabrai"]},
        {"slug": "fixed-income-bonds", "name": "Fixed Income & Bonds",
         "stars": ["The Handbook of Fixed Income Securities — Frank Fabozzi", "Bond Markets — Frank Fabozzi", "The Bond Book — Annette Thau"]},
        {"slug": "real-estate", "name": "Real Estate",
         "stars": ["What Every Real Estate Investor Needs to Know About Cash Flow — Frank Gallinelli"]},
        {"slug": "commodities-energy", "name": "Commodities & Energy",
         "stars": ["The Prize — Daniel Yergin", "The World for Sale — Javier Blas", "Hot Commodities — Jim Rogers"]},
        {"slug": "forex-currencies", "name": "Forex & Currencies",
         "stars": ["Trade Wars Are Class Wars — Matthew Klein", "Making Sense of the Dollar — Marc Chandler"]},
        {"slug": "options-derivatives", "name": "Options & Derivatives",
         "stars": ["Option Volatility and Pricing — Sheldon Natenberg", "Options As A Strategic Investment — Lawrence McMillan"]},
        {"slug": "crypto-digital-money", "name": "Crypto & Digital Money",
         "stars": []},
     ]},
    {"tier": 4, "name": "Tier 4 \u2014 Advanced Strategies",
     "desc": "Active trading, cycles, quant methods, and global macro. For when you want to go deeper.",
     "cats": [
        {"slug": "trading-technical-analysis", "name": "Trading & Technical Analysis",
         "stars": ["Winning on Wall Street — Martin Zweig", "Market Wizards — Jack Schwager", "Hedge Fund Market Wizards — Jack Schwager", "Reminiscences of a Stock Operator — Edwin Lefevre", "Come Into My Trading Room — Alexander Elder", "Trade Your Way To Financial Freedom — Van Tharp"]},
        {"slug": "trading-psychology", "name": "Trading Psychology",
         "stars": ["Trading Psychology 2.0 — Brett Steenbarger"]},
        {"slug": "cycles-market-timing", "name": "Cycles & Market Timing",
         "stars": ["Secular Cycles — Peter Turchin", "The Fourth Turning — Strauss & Howe", "Generations — Strauss & Howe", "Capital Wars: The Rise of Global Liquidity — Michael Howell", "Mastering the Market Cycle — Howard Marks"]},
        {"slug": "quantitative-algorithmic-trading", "name": "Quantitative & Algorithmic Trading",
         "stars": ["The Quants — Scott Patterson", "Flash Boys — Michael Lewis", "Fortune's Formula — William Poundstone", "The Signal and the Noise — Nate Silver"]},
        {"slug": "risk-management-position-sizing", "name": "Risk Management & Position Sizing",
         "stars": ["Safe Haven — Mark Spitznagel", "Super Trader — Van Tharp", "Definitive Guide To Position Sizing Strategies — Van Tharp"]},
        {"slug": "macro-investing-geopolitics", "name": "Macro Investing & Geopolitics",
         "stars": ["The Changing World Order — Ray Dalio", "Principles — Ray Dalio", "The Rise and Fall of Great Powers — Paul Kennedy", "Why Nations Fail — Acemoglu & Robinson", "The Accidental Superpower — Peter Zeihan"]},
        {"slug": "economic-indicators", "name": "Economic Indicators",
         "stars": ["The Trader's Guide to Key Economic Indicators — Richard Yamarone"]},
     ]},
    {"tier": 5, "name": "Tier 5 \u2014 Wisdom & Perspective",
     "desc": "Wall Street war stories, big-picture thinking, and the mindset to keep going.",
     "cats": [
        {"slug": "wall-street-stories-biographies", "name": "Wall Street Stories & Biographies",
         "stars": ["Liar's Poker — Michael Lewis", "Barbarians at the Gate — Burrough & Helyar", "More Money Than God — Sebastian Mallaby", "The Ascent of Money — Niall Ferguson", "Lords Of Finance — Liaquat Ahamed"]},
        {"slug": "corporate-finance-investment-banking", "name": "Corporate Finance & Investment Banking",
         "stars": ["Corporate Finance — Berk & DeMarzo", "Investment Banking — Rosenbaum & Pearl"]},
        {"slug": "geopolitics-sociology-power", "name": "Geopolitics, Sociology & Power",
         "stars": ["Guns, Germs, and Steel — Jared Diamond", "Sapiens — Yuval Noah Harari", "Bowling Alone — Robert Putnam", "The Great Leveler — Walter Scheidel"]},
        {"slug": "self-development-mindset", "name": "Self-Development & Mindset",
         "stars": ["Grit — Angela Duckworth", "Influence: The Psychology of Persuasion — Robert Cialdini", "Think and Grow Rich — Napoleon Hill", "Meditations — Marcus Aurelius"]},
        {"slug": "training-nutrition", "name": "Training & Nutrition",
         "stars": ["The Muscle & Strength Pyramid: Training — Eric Helms, Andy Morgan & Andrea Valdez"]},
        {"slug": "courses", "name": "Courses",
         "stars": []},
     ]},
]

CATEGORIES = {c["name"]: dict(c, tier=t["tier"], tier_name=t["name"])
              for t in OUTLINE for c in t["cats"]}
CATEGORY_NAMES = list(CATEGORIES)
FLAGS = ("star", "plain", "deep")   # must-know / standard / deep cut

# Categories the bot may file concepts into (the rest are book-only shelves)
FILEABLE = [n for n in CATEGORY_NAMES if n not in (
    "Wall Street Stories & Biographies", "Self-Development & Mindset",
    "Training & Nutrition", "Courses")]

# Legacy category -> outline category, used only until backfill has run
LEGACY_CATEGORY = {
    "monetary_policy": "Monetary Policy & Central Banking",
    "credit_bonds": "Fixed Income & Bonds",
    "fiscal_policy": "Macro Investing & Geopolitics",
    "macro": "Macro Investing & Geopolitics",
    "labor_economics": "Economic Indicators",
    "commodities": "Commodities & Energy",
    "market_structure": "Portfolio Management & Asset Allocation",
    "real_estate": "Real Estate",
    "crypto": "Crypto & Digital Money",
    "technicals": "Trading & Technical Analysis",
    "derivatives": "Options & Derivatives",
    "sentiment_flows": "Behavioral Finance & Psychology",
}


def concept_category(c):
    """Outline category for a concept, tolerating legacy values."""
    cat = c.get("category", "")
    if cat in CATEGORIES:
        return cat
    return LEGACY_CATEGORY.get(cat, "Macro Investing & Geopolitics")


def concept_flag(c):
    f = c.get("flag", "plain")
    return f if f in FLAGS else "plain"


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


# === NETWORK ===
class NetworkError(Exception):
    """The network was down, not the data.  Never counts against a video."""


def network_up(host="www.youtube.com", port=443, timeout=5):
    """True if we can actually open a TCP connection to YouTube.  A plain
    DNS lookup is not enough: right after wake, macOS can answer from its
    cache while the Wi-Fi interface is still coming up."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def wait_for_network(max_wait=NETWORK_WAIT):
    """After login or wake, Wi-Fi takes a few seconds to come back.  Poll
    until it does instead of firing yt-dlp into a dead network — that was
    logging a DNS error and then, worse, resetting the 6-hour timer as if
    the check had succeeded."""
    if network_up():
        return True
    log("  Network not up yet — waiting for Wi-Fi")
    deadline = time.time() + max_wait
    while time.time() < deadline:
        time.sleep(5)
        if network_up():
            log("  Network is up")
            return True
    log(f"  Network still down after {max_wait // 60} min — will retry")
    return False


# === STEP 1: Pull new video IDs from channels ===
def get_channel_videos(channel_url, limit=30):
    """Pull recent video IDs and titles from a YouTube channel.

    Returns a list of videos, or None if the check itself failed (yt-dlp
    missing, crashed, or the network was down).  None must never be
    treated as "the channel has no new videos"."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "--print", "id", "--print", "title",
             "--playlist-end", str(limit), channel_url],
            capture_output=True, text=True, timeout=120
        )
    except FileNotFoundError:
        log("  ERROR yt-dlp not found on PATH — install it or fix the PATH "
            "block at the top of this script")
        return None
    except Exception as e:
        log(f"  ERROR pulling channel: {e}")
        return None

    # yt-dlp breaks whenever YouTube changes its page layout.  It exits
    # non-zero and prints the reason to stderr; treat that as a real error,
    # not "the channel has no videos".
    if result.returncode != 0:
        err = (result.stderr or '').strip()
        log(f"  ERROR yt-dlp exit {result.returncode}: {err[-300:]}")
        if re.search(r"resolve|nodename|servname|getaddrinfo|network|connection|timed out|unreachable", err, re.I):
            log("  -> looks like the network, not yt-dlp; will retry soon")
        else:
            log("  -> try: pip3 install -U yt-dlp   (or: brew upgrade yt-dlp)")
        return None

    lines = result.stdout.strip().split("\n")
    videos = []
    for i in range(0, len(lines) - 1, 2):
        vid_id = lines[i].strip()
        title = lines[i + 1].strip()
        if vid_id and title:
            videos.append({"id": vid_id, "title": title})
    if not videos:
        log(f"  WARNING yt-dlp returned 0 videos for {channel_url}: "
            f"{(result.stderr or '').strip()[-300:] or 'no stderr'}")
        log("  -> yt-dlp is probably out of date: pip3 install -U yt-dlp")
        return None
    return videos


def _needs_processing(vid_id, processed):
    entry = processed.get(vid_id)
    return entry is None or entry.get("retry", False)


def find_new_videos():
    """Check all channels.  Returns (videos_not_yet_processed, ok) where
    ok is False if any channel could not be checked.

    First run for a channel: marks all existing videos as processed
    (backlog skip) so only future uploads get picked up.
    """
    channels = load_json(CHANNELS_FILE)
    if isinstance(channels, dict):
        channels = []
    processed = load_json(PROCESSED_FILE)
    seen_channels = load_json(BASE_DIR / "seen_channels.json")

    new_videos = []
    ok = True
    for channel in channels:
        log(f"  Checking: {channel['name']}")
        videos = get_channel_videos(channel["url"])
        if videos is None:
            # Skip, don't guess.  In particular a NEW channel must not get
            # an empty backlog recorded, or its whole history floods in on
            # the next good check.
            log(f"  Could not check {channel['name']} — will retry")
            ok = False
            continue

        # First time seeing this channel? Mark backlog as processed
        if channel["name"] not in seen_channels:
            log(f"  New channel — marking {len(videos)} existing videos as backlog")
            for v in videos:
                if v["id"] not in processed:
                    processed[v["id"]] = {
                        "title": v["title"],
                        "channel": channel["name"],
                        "processed": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "concepts_extracted": 0,
                        "skipped": "backlog_marked",
                    }
            seen_channels[channel["name"]] = datetime.now().strftime("%Y-%m-%d")
            save_json(BASE_DIR / "seen_channels.json", seen_channels)
            save_json(PROCESSED_FILE, processed)
            continue

        picked = []
        for v in videos:
            if _needs_processing(v["id"], processed):
                v["channel"] = channel["name"]
                picked.append(v)
        new_videos.extend(picked)
        log(f"  Found {len(videos)} total, {len(picked)} new/retry")

    if MAX_VIDEOS_PER_RUN:
        new_videos = new_videos[:MAX_VIDEOS_PER_RUN]
    return new_videos, ok


# === STEP 2: Download transcript ===
def download_transcript(video_id):
    """Download auto-captions and clean to plain text."""
    txt_path = TRANSCRIPTS_DIR / f"{video_id}.txt"

    if txt_path.exists():
        return txt_path.read_text()

    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        ytt = YouTubeTranscriptApi()
        t = ytt.fetch(video_id)
        text = " ".join(s.text for s in t.snippets)
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            txt_path.write_text(text)
            return text
    except Exception as e:
        # A dead network must not burn one of the video's 4 "no captions"
        # attempts — after 4 wakes with Wi-Fi still connecting, the video
        # would be skipped forever.
        if re.search(r"Connection|Timeout|resolve|nodename|servname|getaddrinfo|Name or service|unreachable",
                     f"{type(e).__name__} {e}", re.I):
            raise NetworkError(str(e)[:200])
        log(f"  Transcript download failed for {video_id}: {e}")

    return None


# === Claude CLI helper ===
CHUNK_CHARS = 25000        # max transcript chars per extraction call
CHUNK_OVERLAP = 1500       # overlap between chunks so nothing is cut mid-idea
EXCERPT_MAX = 15000        # chapter writer sees the whole transcript up to this


def run_claude(prompt, timeout=300, model="sonnet"):
    """Run `claude -p` and return stdout, or None on any failure.

    The CLI exits 0 and prints "API Error: ..." on network failures,
    so a return-code check alone is not enough.

    Claude Code auto-updates by reinstalling itself, and for a few seconds
    the `claude` symlink does not exist.  A call that lands in that gap
    gets FileNotFoundError — wait and retry instead of failing the video.
    """
    for attempt in range(4):
        try:
            result = subprocess.run(
                ["claude", "-p", prompt, "--model", model],
                capture_output=True, text=True, timeout=timeout
            )
            break
        except FileNotFoundError as e:
            if attempt == 3:
                log(f"  ERROR running claude: {e}")
                return None
            log(f"  claude not found (mid-update?) — retrying in 30s")
            time.sleep(30)
        except Exception as e:
            log(f"  ERROR running claude: {e}")
            return None
    out = (result.stdout or "").strip()
    if result.returncode != 0:
        log(f"  ERROR claude exit {result.returncode}: "
            f"{(result.stderr or out)[:200]}")
        return None
    if not out or re.match(r"^(API Error|Error:)", out):
        log(f"  ERROR claude returned: {out[:200]}")
        return None
    return out


def clean_chapter_html(text, slug=None):
    """Strip markdown fences / preamble; require a real chapter.

    Returns cleaned HTML or None if the output is not a usable chapter.
    """
    if not text:
        return None
    t = text.strip()
    # Drop ```html ... ``` fences (with or without the language tag)
    t = re.sub(r"^```[a-zA-Z]*\s*\n?", "", t)
    t = re.sub(r"\n?```\s*$", "", t)
    t = t.strip()
    # Drop anything before the first <h4 (chatty preamble)
    idx = t.find("<h4")
    if idx == -1:
        return None
    t = t[idx:]
    # Sanity: must contain real paragraphs
    if t.count("<p") < 3:
        return None
    if slug and f'id="{slug}"' not in t:
        t = re.sub(r'<h4[^>]*>', f'<h4 id="{slug}">', t, count=1)
    return t


def relevant_excerpt(transcript, concept, max_chars=EXCERPT_MAX,
                     window=3000, top_n=3):
    """Give the chapter writer the part of the transcript that actually
    discusses the concept, not just the intro.

    Short transcripts are returned whole. Long ones are split into windows,
    scored by keyword hits from the concept title/summary, and the best
    windows are joined in order.
    """
    if len(transcript) <= max_chars:
        return transcript

    stop = {"the", "and", "of", "in", "vs", "as", "a", "an", "to", "on",
            "for", "or", "with", "from", "by", "at", "rate", "market"}
    words = re.findall(r"[a-zA-Z][a-zA-Z\-]{3,}",
                       f"{concept.get('title','')} {concept.get('summary','')}")
    keys = {w.lower() for w in words if w.lower() not in stop}
    if not keys:
        return transcript[:max_chars]

    low = transcript.lower()
    step = window // 2
    scored = []
    for start in range(0, len(low), step):
        seg = low[start:start + window]
        score = sum(seg.count(k) for k in keys)
        scored.append((score, start))
    best = sorted(scored, reverse=True)[:top_n]

    # Merge overlapping windows into ranges, in transcript order
    ranges = []
    for s in sorted(s for _, s in best):
        e = min(s + window, len(transcript))
        if ranges and s <= ranges[-1][1]:
            ranges[-1][1] = max(ranges[-1][1], e)
        else:
            ranges.append([s, e])
    out = "\n[...]\n".join(transcript[s:e] for s, e in ranges)
    return out[:max_chars]


# === DEDUP: keep the book from re-covering old concepts ===
# Fuzzy title matching is a RETRIEVAL step (it picks what the judge sees),
# not a decision step: finance titles share too many domain words for it to
# be trusted ("Farm Debt-to-Asset Ratio" vs "Farm Debt Service Ratio").
# It only auto-merges near-exact rewordings; the LLM judge decides the rest.
FUZZY_DUP_RATIO = 0.95     # difflib ratio on normalized titles → auto-merge
FUZZY_DUP_JACCARD = 1.01   # disabled as an auto-merge trigger
JUDGE_CANDIDATES = 10      # closest existing concepts shown with summaries
JUDGE_MODEL = "haiku"

_STOP = {"the", "and", "of", "in", "vs", "as", "a", "an", "to", "on", "for",
         "or", "with", "from", "by", "at", "into", "its", "their", "concept",
         "mechanism", "dynamics", "risk", "effect", "effects"}


def _norm_tokens(title):
    """Lowercase, drop punctuation/stopwords, crude stem.  Parenthetical
    text is kept so acronyms match either way: "CPI (Consumer Price Index)"
    and "Consumer Price Index (CPI)" produce the same tokens."""
    t = re.sub(r"[^a-z0-9 ]+", " ", title.lower())
    toks = []
    for w in t.split():
        if w in _STOP or len(w) < 3:
            continue
        for suf in ("ization", "isation", "ations", "ation", "ings", "ing",
                    "ies", "ers", "er", "es", "s"):
            if w.endswith(suf) and len(w) - len(suf) >= 4:
                w = w[: -len(suf)]
                break
        toks.append(w)
    return toks


def _similarity(a, b):
    """Return (ratio, jaccard) between two titles."""
    import difflib
    ta, tb = _norm_tokens(a), _norm_tokens(b)
    if not ta or not tb:
        return 0.0, 0.0
    ratio = difflib.SequenceMatcher(None, " ".join(ta), " ".join(tb)).ratio()
    sa, sb = set(ta), set(tb)
    jacc = len(sa & sb) / len(sa | sb)
    return ratio, jacc


def closest_concepts(title, concepts, n=JUDGE_CANDIDATES):
    """Rank existing concepts by similarity to a candidate title.
    Compares against each concept's title AND its aliases."""
    scored = []
    for slug, c in concepts.items():
        names = [c.get("title", "")] + c.get("aliases", [])
        best = max(_similarity(title, nm) for nm in names)
        scored.append((max(best), best, slug))
    scored.sort(reverse=True)
    return [(slug, best) for _, best, slug in scored[:n]]


def find_fuzzy_duplicate(title, concepts):
    """Layer 1: free local match. Returns matching slug or None."""
    ranked = closest_concepts(title, concepts, n=1)
    if not ranked:
        return None
    slug, (ratio, jacc) = ranked[0]
    if ratio >= FUZZY_DUP_RATIO or jacc >= FUZZY_DUP_JACCARD:
        log(f"    Dedup (fuzzy {ratio:.2f}/{jacc:.2f}): "
            f"'{title}' ~ {slug}")
        return slug
    return None


def judge_duplicate(candidate, concepts):
    """Layer 2: cheap LLM judge against the closest existing concepts.

    Returns {"verdict": "same|instance|new", "match_slug": str|None}
    or None if the call failed (caller treats that as a failure so the
    video is retried, rather than silently writing a possible duplicate).
    """
    ranked = closest_concepts(candidate["title"], concepts)
    if not ranked:
        return {"verdict": "new", "match_slug": None}
    shown = {slug for slug, _ in ranked}
    listing = "\n".join(
        f"- {slug}: {concepts[slug]['title']} — {concepts[slug].get('summary','')}"
        for slug, _ in ranked
    )
    # Same-category entries (titles only) widen recall cheaply
    cat = concept_category(candidate)
    same_cat = [
        f"- {slug}: {c['title']}" for slug, c in concepts.items()
        if concept_category(c) == cat and slug not in shown
    ]
    cat_block = ""
    if same_cat:
        cat_block = (f"\nOTHER EXISTING ENTRIES IN THE SAME CATEGORY ({cat}):\n"
                     + "\n".join(same_cat[:60]) + "\n")
    prompt = f"""You maintain a finance glossary. Decide whether a CANDIDATE concept is
already covered by one of the EXISTING entries.

CANDIDATE:
- title: {candidate['title']}
- summary: {candidate.get('summary','')}

EXISTING (closest matches by title):
{listing}
{cat_block}
Verdicts:
- "same": the candidate is the same concept as an existing entry, just worded differently.
- "instance": the existing entry's chapter plus one added sentence would fully cover the
  candidate. The candidate has no definition or mechanism a reader of the existing chapter
  wouldn't already know (e.g. "Diesel Cost Pass-Through" is an instance of "Cost Pass-Through";
  "China Reducing Treasury Holdings" is an instance of "Foreign Treasury Holdings").
- "new": the candidate has its own definition or mechanism that the existing entry doesn't
  teach. Two concepts defined relative to each other are still two concepts
  (e.g. "Neutral Interest Rate" and "Accommodative Monetary Policy" are both "new").

Be strict: when in doubt between "instance" and "new", answer "instance".
Output ONLY JSON: {{"verdict": "same|instance|new", "match_slug": "<slug or null>"}}
"""
    out = run_claude(prompt, timeout=120, model=JUDGE_MODEL)
    if out is None:
        return None
    m = re.search(r"\{.*\}", out, re.DOTALL)
    if not m:
        log(f"  ERROR judge output not JSON: {out[:150]}")
        return None
    try:
        data = json.loads(m.group())
    except json.JSONDecodeError:
        log(f"  ERROR judge bad JSON: {out[:150]}")
        return None
    verdict = str(data.get("verdict", "new")).lower()
    match = data.get("match_slug")
    if verdict in ("same", "instance") and match in concepts:
        log(f"    Dedup (judge {verdict}): '{candidate['title']}' -> {match}")
        return {"verdict": verdict, "match_slug": match}
    return {"verdict": "new", "match_slug": None}


FG_SYNC_URL = ("https://script.google.com/macros/s/"
               "AKfycbwt438APIycBc534W6T66O3IgtxLUU9cczw-PZAN6Mc9p2xfU2ySsND_"
               "wEMJDHUvrXyUg/exec")

_done_cache = None
_done_fetched = 0


def get_done_slugs():
    """Fetch completed concept slugs from Apps Script (cached 1 hour)."""
    global _done_cache, _done_fetched
    if _done_cache is not None and time.time() - _done_fetched < 3600:
        return _done_cache
    try:
        import urllib.request
        url = FG_SYNC_URL + "?action=fg_get_done"
        # JSONP comes back as callback({...}), extract the JSON
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=15) as resp:
            text = resp.read().decode()
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            data = json.loads(m.group())
            if data.get("status") == "ok" and data.get("fg_done"):
                _done_cache = set(data["fg_done"].keys())
                _done_fetched = time.time()
                return _done_cache
    except Exception as e:
        log(f"    Could not fetch done list: {e}")
    if _done_cache is None:
        _done_cache = set()
        _done_fetched = time.time()
    return _done_cache


def merge_into(existing_slug, candidate_title, vid_id, concepts):
    """Record a duplicate against its existing concept: video becomes a
    source, the alternate wording becomes an alias (so both the prompt
    list and future fuzzy matches see it)."""
    c = concepts[existing_slug]
    src = c.setdefault("sources", [])
    if vid_id and vid_id not in src:
        src.append(vid_id)
    aliases = c.setdefault("aliases", [])
    if candidate_title and candidate_title != c.get("title") \
            and candidate_title not in aliases:
        aliases.append(candidate_title)


def resolve_candidate(candidate, concepts):
    """Run both dedup layers. Returns ("new", None), ("dup", slug),
    ("instance", slug), or (None, None) on judge failure."""
    dup = find_fuzzy_duplicate(candidate["title"], concepts)
    if dup:
        return "dup", dup
    verdict = judge_duplicate(candidate, concepts)
    if verdict is None:
        return None, None
    if verdict["verdict"] == "same":
        return "dup", verdict["match_slug"]
    if verdict["verdict"] == "instance":
        return "instance", verdict["match_slug"]
    return "new", None


# === STEP 3: Extract concepts via Claude CLI ===
def category_rubric():
    return "\n".join(
        f"- {n}  ({CATEGORIES[n]['tier_name']})" for n in FILEABLE)


def _extract_from_chunk(title, chunk, concept_list, part_label):
    """One extraction call. Returns dict {"new": [...], "existing": [...]}
    or None on failure."""
    category_rubric_text = category_rubric()
    prompt = f"""You are building a living finance education guide. Read this YouTube video transcript
and extract every distinct finance/economics/market concept it teaches or relies on.

VIDEO: "{title}"{part_label}
TRANSCRIPT:
{chunk}

ALREADY COVERED CONCEPTS (do NOT re-extract these):
{concept_list if concept_list else "(none yet)"}

Output ONE JSON object:
{{
  "new": [
    {{
      "slug": "yield_curve_inversion",
      "title": "Yield Curve Inversion",
      "category": "<exactly one of the CATEGORIES below>",
      "flag": "star|plain|deep",
      "summary": "One sentence explaining what this concept is",
      "context": "How the video discussed it — what claim was made, what evidence given"
    }}
  ],
  "existing": ["slug_of_already_covered_concept_this_video_discussed", "..."]
}}

CATEGORIES (use the exact name; pick the shelf a textbook on this concept would sit on):
{category_rubric_text}

FLAG:
- "star": must-know — you cannot follow a markets conversation without it
  (Federal Funds Rate, Term Premium, Yield Curve, CPI).
- "plain": standard working knowledge for someone actively trading or investing.
- "deep": deep cut — sector plumbing, single-country or single-industry mechanics,
  a curiosity (fertilizer pricing, farm loan-loss provisions, COMEX inventories).

Rules:
- A CONCEPT is something that would have its own glossary or textbook entry and
  would still make sense in a video from a different year. "Federal Funds Rate" is
  a concept. "Fed raised rates" is news. "China cutting Treasury holdings" is a claim
  about a concept (Foreign Treasury Holdings), not a new concept.
- THE TEXTBOOK TEST: a concept qualifies only if it would plausibly have its own
  entry in a finance textbook, CFA curriculum, or Investopedia — a named term,
  instrument, metric, institution, or market mechanism that a learner needs in
  order to understand markets. If the title only makes sense with this video's
  story attached, it is not a concept.
- Basic, well-known concepts count and matter MOST (VIX, share buybacks, risk
  parity, yield curve). Never skip a concept because it seems too obvious — this
  guide is for a learner building from the ground up.
- NOT concepts (never extract these as "new"):
  * the presenter's analogies or historical comparisons ("1999 dot-com analogy",
    "this looks like 2008") — file the underlying event as a concept if it is
    one (Dot-Com Bubble), never the comparison itself;
  * commentary heuristics or ways of reading a story ("multi-causal attribution",
    "narrow vs broad decline as a signal", "unconfirmed vs confirmed reporting");
  * generic business vocabulary that isn't finance-specific ("year-over-year
    growth rate", "supply chain", "long-term contract") unless the video teaches
    it as a finance mechanism;
  * company-, deal-, or sector-specific plumbing that a general investor would
    never need (mark genuinely useful sector mechanics "deep" instead).
- A concept counts if the video names it OR clearly relies on it.
- Work in two passes: first list every finance term or mechanism in the transcript;
  then apply the textbook test to each. Survivors already covered go in "existing"
  (exact slug); the rest go in "new". Drop news, one-off claims, presenter
  opinions, and instances of a general mechanism you've already listed.
- Do NOT create a new concept for a specific instance, example, or framing of an
  existing one. Prefer the general mechanism ("Cost Pass-Through") over the
  instance ("Diesel Cost Pass-Through to Freight").
- Be specific where the distinction matters: "Credit Default Swaps" not "derivatives".
- Slugs: lowercase, underscores, no filler words.
- If the video substantively discusses a concept already covered, put its EXACT slug
  (as written in the list) in "existing" — do not re-extract it.
- There is no target count. A dense explainer may yield 15+ concepts; a news
  recap may legitimately yield 2-3 (mostly "existing"). Quality over quantity —
  a padded list is worse than a short one.
- If nothing new, "new" is an empty array.
- Output ONLY the JSON object, nothing else.
"""
    out = run_claude(prompt)
    if out is None:
        return None
    # Accept either the new object format or a bare array (old format)
    m = re.search(r"\{.*\}", out, re.DOTALL) or re.search(r"\[.*\]", out, re.DOTALL)
    if not m:
        log(f"  ERROR no JSON in extraction output: {out[:200]}")
        return None
    try:
        data = json.loads(m.group())
    except json.JSONDecodeError as e:
        log(f"  ERROR bad JSON from extraction: {e}")
        return None
    if isinstance(data, list):
        data = {"new": data, "existing": []}
    data.setdefault("new", [])
    data.setdefault("existing", [])
    return data


def extract_concepts(video_id, title, transcript, existing_concepts):
    """Call Claude to read the transcript and extract finance concepts.

    Long transcripts are processed in overlapping chunks and merged.
    Returns {"new": [...], "existing": [...]} or None if ANY chunk failed
    (so the caller can leave the video unprocessed and retry later).
    """
    def _line(slug, c):
        line = f"- {slug}: {c['title']} ({c['category']})"
        if c.get("aliases"):
            line += " [aka: " + "; ".join(c["aliases"][:4]) + "]"
        return line
    concept_list = "\n".join(
        _line(slug, c) for slug, c in existing_concepts.items()
    )

    chunks = []
    if len(transcript) <= CHUNK_CHARS:
        chunks = [transcript]
    else:
        start = 0
        while start < len(transcript):
            chunks.append(transcript[start:start + CHUNK_CHARS])
            start += CHUNK_CHARS - CHUNK_OVERLAP

    merged_new, merged_existing = {}, set()
    for i, chunk in enumerate(chunks):
        label = f" (part {i + 1} of {len(chunks)})" if len(chunks) > 1 else ""
        data = _extract_from_chunk(title, chunk, concept_list, label)
        if data is None:
            return None
        for c in data["new"]:
            slug = c.get("slug")
            if not slug or not c.get("title"):
                continue
            if slug in existing_concepts or slug in merged_new:
                continue
            if c.get("category") not in CATEGORIES:
                c["category"] = concept_category(c)
            if c.get("flag") not in FLAGS:
                c["flag"] = "plain"
            c.setdefault("summary", "")
            c.setdefault("context", "")
            merged_new[slug] = c
        for s in data["existing"]:
            if s in existing_concepts:
                merged_existing.add(s)
    total = len(merged_new) + len(merged_existing)
    if total < 4 and len(transcript) > 2000:
        # Safety net: re-scan for missed concepts
        found_so_far = ", ".join(
            [c["title"] for c in merged_new.values()] +
            [existing_concepts[s]["title"] for s in merged_existing
             if s in existing_concepts]
        )
        retry_prompt = f"""A finance video was scanned and only {total} concepts
were found, which seems low. Here is what was found so far:
{found_so_far}

Re-read this transcript and list any finance terms or mechanisms that were
missed. Include basic/well-known concepts (VIX, buybacks, risk parity, etc.)
— never skip something for being too obvious. Apply the textbook test: only
named terms, instruments, metrics, institutions, or market mechanisms that
would have their own textbook or Investopedia entry. No analogies, presenter
heuristics, news, or generic business vocabulary. If nothing was genuinely
missed, return empty arrays.

VIDEO: "{title}"
TRANSCRIPT:
{transcript[:CHUNK_CHARS]}

ALREADY COVERED CONCEPTS:
{concept_list if concept_list else "(none yet)"}

Output ONE JSON object with "new" and "existing" arrays, same format as before.
Only include concepts NOT in the found-so-far list above.
"""
        log(f"    Safety net: only {total} concepts, re-scanning...")
        retry = run_claude(retry_prompt)
        if retry:
            m = re.search(r"\{.*\}", retry, re.DOTALL)
            if m:
                try:
                    extra = json.loads(m.group())
                    for c in extra.get("new", []):
                        slug = c.get("slug")
                        if slug and c.get("title") and slug not in existing_concepts \
                                and slug not in merged_new:
                            if c.get("category") not in CATEGORIES:
                                c["category"] = concept_category(c)
                            if c.get("flag") not in FLAGS:
                                c["flag"] = "plain"
                            c.setdefault("summary", "")
                            c.setdefault("context", "")
                            merged_new[slug] = c
                    for s in extra.get("existing", []):
                        if s in existing_concepts:
                            merged_existing.add(s)
                    log(f"    Safety net found {len(extra.get('new', []))} new, "
                        f"{len(extra.get('existing', []))} existing")
                except json.JSONDecodeError:
                    pass

    return {"new": list(merged_new.values()),
            "existing": sorted(merged_existing)}


# === STEP 4: Write chapter for a concept via Claude CLI ===
def write_chapter(concept, video_title, transcript):
    """Call Claude to write a bookai-depth chapter for one concept.

    Returns cleaned chapter HTML, or None if the call failed or the
    output was not a usable chapter (so the caller does NOT save it).
    """
    excerpt = relevant_excerpt(transcript, concept)

    prompt = f"""You are writing a chapter for a personal finance education guide.
Write a thorough, clear explanation of this concept that would help someone
truly understand it — not a summary, but real teaching.

CONCEPT: {concept['title']}
CATEGORY: {concept['category']}
CONTEXT FROM VIDEO: {concept.get('context') or concept.get('summary', '')}
VIDEO: "{video_title}"

RELEVANT TRANSCRIPT EXCERPT:
{excerpt}

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
- Output ONLY the raw HTML content — no markdown code fences, no preamble
"""

    out = run_claude(prompt)
    html = clean_chapter_html(out, concept.get("slug"))
    if html is None:
        log(f"  ERROR unusable chapter output for {concept['title']}: "
            f"{(out or '')[:120]!r}")
    return html


# === STEP 5: Rebuild HTML (tier -> category -> concept) ===

# Shared CSS for all pages (on top of the site's book.css)
PAGE_CSS = """
.prog-stats { display:grid; grid-template-columns:repeat(auto-fit,minmax(112px,1fr));
  gap:10px; margin:1rem 0 1.5rem; }
.prog-stat { background:#e8e0d0; border:1px solid #d4c8b0; border-radius:8px;
  padding:0.7rem 0.9rem; }
.prog-stat .n { display:block; font-size:1.5rem; color:#5a3e1a; line-height:1.1; }
.prog-stat .l { display:block; font-size:0.75rem; color:#8a7a60; margin-top:0.2rem; }
.prog-chart { position:relative; margin:0.5rem 0 0.4rem; }
.prog-chart svg { width:100%; height:auto; display:block; overflow:visible; }
.prog-chart .grid { stroke:#ddd3c0; stroke-width:1; }
.prog-chart .axis { stroke:#c8bca4; stroke-width:1; }
.prog-chart .tick { fill:#8a7a60; font-size:11px; }
.prog-chart .ylab { fill:#8a7a60; font-size:11px; }
.prog-chart .actual { fill:none; stroke:#9a5a22; stroke-width:2; stroke-linejoin:round; }
.prog-chart .actual-dot { fill:#9a5a22; stroke:#f4efe8; stroke-width:2; }
.prog-chart .model { fill:none; stroke:#0e9488; stroke-width:2; stroke-dasharray:6 4; }
.prog-chart .ceiling { stroke:#8a7a60; stroke-width:1; stroke-dasharray:2 4; }
.prog-chart .here { stroke:#9a5a22; stroke-width:1; stroke-dasharray:2 3; opacity:0.6; }
.prog-chart .dlabel { font-size:11px; fill:#3a2e1e; }
.prog-chart .bar { fill:#9a5a22; opacity:0.75; }
.prog-chart .bar-model { fill:none; stroke:#0e9488; stroke-width:2; stroke-dasharray:6 4; }
.prog-chart .hit { fill:transparent; cursor:crosshair; }
.prog-tip { position:absolute; pointer-events:none; display:none;
  background:#3a2e1e; color:#f4efe8; font-size:12px; line-height:1.4;
  padding:6px 9px; border-radius:6px; white-space:nowrap; z-index:5; }
.prog-legend { display:flex; gap:1.2rem; font-size:0.8rem; color:#5a3e1a;
  margin:0 0 1.5rem; flex-wrap:wrap; }
.prog-legend span::before { content:""; display:inline-block; width:18px; height:0;
  border-top:2px solid; margin-right:6px; vertical-align:middle; }
.prog-legend .lg-actual::before { border-color:#9a5a22; }
.prog-legend .lg-model::before { border-color:#0e9488; border-top-style:dashed; }
.prog-legend .lg-ceiling::before { border-color:#8a7a60; border-top-style:dotted; }
.prog-eq { background:#e8e0d0; border:1px solid #d4c8b0; border-radius:8px;
  padding:0.9rem 1.1rem; font-family:Georgia,serif; font-size:1.05rem; color:#3a2e1e;
  margin:1rem 0; }
.prog-eq .sub { display:block; font-size:0.85rem; color:#8a7a60; margin-top:0.4rem;
  font-family:inherit; }
.prog-note { font-size:0.85rem; color:#8a7a60; }
.prog-link { font-size:0.85rem; margin:-0.8rem 0 1.2rem; }
.prog-link a { color:#0e9488; }
table.prog-table { font-size:0.85rem; margin:1rem 0; }
.fg-bar {
  display: flex; gap: 8px; align-items: center; flex-wrap: wrap;
  margin: 0 0 1.5rem; padding: 0.6rem 0.9rem;
  background: #e8e0d0; border-radius: 8px;
  border: 1px solid #d4c8b0; font-size: 0.85rem;
}
.fg-btn {
  background: none; border: 1px solid #d4c8b0; color: #3a2a1a;
  padding: 0.3rem 0.8rem; border-radius: 4px; cursor: pointer;
  font-size: 0.8rem; transition: all 0.2s;
}
.fg-btn:hover { border-color: #a08060; }
.fg-btn.active { background: #a08060; color: #f4efe8; border-color: #a08060; }
.fg-count { color: #a08060; margin-left: auto; }
.tier { margin: 0 0 2rem; }
.tier h2 {
  font-weight: 400; font-size: 1.3rem; margin: 0 0 0.1rem;
  padding-bottom: 0.35rem; border-bottom: 2px solid #d4c8b0;
}
.tier .tier-desc { color: #a08060; font-size: 0.85rem; margin: 0.4rem 0 0.8rem; }
.cat-card {
  display: flex; align-items: baseline; gap: 12px;
  padding: 0.7rem 0.9rem; margin: 0 0 0.5rem;
  background: #e8e0d0; border: 1px solid #d4c8b0; border-radius: 8px;
  text-decoration: none; color: #3a2a1a; transition: all 0.2s;
}
.cat-card:hover { border-color: #a08060; background: #ded4c0; }
.cat-card .cat-name { font-size: 1.05rem; }
.cat-card .cat-count { margin-left: auto; color: #a08060; font-size: 0.8rem; white-space: nowrap; }
.cat-card.done { opacity: 0.3; }
.cat-card.fg-empty { display: none; }
.tier-empty { color: #a08060; font-size: 0.8rem; margin: 0.4rem 0 0; }
.concept-row {
  display: flex; align-items: baseline; gap: 10px;
  padding: 0.6rem 0.4rem; border-bottom: 1px solid #d4c8b0;
  text-decoration: none; color: #3a2a1a;
}
.concept-row:hover { background: #ede5d6; }
.concept-row .mark { width: 22px; text-align: center; color: #b8863b; flex: none; }
.concept-row .mark.deep { color: #a08060; font-size: 0.7rem; }
.concept-row.done .ctitle { opacity: 0.35; text-decoration: line-through; }
.concept-row.fg-hidden, body.hide-done .concept-row.done,
body.hide-done .cat-card.done { display: none; }
.fg-hidden-note { color: #a08060; font-size: 0.8rem; margin: 0.6rem 0 0; }
.books {
  margin: 2rem 0 0; padding: 0.9rem 1.1rem;
  background: #e8e0d0; border: 1px solid #d4c8b0; border-radius: 8px;
}
.books h3 { font-weight: 400; font-size: 1rem; margin: 0 0 0.4rem; }
.books ul { margin: 0; padding-left: 1.2rem; }
.books li { font-size: 0.85rem; margin: 0.15rem 0; }
.concept-meta {
  display: flex; gap: 14px; flex-wrap: wrap;
  color: #a08060; font-size: 0.8rem; margin: 0 0 1.2rem;
}
.concept-meta .star { color: #b8863b; }
.concept-side {
  margin: 2rem 0 0; padding-top: 1rem; border-top: 1px solid #d4c8b0;
  color: #a08060; font-size: 0.85rem; line-height: 1.7;
}
.concept-side a { color: #3a2a1a; border-bottom: 1px dotted #a08060; text-decoration: none; }
.concept-done {
  display: inline-flex; align-items: center; gap: 0.4rem;
  background: none; border: 1px solid #d4c8b0; border-radius: 4px;
  padding: 0.3rem 0.8rem; cursor: pointer; font-size: 0.8rem;
  color: #a08060; transition: all 0.2s; margin-top: 1.2rem;
}
.concept-done:hover { border-color: #4ade80; color: #4ade80; }
.concept-done.on { border-color: #4ade80; background: #4ade80; color: #1a1008; }
.back-link {
  display: inline-block; margin-bottom: 1rem;
  color: #a08060; text-decoration: none; font-size: 0.9rem;
}
.back-link:hover { color: #d4a574; }
.vid-tab {
  margin: 0 0 1.2rem; background: #e8e0d0; border: 1px solid #d4c8b0;
  border-radius: 8px; overflow: hidden;
}
.vid-tab summary {
  padding: 0.6rem 0.9rem; cursor: pointer; font-size: 0.85rem;
  color: #3a2a1a; list-style: none; user-select: none;
}
.vid-tab summary::-webkit-details-marker { display: none; }
.vid-tab summary::before {
  content: '\u25b6'; display: inline-block; margin-right: 0.5rem;
  font-size: 0.7rem; transition: transform 0.2s;
}
.vid-tab[open] summary::before { transform: rotate(90deg); }
.vid-tab .vid-status {
  float: right; font-size: 0.75rem; padding: 0.15rem 0.5rem;
  border-radius: 3px; margin-left: 0.5rem;
}
.vid-tab .vid-ok { background: #4ade8040; color: #2d6a4f; }
.vid-tab .vid-err { background: #f8717140; color: #9b2c2c; }
.vid-tab .vid-list {
  padding: 0 0.9rem 0.7rem; margin: 0;
  list-style: none; font-size: 0.8rem;
}
.vid-tab .vid-list li {
  padding: 0.35rem 0; border-top: 1px solid #d4c8b0;
  display: flex; justify-content: space-between; gap: 8px;
}
.vid-tab .vid-list .vid-date {
  color: #a08060; white-space: nowrap; flex: none;
}
.vid-tab .vid-list .vid-concepts {
  color: #a08060; white-space: nowrap; flex: none; font-size: 0.75rem;
}
.vid-tab .vid-none {
  padding: 0.4rem 0.9rem 0.7rem; color: #a08060; font-size: 0.8rem;
}
"""

# Shared JS is now in fg.js — loaded as external script
PAGE_JS = True  # sentinel: _page_wrap adds <script src="fg.js"> when truthy

FILTER_BAR = """
<div class="fg-bar">
  <button class="fg-btn" data-filter="all" onclick="setFilter('all')">Everything</button>
  <button class="fg-btn" data-filter="nodeep" onclick="setFilter('nodeep')">Hide deep cuts</button>
  <button class="fg-btn" data-filter="star" onclick="setFilter('star')">&#9733; Must-Know Only</button>
  <button class="fg-btn fg-btn-hide" onclick="toggleHideDone()">Hide completed</button>
  <span class="fg-count" id="fgCount"></span>
</div>"""


def _words(c):
    """Approximate reading length of a concept's chapter (words)."""
    txt = re.sub(r"<[^>]+>", " ", c.get("chapter_html") or c.get("summary") or "")
    return len(txt.split())


def _esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def _page_wrap(title, body, css_path="../book.css", back_href=None,
               back_label=None, bm_key=None, extra_js=""):
    """Wrap content in a full HTML page (site chrome from book.css/book.js)."""
    back = ""
    if back_href:
        back = (f'<a class="back-link" href="{back_href}">'
                f'&larr; {_esc(back_label or "Back")}</a>')
    bm = ""
    if bm_key:
        bm = f"<script>var BM_KEY = '{bm_key}';</script>"
    # PAGE_JS sentinel → load external fg.js (path relative to css_path)
    if extra_js is PAGE_JS:
        fg_dir = css_path.rsplit('book.css', 1)[0].rstrip('/')
        # css_path is relative to the HTML file, fg.js is in FinanceGuide/
        # ../book.css → fg.js, ../../book.css → ../fg.js
        if css_path.startswith('../../'):
            extra_js = '<script src="../fg.js"></script>'
        else:
            extra_js = '<script src="fg.js"></script>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="theme-color" content="#f4efe8">
<title>{_esc(title)} - Finance Guide</title>
<link rel="stylesheet" href="{css_path}">
<style>{PAGE_CSS}</style>
</head>
<body>
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
<script src="{css_path.replace('book.css', 'book.js')}"></script>
{extra_js}
</body>
</html>"""


def _mark(flag):
    if flag == "star":
        return '<span class="mark">&#9733;</span>'
    if flag == "deep":
        return '<span class="mark deep">deep</span>'
    return '<span class="mark"></span>'


def _concept_rows(items, href_prefix):
    order = {"star": 0, "plain": 1, "deep": 2}
    items = sorted(items, key=lambda x: (order[concept_flag(x[1])],
                                          x[1]["title"].lower()))
    return "".join(
        f'<a class="concept-row" href="{href_prefix}{slug}.html"'
        f' data-slug="{slug}" data-flag="{concept_flag(c)}" data-words="{_words(c)}">'
        f'{_mark(concept_flag(c))}'
        f'<span class="ctitle">{_esc(c["title"])}</span></a>'
        for slug, c in items
    )


def _videos_this_week_html(processed, concepts):
    """Build a collapsible tab showing videos processed in the last 7 days,
    including partial ones (some chapters written, rest queued for retry).
    Concept counts come from the guide itself — concepts whose first source
    is the video — so a video finished across several runs shows its full
    total, not just the last run's."""
    added_by = {}
    for c in concepts.values():
        if c.get("sources"):
            added_by[c["sources"][0]] = added_by.get(c["sources"][0], 0) + 1
    now = datetime.now()
    cutoff = (now - timedelta(days=7)).strftime("%Y-%m-%d")
    week_vids = []
    for vid_id, v in processed.items():
        if v.get("skipped"):
            continue
        ts = v.get("processed", "")
        if ts >= cutoff:
            week_vids.append((vid_id, v))
    week_vids.sort(key=lambda x: x[1].get("processed", ""), reverse=True)

    # Check bot health: last successful run
    last_run = ""
    for v in processed.values():
        ts = v.get("processed", "")
        if ts > last_run and not v.get("skipped"):
            last_run = ts
    if last_run:
        try:
            lr = datetime.strptime(last_run, "%Y-%m-%d %H:%M")
            hours_ago = (now - lr).total_seconds() / 3600
            if hours_ago < 24:
                status = f'<span class="vid-status vid-ok">bot ok</span>'
            else:
                status = (f'<span class="vid-status vid-err">'
                          f'last run {int(hours_ago)}h ago</span>')
        except ValueError:
            status = ""
    else:
        status = '<span class="vid-status vid-err">no runs</span>'

    count = len(week_vids)
    label = f"Videos this week ({count})" if count else "Videos this week"

    if not week_vids:
        inner = '<p class="vid-none">No videos processed this week.</p>'
    else:
        rows = []
        for vid_id, v in week_vids:
            ts = v.get("processed", "")[:10]
            title = _esc(v.get("title", "?"))
            n = added_by.get(vid_id, 0)
            ctext = f"{n} concept{'s' if n != 1 else ''}" if n else "0 new"
            if v.get("partial"):
                ctext += " &middot; finishing"
            rows.append(
                f'<li><span>{title}</span>'
                f'<span class="vid-concepts">{ctext}</span>'
                f'<span class="vid-date">{ts}</span></li>'
            )
        inner = f'<ul class="vid-list">{"".join(rows)}</ul>'

    return f"""<details class="vid-tab">
<summary>{status}{label}</summary>
{inner}
</details>"""



# === PROGRESS: "how close is the guide to running out?" ===
def _video_series(processed, concepts):
    """Chronological (date, new_concepts) per processed video, counting the
    concepts that actually exist in the guide today (each credited to its
    earliest source video), so the curve matches the shelf count even after
    manual pruning or merges.  A concept with no known source is credited to
    the first video."""
    vids = sorted(((v["processed"], k) for k, v in processed.items()
                   if not v.get("skipped") and v.get("processed")))
    if not vids:
        return []
    order = {k: i for i, (_, k) in enumerate(vids)}
    counts = [0] * len(vids)
    for c in concepts.values():
        hits = [order[x] for x in c.get("sources", []) if x in order]
        counts[min(hits) if hits else 0] += 1
    return [(ts, n) for (ts, _), n in zip(vids, counts)]


def _fit_saturation(cum):
    """Fit total(n) = K * (1 - exp(-n / tau)) to cumulative points
    [(n, total), ...] by least squares.  Coarse grid then a fine pass;
    cheap enough to run on every rebuild.  Returns (K, tau) or None."""
    import math
    if len(cum) < 5:
        return None
    last = cum[-1][1]

    def sse(K, tau):
        return sum((K * (1 - math.exp(-n / tau)) - t) ** 2 for n, t in cum)

    best = None
    for K in range(max(last, 50), max(last * 6, 200) + 1, 10):
        for tau in range(4, 301, 4):
            e = sse(K, tau)
            if best is None or e < best[0]:
                best = (e, K, tau)
    _, K0, t0 = best
    for K in range(max(last, K0 - 10), K0 + 11):
        for tau in range(max(2, t0 - 4), t0 + 5):
            e = sse(K, tau)
            if e < best[0]:
                best = (e, K, tau)
    return best[1], best[2]


def _progress_model(processed, concepts):
    """Everything the progress page and index teaser need, or None."""
    import math
    series = _video_series(processed, concepts)
    if len(series) < 5:
        return None
    cum, total = [], 0
    for i, (ts, n) in enumerate(series, 1):
        total += n
        cum.append((i, total))
    fit = _fit_saturation(cum)
    if not fit:
        return None
    K, tau = fit
    n_now = len(series)
    rate_now = (K / tau) * math.exp(-n_now / tau)          # new concepts per video today
    # first video count at which the model rate drops below 1, then 0.5
    n_lt1 = max(n_now, math.ceil(tau * math.log(K / tau))) if K > tau else n_now
    n_lt05 = max(n_now, math.ceil(tau * math.log(2 * K / tau))) if 2 * K > tau else n_now
    first = datetime.strptime(series[0][0][:10], "%Y-%m-%d")
    last = datetime.strptime(series[-1][0][:10], "%Y-%m-%d")
    days = max(1, (last - first).days)
    per_day = n_now / days
    return {
        "series": series, "cum": cum, "K": K, "tau": tau, "n_now": n_now,
        "total": total, "remaining": max(0, K - total), "rate_now": rate_now,
        "videos_to_lt1": max(0, n_lt1 - n_now), "videos_to_lt05": max(0, n_lt05 - n_now),
        "per_day": per_day,
        "days_to_lt1": (n_lt1 - n_now) / per_day if per_day else None,
        "days_to_lt05": (n_lt05 - n_now) / per_day if per_day else None,
        "n_end": max(n_lt05 + 5, n_now + 10),
    }


def _progress_teaser(m):
    if not m:
        return ""
    wk = f" &middot; ~{m['days_to_lt1'] / 7:.0f} weeks until &lt;1 new per video" \
        if m["days_to_lt1"] is not None else ""
    return (f'<p class="prog-link"><a href="progress.html">Running out? &rarr;</a> '
            f'est. ceiling ~{m["K"]} concepts, ~{m["remaining"]} to go{wk}</p>')


def _progress_html(m, concepts):
    """Progress page body: stats, the saturation chart, the equation and a
    plain-English explanation.  Fully static SVG; a little JS for hover."""
    import math
    from collections import Counter
    W, H = 720, 320
    L, R, T, B = 48, 16, 16, 30
    pw, ph = W - L - R, H - T - B
    K, tau = m["K"], m["tau"]
    n_end = m["n_end"]
    y_max = max(K * 1.05, m["total"] * 1.05)

    def X(n):
        return L + pw * n / n_end

    def Y(v):
        return T + ph * (1 - v / y_max)

    # gridlines: ~5 nice y ticks
    step = 10 ** math.floor(math.log10(y_max / 5))
    for mult in (1, 2, 5, 10):
        if y_max / (step * mult) <= 6:
            step *= mult
            break
    grid = []
    v = 0
    while v <= y_max:
        grid.append(f'<line class="grid" x1="{L}" x2="{W - R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/>'
                    f'<text class="ylab" x="{L - 6}" y="{Y(v) + 4:.1f}" text-anchor="end">{int(v)}</text>')
        v += step
    xt = []
    xstep = 10 if n_end <= 120 else 25
    for n in range(0, n_end + 1, xstep):
        xt.append(f'<text class="tick" x="{X(n):.1f}" y="{H - 8}" text-anchor="middle">{n}</text>')

    # model curve, ceiling, actual
    model_pts = " ".join(f"{X(n):.1f},{Y(K * (1 - math.exp(-n / tau))):.1f}"
                         for n in range(0, n_end + 1))
    actual_pts = " ".join(f"{X(n):.1f},{Y(t):.1f}" for n, t in m["cum"])
    dots, hits = [], []
    for (n, t), (ts, new) in zip(m["cum"], m["series"]):
        dots.append(f'<circle class="actual-dot" cx="{X(n):.1f}" cy="{Y(t):.1f}" r="3.5"/>')
        hits.append(f'<rect class="hit" x="{X(n) - pw / n_end / 2:.1f}" y="{T}" '
                    f'width="{pw / n_end:.1f}" height="{ph}" '
                    f'data-tip="Video {n} &middot; {ts[:10]}&lt;br&gt;+{new} new &middot; {t} total'
                    f'&lt;br&gt;model: {K * (1 - math.exp(-n / tau)):.0f}"/>')
    n_now = m["n_now"]
    chart = f"""
<div class="prog-chart" id="progChart">
<svg viewBox="0 0 {W} {H}" role="img"
 aria-label="Cumulative concepts per video: actual points versus fitted saturation curve">
{"".join(grid)}
<line class="axis" x1="{L}" x2="{W - R}" y1="{Y(0):.1f}" y2="{Y(0):.1f}"/>
{"".join(xt)}
<line class="ceiling" x1="{L}" x2="{W - R}" y1="{Y(K):.1f}" y2="{Y(K):.1f}"/>
<text class="dlabel" x="{W - R}" y="{Y(K) - 5:.1f}" text-anchor="end">ceiling K = {K}</text>
<polyline class="model" points="{model_pts}"/>
<polyline class="actual" points="{actual_pts}"/>
<line class="here" x1="{X(n_now):.1f}" x2="{X(n_now):.1f}" y1="{T}" y2="{Y(0):.1f}"/>
<text class="dlabel" x="{X(n_now) + 5:.1f}" y="{Y(m['total']) + 18:.1f}">you are here: {m['total']} after {n_now} videos</text>
{"".join(dots)}
{"".join(hits)}
</svg>
<div class="prog-tip" id="progTip"></div>
</div>
<div class="prog-legend">
 <span class="lg-actual">Actual concepts (cumulative)</span>
 <span class="lg-model">Model: K&middot;(1&minus;e<sup>&minus;n/&tau;</sup>)</span>
 <span class="lg-ceiling">Estimated ceiling</span>
</div>"""

    # new-per-video bars + model rate
    H2, B2 = 150, 26
    ph2 = H2 - T - B2
    r_max = max([n for _, n in m["series"]] + [K / tau]) * 1.1

    def Y2(v):
        return T + ph2 * (1 - v / r_max)

    bars = []
    bw = max(2, pw / n_end - 2)
    for (n, t), (ts, new) in zip(m["cum"], m["series"]):
        bars.append(f'<rect class="bar" x="{X(n) - bw / 2:.1f}" y="{Y2(new):.1f}" '
                    f'width="{bw:.1f}" height="{max(0, Y2(0) - Y2(new)):.1f}" rx="2"/>')
    rate_pts = " ".join(f"{X(n):.1f},{Y2((K / tau) * math.exp(-n / tau)):.1f}"
                        for n in range(1, n_end + 1))
    one_y = Y2(1)
    chart2 = f"""
<div class="prog-chart">
<svg viewBox="0 0 {W} {H2}" role="img" aria-label="New concepts per video, actual bars and model rate">
<line class="grid" x1="{L}" x2="{W - R}" y1="{one_y:.1f}" y2="{one_y:.1f}"/>
<text class="ylab" x="{L - 6}" y="{one_y + 4:.1f}" text-anchor="end">1</text>
<text class="ylab" x="{L - 6}" y="{Y2(r_max / 2) + 4:.1f}" text-anchor="end">{int(r_max / 2)}</text>
<text class="ylab" x="{L - 6}" y="{T + 8}" text-anchor="end">{int(r_max)}</text>
<line class="axis" x1="{L}" x2="{W - R}" y1="{Y2(0):.1f}" y2="{Y2(0):.1f}"/>
{"".join(f'<text class="tick" x="{X(n):.1f}" y="{H2 - 6}" text-anchor="middle">{n}</text>' for n in range(0, n_end + 1, xstep))}
{"".join(bars)}
<polyline class="bar-model" points="{rate_pts}"/>
</svg>
</div>
<div class="prog-legend">
 <span class="lg-actual">New concepts per video</span>
 <span class="lg-model">Model rate (K/&tau;)&middot;e<sup>&minus;n/&tau;</sup></span>
</div>"""

    flags = Counter(concept_flag(c) for c in concepts.values())
    total_words = sum(_words(c) for c in concepts.values())
    avg_words = total_words / max(1, len(concepts))
    WPM = 230
    done_slugs = get_done_slugs() or set()
    unread_words = sum(_words(c) for sl, c in concepts.items() if sl not in done_slugs)
    unfound_words = avg_words * m["remaining"]

    def _hm(words):
        mins = words / WPM
        return f"{int(mins // 60)}h {int(mins % 60):02d}m" if mins >= 60 else f"{int(round(mins))} min"
    wk1 = f"~{m['days_to_lt1'] / 7:.0f} wk" if m["days_to_lt1"] is not None else "&mdash;"
    wk05 = f"~{m['days_to_lt05'] / 7:.0f} wk" if m["days_to_lt05"] is not None else "&mdash;"
    stats = f"""
<div class="prog-stats">
 <div class="prog-stat"><span class="n">{m['total']}</span><span class="l">concepts so far</span></div>
 <div class="prog-stat"><span class="n">~{K}</span><span class="l">estimated ceiling</span></div>
 <div class="prog-stat"><span class="n">~{m['remaining']}</span><span class="l">left to find</span></div>
 <div class="prog-stat"><span class="n">{m['rate_now']:.1f}</span><span class="l">new per video right now</span></div>
 <div class="prog-stat"><span class="n">{m['videos_to_lt1']}</span><span class="l">videos until &lt;1 new/video ({wk1})</span></div>
 <div class="prog-stat"><span class="n">{m['videos_to_lt05']}</span><span class="l">videos until it's a trickle ({wk05})</span></div>
</div>
<div class="prog-stats">
 <div class="prog-stat"><span class="n">{_hm(unread_words)}</span><span class="l">to read what's written and not yet completed ({len(concepts) - len([s for s in done_slugs if s in concepts])} concepts)</span></div>
 <div class="prog-stat"><span class="n">~{_hm(unfound_words)}</span><span class="l">more for the ~{m['remaining']} concepts still to be found</span></div>
 <div class="prog-stat"><span class="n">~{_hm(unread_words + unfound_words)}</span><span class="l">total reading left, at {WPM} wpm &middot; ~{avg_words:.0f} words/concept</span></div>
</div>"""

    n_lt1 = m["n_now"] + m["videos_to_lt1"]
    body = f"""
<h1>Is it running out?</h1>
<p class="subtitle">{m['n_now']} videos &middot; {m['per_day']:.1f} videos/day
 &middot; {flags.get('star', 0)} &#9733; must-know &middot; {flags.get('plain', 0)} standard
 &middot; {flags.get('deep', 0)} deep cuts &middot; refit on every rebuild</p>
{stats}
<h2 id="curve">Concepts found vs. videos watched</h2>
{chart}
<h2 id="rate">New concepts per video</h2>
{chart2}
<h2 id="equation">The equation</h2>
<div class="prog-eq">
 total(n) = K &middot; (1 &minus; e<sup>&minus;n/&tau;</sup>)
 <span class="sub">n = videos processed &middot; K = {K} (ceiling) &middot; &tau; = {tau} videos
 &middot; fitted by least squares to the {m['n_now']} points above</span>
</div>
<p>Finance has a big but finite vocabulary, and this channel draws from one
bag of it. Picture a bag of K marbles: every video grabs a handful, but
only the ones you don't already own count as new. Early on nearly every
grab is new; later almost every grab is a repeat. That produces a curve
that climbs fast and flattens toward K, and the formula above is the
standard shape for it. &tau; ("tau") is how many videos it takes to burn
through about 63% of the bag.</p>
<p>The bot refits K and &tau; every time it rebuilds this page: it tries
every plausible pair and keeps the one whose curve sits closest to the real
dots. Everything else falls out of those two numbers. The rate of new
concepts at video n is (K/&tau;)&middot;e<sup>&minus;n/&tau;</sup>, which is
{m['rate_now']:.1f} today; it drops below one per video at video
{n_lt1}. At the channel's pace of {m['per_day']:.1f} videos a day, that
is roughly {wk1} away.</p>
<p class="prog-note">Caveats: this is one channel's vocabulary fitted with two
parameters, so treat it as a trend line, not a promise. If the presenter
starts a new topic series the ceiling moves up. The tail is mostly deep
cuts, so the must-know material will feel finished a week or two before
the bot literally goes quiet. When a few weeks pass with nothing new
starred or standard, the goal is met &mdash; turn on "Hide deep cuts",
finish what's left, and go read books.</p>
<h2 id="table">The data</h2>
<table class="prog-table" role="presentation">
<tr><th>#</th><th>Date</th><th>New</th><th>Total</th><th>Model</th></tr>
{"".join(f"<tr><td>{n}</td><td>{ts[:10]}</td><td>{new}</td><td>{t}</td><td>{K * (1 - math.exp(-n / tau)):.0f}</td></tr>" for (n, t), (ts, new) in zip(m['cum'], m['series']))}
</table>
<script>
(function(){{
  var c=document.getElementById('progChart'), tip=document.getElementById('progTip');
  if(!c||!tip) return;
  c.querySelectorAll('.hit').forEach(function(h){{
    h.addEventListener('mousemove',function(e){{
      var r=c.getBoundingClientRect();
      tip.innerHTML=h.getAttribute('data-tip');
      tip.style.display='block';
      tip.style.left=Math.min(e.clientX-r.left+12, r.width-tip.offsetWidth-4)+'px';
      tip.style.top=(e.clientY-r.top-tip.offsetHeight-8)+'px';
    }});
    h.addEventListener('mouseleave',function(){{ tip.style.display='none'; }});
  }});
}})();
</script>"""
    return body


def rebuild_html(concepts):
    """Rebuild the site: index (tiers -> categories) -> category pages ->
    one page per concept, plus recent.html.  Layout follows the Master
    Reading List outline; filing decided at extraction time."""
    processed = load_json(PROCESSED_FILE)
    videos_done = sum(1 for v in processed.values()
                      if not v.get("skipped") and not v.get("retry"))
    video_titles = {k: v.get("title", k) for k, v in processed.items()}

    by_cat = {n: [] for n in CATEGORY_NAMES}
    for slug, c in concepts.items():
        by_cat[concept_category(c)].append((slug, c))

    total = len(concepts)
    written = set()

    # ---- index: tiers -> category cards ----
    tiers_html = []
    for t in OUTLINE:
        cards, empty = [], []
        for cat in t["cats"]:
            items = by_cat[cat["name"]]
            if not items:
                empty.append(cat["name"])
                continue
            slugs = ",".join(sl for sl, _ in items)
            flags = ",".join(concept_flag(c) for _, c in items)
            words = ",".join(str(_words(c)) for _, c in items)
            stars = sum(1 for _, c in items if concept_flag(c) == "star")
            cards.append(
                f'<a class="cat-card" href="{cat["slug"]}.html"'
                f' data-slugs="{slugs}" data-flags="{flags}" data-words="{words}" data-stars="{stars}">'
                f'<span class="cat-name">{_esc(cat["name"])}</span>'
                f'<span class="cat-count">{len(items)} concepts &middot; {stars} &#9733;</span></a>'
            )
        if not cards:
            cards.append('<p class="tier-empty">No concepts filed here yet.</p>')
        tiers_html.append(
            f'<div class="tier"><h2>{_esc(t["name"])}</h2>'
            f'<p class="tier-desc">{_esc(t["desc"])}</p>'
            f'{"".join(cards)}</div>'
        )

    recent = _recent_concepts(concepts)
    vid_tab = _videos_this_week_html(processed, concepts)
    prog = _progress_model(processed, concepts)
    body = f"""
<h1>Finance Guide</h1>
<p class="subtitle">A living book &middot; {total} concepts
 &middot; {videos_done} videos &middot;
 <a href="recent.html" style="color:#a08060">Added this week ({len(recent)})</a></p>
{_progress_teaser(prog)}
{vid_tab}
{FILTER_BAR}
{"".join(tiers_html)}"""
    HTML_FILE.write_text(_page_wrap("Finance Guide", body, css_path="../book.css",
                                    bm_key="finance_guide", extra_js=PAGE_JS))
    written.add(HTML_FILE)

    # ---- category pages ----
    for name, cat in CATEGORIES.items():
        items = by_cat[name]
        if not items:
            continue
        body = f"""
<h1>{_esc(name)}</h1>
<p class="subtitle">{_esc(cat["tier_name"])} &middot; {len(items)} concepts</p>
{FILTER_BAR}
{_concept_rows(items, "concepts/")}
<p class="fg-hidden-note" id="fgHiddenNote"></p>"""
        path = BASE_DIR / f"{cat['slug']}.html"
        path.write_text(_page_wrap(name, body, css_path="../book.css",
                                   back_href="index.html", back_label="Finance Guide",
                                   bm_key=f"fg_{cat['slug']}", extra_js=PAGE_JS))
        written.add(path)

    # ---- recent page ----
    body = f"""
<h1>Added this week</h1>
<p class="subtitle">{len(recent)} concepts, newest first</p>
{FILTER_BAR}
{_concept_rows(recent, "concepts/")}
<p class="fg-hidden-note" id="fgHiddenNote"></p>"""
    path = BASE_DIR / "recent.html"
    path.write_text(_page_wrap("Added this week", body, css_path="../book.css",
                               back_href="index.html", back_label="Finance Guide",
                               bm_key="fg_recent", extra_js=PAGE_JS))
    written.add(path)

    # ---- progress page: saturation fit, "is it running out?" ----
    if prog:
        path = BASE_DIR / "progress.html"
        path.write_text(_page_wrap("Is it running out?", _progress_html(prog, concepts),
                                   css_path="../book.css", back_href="index.html",
                                   back_label="Finance Guide", bm_key="fg_progress",
                                   extra_js=PAGE_JS))
        written.add(path)

    # ---- one page per concept ----
    cdir = BASE_DIR / "concepts"
    cdir.mkdir(exist_ok=True)
    for slug, c in concepts.items():
        cat_name = concept_category(c)
        cat = CATEGORIES[cat_name]
        flag = concept_flag(c)
        flag_html = ('<span><span class="star">&#9733;</span> must-know</span>' if flag == "star"
                     else "<span>deep cut</span>" if flag == "deep" else "<span>standard</span>")
        chapter = c.get("chapter_html") or (
            f'<h4 id="{slug}">{_esc(c["title"])}</h4><p>{_esc(c.get("summary", ""))}</p>')
        related = [(sl, x) for sl, x in by_cat[cat_name] if sl != slug][:6]
        side_parts = []
        if c.get("aliases"):
            side_parts.append("Also called: " + _esc(", ".join(c["aliases"])))
        if related:
            side_parts.append("Related in this category: "
                              + ", ".join(f'<a href="{sl}.html">{_esc(x["title"])}</a>' for sl, x in related))
        side = "<br>".join(side_parts)
        body = f"""
<div class="concept-meta">{flag_html}<span>{_esc(cat_name)}</span><span>added {c.get("added", "")}</span></div>
{chapter}
{f'<div class="concept-side">{side}</div>' if side else ""}
<button class="concept-done" data-slug="{slug}" onclick="toggleDone('{slug}')">&#x2713; Mark complete</button>"""
        path = cdir / f"{slug}.html"
        path.write_text(_page_wrap(c["title"], body, css_path="../../book.css",
                                   back_href=f"../{cat['slug']}.html", back_label=cat_name,
                                   bm_key=f"fg_c_{slug}", extra_js=PAGE_JS))
        written.add(path)

    # ---- remove pages the bot owns but no longer generates ----
    owned = {BASE_DIR / f"{c['slug']}.html" for c in CATEGORIES.values()}
    owned.add(BASE_DIR / "recent.html")
    owned.add(BASE_DIR / "progress.html")
    for stale in list(owned) + list(cdir.glob("*.html")):
        if stale.exists() and stale not in written:
            stale.unlink()
            log(f"  Removed stale page: {stale.relative_to(BASE_DIR)}")
    for ydir in BASE_DIR.glob("[12][0-9][0-9][0-9]"):
        if ydir.is_dir():
            for f in ydir.glob("*.html"):
                f.unlink()
            try:
                ydir.rmdir()
                log(f"  Removed old layout dir: {ydir.name}/")
            except OSError:
                pass

    log(f"  HTML rebuilt: {total} concepts, "
        f"{sum(1 for v in by_cat.values() if v)} categories, "
        f"{len(recent)} added this week")


def _recent_concepts(concepts, days=7):
    if not concepts:
        return []
    latest = max(c.get("added", "2026-01-01") for c in concepts.values())
    cutoff = (datetime.strptime(latest, "%Y-%m-%d") - timedelta(days=days - 1)).strftime("%Y-%m-%d")
    items = [(s, c) for s, c in concepts.items() if c.get("added", "") >= cutoff]
    return sorted(items, key=lambda x: x[1].get("added", ""), reverse=True)


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
    """Single check-and-process cycle.

    Returns "ok" if the cycle completed cleanly (including "nothing new"),
    "waiting" if it was clean but a new video has no captions yet (worth a
    look again in an hour), or "failed" if something broke and is worth
    retrying soon rather than in 6 hours: the channel check, a transcript
    fetch, a Claude call.
    """
    log("=== Finance Guide check ===")

    # Find new videos
    new_videos, ok = find_new_videos()
    if not new_videos:
        log("  No new videos found" if ok else "  Channel check failed")
        return "ok" if ok else "failed"
    waiting = False

    log(f"  Processing {len(new_videos)} new videos")

    concepts = load_json(CONCEPTS_FILE)
    processed = load_json(PROCESSED_FILE)
    new_concept_count = 0
    videos_done = 0

    for video in new_videos:
        vid_id = video["id"]
        title = video["title"]
        channel = video.get("channel", "unknown")
        log(f"  Video: {title}")

        # Download transcript
        try:
            transcript = download_transcript(vid_id)
        except NetworkError as e:
            log(f"    Network error fetching transcript ({e}) — will retry soon")
            ok = False
            continue
        if not transcript:
            # Captions often appear a few hours after upload — leave the
            # video unprocessed so it is retried, but give up after a while.
            attempts = processed.get(vid_id, {}).get("no_transcript_attempts", 0) + 1
            if attempts >= 4:
                log(f"    Skipped (no transcript after {attempts} tries)")
                processed[vid_id] = {
                    "title": title, "channel": channel,
                    "processed": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "concepts_extracted": 0, "skipped": "no_transcript",
                }
            else:
                log(f"    No transcript yet (attempt {attempts}), will retry")
                entry = processed.get(vid_id, {"title": title, "channel": channel})
                entry["no_transcript_attempts"] = attempts
                entry["retry"] = True
                processed[vid_id] = entry
                waiting = True
            save_json(PROCESSED_FILE, processed)
            continue

        log(f"    Transcript: {len(transcript)} chars")

        # Extract concepts — None means the call failed; leave the video
        # unprocessed so the next cycle retries it.
        result = extract_concepts(vid_id, title, transcript, concepts)
        if result is None:
            log(f"    Extraction FAILED — will retry soon")
            ok = False
            continue
        new_concepts = result["new"]
        log(f"    Extracted: {len(new_concepts)} candidates, "
            f"{len(result['existing'])} existing mentioned")

        # Record this video as a source on existing concepts it discussed
        for slug in result["existing"]:
            src = concepts[slug].setdefault("sources", [])
            if vid_id not in src:
                src.append(vid_id)
        if result["existing"]:
            save_json(CONCEPTS_FILE, concepts)

        # Write chapters for each new concept
        failed = 0
        merged = 0
        for concept in new_concepts:
            slug = concept["slug"]
            if slug in concepts:
                log(f"    Skip (exists): {concept['title']}")
                merge_into(slug, concept["title"], vid_id, concepts)
                save_json(CONCEPTS_FILE, concepts)
                continue

            # Dedup layers: fuzzy title match, then LLM judge
            verdict, match = resolve_candidate(concept, concepts)
            if verdict is None:
                failed += 1
                continue
            if verdict in ("dup", "instance"):
                # Instances and dups are recorded as a source/alias only.
                # Existing chapters are never rewritten or appended to:
                # the guide is read once, concept by concept, then put away.
                merge_into(match, concept["title"], vid_id, concepts)
                save_json(CONCEPTS_FILE, concepts)
                merged += 1
                continue
            log(f"    Writing: {concept['title']}")
            chapter_html = write_chapter(concept, title, transcript)

            if chapter_html:
                concepts[slug] = {
                    "title": concept["title"],
                    "category": concept["category"],
                    "flag": concept.get("flag", "plain"),
                    "summary": concept["summary"],
                    "context": concept.get("context", ""),
                    "sources": [vid_id],
                    "added": datetime.now().strftime("%Y-%m-%d"),
                    "chapter_html": chapter_html,
                }
                new_concept_count += 1
                # Save after each concept (crash safety)
                save_json(CONCEPTS_FILE, concepts)
            else:
                failed += 1

        if failed:
            # Concepts that did get written are saved and will be skipped
            # next time; the video stays queued (retry) so the rest get
            # retried.  Record it as partial so "Videos this week" lists it
            # alongside the concepts it already added to the guide.
            log(f"    {failed} chapter(s) failed — video left for retry")
            entry = processed.get(vid_id, {})
            entry.update({
                "title": title,
                "channel": channel,
                "processed": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "retry": True,
                "partial": True,
            })
            processed[vid_id] = entry
            save_json(PROCESSED_FILE, processed)
            ok = False
            continue

        # Mark video as processed.  Health metric: over time a channel's
        # videos should show fewer "new" and more "existing"/"merged".
        processed[vid_id] = {
            "title": title,
            "channel": channel,
            "processed": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "concepts_extracted": len(new_concepts) - merged,
            "merged_duplicates": merged,
            "existing_mentioned": len(result["existing"]),
        }
        save_json(PROCESSED_FILE, processed)
        videos_done += 1

    if videos_done > 0 or new_concept_count > 0:
        log(f"  Videos completed: {videos_done}, "
            f"new concepts: {new_concept_count}")
        rebuild_html(concepts)
        git_push()
    else:
        log("  Nothing completed this cycle")

    log("=== Done ===\n")
    return "failed" if not ok else ("waiting" if waiting else "ok")


# === LOCK ===
# An OS-level advisory lock (flock) instead of a PID file.  The kernel
# releases it the instant the holding process dies — kill -9, reboot,
# power loss, anything — so it can never go stale.  The old PID-file
# scheme left .bot.lock behind on any non-Ctrl-C exit, and on the next
# start `os.kill(pid, 0)` would either find an unrelated process that had
# reused the PID ("already running", exit) or hit a root-owned one and
# crash with PermissionError.  Either way the bot silently never started.
LOCK_FILE = BASE_DIR / ".bot.lock"


def acquire_lock():
    """Return an open file handle holding the lock, or None if another
    instance holds it.  Keep the handle alive for the life of the process."""
    fh = open(LOCK_FILE, "a+")
    try:
        fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except (BlockingIOError, OSError):
        fh.close()
        return None
    fh.seek(0)
    fh.truncate()
    fh.write(str(os.getpid()))   # informational only — not used for checks
    fh.flush()
    return fh


def lock_holder_pid():
    """PID of the running bot, or None if no instance holds the lock."""
    if not LOCK_FILE.exists():
        return None
    with open(LOCK_FILE, "r") as fh:
        try:
            fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except (BlockingIOError, OSError):
            try:
                return int(fh.read().strip() or 0) or "?"
            except ValueError:
                return "?"
        fcntl.flock(fh, fcntl.LOCK_UN)
    return None


def status():
    """Answer 'is the bot alive and what did it last do?' in one screen."""
    pid = lock_holder_pid()
    print(f"Bot running:      {'yes (PID ' + str(pid) + ')' if pid else 'NO'}")

    try:
        v = subprocess.run(["yt-dlp", "--version"], capture_output=True,
                           text=True, timeout=15).stdout.strip()
    except Exception as e:
        v = f"NOT FOUND ({e})"
    print(f"yt-dlp version:   {v}")
    print(f"Network:          {'up' if network_up() else 'DOWN (cannot reach youtube.com)'}")

    processed = load_json(PROCESSED_FILE)
    done = sorted(((v.get("processed", ""), k, v) for k, v in processed.items()
                   if not v.get("skipped")), reverse=True)
    if done:
        ts, vid, v = done[0]
        print(f"Last video done:  {ts}  {vid}  {v.get('title', '')[:60]}")
    pending = [k for k, v in processed.items() if v.get("retry")]
    if pending:
        print(f"Awaiting caption: {len(pending)} video(s) queued for retry")

    if LOG_FILE.exists():
        lines = LOG_FILE.read_text().splitlines()
        checks = [l for l in lines if "Finance Guide check" in l]
        if checks:
            print(f"Last check:       {checks[-1][1:20]}")
        errs = [l for l in lines[-400:] if "ERROR" in l or "WARNING" in l]
        if errs:
            print(f"Recent errors:    {len(errs)} in last 400 log lines")
        print("\n--- last 15 log lines ---")
        print("\n".join(lines[-15:]))
    else:
        print(f"No log file at {LOG_FILE}")


def main():
    lock = acquire_lock()
    if lock is None:
        log(f"Bot already running (PID {lock_holder_pid()}). Exiting.")
        sys.exit(1)

    # `kill <pid>` sends SIGTERM, which Python ignores by default — the
    # loop would only stop on Ctrl-C.  Turn it into a clean exit so the
    # log records the stop and launchd/nohup restarts behave predictably.
    def _stop(signum, frame):
        log(f"Received signal {signum} — stopping")
        sys.exit(0)
    signal.signal(signal.SIGTERM, _stop)
    signal.signal(signal.SIGHUP, _stop)

    log(f"Finance Guide Bot starting (PID {os.getpid()})")
    log(f"Check interval: {CHECK_INTERVAL // 3600}h, plus a check on every wake from sleep")
    log(f"Channels: {CHANNELS_FILE}")

    failures = 0
    try:
        while True:
            # At login and right after wake, Wi-Fi is usually still
            # reconnecting.  Wait for it; a check into a dead network is
            # worse than no check because it used to reset the 6h timer.
            outcome = "failed"
            if wait_for_network():
                try:
                    outcome = run_once()
                except Exception:
                    # Full traceback, not just the message — a one-line
                    # "ERROR in run_once: 'x'" is undebuggable a day later.
                    log("ERROR in run_once:\n" + traceback.format_exc())
            if outcome == "failed":
                failures += 1
                delay = min(RETRY_INTERVAL * 2 ** (failures - 1), CHECK_INTERVAL)
                log(f"Check did not complete — retrying in {delay // 60} min")
            else:
                failures = 0
                if outcome == "waiting":
                    delay = CAPTION_RETRY
                    log(f"New video has no captions yet — checking again in {delay // 60} min")
                else:
                    delay = CHECK_INTERVAL
            next_run = time.time() + delay
            log(f"Next check at {time.strftime('%H:%M', time.localtime(next_run))} "
                f"(or on wake)")
            # Sleep in short intervals.  If a single 60s nap takes much
            # longer than 60s of wall-clock time, the machine was asleep:
            # the lid was closed and just reopened.  Check right away so
            # "open the laptop" == "look for new videos".
            last_tick = time.time()
            while time.time() < next_run:
                time.sleep(60)
                now = time.time()
                if now - last_tick > WAKE_GAP:
                    log(f"Woke from sleep ({int(now - last_tick) // 60} min "
                        f"gap) — checking now")
                    break
                last_tick = now
    finally:
        log("Finance Guide Bot stopped")
        lock.close()   # releases the flock


if __name__ == "__main__":
    if "--status" in sys.argv:
        status()
    elif "--once" in sys.argv:
        lock = acquire_lock()
        if lock is None:
            print(f"Bot is already running (PID {lock_holder_pid()}); "
                  f"it will pick up new videos on its next check or on wake. "
                  f"To force one now: launchctl kickstart -k gui/$(id -u)/com.a.financeguide")
            sys.exit(1)
        try:
            run_once()
        finally:
            lock.close()
    else:
        try:
            main()
        except SystemExit:
            raise
        except Exception:
            # Startup crashes used to go only to nohup.out, where nobody
            # looks.  Put them in the real log too.
            log("FATAL at startup:\n" + traceback.format_exc())
            raise
