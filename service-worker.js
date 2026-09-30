/* Book Notes service worker — keeps the whole library readable offline.

   - Pages, CSS, JS and JSON: network first, so you always get the latest
     version when online. If the network fails, or is too slow (see
     PAGE_TIMEOUT_MS), the saved copy is served instead.
   - Images: served from the saved copy when there is one.
   - Library sync: when a page pings it (shelf and book pages do on load),
     it walks every link on the shelf (books, plain-English companions,
     guides and their pages) and saves anything not on the device yet.
     Images are saved only on Wi-Fi / unmetered connections; on mobile data
     they are saved as you view them.

   Why IndexedDB and not the Cache API: every app on atdi1029-byte.github.io
   shares one origin, and the other apps' service workers delete every cache
   that isn't theirs whenever they update. Anything stored in Cache Storage
   would vanish the next time Cadence, Zercher, etc. shipped.

   Content updates never need a version bump here (pages are fetched fresh
   whenever there is a connection). Bump SW_VERSION only when this file's
   logic changes.

   Kill switch: replace this file with one that calls
   self.registration.unregister() and indexedDB.deleteDatabase(DB_NAME).
*/
'use strict';

const SW_VERSION = 2;
const DB_NAME = 'book-notes-offline';
const SCOPE = new URL('./', self.location).href;   // …/book-notes/
const SHELF = SCOPE + 'index.html';

// Saved at install so the app opens offline even before the first full sync.
const CORE = [
  'index.html', 'book.css', 'book.js', 'bg.jpg', 'icon.png', 'icon-512.png',
  'manifest.json', 'web.html', 'metadata.json'
].map(p => SCOPE + p);

// How long to wait for the network before using the saved copy (only matters
// on a bad connection: with none at all the fallback is immediate).
const PAGE_TIMEOUT_MS = 3000;
const ASSET_TIMEOUT_MS = 1200;   // book.css / book.js, so a slow page isn't twice as slow
const SYNC_EVERY_MS = 12 * 3600e3;            // full library pass at most twice a day
const RETRY_AFTER_MS = 2 * 60e3;              // after a pass that didn't finish
const TEXT_STALE_WIFI_MS = 2 * 86400e3;       // re-download saved pages after 2 days on Wi-Fi,
const TEXT_STALE_METERED_MS = 14 * 86400e3;   // 14 days on mobile data
const MEDIA_STALE_MS = 30 * 86400e3;          // images almost never change
const MAX_DEPTH = 3;                          // shelf → guide → category → concept page
const WORKERS = 4;

const FONT_HOSTS = /^(fonts\.googleapis\.com|fonts\.gstatic\.com)$/;
const TEXT_EXT = /\.(html?|css|js|json|webmanifest|txt)$/i;
const MEDIA_EXT = /\.(png|jpe?g|gif|webp|svg|ico|woff2?|ttf|otf)$/i;
const IMAGE_EXT = /\.(png|jpe?g|gif|webp|svg)$/i;
const ASSET_EXT = /\.(css|js|json)$/i;

// ── IndexedDB ──────────────────────────────────────────────────────────
// files: normalized URL → { body: Blob, type, saved, url }
// meta:  name → value

let dbPromise = null;
function openDb() {
  if (!dbPromise) {
    dbPromise = new Promise((resolve, reject) => {
      const req = indexedDB.open(DB_NAME, 1);
      req.onupgradeneeded = () => {
        req.result.createObjectStore('files');
        req.result.createObjectStore('meta');
      };
      req.onsuccess = () => {
        const db = req.result;
        db.onversionchange = () => { db.close(); dbPromise = null; };
        resolve(db);
      };
      req.onerror = () => { dbPromise = null; reject(req.error); };
      req.onblocked = () => { dbPromise = null; reject(new Error('IndexedDB blocked')); };
    });
  }
  return dbPromise;
}

function tx(store, mode, fn) {
  return openDb().then(db => new Promise((resolve, reject) => {
    const t = db.transaction(store, mode);
    const req = fn(t.objectStore(store));
    t.oncomplete = () => resolve(req ? req.result : undefined);
    t.onerror = t.onabort = () => reject(t.error);
  }));
}

const getFile = key => tx('files', 'readonly', s => s.get(key));
const putFile = (key, entry) => tx('files', 'readwrite', s => s.put(entry, key));
const deleteFile = key => tx('files', 'readwrite', s => s.delete(key));
const fileKeys = () => tx('files', 'readonly', s => s.getAllKeys());
const getMeta = key => tx('meta', 'readonly', s => s.get(key));
const setMeta = (key, value) => tx('meta', 'readwrite', s => s.put(value, key));

