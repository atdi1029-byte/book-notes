// Offline library: a fresh device opens the shelf, the service worker saves
// the library, then the connection goes away.
//   node offline_test.js
const { start } = require('./server');
const { launch, newPage, get, swStatus, waitFor, check, sleep, failures } = require('./lib');

const PORT = 8791;

(async () => {
  const srv = await start(PORT);
  const B = srv.base;
  const browser = await launch();
  try {
    console.log('First visit: install + library sync');
    const page = await newPage(browser);
    await page.goto(B + 'index.html');
    await page.evaluate(() => navigator.serviceWorker.ready);
    const t0 = Date.now();
    const st = await waitFor(async () => {
      const s = await swStatus(page);
      return s.lastSync && !s.syncing ? s : null;
    }, { timeout: 10 * 60e3, every: 2000, label: 'library sync' });
    const r = st.lastSync.result;
    console.log(`  synced in ${((Date.now() - t0) / 1000).toFixed(1)}s:`, JSON.stringify(r));
    check('sync finished cleanly', st.lastSync.complete && r.failed === 0, r);
    check('500+ pages saved', st.pages >= 500, st.pages);
    check('images saved (unmetered)', r.images > 800 && !r.imagesSkipped, r);
    check('no errors on the shelf', page.errors.length === 0, page.errors);

    // What every other app on the shared origin does when it updates
    await page.evaluate(async () => {
      const names = await caches.keys();
      await Promise.all(names.map(n => caches.delete(n)));
    });

    console.log('Offline');
    await get(B + '__offline?on=1');
    const offline = async (rel, fn, label) => {
      const resp = await page.goto(B + rel, { waitUntil: 'load', timeout: 15000 }).catch(e => ({ error: e.message }));
      const res = resp && resp.error ? { error: resp.error } : await page.evaluate(fn);
      check(label || rel, res && !res.error && res.ok, res);
      return res;
    };
    await offline('', () => ({ ok: document.querySelectorAll('.book').length >= 170, books: document.querySelectorAll('.book').length }), 'shelf opens (start_url ./)');
    const plain = await page.evaluate(() => {
      const a = document.querySelector('a.book[href$="plain.html"]');
      return a && a.getAttribute('href');
    });
    const h1 = () => { const h = document.querySelector('h1'); return { ok: !!h && h.textContent.trim().length > 3, h1: h && h.textContent.trim().slice(0, 50) }; };
    await offline('Antifragile/index.html', h1);
    await offline(plain, h1, 'plain-English companion ' + plain);
    await offline('FinanceGuide/index.html', () => ({ ok: document.querySelectorAll('a.cat-card').length > 5 }), 'Finance Guide');
    await offline('FinanceGuide/concepts/basis_point.html', () => ({ ok: document.querySelectorAll('p').length > 5 }), 'Finance Guide concept page');
    await offline('How_Not_To_Be_Wrong/index.html', () => {
      const imgs = [...document.images].filter(i => !i.closest('.bm-btn'));
      imgs.forEach(i => i.scrollIntoView());
      return new Promise(res => setTimeout(() => {
        const broken = imgs.filter(i => !i.complete || !i.naturalWidth).map(i => i.getAttribute('src'));
        res({ ok: imgs.length > 5 && broken.length === 0, images: imgs.length, broken });
      }, 1500));
    }, 'book with inline images');
    await offline('web.html', () => new Promise(res => setTimeout(() => {
      const text = document.getElementById('content').innerText;
      res({ ok: /\d+ books/.test(text) && !/Failed to load/.test(text), text: text.slice(0, 80) });
    }, 1500)), 'Book Universe');
    await offline('Antifragile', () => ({ ok: location.pathname.endsWith('/Antifragile/') && !!document.querySelector('h1') }), 'folder URL without trailing slash');
    await offline('no-such-page.html', () => ({ ok: /You're offline/.test(document.body.textContent) }), 'unsaved page → offline notice');
    check('no page errors while offline', page.errors.length === 0, page.errors);

    console.log('Back online: pages are fresh');
    await get(B + '__offline?on=0');
    await get(B + '__patch?path=Antifragile/index.html&marker=FRESH_COPY_1');
    await page.goto(B + 'Antifragile/index.html');
    check('online: newest version shown', (await page.content()).includes('FRESH_COPY_1'));
    await sleep(500);
    await get(B + '__offline?on=1');
    await page.goto(B + 'Antifragile/index.html');
    check('offline: saved copy was refreshed too', (await page.content()).includes('FRESH_COPY_1'));
    await get(B + '__offline?on=0');

    console.log('Slow connection');
    await get(B + '__slow?ms=8000');
    const t1 = Date.now();
    await page.goto(B + 'Antifragile/index.html', { timeout: 20000 });
    const took = Date.now() - t1;
    check('slow network falls back to saved copy (~3s page + ~1s css/js)', took < 6500 && !!(await page.$('h1')), took + 'ms');
    await get(B + '__slow?ms=0');
  } catch (e) {
    check('test run', false, e.stack);
  } finally {
    await browser.cleanup();
    await srv.close();
  }
  console.log(failures() ? `\n${failures()} FAILED` : '\nALL PASSED');
  process.exit(failures() ? 1 : 0);
})();
