// Sync behaviour: the merge rules, the backend, and the shelf/book pages
// talking to a local copy of the backend.
//   node sync_test.js
const fs = require('fs');
const path = require('path');
const { start } = require('./server');
const { loadGas } = require('./gas_harness');
const { launch, newPage, get, waitFor, check, sleep, failures } = require('./lib');

const ROOT = process.env.BOOKS_ROOT || path.resolve(__dirname, '..');
const PORT = 8793;
const RS_KEY = 'reading_speed_data';

// Pull one function's source out of a file (braces balanced).
function extractFunction(file, name) {
  const src = fs.readFileSync(path.join(ROOT, file), 'utf8');
  const i = src.indexOf('function ' + name + '(');
  if (i < 0) throw new Error(name + ' not found in ' + file);
  let depth = 0, j = src.indexOf('{', i);
  for (let k = j; k < src.length; k++) {
    if (src[k] === '{') depth++;
    else if (src[k] === '}' && --depth === 0) return new Function('return ' + src.slice(i, k + 1))();
  }
  throw new Error('unbalanced ' + name);
}

function mergeRules() {
  console.log('Merge rules are identical in book.js, index.html and apps_script.gs');
  const merges = [
    extractFunction('book.js', 'mergeProgress'),
    extractFunction('index.html', 'mergeProgress'),
    extractFunction('apps_script.gs', 'mergeProgress_'),
  ];
  const readers = [
    extractFunction('book.js', 'readerIsNewer'),
    extractFunction('index.html', 'readerIsNewer'),
    extractFunction('apps_script.gs', 'readerIsNewer_'),
  ];
  const pick = arr => arr[Math.floor(Math.random() * arr.length)];
  const rec = () => {
    const r = {};
    if (Math.random() < 0.9) r.words = pick([0, 12000, 30000]);
    if (Math.random() < 0.8) r.maxWordsRead = pick([0, 500, 6000, 24000]);
    if (Math.random() < 0.9) r.maxScroll = pick([0, 0.2, 0.8, 1]);
    if (Math.random() < 0.7) r.updatedAt = pick([1000, 2000, 3000, 4000]);
    if (Math.random() < 0.3) r.resetAt = pick([1500, 2500, 3500]);
    r.title = pick(['A', 'B']);
    return r;
  };
  const model = () => ({ averageWPM: pick([60, 123, 150, 225, 600]), samples: pick([0, 1, 30, 43]), updatedAt: pick([0, 1000, 2000]) });
  let same = true, sameR = true;
  for (let n = 0; n < 5000; n++) {
    const a = Math.random() < 0.05 ? null : rec(), b = rec();
    const out = merges.map(f => JSON.stringify(f(a && { ...a }, { ...b })));
    if (out[0] !== out[1] || out[0] !== out[2]) { same = false; console.log(a, b, out); break; }
    const x = model(), y = Math.random() < 0.1 ? null : model();
    const r = readers.map(f => f(x, y));
    if (r[0] !== r[1] || r[0] !== r[2]) { sameR = false; console.log(x, y, r); break; }
  }
  check('mergeProgress: same result everywhere (5000 random cases)', same);
  check('readerIsNewer: same result everywhere', sameR);

  const m = merges[0], newer = readers[0];
  const p = (mw, upd, reset) => ({ words: 30000, maxWordsRead: mw, maxScroll: mw / 30000, updatedAt: upd, ...(reset ? { resetAt: reset } : {}) });
  check('progress never goes backwards', m(p(24000, 1000), p(7000, 2000)).maxWordsRead === 24000);
  check('…but keeps the newest timestamp', m(p(24000, 1000), p(7000, 2000)).updatedAt === 2000);
  check('a newer reset wins', m(p(24000, 1000), p(0, 3000, 3000)).maxWordsRead === 0);
  check('reading after a reset on another device is kept', m(p(8000, 1000), p(500, 4000, 3000)).maxWordsRead === 500);
  check('an older reset loses to later reading', m(p(8200, 5000), p(500, 4000, 3000)).maxWordsRead === 8200);
  const real = { averageWPM: 123, samples: 43, updatedAt: 1000 };
  check('a new device\'s default model never replaces the real one', !newer({ averageWPM: 225, samples: 0, updatedAt: 0 }, real));
  check('a 1-session model (even newer) never replaces 43 sessions', !newer({ averageWPM: 112, samples: 1, updatedAt: 9999 }, real));
  check('more sessions wins', newer({ averageWPM: 130, samples: 44, updatedAt: 500 }, real));
  check('an out-of-range model never wins', !newer({ averageWPM: 71, samples: 99, updatedAt: 9999 }, real));
  check('a valid model replaces a corrupt one', newer(real, { averageWPM: 71, samples: 99, updatedAt: 9999 }));
}

