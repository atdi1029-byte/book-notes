// Plain-English boxes and primers on a book page: boxes start closed, open on
// tap, a bookmark inside one reopens it, and reading progress ignores the help.
//   node help_test.js
const { start } = require('./server');
const { launch, newPage, check, sleep, failures } = require('./lib');

(async () => {
  const srv = await start(8795);
  const URL = srv.base + 'tests/Plain_Help_Fixture/index.html';
  const browser = await launch();
  try {
    const page = await newPage(browser);
    await page.setViewport({ width: 800, height: 700 });
    await page.goto(URL, { waitUntil: 'load' });
    await sleep(500);

    const closed = await page.evaluate(() => ({
      open: [...document.querySelectorAll('details.plain-help')].map(d => d.open),
      helpVisible: document.getElementById('help1').checkVisibility(),
      primerVisible: document.getElementById('primer1').checkVisibility(),
    }));
    check('plain-English boxes start closed', closed.open.every(o => !o) && !closed.helpVisible, closed);
    check('primers are open', closed.primerVisible, closed);

    await page.click('details.plain-help summary');
    const opened = await page.evaluate(() => document.querySelector('details.plain-help').open &&
      document.getElementById('help1').checkVisibility());
    check('tapping "Plain English" opens the box', opened);

    // Bookmark a help paragraph, reload: the box opens and the page goes there.
    await page.evaluate(() => setBookmark(document.getElementById('help2')));
    await sleep(300);
    await page.goto(URL, { waitUntil: 'load' });
    await sleep(1500);
    const back = await page.evaluate(() => {
      const el = document.getElementById('help2');
      const r = el.getBoundingClientRect();
      return { open: el.closest('details').open, top: Math.round(r.top), h: innerHeight };
    });
    check('a bookmark inside a closed box reopens it on load', back.open && back.top >= -5 && back.top < back.h, back);
    await page.evaluate(() => { document.querySelectorAll('details').forEach(d => (d.open = false)); scrollTo(0, 0); });
    await page.evaluate(() => jumpToBookmark());
    await sleep(1200);
    const jumped = await page.evaluate(() => document.getElementById('help2').closest('details').open);
    check('the Resume bar reopens the box too', jumped);

    // Reading progress and time left count the book's own words only.
    const words = await page.evaluate(() => {
      const count = el => (el.textContent || '').split(/\s+/).filter(Boolean).length;
      const body = document.body.cloneNode(true);
      body.querySelectorAll('script, nav, .bm-btn, #bookmarkBar, #bmToast, #progressBar').forEach(e => e.remove());
      const all = count(body);
      body.querySelectorAll('.plain-help, .primer').forEach(e => e.remove());
      const rs = JSON.parse(localStorage.getItem('reading_speed_data') || '{}');
      return { all, book: count(body), tracked: ((rs.books || {})['Plain_Help_Fixture/index.html'] || {}).words };
    });
    // (a few words of page chrome book.js adds may differ; the help is ~360 words)
    check("progress counts the book's words, not the help",
      Math.abs(words.tracked - words.book) <= 10 && words.all - words.tracked > 300, words);

    check('no JavaScript errors', page.errors.length === 0, page.errors);
  } finally {
    await browser.cleanup();
    srv.close();
  }
  console.log(failures() ? `\n${failures()} FAILED` : '\nALL PASSED');
  process.exit(failures() ? 1 : 0);
})();
