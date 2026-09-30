const fs = require('fs');
const os = require('os');
const path = require('path');
const http = require('http');
const puppeteer = require('puppeteer-core');

const sleep = ms => new Promise(r => setTimeout(r, ms));

// Tests run Chrome for Testing, never the Chrome app. macOS sends AppleScript for
// "Google Chrome" to the newest running copy of that app, so even a headless test
// copy takes over the outreach night run's Chrome commands (it stopped the
// Sep 30 2026 night). Chrome for Testing is a separate app, so it can't.
// Install once: npx @puppeteer/browsers install chrome@stable --path ~/.cache/puppeteer
function chromeBin() {
  let bin = process.env.CHROME || '';
  if (!bin) {
    const root = path.join(os.homedir(), '.cache', 'puppeteer', 'chrome');
    const ver = d => (d.split('-')[1] || '').split('.').map(Number);
    const newer = (a, b) => {
      const x = ver(a), y = ver(b);
      for (let i = 0; i < 4; i++) if ((x[i] || 0) !== (y[i] || 0)) return (y[i] || 0) - (x[i] || 0);
      return 0;
    };
    const builds = fs.existsSync(root) ? fs.readdirSync(root).filter(d => d.startsWith('mac')).sort(newer) : [];
    for (const d of builds) {
      for (const sub of ['chrome-mac-arm64', 'chrome-mac-x64']) {
        const p = path.join(root, d, sub, 'Google Chrome for Testing.app', 'Contents', 'MacOS', 'Google Chrome for Testing');
        if (!bin && fs.existsSync(p)) bin = p;
      }
    }
  }
  if (!bin) {
    throw new Error('Chrome for Testing is not installed. Run: npx @puppeteer/browsers install chrome@stable --path ~/.cache/puppeteer');
  }
  if (bin.includes('/Google Chrome.app/')) {
    throw new Error(`${bin} is the Chrome app; a test copy of it takes the night run's AppleScript. Use Chrome for Testing.`);
  }
  return bin;
}

// Every host except localhost is unreachable, so nothing in a test can ever
// touch the real Apps Script backend or your reading data.
async function launch() {
  const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'book-notes-test-'));
  const browser = await puppeteer.launch({
    executablePath: chromeBin(),
    headless: true,
    userDataDir: profile,
    args: ['--no-first-run', '--no-default-browser-check',
      '--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE localhost'],
  });
  browser.cleanup = async () => {
    await browser.close();
    fs.rmSync(profile, { recursive: true, force: true });
  };
  return browser;
}

// A page that records uncaught errors
async function newPage(browserOrContext) {
  const page = await browserOrContext.newPage();
  page.errors = [];
  page.on('pageerror', e => page.errors.push(e.message));
  page.on('dialog', d => d.accept());
  return page;
}

function get(url) {
  return new Promise((resolve, reject) => {
    http.get(url, res => { let b = ''; res.on('data', d => (b += d)); res.on('end', () => resolve(b)); }).on('error', reject);
  });
}

// Ask the service worker for its status (see service-worker.js "status")
function swStatus(page) {
  return page.evaluate(() => new Promise(resolve => {
    const onMsg = e => {
      if (e.data && e.data.type === 'offline-status') {
        navigator.serviceWorker.removeEventListener('message', onMsg);
        resolve(e.data);
      }
    };
    navigator.serviceWorker.addEventListener('message', onMsg);
    navigator.serviceWorker.ready.then(r => r.active.postMessage({ type: 'status' }));
  }));
}

async function waitFor(fn, { timeout = 30000, every = 250, label = 'condition' } = {}) {
  const t0 = Date.now();
  let last;
  while (Date.now() - t0 < timeout) {
    last = await fn();
    if (last) return last;
    await sleep(every);
  }
  throw new Error('timed out waiting for ' + label);
}

let failures = 0;
function check(name, ok, detail) {
  console.log((ok ? '  PASS ' : '  FAIL ') + name +
    (ok || detail === undefined ? '' : '  → ' + (typeof detail === 'string' ? detail : JSON.stringify(detail))));
  if (!ok) failures++;
  return ok;
}

module.exports = { launch, newPage, get, swStatus, waitFor, check, sleep, failures: () => failures };
