/* Book Notes — Shared Bookmark & Progress Script
   Usage: set BM_KEY before loading this script, e.g.:
   <script>var BM_KEY = 'bm_my_book';</script>
   <script src="../book.js"></script>
*/

(function() {
  var SYNC_URL = 'https://script.google.com/macros/s/AKfycbwt438APIycBc534W6T66O3IgtxLUU9cczw-PZAN6Mc9p2xfU2ySsND_wEMJDHUvrXyUg/exec';
  var bar = document.getElementById('bookmarkBar');
  var label = document.getElementById('bmLabel');
  var toast = document.getElementById('bmToast');

  function jsonpFetch(url, cb) {
    var cbName = '_bmCb_' + Date.now() + '_' + Math.random().toString(36).substr(2, 5);
    var script = document.createElement('script');
    var done = false;
    window[cbName] = function(resp) { done = true; delete window[cbName]; script.remove(); cb(null, resp); };
    script.src = url + (url.includes('?') ? '&' : '?') + 'callback=' + cbName;
    script.onerror = function() { if (!done) { delete window[cbName]; script.remove(); cb('Failed'); } };
    setTimeout(function() { if (!done) { delete window[cbName]; script.remove(); cb('Timeout'); } }, 15000);
    document.head.appendChild(script);
  }

  function stableId(text) {
    var s = text.replace(/[^a-zA-Z0-9]+/g, '_').toLowerCase().slice(0, 60);
    return 'bm_' + s;
  }

  function initBookmark() {
    var saved = localStorage.getItem(BM_KEY);
    if (saved) {
      try {
        var d = JSON.parse(saved);
        bar.style.display = 'flex';
        label.textContent = 'Resume: ' + d.title;
      } catch(e) { localStorage.removeItem(BM_KEY); }
    }
    document.querySelectorAll('h2[id], h3, h4').forEach(function(h) {
      if (!h.id) h.id = stableId(h.textContent);
      var btn = document.createElement('span');
      btn.className = 'bm-btn';
      btn.textContent = '\u{1F516}';
      btn.onclick = function(e) { e.stopPropagation(); setBookmark(h); };
      h.appendChild(btn);
    });
    // Make li items with <strong> leads bookmarkable
    document.querySelectorAll('li > strong:first-child').forEach(function(s) {
      if (!s.id) s.id = stableId(s.textContent);
      var btn = document.createElement('span');
      btn.className = 'bm-btn';
      btn.textContent = '\u{1F516}';
      btn.onclick = function(e) { e.stopPropagation(); setBookmark(s); };
      s.appendChild(btn);
    });
    // Make every paragraph bookmarkable
    document.querySelectorAll('p').forEach(function(p) {
      if (p.querySelector('.bm-btn')) return; // already has one
      var preview = p.textContent.replace(/\s+/g, ' ').trim().slice(0, 50);
      if (!preview) return;
      if (!p.id) p.id = stableId(preview);
      var btn = document.createElement('span');
      btn.className = 'bm-btn bm-p';
      btn.textContent = '\u{1F516}';
      btn.onclick = function(e) { e.stopPropagation(); setBookmark(p); };
      p.insertBefore(btn, p.firstChild);
    });
  }

  window.setBookmark = function(el) {
    var id = el.id || stableId(el.textContent);
    if (!el.id) el.id = id;
    var rawTitle = el.textContent.replace('\u{1F516}','').trim();
    var d = { id: id, title: rawTitle.length > 60 ? rawTitle.slice(0, 60) + '...' : rawTitle, y: window.scrollY, ts: Date.now() };
    localStorage.setItem(BM_KEY, JSON.stringify(d));
    bar.style.display = 'flex';
    label.textContent = 'Resume: ' + d.title;
    showToast('Bookmark saved \u2014 available offline');
    // Sync to backend
    jsonpFetch(SYNC_URL + '?action=set_bookmark&key=' + encodeURIComponent(BM_KEY) + '&data=' + encodeURIComponent(JSON.stringify(d)), function(){});
    document.querySelectorAll('.bm-btn').forEach(function(b) { b.classList.remove('active'); });
    var activeBtn = el.querySelector('.bm-btn');
    if (activeBtn) activeBtn.classList.add('active');
    // Cache this book for offline reading
    if (navigator.serviceWorker && navigator.serviceWorker.controller) {
      navigator.serviceWorker.controller.postMessage({
        type: 'cache-book',
        path: location.pathname
      });
    }
  };

  window.jumpToBookmark = function() {
    var saved = localStorage.getItem(BM_KEY);
    if (!saved) return;
    var d = JSON.parse(saved);
    var el = document.getElementById(d.id);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    else window.scrollTo({ top: d.y, behavior: 'smooth' });
  };

  window.clearBookmark = function() {
    localStorage.removeItem(BM_KEY);
    bar.style.display = 'none';
    document.querySelectorAll('.bm-btn').forEach(function(b) { b.classList.remove('active'); });
    showToast('Bookmark cleared');
    // Sync clear to backend
    jsonpFetch(SYNC_URL + '?action=set_bookmark&key=' + encodeURIComponent(BM_KEY) + '&data=', function(){});
    // Remove this book from offline cache
    if (navigator.serviceWorker && navigator.serviceWorker.controller) {
      navigator.serviceWorker.controller.postMessage({
        type: 'uncache-book',
        path: location.pathname
      });
    }
  };

  function showToast(msg) {
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(function() { toast.classList.remove('show'); }, 1500);
  }

  // Progress bar
  function updateProgress() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    document.getElementById('progressBar').style.width = h > 0 ? (window.scrollY / h * 100) + '%' : '0%';
  }
  window.addEventListener('scroll', updateProgress);

  // Wrap tables for horizontal scroll on mobile
  document.querySelectorAll('table').forEach(function(t) {
    if (t.parentElement.classList.contains('table-wrap')) return;
    var wrap = document.createElement('div');
    wrap.className = 'table-wrap';
    t.parentNode.insertBefore(wrap, t);
    wrap.appendChild(t);
  });

  initBookmark();

  // Prevent browser from restoring its own scroll position
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';

  function scrollToBookmarkData(d) {
    // If new content exists, don't auto-scroll —
    // let user read new stuff first
    if (window.__skipBookmarkScroll ||
        document.querySelectorAll('.new-badge').length > 0) return;
    var target = document.getElementById(d.id);
    if (target) {
      var rect = target.getBoundingClientRect();
      window.scrollTo(0, window.scrollY + rect.top);
    } else if (d.y) {
      window.scrollTo(0, d.y);
    }
    setTimeout(updateProgress, 300);
  }

  function applyBookmark(d) {
    bar.style.display = 'flex';
    label.textContent = 'Resume: ' + d.title;
    // Wait for full page load before scrolling
    if (document.readyState === 'complete') {
      setTimeout(function() { scrollToBookmarkData(d); }, 200);
    } else {
      window.addEventListener('load', function() {
        setTimeout(function() { scrollToBookmarkData(d); }, 200);
      });
    }
  }

  // Sync from backend (backend wins), then auto-scroll
  jsonpFetch(SYNC_URL + '?action=get_bookmarks', function(err, json) {
    if (!err && json && json.status === 'ok' && json.bookmarks && json.bookmarks[BM_KEY]) {
      var remote = json.bookmarks[BM_KEY];
      localStorage.setItem(BM_KEY, JSON.stringify(remote));
      applyBookmark(remote);
    } else {
      // Offline or no remote — use local if exists
      var local = localStorage.getItem(BM_KEY);
      if (local) applyBookmark(JSON.parse(local));
    }
  });

  // Preserve scroll position across orientation changes
  var _anchorEl = null;
  var _anchorOffset = 0;

  function findAnchorElement() {
    // Find the element closest to the top of the viewport
    var candidates = document.querySelectorAll(
      'h1, h2[id], h3[id], h4[id], p[id], blockquote'
    );
    var best = null;
    var bestDist = Infinity;
    for (var i = 0; i < candidates.length; i++) {
      var rect = candidates[i].getBoundingClientRect();
      // Pick the element whose top is closest to viewport top
      var dist = Math.abs(rect.top);
      if (dist < bestDist) {
        bestDist = dist;
        best = candidates[i];
      }
    }
    return best;
  }

  window.addEventListener('orientationchange', function() {
    // Capture anchor before resize happens
    _anchorEl = findAnchorElement();
    if (_anchorEl) {
      _anchorOffset = _anchorEl.getBoundingClientRect().top;
    }
  });

  window.addEventListener('resize', function() {
    if (_anchorEl) {
      var el = _anchorEl;
      var offset = _anchorOffset;
      // Use rAF to let the browser finish layout
      requestAnimationFrame(function() {
        var newRect = el.getBoundingClientRect();
        window.scrollBy(0, newRect.top - offset);
        _anchorEl = null;
        _anchorOffset = 0;
      });
    }
  });

  // Initialize progress bar on load
  setTimeout(updateProgress, 100);

  // Register service worker from book pages too
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('../service-worker.js');
  }

  // ── Reading Speed Tracker ──
  // Silently tracks scroll behavior to estimate reading speed (WPM)
  // and progress. Data saved to localStorage for shelf display.

  var RS_KEY = 'reading_speed_data';

  function countWords() {
    // Count words in main content, excluding nav/UI elements
    var body = document.body.cloneNode(true);
    // Remove bookmark bar, progress bar, toast, TOC nav
    ['bookmarkBar', 'bmToast', 'progressBar'].forEach(function(id) {
      var el = body.querySelector('#' + id);
      if (el) el.remove();
    });
    body.querySelectorAll('script, style, nav, .bm-btn').forEach(
      function(el) { el.remove(); }
    );
    var text = body.textContent || '';
    return text.split(/\s+/).filter(function(w) {
      return w.length > 0;
    }).length;
  }

  function getBookPath() {
    // e.g. "/book-notes/Some_Book/index.html" → "Some_Book/index.html"
    var p = location.pathname;
    var parts = p.split('/');
    // Get last two segments: folder/file
    if (parts.length >= 2) {
      return parts.slice(-2).join('/');
    }
    return p;
  }

  function loadSpeedData() {
    try {
      return JSON.parse(
        localStorage.getItem(RS_KEY)
      ) || { books: {}, sessions: [] };
    } catch(e) {
      return { books: {}, sessions: [] };
    }
  }

  function saveSpeedData(data) {
    // Keep sessions array from growing forever — last 50
    if (data.sessions.length > 50) {
      data.sessions = data.sessions.slice(-50);
    }
    localStorage.setItem(RS_KEY, JSON.stringify(data));
  }

  (function initReadingTracker() {
    var totalWords = countWords();
    if (totalWords < 200) return; // too short, skip

    var bookPath = getBookPath();
    var data = loadSpeedData();

    // Save word count + current progress for this book
    if (!data.books[bookPath]) {
      data.books[bookPath] = {
        words: totalWords,
        maxScroll: 0,
        title: document.title
      };
    }
    data.books[bookPath].words = totalWords;
    data.books[bookPath].title = document.title;

    var lastY = window.scrollY;
    var lastT = Date.now();
    var readingWords = 0;
    var readingTime = 0; // ms of actual reading

    // Pause detection: skip if tab hidden or idle too long
    var tabVisible = true;
    document.addEventListener('visibilitychange', function() {
      tabVisible = !document.hidden;
      if (tabVisible) {
        // Reset timer so gap during hide isn't counted
        lastT = Date.now();
        lastY = window.scrollY;
      }
    });

    // Sample every 2 seconds
    var tracker = setInterval(function() {
      // Skip if tab is hidden (phone locked, switched tabs)
      if (!tabVisible) {
        lastT = Date.now();
        lastY = window.scrollY;
        return;
      }

      var nowY = window.scrollY;
      var nowT = Date.now();
      var dt = nowT - lastT; // ms since last sample
      var dy = Math.abs(nowY - lastY); // px moved

      // If dt > 30s, user was idle (thinking, AFK)
      // Reset without counting
      if (dt > 30000) {
        lastT = nowT;
        lastY = nowY;
        return;
      }

      // Velocity in px/s
      var vel = dy / (dt / 1000);

      // Only count as reading if:
      // - scrolled some (not idle) but not too fast
      // - velocity < 1500 px/s (reading pace)
      // - velocity > 5 px/s (not completely idle)
      if (vel > 5 && vel < 1500 && dt > 500) {
        // Map scroll distance to words
        var docH = document.documentElement.scrollHeight
          - window.innerHeight;
        if (docH > 0) {
          var pctMoved = dy / docH;
          var wordsRead = pctMoved * totalWords;
          readingWords += wordsRead;
          readingTime += dt;
        }
      }

      // Track max scroll position (progress %)
      var docH2 = document.documentElement.scrollHeight
        - window.innerHeight;
      if (docH2 > 0) {
        var pct = Math.min(1, nowY / docH2);
        if (pct > (data.books[bookPath].maxScroll || 0)) {
          data.books[bookPath].maxScroll = pct;
        }
      }

      lastY = nowY;
      lastT = nowT;
    }, 2000);

    // Save session data on page unload
    function saveSession() {
      if (readingTime < 10000) return; // < 10s, skip

      var wpm = readingWords / (readingTime / 60000);
      // Sanity check: typical reading is 150-500 WPM
      if (wpm >= 50 && wpm <= 800) {
        data.sessions.push({
          book: bookPath,
          wpm: Math.round(wpm),
          duration: Math.round(readingTime / 1000),
          words: Math.round(readingWords),
          ts: Date.now()
        });
      }

      // Update max scroll
      var docH = document.documentElement.scrollHeight
        - window.innerHeight;
      if (docH > 0) {
        var pct = Math.min(1, window.scrollY / docH);
        if (pct > (data.books[bookPath].maxScroll || 0)) {
          data.books[bookPath].maxScroll = pct;
        }
      }

      saveSpeedData(data);
    }

    window.addEventListener('beforeunload', saveSession);
    // Also save periodically (every 30s) in case
    // beforeunload doesn't fire (mobile)
    setInterval(function() {
      if (readingTime >= 10000) {
        var docH = document.documentElement.scrollHeight
          - window.innerHeight;
        if (docH > 0) {
          var pct = Math.min(1, window.scrollY / docH);
          if (pct > (data.books[bookPath].maxScroll || 0)) {
            data.books[bookPath].maxScroll = pct;
          }
        }
        saveSpeedData(data);
      }
    }, 30000);
  })();
})();
