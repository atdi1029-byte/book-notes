// "% read" counts what was read: words on screen, at reading speed. A jump to
// another part of the book, flicking through pages or a quick look ahead adds
// next to nothing; reading adds what was read; progress saved before this
// rule existed is kept as it was.
//   node progress_test.js
const fs = require('fs');
const path = require('path');
const { start } = require('./server');
const { launch, newPage, waitFor, check, sleep, failures } = require('./lib');

const ROOT = process.env.BOOKS_ROOT || path.resolve(__dirname, '..');
const PORT = 8796;
const RS_KEY = 'reading_speed_data';
const BOOK = 'Economics_101/index.html';
// The reader's clock ticks once a second. The tests run it 20× faster, so a
// "second" of reading takes 50 ms and a page is read in a second or two.
const TICK = 50;
const secs = n => sleep(n * TICK);
const WORDS_A_SEC = 500 / 60;
// Word positions on screen can shift by a word or two when the page's layout
// moves (the bar at the top appears 3 s after the page loads).
const near = (a, b) => Math.abs(a - b) <= 3;

// One function's source out of book.js (braces balanced).
function source(name) {
  const src = fs.readFileSync(path.join(ROOT, 'book.js'), 'utf8');
  const i = src.indexOf('function ' + name + '(');
  if (i < 0) throw new Error(name + ' not found in book.js');
  let depth = 0;
  for (let k = src.indexOf('{', i); k < src.length; k++) {
    if (src[k] === '{') depth++;
    else if (src[k] === '}' && --depth === 0) return src.slice(i, k + 1);
  }
  throw new Error('unbalanced ' + name);
}

function helpers() {
  console.log('Read ranges (the functions in book.js)');
  const names = ['rangesClean', 'rangesTotal', 'rangesNextUnread', 'rangesFill', 'rangesTrim', 'readRanges', 'settleRead'];
  const f = new Function(names.map(source).join('\n') + '\nreturn {' + names.join(',') + '};')();
  const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);

  check('clean: in order, overlaps and touching stretches joined, junk dropped',
    same(f.rangesClean([300, 400, 0, 100, 100, 200, 350, 500, 7, 7, 'x', 3, -5, 2]), [0, 200, 300, 500]),
    f.rangesClean([300, 400, 0, 100, 100, 200, 350, 500, 7, 7, 'x', 3, -5, 2]));
  check('clean: nothing past the end of the book', same(f.rangesClean([0, 50, 90, 400], 100), [0, 50, 90, 100]));
  check('total', f.rangesTotal([0, 200, 300, 500]) === 400);
  check('next unread word', f.rangesNextUnread([0, 200, 300, 500], 150) === 200 &&
    f.rangesNextUnread([0, 200, 300, 500], 250) === 250 && f.rangesNextUnread([0, 200, 300, 500], 300) === 500 &&
    f.rangesNextUnread([], 42) === 42);
  check('fill: an old count becomes "read from the start"', same(f.rangesFill([], 6000, 16549), [0, 6000]));
  check('fill: extra words go into the first gap', same(f.rangesFill([0, 4000], 1000, 16549), [0, 5000]) &&
    same(f.rangesFill([5000, 6000], 3000, 16549), [0, 3000, 5000, 6000]) &&
    same(f.rangesFill([100, 200, 300, 400], 250, 1000), [0, 450]));
  check('fill: never past the end', same(f.rangesFill([0, 90], 50, 100), [0, 100]));
  check('trim: the shortest stretches go, never the one being read',
    same(f.rangesTrim([0, 10, 20, 25, 40, 100, 200, 203], 2, 203), [40, 100, 200, 203]),
    f.rangesTrim([0, 10, 20, 25, 40, 100, 200, 203], 2, 203));
  check('a record from before ranges: read from the start', same(f.readRanges({ maxWordsRead: 6000 }, 16549), [0, 6000]));
  check('a count higher than its ranges is topped up from the start',
    same(f.readRanges({ maxWordsRead: 5000, ranges: [0, 4000] }, 16549), [0, 5000]));
  check('a count is never more than the book', same(f.readRanges({ maxWordsRead: 99999 }, 16549), [0, 16549]));
  const rec = { maxWordsRead: 100, ranges: [0, 4000] };
  check('ranges longer than the count raise the count', f.settleRead(rec, 16549) === 4000 && rec.maxWordsRead === 4000, rec);
  const keep = { maxWordsRead: 7615 };
  check('settling an old record keeps its count', f.settleRead(keep, 16549) === 7615 && keep.maxWordsRead === 7615 &&
    same(keep.ranges, [0, 7615]), keep);
}

