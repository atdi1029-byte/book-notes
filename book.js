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

  // Single sync request — handles both bookmarks and reading data
  jsonpFetch(SYNC_URL + '?action=get_bookmarks', function(err, json) {
    if (!err && json && json.status === 'ok' && json.bookmarks) {
      // Bookmark restore
      if (json.bookmarks[BM_KEY]) {
        var remote = json.bookmarks[BM_KEY];
        localStorage.setItem(BM_KEY, JSON.stringify(remote));
        applyBookmark(remote);
      } else {
        var local = localStorage.getItem(BM_KEY);
        if (local) applyBookmark(JSON.parse(local));
      }
      // Reading speed merge (shared from same response)
      window._bmSyncJson = json;
    } else {
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
  // Tracks active reading time (not scroll time) to estimate WPM.
  // Uses activity-based timing: counts seconds the user is engaged,
  // and progress-based word estimation from max scroll reached.

  var RS_KEY = 'reading_speed_data';

  function countWords() {
    // Count words in main content only — skip UI chrome
    var container = document.querySelector(
      'main, article, .content'
    ) || document.body;
    var clone = container.cloneNode(true);
    // Remove UI elements that aren't reading content
    ['bookmarkBar', 'bmToast', 'progressBar'].forEach(function(id) {
      var el = clone.querySelector('#' + id);
      if (el) el.remove();
    });
    clone.querySelectorAll(
      'script, style, nav, .bm-btn, footer, .toc'
    ).forEach(function(el) { el.remove(); });
    var text = clone.textContent || '';
    return text.split(/\s+/).filter(function(w) {
      return w.length > 0;
    }).length;
  }

  function getBookPath() {
    var p = location.pathname;
    var parts = p.split('/');
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
    if (data.sessions.length > 50) {
      data.sessions = data.sessions.slice(-50);
    }
    localStorage.setItem(RS_KEY, JSON.stringify(data));
    syncSpeedToBackend(data);
  }

  var _lastSync = 0;
  function syncSpeedToBackend(data) {
    var now = Date.now();
    if (now - _lastSync < 60000) return;
    _lastSync = now;
    jsonpFetch(
      SYNC_URL + '?action=set_bookmark&key=' +
      encodeURIComponent(RS_KEY) + '&data=' +
      encodeURIComponent(JSON.stringify(data)),
      function() {}
    );
  }

  // Merge remote reading data — reuse the bookmark sync response
  function mergeRemoteReadingData(json) {
    if (!json || !json.bookmarks || !json.bookmarks[RS_KEY]) return;
    var remote = json.bookmarks[RS_KEY];
    var local = loadSpeedData();
    var changed = false;

    if (remote.books) {
      if (!local.books) local.books = {};
      Object.keys(remote.books).forEach(function(path) {
        var rb = remote.books[path];
        var lb = local.books[path];
        if (!lb) {
          local.books[path] = rb;
          changed = true;
        } else {
          if ((rb.maxScroll || 0) > (lb.maxScroll || 0)) {
            lb.maxScroll = rb.maxScroll;
            changed = true;
          }
          if ((rb.words || 0) > (lb.words || 0)) {
            lb.words = rb.words;
            changed = true;
          }
        }
      });
    }

    if (remote.sessions && remote.sessions.length > 0) {
      if (!local.sessions) local.sessions = [];
      var existing = {};
      local.sessions.forEach(function(s) {
        existing[s.ts || s.date] = true;
      });
      remote.sessions.forEach(function(s) {
        if (!existing[s.ts || s.date]) {
          local.sessions.push(s);
          changed = true;
        }
      });
      if (local.sessions.length > 50) {
        local.sessions = local.sessions.slice(-50);
      }
    }

    // Sync reader model — take the one with more samples
    if (remote.reader) {
      if (!local.reader || (remote.reader.samples || 0) > (local.reader.samples || 0)) {
        local.reader = remote.reader;
        changed = true;
      }
    }

    if (changed) {
      localStorage.setItem(RS_KEY, JSON.stringify(local));
    }
  }

  // If sync already completed, merge now; otherwise poll briefly
  if (window._bmSyncJson) {
    mergeRemoteReadingData(window._bmSyncJson);
  } else {
    var _pollCount = 0;
    var _pollTimer = setInterval(function() {
      _pollCount++;
      if (window._bmSyncJson) {
        clearInterval(_pollTimer);
        mergeRemoteReadingData(window._bmSyncJson);
      } else if (_pollCount > 20) {
        clearInterval(_pollTimer); // give up after 2s
      }
    }, 100);
  }

  (function initReadingTracker() {
    var bookPath = getBookPath();
    var data = loadSpeedData();

    if (!data.books[bookPath]) {
      data.books[bookPath] = {
        words: 0,
        maxScroll: 0,
        title: document.title
      };
    }

    // Cache word count — only recount if not yet stored
    var totalWords = data.books[bookPath].words;
    if (!totalWords) {
      totalWords = countWords();
      data.books[bookPath].words = totalWords;
      saveSpeedData(data);
    }
    data.books[bookPath].title = document.title;

    if (totalWords < 200) return;

    // ── Activity-based timing ──
    var activeTime = 0;
    var lastActivity = Date.now();
    var startProgress = data.books[bookPath].maxScroll || 0;
    var IDLE_THRESHOLD = 30000;

    function markActivity() {
      lastActivity = Date.now();
    }

    // ── Single scroll listener for everything ──
    function getProgress() {
      var docH = document.documentElement.scrollHeight
        - window.innerHeight;
      if (docH <= 0) return 0;
      return Math.min(1, window.scrollY / docH);
    }

    var _scrollSaveTimer = null;
    window.addEventListener('scroll', function() {
      // Progress bar
      updateProgress();
      // Activity tracking
      markActivity();
      // Max scroll progress
      var pct = getProgress();
      if (pct > (data.books[bookPath].maxScroll || 0)) {
        data.books[bookPath].maxScroll = pct;
        // Debounced save — persist maxScroll every 2s of scrolling
        if (!_scrollSaveTimer) {
          _scrollSaveTimer = setTimeout(function() {
            _scrollSaveTimer = null;
            saveSpeedData(data);
          }, 2000);
        }
      }
    });

    // Non-scroll activity signals
    window.addEventListener('keydown', markActivity);
    window.addEventListener('touchstart', markActivity);
    window.addEventListener('click', markActivity);
    window.addEventListener('wheel', markActivity);

    // Tick every 1 second — count if user was recently active
    setInterval(function() {
      if (document.hidden) return;
      if (Date.now() - lastActivity < IDLE_THRESHOLD) {
        activeTime += 1000;
      }
    }, 1000);

    // ── Reader model (Kindle-style EMA) ──
    // One-time fix: reset if WPM got corrupted by outlier
    if (data.reader && (data.reader.averageWPM > 500 || data.reader.averageWPM < 80)) {
      data.reader = { averageWPM: 225, samples: 0 };
      saveSpeedData(data);
    }
    if (!data.reader) {
      data.reader = { averageWPM: 225, samples: 0 };
      // Bootstrap from existing sessions if upgrading
      if (data.sessions && data.sessions.length > 0) {
        var recent = data.sessions.slice(-10);
        var tw = 0, tm = 0;
        recent.forEach(function(s) {
          if (s.words >= 300 && s.duration >= 60) {
            tw += s.words;
            tm += s.duration / 60;
          }
        });
        if (tm > 0) {
          data.reader.averageWPM = Math.round(tw / tm);
          data.reader.samples = recent.length;
        }
      }
    }

    function updateReaderModel(sessionWpm) {
      var r = data.reader;
      // Always clamp to ±50% of current average to reject outliers
      var clamped = Math.max(
        r.averageWPM * 0.5,
        Math.min(sessionWpm, r.averageWPM * 1.5)
      );
      if (r.samples < 5) {
        // Bootstrap: weighted accumulation with clamped input
        r.averageWPM = (r.averageWPM * r.samples + clamped)
          / (r.samples + 1);
      } else {
        // EMA with alpha=0.2
        r.averageWPM = r.averageWPM * 0.8 + clamped * 0.2;
      }
      r.samples++;
      r.averageWPM = Math.round(r.averageWPM);
    }

    // ── Session save ──
    var lastSavedProgress = startProgress;
    var lastSavedTime = 0;

    function saveSession() {
      // Always persist progress, even if WPM sample doesn't qualify
      saveSpeedData(data);

      var timeDelta = activeTime - lastSavedTime;
      if (timeDelta < 60000) return; // min 1 minute for WPM sample

      var endProgress = data.books[bookPath].maxScroll || 0;
      var progressDelta = Math.max(0, endProgress - lastSavedProgress);

      var wordsRead = progressDelta * totalWords;
      if (wordsRead < 300) return; // min 300 words for WPM sample

      var minutes = timeDelta / 60000;
      var wpm = wordsRead / minutes;

      if (wpm >= 50 && wpm <= 800) {
        data.sessions.push({
          book: bookPath,
          wpm: Math.round(wpm),
          duration: Math.round(timeDelta / 1000),
          words: Math.round(wordsRead),
          progress: endProgress,
          ts: Date.now()
        });
        updateReaderModel(wpm);
      }

      lastSavedProgress = endProgress;
      lastSavedTime = activeTime;
      saveSpeedData(data);
    }

    window.addEventListener('beforeunload', saveSession);
    // Also save on visibilitychange (mobile tab switches/closes)
    document.addEventListener('visibilitychange', function() {
      if (document.hidden) saveSession();
    });
    // Also save on pagehide (iOS Safari kills tabs without beforeunload)
    window.addEventListener('pagehide', saveSession);
    // Periodic save every 15s if progress changed
    setInterval(function() {
      var endProgress = data.books[bookPath].maxScroll || 0;
      if (endProgress > lastSavedProgress || activeTime - lastSavedTime > 60000) {
        saveSession();
      }
    }, 15000);
  })();
})();
