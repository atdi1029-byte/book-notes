#!/usr/bin/env python3
"""
Finance Guide Bot — pulls YouTube transcripts, extracts finance concepts,
builds a living book on the Books shelf.

Preferred: run under launchd so it starts at login and is restarted if it
dies (see install_launchd.sh).  Manual: nohup python3 finance_guide.py &
Checks channels every 6 hours for new videos.

  python3 finance_guide.py --status   # is it alive? what did it last do?
  python3 finance_guide.py --once     # one check-and-process cycle, then exit
"""

import fcntl
import json
import os
import re
import signal
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


# === STEP 1: Pull new video IDs from channels ===
def get_channel_videos(channel_url, limit=30):
    """Pull recent video IDs and titles from a YouTube channel."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "--print", "id", "--print", "title",
             "--playlist-end", str(limit), channel_url],
            capture_output=True, text=True, timeout=120
        )
    except FileNotFoundError:
        log("  ERROR yt-dlp not found on PATH — install it or fix the PATH "
            "block at the top of this script")
        return []
    except Exception as e:
        log(f"  ERROR pulling channel: {e}")
        return []

    # yt-dlp breaks whenever YouTube changes its page layout.  It exits
    # non-zero and prints the reason to stderr; treat that as a real error,
    # not "the channel has no videos".
    if result.returncode != 0:
        log(f"  ERROR yt-dlp exit {result.returncode}: "
            f"{(result.stderr or '').strip()[-300:]}")
        log("  -> try: pip3 install -U yt-dlp   (or: brew upgrade yt-dlp)")
        return []

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
    return videos


def _needs_processing(vid_id, processed):
    entry = processed.get(vid_id)
    return entry is None or entry.get("retry", False)


def find_new_videos():
    """Check all channels, return videos not yet processed.

    First run for a channel: marks all existing videos as processed
    (backlog skip) so only future uploads get picked up.
    """
    channels = load_json(CHANNELS_FILE)
    if isinstance(channels, dict):
        channels = []
    processed = load_json(PROCESSED_FILE)
    seen_channels = load_json(BASE_DIR / "seen_channels.json")

    new_videos = []
    for channel in channels:
        log(f"  Checking: {channel['name']}")
        videos = get_channel_videos(channel["url"])

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

    return new_videos if MAX_VIDEOS_PER_RUN == 0 else new_videos[:MAX_VIDEOS_PER_RUN]


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
    """
    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", model],
            capture_output=True, text=True, timeout=timeout
        )
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
- "instance": the candidate is a specific example, application, or narrower framing of an
  existing entry (e.g. "Diesel Cost Pass-Through" is an instance of "Cost Pass-Through";
  "China Reducing Treasury Holdings" is an instance of "Foreign Treasury Holdings").
- "new": a genuinely distinct concept that deserves its own glossary entry.

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
    or (None, None) on judge failure."""
    dup = find_fuzzy_duplicate(candidate["title"], concepts)
    if dup:
        return "dup", dup
    verdict = judge_duplicate(candidate, concepts)
    if verdict is None:
        return None, None
    if verdict["verdict"] in ("same", "instance"):
        return "dup", verdict["match_slug"]
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
- Do NOT create a new concept for a specific instance, example, or framing of an
  existing one. Prefer the general mechanism ("Cost Pass-Through") over the
  instance ("Diesel Cost Pass-Through to Freight").
- Be specific where the distinction matters: "Credit Default Swaps" not "derivatives".
- Slugs: lowercase, underscores, no filler words.
- If the video substantively discusses a concept already covered, put its EXACT slug
  (as written in the list) in "existing" — do not re-extract it.
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
        f' data-slug="{slug}" data-flag="{concept_flag(c)}">'
        f'{_mark(concept_flag(c))}'
        f'<span class="ctitle">{_esc(c["title"])}</span></a>'
        for slug, c in items
    )


def rebuild_html(concepts):
    """Rebuild the site: index (tiers -> categories) -> category pages ->
    one page per concept, plus recent.html.  Layout follows the Master
    Reading List outline; filing decided at extraction time."""
    processed = load_json(PROCESSED_FILE)
    videos_done = sum(1 for v in processed.values() if not v.get("skipped"))
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
            stars = sum(1 for _, c in items if concept_flag(c) == "star")
            cards.append(
                f'<a class="cat-card" href="{cat["slug"]}.html"'
                f' data-slugs="{slugs}" data-flags="{flags}" data-stars="{stars}">'
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
    body = f"""
<h1>Finance Guide</h1>
<p class="subtitle">A living book &middot; {total} concepts
 &middot; {videos_done} videos &middot;
 <a href="recent.html" style="color:#a08060">Added this week ({len(recent)})</a></p>
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
        srcs = "; ".join(_esc(video_titles.get(v, v)) for v in c.get("sources", []))
        related = [(sl, x) for sl, x in by_cat[cat_name] if sl != slug][:6]
        side = f"Sources: {srcs}"
        if c.get("aliases"):
            side += "<br>Also called: " + _esc(", ".join(c["aliases"]))
        if related:
            side += ("<br>Related in this category: "
                     + ", ".join(f'<a href="{sl}.html">{_esc(x["title"])}</a>' for sl, x in related))
        body = f"""
<div class="concept-meta">{flag_html}<span>{_esc(cat_name)}</span><span>added {c.get("added", "")}</span></div>
{chapter}
<div class="concept-side">{side}</div>
<button class="concept-done" data-slug="{slug}" onclick="toggleDone('{slug}')">&#x2713; Mark complete</button>"""
        path = cdir / f"{slug}.html"
        path.write_text(_page_wrap(c["title"], body, css_path="../../book.css",
                                   back_href=f"../{cat['slug']}.html", back_label=cat_name,
                                   bm_key=f"fg_c_{slug}", extra_js=PAGE_JS))
        written.add(path)

    # ---- remove pages the bot owns but no longer generates ----
    owned = {BASE_DIR / f"{c['slug']}.html" for c in CATEGORIES.values()}
    owned.add(BASE_DIR / "recent.html")
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
    videos_done = 0

    for video in new_videos:
        vid_id = video["id"]
        title = video["title"]
        channel = video.get("channel", "unknown")
        log(f"  Video: {title}")

        # Download transcript
        transcript = download_transcript(vid_id)
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
            save_json(PROCESSED_FILE, processed)
            continue

        log(f"    Transcript: {len(transcript)} chars")

        # Extract concepts — None means the call failed; leave the video
        # unprocessed so the next cycle retries it.
        result = extract_concepts(vid_id, title, transcript, concepts)
        if result is None:
            log(f"    Extraction FAILED — will retry next cycle")
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
            status, match = resolve_candidate(concept, concepts)
            if status is None:
                failed += 1
                continue
            if status == "dup":
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
            # next time; the video stays unprocessed so the rest get retried.
            log(f"    {failed} chapter(s) failed — video left for retry")
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

    try:
        while True:
            try:
                run_once()
            except Exception:
                # Full traceback, not just the message — a one-line
                # "ERROR in run_once: 'x'" is undebuggable a day later.
                log("ERROR in run_once:\n" + traceback.format_exc())
            next_run = time.time() + CHECK_INTERVAL
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
