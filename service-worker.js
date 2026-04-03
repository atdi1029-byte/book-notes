// Book Notes Service Worker v1
// Caches books you're reading for offline access

var CACHE = 'books-v1';

// Core assets always cached
var CORE = [
  './',
  './book.css',
  './book.js'
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

// Cache book pages, CSS, JS, and cover images
function shouldCache(path) {
  if (path.endsWith('/index.html') ||
      path.endsWith('/') ||
      path.endsWith('.css') ||
      path.endsWith('.js') ||
      path.endsWith('.json')) {
    return true;
  }
  return false;
}

// Listen for messages from book.js
self.addEventListener('message', function(e) {
  if (!e.data) return;

  // Cache a book for offline reading
  if (e.data.type === 'cache-book') {
    var bookPath = e.data.path;
    caches.open(CACHE).then(function(cache) {
      // Cache the book's index.html
      cache.add(bookPath).catch(function() {});
    });
  }

  // Remove a book from offline cache
  if (e.data.type === 'uncache-book') {
    var bookPath = e.data.path;
    caches.open(CACHE).then(function(cache) {
      cache.delete(bookPath).catch(function() {});
    });
  }
});
