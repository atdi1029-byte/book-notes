// Every page linked from the shelf loads without a JavaScript error.
//   node pages_test.js
const { start } = require('./server');
const { launch, newPage, check, failures } = require('./lib');

(async () => {
  const srv = await start(8794);
  const B = srv.base;
  const browser = await launch();
  try {
    const page = await newPage(browser);
    await page.goto(B + 'index.html');
    const links = await page.evaluate(() =>
      [...new Set([...document.querySelectorAll('a[href$=".html"]')]
        .map(a => a.getAttribute('href')).filter(h => !/^https?:/.test(h)))]);
    console.log(links.length + ' pages');
    const bad = [];
    let glossPages = 0;
    for (const rel of links) {
      page.errors.length = 0;
      await page.goto(B + rel, { waitUntil: 'load', timeout: 30000 }).catch(e => page.errors.push(e.message));
      const info = await page.evaluate(() => ({
        gloss: document.querySelectorAll('.gloss').length,
        hasGlossary: !!document.getElementById('glossary'),
      })).catch(() => ({}));
      if (info.hasGlossary && info.gloss > 0) glossPages++;
      if (page.errors.length) bad.push(rel + ': ' + page.errors.join(' | '));
    }
    check('no JavaScript errors on any page', bad.length === 0, bad.slice(0, 10));
    console.log('  pages with working glossary tooltips: ' + glossPages);
  } catch (e) {
    check('test run', false, e.stack);
  } finally {
    await browser.cleanup();
    await srv.close();
  }
  console.log(failures() ? `\n${failures()} FAILED` : '\nALL PASSED');
  process.exit(failures() ? 1 : 0);
})();
