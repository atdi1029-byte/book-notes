// Caches books you're reading for offline access

// Book Notes Service Worker v4
var CACHE = 'books-v4';

// Core assets always cached
var CORE = [
  './',
  './index.html',
  './book.css',
  './book.js',
  './manifest.json'
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

  // Cache a book for offline reading
  if (e.data.type === 'cache-book') {
    var bookPath = e.data.path;
    // Resolve to absolute URL
    var url = new URL(bookPath, self.location).href;
    caches.open(CACHE).then(function(cache) {
      cache.match(url).then(function(existing) {
        if (!existing) {
          console.log('[SW] Caching for offline: ' +
            bookPath);
          cache.add(url).catch(function(err) {
            console.warn('[SW] Failed to cache: ' +
              bookPath, err);
          });
        }
      });
    });
  }

  // Remove a book from offline cache
  if (e.data.type === 'uncache-book') {
    var bookPath = e.data.path;
    var url = new URL(bookPath, self.location).href;
    caches.open(CACHE).then(function(cache) {
      cache.delete(url).then(function(deleted) {
        if (deleted) {
          console.log('[SW] Removed from offline: ' +
            bookPath);
        }
      });
    });
  }
});
