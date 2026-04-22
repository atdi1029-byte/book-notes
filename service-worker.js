// Caches books you're reading for offline access

// Book Notes Service Worker v6
var CACHE = 'books-v6';

// Core assets always cached
var CORE = [
  './',
  './index.html',
  './book.css',
  './book.js',
  './manifest.json',
  './bg.jpg',
  './icon.png'
];

self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open(CACHE).then(function(cache) {
      return cache.addAll(CORE);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(names) {
      return Promise.all(
        names.filter(function(n) {
          return n !== CACHE;
        }).map(function(n) {
          return caches.delete(n);
        })
      );
    })
  );
  self.clients.claim();
});

// Network-first for everything, falling back to cache
self.addEventListener('fetch', function(e) {
  // Skip non-GET and cross-origin
  if (e.request.method !== 'GET') return;
  var url = new URL(e.request.url);
  if (url.origin !== location.origin) return;

  e.respondWith(
    fetch(e.request).then(function(resp) {
      // Cache successful responses for book pages
      // and core assets
      if (resp.ok && shouldCache(url.pathname)) {
        var clone = resp.clone();
        caches.open(CACHE).then(function(cache) {
          cache.put(e.request, clone);
        });
      }
      return resp;
    }).catch(function() {
      // Offline — serve from cache
      return caches.match(e.request).then(function(r) {
        if (r) return r;
        // If it's a navigation request, show offline page
        if (e.request.mode === 'navigate') {
          return caches.match('./');
        }
      });
    })
  );
});

// Cache book pages, CSS, JS, images
function shouldCache(path) {
  if (path.endsWith('/index.html') ||
      path.endsWith('/') ||
      path.endsWith('.css') ||
      path.endsWith('.js') ||
      path.endsWith('.json') ||
      path.endsWith('.jpg') ||
      path.endsWith('.png') ||
      path.endsWith('.webp')) {
    return true;
  }
  return false;
}

// Listen for messages from book.js / shelf
self.addEventListener('message', function(e) {
  if (!e.data) return;

  // Cache a book and all its assets for offline reading
  if (e.data.type === 'cache-book') {
    var bookPath = e.data.path;
    var url = new URL(bookPath, self.location).href;
    caches.open(CACHE).then(function(cache) {
      // Fetch the HTML, cache it, then parse for images
      fetch(url).then(function(resp) {
        if (!resp.ok) return;
        var clone = resp.clone();
        cache.put(url, clone);
        console.log('[SW] Cached: ' + bookPath);
        // Parse HTML for embedded images
        return resp.text();
      }).then(function(html) {
        if (!html) return;
        // Find all src="..." in img tags
        var imgs = [];
        var re = /<img[^>]+src=["']([^"']+)["']/gi;
        var m;
        while ((m = re.exec(html)) !== null) {
          imgs.push(m[1]);
        }
        // Also cache cover.jpg in the book's directory
        var dir = bookPath.replace(/index\.html$/, '')
          .replace(/\/$/, '') + '/';
        imgs.push(dir + 'cover.jpg');
        // Cache each unique asset
        var seen = {};
        imgs.forEach(function(src) {
          var absUrl = new URL(src, url).href;
          if (seen[absUrl]) return;
          seen[absUrl] = true;
          cache.add(absUrl).then(function() {
            console.log('[SW] Cached asset: ' + src);
          }).catch(function() {
            // cover.jpg or image may not exist — that's ok
          });
        });
      }).catch(function(err) {
        console.warn('[SW] Failed to cache: ' +
          bookPath, err);
      });
    });
  }

  // Remove a book and its assets from offline cache
  if (e.data.type === 'uncache-book') {
    var bookPath = e.data.path;
    var url = new URL(bookPath, self.location).href;
    var dir = new URL(
      bookPath.replace(/index\.html$/, '').replace(/\/$/, '') + '/',
      self.location
    ).href;
    caches.open(CACHE).then(function(cache) {
      // Delete all cached entries under this book's directory
      cache.keys().then(function(requests) {
        requests.forEach(function(req) {
          if (req.url === url || req.url.startsWith(dir)) {
            cache.delete(req);
          }
        });
        console.log('[SW] Removed from offline: ' + bookPath);
      });
    });
  }
});