// ── Helpers ────────────────────────────────────────────────────────────

// Same-origin: ignore ?v=… cache busters and #hashes, and treat "dir/" as
// "dir/index.html". Cross-origin (fonts): the query is part of the identity.
function keyFor(url) {
  const u = new URL(url, SCOPE);
  u.hash = '';
  if (u.origin === self.location.origin) {
    u.search = '';
    if (u.pathname.endsWith('/')) u.pathname += 'index.html';
  }
  return u.href;
}

const inScope = url => url.startsWith(SCOPE);
const pathOf = key => new URL(key).pathname;
const isHtmlKey = key => /\.html?$/i.test(pathOf(key));
const isTextKey = key => TEXT_EXT.test(pathOf(key));

function unmetered() {
  const c = self.navigator && self.navigator.connection;
  if (!c) return true;
  if (c.saveData) return false;
  return c.type !== 'cellular';
}

function fromEntry(entry) {
  return new Response(entry.body, {
    status: 200,
    headers: { 'Content-Type': entry.type || 'application/octet-stream' }
  });
}

async function save(key, resp) {
  const body = await resp.blob();
  const entry = {
    body,
    type: resp.headers.get('Content-Type') || body.type || '',
    saved: Date.now(),
    url: resp.url || key
  };
  await putFile(key, entry);
  return entry;
}

function offlinePage() {
  const html = `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Offline</title></head>
<body style="margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
background:#f4efe8;color:#3a2e1e;font-family:Georgia,serif;text-align:center;padding:24px">
<div><h1 style="color:#5a3e1a;font-weight:normal">You're offline</h1>
<p>This page hasn't been saved on this device yet.</p>
<p><a href="${SHELF}" style="color:#8b6914">Back to the shelf</a></p></div>
</body></html>`;
  return new Response(html, { status: 503, headers: { 'Content-Type': 'text/html; charset=utf-8' } });
}

// ── Fetch handling ─────────────────────────────────────────────────────

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET' || req.headers.has('range')) return;
  const url = new URL(req.url);

  if (url.origin === self.location.origin) {
    if (!inScope(url.href)) return;
    if (req.mode === 'navigate' || TEXT_EXT.test(url.pathname) || url.pathname.endsWith('/')) {
      event.respondWith(networkFirst(event, req));
    } else if (MEDIA_EXT.test(url.pathname)) {
      event.respondWith(savedFirst(event, req, false));
    }
    return;
  }
  if (FONT_HOSTS.test(url.hostname)) {
    event.respondWith(savedFirst(event, req, true));
  }
  // Everything else (the Apps Script sync, external links) goes straight to
  // the network untouched.
});

function networkFirst(event, req) {
  const key = keyFor(req.url);
  const network = fetch(req);
  // Save every good response (the clone is taken before the page reads it).
  event.waitUntil(network.then(resp => {
    if (resp.ok && resp.type === 'basic') return save(key, resp.clone());
  }).catch(() => {}));

  return new Promise(resolve => {
    let done = false;
    const finish = resp => { if (!done && resp) { done = true; resolve(resp); } };
    const wait = req.mode === 'navigate' ? PAGE_TIMEOUT_MS : ASSET_TIMEOUT_MS;
    const timer = setTimeout(() => lookup(req, key).then(finish), wait);
    network.then(
      resp => { clearTimeout(timer); finish(resp); },
      () => {
        clearTimeout(timer);
        lookup(req, key).then(saved => finish(saved ||
          (req.mode === 'navigate' ? offlinePage() : Response.error())));
      });
  });
}

// The saved copy for a request. For a folder URL without its trailing slash
// ("…/Antifragile"), redirect to the slash form so relative links still work.
async function lookup(req, key) {
  try {
    const entry = await getFile(key);
    if (entry) return fromEntry(entry);
    if (req.mode === 'navigate') {
      const u = new URL(req.url);
      const last = u.pathname.split('/').pop();
      if (last && !last.includes('.') && await getFile(keyFor(u.origin + u.pathname + '/'))) {
        return Response.redirect(u.origin + u.pathname + '/' + u.search + u.hash, 302);
      }
    }
  } catch (e) { /* storage unavailable: behave as if nothing is saved */ }
  return null;
}

