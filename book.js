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

  // On mobile, tap a paragraph to reveal its bookmark button
  if ('ontouchstart' in window) {
    var lastRevealedP = null;
    document.addEventListener('click', function(e) {
      var p = e.target.closest('p');
      if (lastRevealedP && lastRevealedP !== p) {
        var oldBtn = lastRevealedP.querySelector('.bm-p');
        if (oldBtn) oldBtn.style.opacity = '';
      }
      if (p) {
        var btn = p.querySelector('.bm-p');
        if (btn && !e.target.classList.contains('bm-btn')) {
          btn.style.opacity = '0.5';
          lastRevealedP = p;
        }
      }
    });
  }

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
  // Content-based word tracking: counts words per DOM element,
  // determines words read from viewport position (not scroll %).
  // Blends session speed (70%) with lifetime average (30%) for ETA.

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

  // Build a map of content elements with cumulative word counts.
  // Used to convert viewport position → exact words read.
  var _wordMap = null;
  var _totalMappedWords = 0;

  function buildWordMap() {
    var container = document.querySelector(
      'main, article, .content'
    ) || document.body;
    var els = container.querySelectorAll(
      'p, li, td, th, blockquote, h1, h2, h3, h4, h5, h6, figcaption, dt, dd'
    );
    var map = [];
    var cumulative = 0;
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      // Skip UI chrome
      if (el.closest('nav, .toc, .bookmark-bar, #bookmarkBar, #bmToast, .bm-toast')) continue;
      if (el.classList.contains('bm-btn')) continue;
      // Don't double-count nested elements (li inside td, etc.)
      var dominated = false;
      for (var j = 0; j < map.length; j++) {
        if (map[j].el.contains(el)) { dominated = true; break; }
      }
      if (dominated) continue;
      // Count direct text words (exclude bookmark button text)
      var clone = el.cloneNode(true);
      clone.querySelectorAll('.bm-btn').forEach(function(b) { b.remove(); });
      var words = (clone.textContent || '').split(/\s+/).filter(function(w) {
        return w.length > 0;
      }).length;
      if (words === 0) continue;
      cumulative += words;
      map.push({ el: el, words: words, cumWords: cumulative });
    }
    _wordMap = map;
    _totalMappedWords = cumulative;
    return cumulative;
  }

  // Given current scroll position, count how many words have been read
  // by checking which content elements are above the viewport bottom.
  function getWordsRead() {
    if (!_wordMap || _wordMap.length === 0) return 0;
    var viewBottom = window.scrollY + window.innerHeight;
    var wordsRead = 0;
    for (var i = 0; i < _wordMap.length; i++) {
      var entry = _wordMap[i];
      var rect = entry.el.getBoundingClientRect();
      var elTop = window.scrollY + rect.top;
      var elBottom = elTop + rect.height;
      if (elBottom <= viewBottom) {
        // Fully above viewport bottom — fully read
        wordsRead = entry.cumWords;
      } else if (elTop < viewBottom) {
        // Partially visible — proportional
        var visible = (viewBottom - elTop) / rect.height;
        wordsRead = (entry.cumWords - entry.words)
          + Math.round(entry.words * visible);
      } else {
        break; // Below viewport — stop
      }
    }
    return wordsRead;
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
    // Send lightweight payload — only current book + reader model
    var bookPath = getBookPath();
    var lite = { books: {}, reader: data.reader };
    if (data.books[bookPath]) {
      lite.books[bookPath] = data.books[bookPath];
    }
    // Include recent sessions (last 5 only)
    lite.sessions = (data.sessions || []).slice(-5);
    jsonpFetch(
      SYNC_URL + '?action=set_bookmark&key=' +
      encodeURIComponent(RS_KEY) + '&data=' +
      encodeURIComponent(JSON.stringify(lite)),
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
        maxWordsRead: 0,
        title: document.title
      };
    }

    // Build content-based word map for accurate tracking
    var totalWords = buildWordMap();
    if (!totalWords) {
      totalWords = countWords(); // fallback
    }
    data.books[bookPath].words = totalWords;
    data.books[bookPath].title = document.title;
    saveSpeedData(data);

    if (totalWords < 200) return;

    // ── Activity-based timing ──
    var activeTime = 0;
    var lastActivity = Date.now();
    var IDLE_THRESHOLD = 30000;

    // Session-level speed tracking (for blended ETA)
    var sessionWordsStart = data.books[bookPath].maxWordsRead || 0;
    var sessionWpm = 0;

    // Rolling window: track recent reading snapshots (words + time)
    // to compute speed from last ~1000 words, not entire session.
    var _snapshots = []; // { words: N, time: activeTimeMs }
    var _lastSnapshotWords = sessionWordsStart;
    var SNAPSHOT_INTERVAL = 50; // only snapshot every 50 words read
    var ROLLING_WORDS = Math.min(1000, Math.round(totalWords * 0.1));

    function markActivity() {
      lastActivity = Date.now();
    }

    // ── Scroll-based progress (for progress bar only) ──
    function getScrollProgress() {
      var docH = document.documentElement.scrollHeight
        - window.innerHeight;
      if (docH <= 0) return 0;
      return Math.min(1, window.scrollY / docH);
    }

    // ── ETA display element ──
    var etaEl = document.createElement('span');
    etaEl.className = 'reading-eta';
    etaEl.style.cssText =
      'font-size:0.8rem;color:rgba(255,255,255,0.7);' +
      'margin-left:0.75rem;white-space:nowrap;';
    // Insert ETA into bookmark bar (after the label)
    var bmBar = document.getElementById('bookmarkBar');
    if (bmBar) {
      var clearBtn = bmBar.querySelector('.bm-clear');
      if (clearBtn) bmBar.insertBefore(etaEl, clearBtn);
      else bmBar.appendChild(etaEl);
    }

    function formatEta(minutes) {
      if (minutes < 1) return '< 1 min left';
      if (minutes < 60) return Math.round(minutes) + ' min left';
      var h = Math.floor(minutes / 60);
      var m = Math.round(minutes % 60);
      return h + 'h ' + m + 'm left';
    }

    function updateEta() {
      var currentWords = getWordsRead();
      var wordsRemaining = Math.max(0, totalWords - currentWords);

      if (wordsRemaining < 30) {
        etaEl.textContent = 'Finished';
        return;
      }

      // Record snapshot only when reader has progressed ~50 words
      if (currentWords - _lastSnapshotWords >= SNAPSHOT_INTERVAL) {
        _snapshots.push({ words: currentWords, time: activeTime });
        _lastSnapshotWords = currentWords;
      }

      // Trim snapshots: keep only those within the rolling window
      // Find the earliest snapshot where (current - snapshot) <= ROLLING_WORDS
      var cutoff = currentWords - ROLLING_WORDS;
      while (_snapshots.length > 2 && _snapshots[0].words < cutoff) {
        _snapshots.shift();
      }

      // Compute rolling WPM from the window
      if (_snapshots.length >= 2) {
        var oldest = _snapshots[0];
        var newest = _snapshots[_snapshots.length - 1];
        var wDelta = newest.words - oldest.words;
        var tDelta = (newest.time - oldest.time) / 60000; // minutes
        if (tDelta > 0.3 && wDelta > 30) {
          sessionWpm = wDelta / tDelta;
        }
      }

      // Blend: 70% rolling speed, 30% lifetime average
      var lifetimeWpm = data.reader
        ? data.reader.averageWPM : 225;
      var effectiveWpm;
      if (sessionWpm > 50 && sessionWpm < 800) {
        effectiveWpm = sessionWpm * 0.7 + lifetimeWpm * 0.3;
      } else {
        effectiveWpm = lifetimeWpm;
      }

      if (effectiveWpm < 50) effectiveWpm = 225; // sanity floor

      var minutesLeft = wordsRemaining / effectiveWpm;
      etaEl.textContent = formatEta(minutesLeft);
    }

    // ── Single scroll listener for everything ──
    var _scrollSaveTimer = null;
    window.addEventListener('scroll', function() {
      // Progress bar (still scroll-based — that's fine for the bar)
      updateProgress();
      // Activity tracking
      markActivity();
      // Content-based word tracking
      var wordsNow = getWordsRead();
      var maxWords = data.books[bookPath].maxWordsRead || 0;
      if (wordsNow > maxWords) {
        data.books[bookPath].maxWordsRead = wordsNow;
      }
      // Also update legacy maxScroll for backward compat
      var scrollPct = getScrollProgress();
      if (scrollPct > (data.books[bookPath].maxScroll || 0)) {
        data.books[bookPath].maxScroll = scrollPct;
      }
      // Debounced save
      if (!_scrollSaveTimer) {
        _scrollSaveTimer = setTimeout(function() {
          _scrollSaveTimer = null;
          saveSpeedData(data);
          updateEta();
        }, 2000);
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

    // Update ETA every 10 seconds
    setInterval(updateEta, 10000);

    // ── Reader model (Kindle-style EMA) ──
    if (data.reader && (data.reader.averageWPM > 500 || data.reader.averageWPM < 80)) {
      data.reader = { averageWPM: 225, samples: 0 };
      saveSpeedData(data);
    }
    if (!data.reader) {
      data.reader = { averageWPM: 225, samples: 0 };
      if (data.sessions && data.sessions.length > 0) {
        var recent = data.sessions.slice(-10);
        var tw = 0, tm = 0;
        recent.forEach(function(s) {
          if (s.words >= 100 && s.duration >= 60) {
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

    function updateReaderModel(sessionWpmVal) {
      var r = data.reader;
      var clamped = Math.max(
        r.averageWPM * 0.5,
        Math.min(sessionWpmVal, r.averageWPM * 1.5)
      );
      if (r.samples < 5) {
        r.averageWPM = (r.averageWPM * r.samples + clamped)
          / (r.samples + 1);
      } else {
        r.averageWPM = r.averageWPM * 0.8 + clamped * 0.2;
      }
      r.samples++;
      r.averageWPM = Math.round(r.averageWPM);
    }

    // ── Session save (content-based) ──
    var lastSavedWords = sessionWordsStart;
    var lastSavedTime = 0;

    function saveSession() {
      saveSpeedData(data);

      var timeDelta = activeTime - lastSavedTime;
      if (timeDelta < 60000) return; // min 1 minute

      var currentMaxWords = data.books[bookPath].maxWordsRead || 0;
      var wordsDelta = Math.max(0, currentMaxWords - lastSavedWords);

      // Lower threshold near end of book: if <500 words remain,
      // accept any reading progress for model update
      var wordsRemaining = totalWords - currentMaxWords;
      var minWords = wordsRemaining < 500 ? 50 : 300;
      if (wordsDelta < minWords) return;

      var minutes = timeDelta / 60000;
      var wpm = wordsDelta / minutes;

      if (wpm >= 50 && wpm <= 800) {
        data.sessions.push({
          book: bookPath,
          wpm: Math.round(wpm),
          duration: Math.round(timeDelta / 1000),
          words: Math.round(wordsDelta),
          wordsRead: currentMaxWords,
          ts: Date.now()
        });
        updateReaderModel(wpm);
      }

      lastSavedWords = currentMaxWords;
      lastSavedTime = activeTime;
      saveSpeedData(data);
    }

    window.addEventListener('beforeunload', saveSession);
    document.addEventListener('visibilitychange', function() {
      if (document.hidden) saveSession();
    });
    window.addEventListener('pagehide', saveSession);
    setInterval(function() {
      var currentMaxWords = data.books[bookPath].maxWordsRead || 0;
      if (currentMaxWords > lastSavedWords || activeTime - lastSavedTime > 60000) {
        saveSession();
      }
    }, 15000);

    // Show bookmark bar if it was hidden, so ETA is visible
    // (only if there's a bookmark or meaningful progress)
    setTimeout(function() {
      updateEta();
      if (etaEl.textContent && bmBar) {
        bmBar.style.display = 'flex';
      }
    }, 3000);
  })();
})();