function backend() {
  console.log('Backend (apps_script.gs in Node)');
  const gas = loadGas(path.join(ROOT, 'apps_script.gs'));
  const put = obj => gas.call({ action: 'set_bookmark', key: RS_KEY, data: JSON.stringify(obj) });
  const book = () => gas.call({ action: 'get_bookmarks' }).bookmarks[RS_KEY].books['Antifragile/index.html'];
  const reader = () => gas.call({ action: 'get_bookmarks' }).bookmarks[RS_KEY].reader;
  put({ books: { 'Antifragile/index.html': { words: 30000, maxWordsRead: 24000, maxScroll: 0.8, updatedAt: 1000 } }, reader: { averageWPM: 123, samples: 43, updatedAt: 1000 } });
  put({ books: { 'Antifragile/index.html': { words: 30000, maxWordsRead: 7000, maxScroll: 0.23, updatedAt: 2000 } } });
  check('an older position sent later does not overwrite 80%', book().maxWordsRead === 24000, book());
  put({ books: { 'Antifragile/index.html': { words: 30000, maxWordsRead: 0, maxScroll: 0, updatedAt: 3000, resetAt: 3000 } } });
  check('a reset still goes through', book().maxWordsRead === 0, book());
  put({ reader: { averageWPM: 225, samples: 0, updatedAt: 0 } });
  put({ reader: { averageWPM: 112, samples: 1, updatedAt: 5000 } });
  check('default / 1-session models don\'t replace the real one', reader().averageWPM === 123, reader());
  put({ reader: { averageWPM: 130, samples: 44, updatedAt: 6000 } });
  check('a model with more sessions does', reader().averageWPM === 130, reader());
  check('ping reports v3', gas.call({ action: 'ping' }).version === 3);
}