async function savedFirst(event, req, crossOrigin) {
  const key = keyFor(req.url);
  let entry = null;
  try { entry = await getFile(key); } catch (e) {}
  const refresh = () =>
    fetch(crossOrigin ? new Request(req.url, { mode: 'cors', credentials: 'omit' }) : req)
      .then(resp => {
        if (resp.ok) event.waitUntil(save(key, resp.clone()).catch(() => {}));
        return resp;
      });
  if (entry) {
    if (Date.now() - entry.saved > MEDIA_STALE_MS && unmetered()) {
      event.waitUntil(refresh().catch(() => {}));
    }
    return fromEntry(entry);
  }
  return refresh().catch(() => Response.error());
}

// ── Library sync ───────────────────────────────────────────────────────

let syncing = null;
let lastResult = null;

function syncLibrary(force) {
  if (syncing) return syncing;
  syncing = (async () => {
    const last = await getMeta('lastSync').catch(() => null);
    if (!force && last) {
      const wait = last.complete ? SYNC_EVERY_MS : RETRY_AFTER_MS;
      if (Date.now() - last.at < wait) return;
    }
    const result = await crawl();
    lastResult = result;
    await setMeta('lastSync', { at: Date.now(), complete: result.complete, result });
  })()
    .catch(err => { lastResult = { error: String(err) }; })
    .finally(() => { syncing = null; broadcast(); });
  return syncing;
}

// Every same-scope link in a page: HTML pages to follow, plus the images and
// CSS/JS/JSON files the page needs.
function extractLinks(html, baseUrl) {
  const pages = [], images = [], assets = [];
  const attr = /\b(href|src|data-fig|data-src|data-full)\s*=\s*["']([^"'<>\s]+)["']/gi;
  let m;
  while ((m = attr.exec(html))) {
    const raw = m[2];
    if (raw.startsWith('#') || /[()+{}]/.test(raw)) continue;   // anchors, pieces of JS strings
    if (/^[a-z][a-z0-9+.-]*:/i.test(raw) && !raw.startsWith(SCOPE)) continue;
    let abs;
    try { abs = new URL(raw, baseUrl).href; } catch (e) { continue; }
    if (!inScope(abs)) continue;
    const path = new URL(abs).pathname;
    if (m[1].toLowerCase() === 'href' && (/\.html?$/i.test(path) || path.endsWith('/'))) {
      pages.push(keyFor(abs));
    } else if (IMAGE_EXT.test(path)) {
      images.push(keyFor(abs));
    } else if (ASSET_EXT.test(path)) {
      assets.push(keyFor(abs));
    }
  }
  return { pages, images, assets };
}