async function pages() {
  const srv = await start(PORT);
  const B = srv.base;
  const browser = await launch();

  // What the page counts as read. (Works on the old book.js too, which has no
  // _rsState: BOOKS_ROOT=/old/checkout node progress_test.js shows the first
  // scenario failing there.)
  const st = page => page.evaluate((key, book) => {
    const eta = document.querySelector('.reading-eta');
    const label = eta ? eta.textContent : '';
    if (window._rsState) return window._rsState();
    const rec = ((JSON.parse(localStorage.getItem(key) || '{}').books) || {})[book] || {};
    return { total: rec.words || 0, read: rec.maxWordsRead || 0, ranges: rec.ranges || [], label };
  }, RS_KEY, BOOK);
  // Has the reader had time to read everything on screen? (The front: how far
  // down the screen reading can have got. A stop that adds under 20 new words
  // is not counted yet, so the ranges alone can't answer this.)
  const screenCounted = page => page.evaluate(() => {
    const s = window._rsState();
    return s.front >= s.bottom;
  });
  const readScreen = page => waitFor(() => screenCounted(page), { label: 'screen read', every: TICK, timeout: 20000 });
  const pageDown = page => page.evaluate(() => scrollBy(0, innerHeight * 0.85));
  // Put word number `w` at the top of the screen.
  const scrollToWord = (page, w) => page.evaluate(w => {
    let lo = 0, hi = document.documentElement.scrollHeight - innerHeight;
    while (lo < hi) {
      const mid = (lo + hi) >> 1;
      scrollTo(0, mid);
      if (window._rsState().top < w) lo = mid + 1; else hi = mid;
    }
    scrollTo(0, lo);
  }, w);
  const open = async (page, rel) => {
    await page.goto(B + (rel || BOOK), { waitUntil: 'load' });
    await waitFor(() => page.evaluate(() => {
      const e = document.querySelector('.reading-eta');
      return !!e && e.textContent !== '';
    }), { label: 'reader started', every: TICK });
  };
  const seedLocal = async (page, rec) => {
    await page.goto(B + 'manifest.json');
    await page.evaluate((k, b, r) => localStorage.setItem(k, JSON.stringify({ books: { [b]: r }, sessions: [] })), RS_KEY, BOOK, rec);
  };
  const seedServer = rec => srv.gas.call({ action: 'set_bookmark', key: RS_KEY, data: JSON.stringify({ books: { [BOOK]: rec } }) });

  // Each scenario gets a fresh "device" (own storage) and a fresh backend.
  const scenario = async (name, fn) => {
    console.log(name);
    // Let the last scenario's requests land before the backend is wiped, or a
    // late one (a Reset, say) ends up in this scenario's backend.
    await sleep(300);
    await fetch(B + '__reset');
    const ctx = await browser.createBrowserContext();
    const page = await newPage(ctx);
    await page.setViewport({ width: 800, height: 700 });
    await page.evaluateOnNewDocument(tick => {
      const real = window.setInterval;
      window.setInterval = (fn, ms, ...rest) => real(fn, ms === 1000 ? tick : ms, ...rest);
      // No offline library here: saving 500 pages in the background would
      // only slow the clock down.
      delete Navigator.prototype.serviceWorker;
    }, TICK);
    try {
      await fn(page);
      check('no page errors', page.errors.length === 0, page.errors);
    } catch (e) { check('ran to the end', false, e.message); }
    await ctx.close();
  };

  await scenario('A jump to the end of the book is not reading', async page => {
    await open(page);
    await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
    await secs(5);
    // The old book.js only shows its count in storage, saved 2 s after a scroll.
    if (!(await page.evaluate(() => !!window._rsState))) await sleep(3200);
    const s = await st(page);
    check('5 s at the end of a ' + s.total + '-word book: under 150 words counted', s.read < 150, s.read);
    check('it does not say "Reading complete"', !/complete/i.test(s.label), s.label);
  });

  await scenario('Reading page after page counts those pages', async page => {
    await open(page);
    for (let i = 0; i < 4; i++) { await readScreen(page); await pageDown(page); }
    await readScreen(page);
    let s = await st(page);
    // A screen counts once it has been left behind, not while it is still up.
    check('everything above the screen is counted: one unbroken stretch from the first word',
      s.ranges.length === 2 && s.ranges[0] === 0 && near(s.ranges[1], s.top), s);
    check('the count is the length of that stretch', s.read === s.ranges[1] && s.read > 200, s);
    check('the bar says the same', s.label.startsWith(Math.round(s.read / s.total * 100) + '% read'), s.label);
    await page.evaluate(() => window.dispatchEvent(new Event('pagehide')));
    s = await st(page);
    check('putting the book away counts the screen that was being read', s.ranges.length === 2 &&
      s.ranges[0] === 0 && near(s.ranges[1], s.bottom) && s.read === s.ranges[1], s);
    const saved = await page.evaluate((k, b) => JSON.parse(localStorage.getItem(k)).books[b], RS_KEY, BOOK);
    check('saved for the shelf as the number of words read', saved.maxWordsRead === s.read &&
      JSON.stringify(saved.ranges) === JSON.stringify(s.ranges), saved);
  });

  await scenario('Sitting on one screen does not move the count (or the time left)', async page => {
    const T = Date.now() - 3600000;
    await seedLocal(page, { words: 30000, maxWordsRead: 3000, maxScroll: 0.25, title: 'Economics 101', updatedAt: T });
    await open(page);
    await scrollToWord(page, 2950);
    await secs(3);
    const first = await st(page);
    await readScreen(page);
    await secs(20);
    const later = await st(page);
    check('same count after 20 s more on the same screen', later.read === 3000 && first.read === 3000, [first.read, later.read]);
    check('same time left', later.label === first.label, [first.label, later.label]);
  });

  await scenario('Flicking through pages counts next to nothing', async page => {
    await open(page);
    const before = (await st(page)).read;
    let passed = 0;
    for (let i = 0; i < 12; i++) {
      const s = await st(page);
      passed += Math.round((s.bottom - s.top) * 0.85);
      await pageDown(page);
      await secs(1.5);
    }
    const s = await st(page);
    check('12 pages (' + passed + ' words) at about 2 s a page: under a tenth of them counted (' + (s.read - before) + ')',
      s.read - before < passed * 0.1, s.read - before);
  });

  await scenario('Skimming faster than anyone reads is counted at reading speed', async page => {
    await open(page);
    await readScreen(page);
    const before = (await st(page)).read;
    let passed = 0;
    const t0 = Date.now();
    for (let i = 0; i < 10; i++) {
      const s = await st(page);
      passed += Math.round((s.bottom - s.top) * 0.85);
      await pageDown(page);
      await secs(6);
    }
    const ticks = (Date.now() - t0) / TICK;
    const got = (await st(page)).read - before;
    // ~6 s a page is well over 2,000 words a minute; 500 a minute is the most that counts.
    check('10 pages (' + passed + ' words) at 6 s a page: some counted, far from all (' + got + ')',
      got > 100 && got < passed * 0.6 && got <= ticks * WORDS_A_SEC + 200, { got, passed, ticks: Math.round(ticks) });
  });

  await scenario('A look ahead, then back: only the reading counts', async page => {
    await open(page);
    await readScreen(page); await pageDown(page); await readScreen(page);
    const here = await st(page); // on the second screen, read to its bottom
    const y = await page.evaluate(() => scrollY);
    await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight * 0.8));
    await secs(2);
    await page.evaluate(y => scrollTo(0, y), y);
    await secs(3);
    let s = await st(page);
    check('a 2 s look at a later chapter adds nothing: the two screens read are what counts',
      s.ranges.length === 2 && s.ranges[0] === 0 && near(s.ranges[1], here.bottom) && s.read === s.ranges[1], s);
    const base = s.read;
    await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight * 0.8));
    await secs(8);
    await page.evaluate(y => scrollTo(0, y), y);
    await secs(3);
    s = await st(page);
    const added = s.read - base;
    check('8 s there adds what 8 s of reading can cover, as its own stretch (' + added + ' words)',
      added >= 20 && added <= 140 && s.ranges.length === 4 && near(s.ranges[1], here.bottom), s);
    // Read on until a screen has been left behind that goes past where the
    // reading had got to (the first screens are mostly the contents box).
    for (let i = 0; i < 8 && (await st(page)).top <= here.bottom + 3; i++) { await pageDown(page); await readScreen(page); }
    await secs(2);
    s = await st(page);
    check('reading on from where you were still joins up', s.ranges.length === 4 && s.ranges[0] === 0 &&
      near(s.ranges[1], s.top) && s.ranges[1] > here.bottom + 3, s);
  });

  await scenario('Progress saved before this rule is kept as it was', async page => {
    const T = Date.now() - 3600000;
    await seedLocal(page, { words: 30000, maxWordsRead: 3000, maxScroll: 0.25, title: 'Economics 101', updatedAt: T });
    await open(page);
    let s = await st(page);
    check('3,000 words read stays 3,000, as "read from the start"',
      s.read === 3000 && JSON.stringify(s.ranges) === '[0,3000]', s);
    check('same % as before', s.label.startsWith(Math.round(3000 / s.total * 100) + '% read'), s.label);
    await scrollToWord(page, 2950);
    await readScreen(page);
    await pageDown(page);
    await waitFor(() => st(page).then(x => x.read > 3000), { label: 'count moved', every: TICK, timeout: 10000 });
    s = await st(page);
    check('reading on from there extends it', s.ranges.length === 2 && s.ranges[0] === 0 &&
      near(s.ranges[1], s.top) && s.read === s.ranges[1], s);
  });

  await scenario('Reset clears it', async page => {
    await seedLocal(page, { words: 30000, maxWordsRead: 3000, ranges: [0, 2000, 5000, 6000], updatedAt: Date.now() - 3600000 });
    await open(page);
    await scrollToWord(page, 4000);
    const after = await page.evaluate(() => { document.querySelector('.bm-reset').click(); return window._rsState(); });
    check('nothing counted as read after Reset', after.read === 0 && after.ranges.length === 0, after);
    const saved = await page.evaluate((k, b) => JSON.parse(localStorage.getItem(k)).books[b], RS_KEY, BOOK);
    check('saved that way, with the reset time', saved.maxWordsRead === 0 && saved.ranges.length === 0 && saved.resetAt > 0, saved);
  });

  await scenario('What another device read is added to what this one read', async page => {
    const T = Date.now() - 60000;
    seedServer({ maxWordsRead: 1000, ranges: [3000, 4000], title: 'Economics 101', updatedAt: T });
    await seedLocal(page, { maxWordsRead: 1500, ranges: [0, 1500], title: 'Economics 101', updatedAt: T - 100000 });
    await open(page);
    await waitFor(() => st(page).then(s => s.ranges.length === 4), { label: 'merge', timeout: 10000 });
    const s = await st(page);
    check('both stretches kept: 2,500 words', JSON.stringify(s.ranges) === '[0,1500,3000,4000]' && s.read === 2500, s);
  });

  await scenario('Another device still on the old book.js (a count, no ranges)', async page => {
    const T = Date.now() - 60000;
    seedServer({ maxWordsRead: 2000, maxScroll: 0.2, title: 'Economics 101', updatedAt: T });
    await seedLocal(page, { maxWordsRead: 500, ranges: [3000, 3500], title: 'Economics 101', updatedAt: T - 100000 });
    await open(page);
    await waitFor(() => st(page).then(s => s.ranges.length === 4), { label: 'merge', timeout: 10000 });
    const s = await st(page);
    check('its 2,000 words count from the start, next to this device\'s own',
      JSON.stringify(s.ranges) === '[0,2000,3000,3500]' && s.read === 2500, s);
  });

  await scenario('A reset on another device clears this one too', async page => {
    const T = Date.now() - 60000;
    seedServer({ maxWordsRead: 0, maxScroll: 0, ranges: [], title: 'Economics 101', updatedAt: T, resetAt: T });
    await seedLocal(page, { maxWordsRead: 500, ranges: [3000, 3500], title: 'Economics 101', updatedAt: T - 100000 });
    await open(page);
    await waitFor(() => st(page).then(s => !s.ranges.includes(3000)), { label: 'merge', timeout: 10000 });
    const s = await st(page);
    check('the old stretch is gone', !s.ranges.includes(3500) && s.read < 300, s);
  });

  await scenario('A page with closed <details> (Italian guide): positions make sense', async page => {
    await open(page, 'italian-guide/index.html');
    const pts = await page.evaluate(() => {
      const out = [];
      const h = document.documentElement.scrollHeight - innerHeight;
      for (let i = 0; i <= 20; i++) {
        scrollTo(0, Math.round(h * i / 20));
        const s = window._rsState();
        out.push([s.top, s.bottom, s.total]);
      }
      return out;
    });
    const total = pts[0][2];
    const ordered = pts.every((p, i) => p[0] <= p[1] && p[1] <= total && (i === 0 || p[0] >= pts[i - 1][0]));
    check('the word at the top of the screen only grows as the page scrolls down', ordered, pts.map(p => p[0]));
    check('starts at the first word and ends at the last', pts[0][0] === 0 && pts[20][1] === total, [pts[0], pts[20]]);
    check('a screen never holds more than a tenth of the book', pts.every(p => p[1] - p[0] < total / 10),
      pts.map(p => p[1] - p[0]));
  });

  await browser.cleanup();
  await srv.close();
}

(async () => {
  try { helpers(); } catch (e) { check('helpers', false, e.stack); }
  await pages();
  console.log(failures() ? `\n${failures()} FAILED` : '\nALL PASSED');
  process.exit(failures() ? 1 : 0);
})();