async function pages() {
  const srv = await start(PORT);
  const B = srv.base;
  const browser = await launch();
  const serverRead = () => srv.gas.call({ action: 'get_read' }).books_read;
  // Each scenario gets a fresh "device" (own storage); a crash fails only it.
  const scenario = async (name, fn) => {
    console.log(name);
    const ctx = await browser.createBrowserContext();
    const page = await newPage(ctx);
    try { await fn(page); } catch (e) { check('ran to the end', false, e.message); }
    await get(B + '__offline?on=0');
    await ctx.close();
  };

  await scenario('Shelf: a book marked read offline stays read', async page => {
    await page.goto(B + 'index.html');
    await waitFor(() => page.evaluate(() => syncReady === true && !!navigator.serviceWorker.controller),
      { label: 'shelf sync + service worker' });
    const id = await page.evaluate(() => document.querySelector('#shelfView .book').dataset.book);
    await get(B + '__offline?on=1');
    await page.evaluate(i => document.querySelector('.book[data-book="' + i + '"] .mark-read').click(), id);
    const local = await page.evaluate(i => ({
      read: !!JSON.parse(localStorage.getItem('books_read'))[i],
      pending: !!JSON.parse(localStorage.getItem('books_pending_writes') || '{}')['read:' + i],
    }), id);
    check('saved locally and queued', local.read && local.pending, local);
    await page.reload();
    await sleep(1000);
    check('still read after an offline reload', await page.evaluate(i => !!JSON.parse(localStorage.getItem('books_read'))[i] &&
      document.querySelector('.book[data-book="' + i + '"] .read-badge').classList.contains('show'), id));
    await get(B + '__offline?on=0');
    await page.evaluate(() => syncFromBackend());
    await waitFor(() => page.evaluate(() => Object.keys(JSON.parse(localStorage.getItem('books_pending_writes') || '{}')).length === 0),
      { label: 'queue drained' });
    await sleep(500);
    check('reaches the server once back online', !!serverRead()[id], serverRead());
    check('and is still read on this device', await page.evaluate(i => !!JSON.parse(localStorage.getItem('books_read'))[i], id));
    check('no page errors', page.errors.length === 0, page.errors);
  });

  await scenario('Shelf: a mark made before the first sync finishes is kept', async page => {
    await get(B + '__delay?action=get_read&ms=3000');
    // Don't wait for "load": the pending sync requests hold it back.
    await page.goto(B + 'index.html', { waitUntil: 'domcontentloaded' });
    check('clicked while the first sync is still running', await page.evaluate(() => syncReady === false));
    const id = await page.evaluate(() => document.querySelectorAll('#shelfView .book')[3].dataset.book);
    await page.evaluate(i => document.querySelector('.book[data-book="' + i + '"] .mark-read').click(), id);
    await sleep(6000);
    check('kept on this device', await page.evaluate(i => !!JSON.parse(localStorage.getItem('books_read'))[i], id));
    check('and sent to the server', !!serverRead()[id]);
  });

  await scenario('Book page: progress from another device, slow backend', async page => {
    const T = Date.now() - 60000;
    srv.gas.call({ action: 'set_bookmark', key: RS_KEY, data: JSON.stringify({
      books: { 'Antifragile/index.html': { words: 30000, maxWordsRead: 24000, maxScroll: 0.8, title: 'Antifragile', updatedAt: T } },
      reader: { averageWPM: 150, samples: 30, updatedAt: T },
    }) });
    await page.goto(B + 'manifest.json');
    await page.evaluate((k, t) => localStorage.setItem(k, JSON.stringify({
      books: { 'Antifragile/index.html': { words: 30000, maxWordsRead: 6000, maxScroll: 0.2, title: 'Antifragile', updatedAt: t } },
      sessions: [],
    })), RS_KEY, T - 100000);
    await get(B + '__delay?action=get_bookmarks&ms=5000');
    await page.goto(B + 'Antifragile/index.html');
    await sleep(8000);
    const rs = await page.evaluate(k => JSON.parse(localStorage.getItem(k)), RS_KEY);
    const rec = rs.books['Antifragile/index.html'];
    check('slow reply (5 s) still merged: 80% adopted', rec.maxWordsRead === 24000, rec);
    check('the real reading-speed model adopted, not the 225 default', rs.reader && rs.reader.averageWPM === 150, rs.reader);
    const srvRs = srv.gas.call({ action: 'get_bookmarks' }).bookmarks[RS_KEY];
    check('server still has 80% and the real model',
      srvRs.books['Antifragile/index.html'].maxWordsRead === 24000 && srvRs.reader.averageWPM === 150, srvRs);
    check('no page errors', page.errors.length === 0, page.errors);
  });

  await scenario('Glossary tooltips', async page => {
    const gloss = async rel => {
      await page.goto(B + rel);
      return page.evaluate(() => {
        const spans = [...document.querySelectorAll('.gloss')];
        return {
          spans: spans.length,
          terms: new Set(spans.map(s => s.dataset.term)).size,
          emoji: spans.some(s => /\u{1F516}/u.test(s.dataset.def + s.dataset.term)),
          // underlines inside the glossary section itself
          inGlossary: spans.some(s => {
            for (let e = s.closest('p, li, ul'); e; e = e.previousElementSibling) {
              if (e.tagName === 'H2') return e.id === 'glossary';
            }
            return false;
          }),
          termList: [...new Set(spans.map(s => s.dataset.term))].slice(0, 60),
        };
      });
    };
    let g = await gloss('Economics_101/index.html');
    check('Economics 101 (list glossary): terms linked', g.spans > 20 && g.terms > 10, g.spans + ' spans, ' + g.terms + ' terms');
    check('Economics 101: no 🔖 in terms/definitions', !g.emoji);
    check('Economics 101: glossary itself not underlined', !g.inGlossary);
    g = await gloss('Trading_Options_Greeks/index.html');
    check('Trading Option Greeks (several terms per paragraph): many terms', g.terms >= 10, g.terms + ' terms');
    g = await gloss('The_Prize/index.html');
    check('The Prize: bold names inside definitions are not terms', !g.termList.includes('Henri Deterding'), g.termList);
    check('The Prize: no 🔖, glossary itself not underlined', !g.emoji && !g.inGlossary, g);
    g = await gloss('A_History_of_Interest_Rates/index.html');
    check('A History of Interest Rates (<section> glossary): terms linked', g.terms > 5, g.terms);
    check('no page errors', page.errors.length === 0, page.errors);
  });

  await scenario('Economics 101 bookmarks', async page => {
    await page.goto(B + 'Economics_101/index.html');
    const maxPerH2 = await page.evaluate(() =>
      Math.max(...[...document.querySelectorAll('h2[id]')].map(h => h.querySelectorAll('.bm-btn').length)));
    check('one bookmark icon per heading', maxPerH2 === 1, maxPerH2);
    await page.evaluate(() => document.querySelector('#glossary .bm-btn').click());
    await sleep(300);
    check('tapping it saves a bookmark without errors', page.errors.length === 0 &&
      await page.evaluate(() => !!localStorage.getItem(BM_KEY)), page.errors);
  });

  await browser.cleanup();
  await srv.close();
}

(async () => {
  try { mergeRules(); } catch (e) { check('merge rules', false, e.message); }
  try { backend(); } catch (e) { check('backend', false, e.message); }
  await pages();
  console.log(failures() ? `\n${failures()} FAILED` : '\nALL PASSED');
  process.exit(failures() ? 1 : 0);
})();