async function crawl() {
  const started = Date.now();
  const wifi = unmetered();
  const staleText = wifi ? TEXT_STALE_WIFI_MS : TEXT_STALE_METERED_MS;
  const seen = new Set();          // everything the library links to
  const images = new Set();
  const queue = CORE.map(url => ({ key: keyFor(url), depth: url === SHELF ? 0 : MAX_DEPTH }));
  let fetched = 0, kept = 0, failed = 0, gone = 0, active = 0;
  let shelfOk = false, quotaFull = false;
  const failures = [];             // the first few, for the status report

  function fail(key, why) {
    failed++;
    if (failures.length < 10) failures.push(pathOf(key).slice(new URL(SCOPE).pathname.length) + ' (' + why + ')');
  }

  // One retry after a dropped connection or a busy server (5xx / 429).
  async function download(key) {
    for (let attempt = 0; ; attempt++) {
      try {
        const resp = await fetch(key, { cache: 'no-cache' });
        if (attempt === 1 || (resp.status < 500 && resp.status !== 429)) return resp;
      } catch (e) {
        if (attempt === 1) throw e;
      }
      await new Promise(r => setTimeout(r, 1500));
    }
  }

  // Make sure `key` is saved and fresh enough. Returns the saved entry (the
  // old one if the download failed) or null.
  async function ensure(key, always, staleMs) {
    let entry = null;
    try { entry = await getFile(key); } catch (e) {}
    if (entry && !always && Date.now() - entry.saved < staleMs) { kept++; return entry; }
    if (quotaFull) return entry;
    try {
      const resp = await download(key);
      if (resp.status === 404 || resp.status === 410) { gone++; return entry; }
      if (!resp.ok) { if (!entry) fail(key, 'HTTP ' + resp.status); return entry; }
      const saved = await save(key, resp);
      fetched++;
      return saved;
    } catch (e) {
      if (e && e.name === 'QuotaExceededError') quotaFull = true;
      if (!entry) fail(key, (e && e.name) || 'error');
      return entry;
    }
  }

  async function pageWorker() {
    for (;;) {
      if (!queue.length) {
        if (active === 0) return;
        await new Promise(r => setTimeout(r, 50));
        continue;
      }
      const item = queue.shift();
      if (seen.has(item.key)) continue;
      seen.add(item.key);
      active++;
      try {
        const isShelf = item.key === SHELF;
        const entry = await ensure(item.key, isShelf, staleText);
        if (isShelf && entry) shelfOk = true;
        if (!entry) continue;
        if (item.key.endsWith('/metadata.json')) {
          // Book Universe loads metadata/<id>.json lazily; save them all.
          const data = JSON.parse(await entry.body.text());
          (data.books || []).forEach(b => {
            if (b && b.id) queue.push({ key: keyFor(SCOPE + 'metadata/' + b.id + '.json'), depth: MAX_DEPTH });
          });
          continue;
        }
        if (!isHtmlKey(item.key)) continue;
        const links = extractLinks(await entry.body.text(), item.key);
        links.images.forEach(k => images.add(k));
        links.assets.forEach(k => { if (!seen.has(k)) queue.push({ key: k, depth: MAX_DEPTH }); });
        if (item.depth < MAX_DEPTH) {
          links.pages.forEach(k => { if (!seen.has(k)) queue.push({ key: k, depth: item.depth + 1 }); });
        }
      } catch (e) {
        fail(item.key, 'unreadable');
      } finally {
        active--;
      }
    }
  }

  // Pages first (the queue grows as pages are parsed), then images.
  await Promise.all(Array.from({ length: WORKERS }, pageWorker));
  const imageList = [...images].filter(k => !seen.has(k));
  imageList.forEach(k => seen.add(k));
  if (wifi) {
    let i = 0;
    await Promise.all(Array.from({ length: WORKERS }, async () => {
      while (i < imageList.length) await ensure(imageList[i++], false, MEDIA_STALE_MS);
    }));
  }

  // Drop saved pages the library no longer links to — only after a clean
  // pass, so a flaky connection can never delete anything. Images are kept.
  let pruned = 0;
  const complete = shelfOk && failed === 0 && !quotaFull;
  if (complete) {
    const keys = await fileKeys().catch(() => []);
    for (const k of keys) {
      if (inScope(k) && isTextKey(k) && !seen.has(k)) {
        await deleteFile(k).catch(() => {});
        pruned++;
      }
    }
  }
  return { complete, fetched, kept, failed, gone, pruned, quotaFull, imagesSkipped: !wifi,
    items: seen.size, images: imageList.length, ms: Date.now() - started, failures };
}

async function status() {
  const keys = await fileKeys().catch(() => []);
  const last = await getMeta('lastSync').catch(() => null);
  return {
    type: 'offline-status', version: SW_VERSION, syncing: !!syncing,
    saved: keys.length, pages: keys.filter(k => inScope(k) && isHtmlKey(k)).length,
    lastSync: last || null, lastResult
  };
}

async function broadcast() {
  try {
    const msg = await status();
    const clients = await self.clients.matchAll({ includeUncontrolled: true });
    clients.forEach(c => c.postMessage(msg));
  } catch (e) {}
}

// ── Lifecycle ──────────────────────────────────────────────────────────

self.addEventListener('install', event => {
  event.waitUntil(Promise.all(CORE.map(url =>
    fetch(url, { cache: 'no-cache' })
      .then(resp => (resp.ok ? save(keyFor(url), resp) : null))
      .catch(() => null)
  )).then(() => self.skipWaiting()));
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    // The old worker (removed Jul 2026) used caches named "books-v39" etc.
    // Only ever touch those: the other apps on this origin own the rest.
    const names = await caches.keys().catch(() => []);
    await Promise.all(names.filter(n => /^books-v\d+$/.test(n)).map(n => caches.delete(n)));
    await self.clients.claim();
  })());
});

self.addEventListener('message', event => {
  const data = event.data || {};
  const reply = () => status().then(s => { if (event.source) event.source.postMessage(s); });
  if (data.type === 'sync') {
    // Each ping also keeps this worker alive while a long first sync runs.
    event.waitUntil(syncLibrary(!!data.force));
    event.waitUntil(reply());
  } else if (data.type === 'status') {
    event.waitUntil(reply());
  }
});
