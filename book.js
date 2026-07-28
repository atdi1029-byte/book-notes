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
    var d = { id: id, title: rawTitle.length > 25 ? rawTitle.slice(0, 25) + '...' : rawTitle, y: window.scrollY, ts: Date.now() };
    localStorage.setItem(BM_KEY, JSON.stringify(d));
    // Update shared bookmark collection for library page
    var all = {};
    try { all = JSON.parse(localStorage.getItem('books_bookmarks')) || {}; } catch(e) {}
    all[BM_KEY] = d;
    localStorage.setItem('books_bookmarks', JSON.stringify(all));
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
      // Bookmark restore — keep newest by timestamp
      var local = null;
      try {
        local = JSON.parse(localStorage.getItem(BM_KEY));
      } catch(e) {}

      var remote = json.bookmarks[BM_KEY];

      if (remote && (!local || (remote.ts || 0) > (local.ts || 0))) {
        localStorage.setItem(BM_KEY, JSON.stringify(remote));
        applyBookmark(remote);
      } else if (local) {
        applyBookmark(local);
        // Push newer local bookmark back to server
        jsonpFetch(
          SYNC_URL +
          '?action=set_bookmark' +
          '&key=' + encodeURIComponent(BM_KEY) +
          '&data=' + encodeURIComponent(JSON.stringify(local)),
          function(){}
        );
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
  // Blends session speed (40%) with lifetime average (60%) for ETA.

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

  // Dwell-time paragraph tracking with proportional word crediting.
  // Three independent concepts:
  //   1. Dwell (visibility) — tracks which paragraphs are on screen
  //   2. Active time — gated by user input, drives WPM calculation
  //   3. Words read — proportional to dwell time and reading speed
  // A paragraph's credited words ramp up based on how long it's been
  // visible and the reader's average WPM, so fast scrolling past 700
  // words credits nothing meaningful, but sitting on a paragraph
  // gradually credits the full word count.
  var _readerWpm = 225; // updated by initReadingTracker

  function getWordsRead() {
    if (!_wordMap || _wordMap.length === 0) return 0;
    var wordsRead = 0;
    for (var i = 0; i < _wordMap.length; i++) {
      wordsRead += (_wordMap[i].credited || 0);
    }
    return Math.round(wordsRead);
  }

  // Called every second when tab is visible. Accumulates visibility
  // time per paragraph and credits words proportionally.
  // Uses combined element/viewport fraction to handle tall elements
  // that can never reach 70% visible on small screens.
  function tickDwell() {
    if (!_wordMap || _wordMap.length === 0) return;
    var vpH = window.innerHeight;
    var wps = _readerWpm / 60; // words per second at reader's pace
    for (var i = 0; i < _wordMap.length; i++) {
      var entry = _wordMap[i];
      if ((entry.credited || 0) >= entry.words) continue;
      var rect = entry.el.getBoundingClientRect();
      var elementHeight = Math.max(1, rect.height);
      var visiblePixels = Math.max(
        0,
        Math.min(rect.bottom, vpH) - Math.max(rect.top, 0)
      );
      var elementFraction = visiblePixels / elementHeight;
      var viewportFraction = visiblePixels / Math.max(1, vpH);
      // Normal elements: 35% visible. Tall elements (taller than
      // viewport): accept if they fill 35%+ of the screen.
      var isMeaningfullyVisible =
        visiblePixels >= 80 &&
        (elementFraction >= 0.35 ||
         viewportFraction >= 0.35 ||
         elementHeight > vpH);
      if (isMeaningfullyVisible) {
        entry.visSec = (entry.visSec || 0) + 1;
        var visWeight = Math.min(
          1, Math.max(0.35, viewportFraction)
        );
        var maxCredit = Math.min(
          entry.words, wps * entry.visSec * visWeight
        );
        entry.credited = Math.max(entry.credited || 0, maxCredit);
      } else {
        // Scrolled away — reset visibility timer but keep credits
        entry.visSec = 0;
      }
    }
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

  function saveSpeedData(data, forceSync) {
    if (data.sessions.length > 50) {
      data.sessions = data.sessions.slice(-50);
    }
    localStorage.setItem(RS_KEY, JSON.stringify(data));
    syncSpeedToBackend(data, forceSync);
  }

  var _lastSync = 0;
  function syncSpeedToBackend(data, force) {
    var now = Date.now();
    if (!force && now - _lastSync < 60000) return;
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
          var localTime = lb.updatedAt || lb.resetAt || 0;
          var remoteTime = rb.updatedAt || rb.resetAt || 0;
          if (localTime || remoteTime) {
            // Timestamped: newest state wins (supports resets)
            if (remoteTime > localTime) {
              // Preserve local word count (total words in book)
              rb.words = Math.max(rb.words || 0, lb.words || 0);
              local.books[path] = rb;
              changed = true;
            }
          } else {
            // Legacy records without timestamps: highest wins
            if ((rb.maxScroll || 0) > (lb.maxScroll || 0)) {
              lb.maxScroll = rb.maxScroll;
              changed = true;
            }
            if ((rb.words || 0) > (lb.words || 0)) {
              lb.words = rb.words;
              changed = true;
            }
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
        title: document.title,
        updatedAt: Date.now()
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
    var _snapshots = [{ words: sessionWordsStart, time: 0 }];
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
      'font-size:0.7rem;color:rgba(255,255,255,0.7);' +
      'margin-left:0.5rem;white-space:nowrap;';
    // Insert ETA into bookmark bar (after the label)
    var bmBar = document.getElementById('bookmarkBar');
    if (bmBar) {
      var clearBtn = bmBar.querySelector('.bm-clear');
      if (clearBtn) bmBar.insertBefore(etaEl, clearBtn);
      else bmBar.appendChild(etaEl);
    }

    function formatEta(minutes) {
      if (minutes < 1) return 'Less than a minute left';
      if (minutes < 60) return '~' + Math.round(minutes) + ' min remaining';
      var h = Math.floor(minutes / 60);
      var m = Math.round(minutes % 60);
      return '~' + h + 'h ' + m + 'm remaining';
    }

    function updateEta() {
      var currentWords = getWordsRead();
      var wordsRemaining = Math.max(0, totalWords - currentWords);

      var percent = Math.round(currentWords / totalWords * 100);

      if (wordsRemaining < 30) {
        etaEl.textContent = '\u2714 Reading complete';
        return;
      }

      if (currentWords < 300) {
        var starterWpm = data.reader
          ? data.reader.averageWPM : 225;
        var starterMin = wordsRemaining / starterWpm;
        etaEl.textContent = percent + '% read \u2022 '
          + formatEta(starterMin) + ' \u2022 calibrating';
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

      // Blend: 40% rolling speed, 60% lifetime for stability
      var lifetimeWpm = data.reader
        ? data.reader.averageWPM : 225;
      var effectiveWpm;
      if (sessionWpm > 50 && sessionWpm < 800) {
        effectiveWpm = sessionWpm * 0.4 + lifetimeWpm * 0.6;
      } else {
        effectiveWpm = lifetimeWpm;
      }

      if (effectiveWpm < 50) effectiveWpm = 225; // sanity floor

      var minutesLeft = wordsRemaining / effectiveWpm;
      etaEl.textContent = percent + '% read \u2022 ' + formatEta(minutesLeft);
    }

    // ── Single scroll listener for everything ──
    var _scrollSaveTimer = null;
    window.addEventListener('scroll', function() {
      // Progress bar (still scroll-based — that's fine for the bar)
      updateProgress();
      // Activity tracking
      markActivity();
      // Update maxWordsRead from dwell-based count
      var wordsNow = getWordsRead();
      var maxWords = data.books[bookPath].maxWordsRead || 0;
      if (wordsNow > maxWords) {
        data.books[bookPath].maxWordsRead = wordsNow;
        data.books[bookPath].updatedAt = Date.now();
      }
      // Also update legacy maxScroll for backward compat
      var scrollPct = getScrollProgress();
      if (scrollPct > (data.books[bookPath].maxScroll || 0)) {
        data.books[bookPath].maxScroll = scrollPct;
        data.books[bookPath].updatedAt = Date.now();
      }
      // Debounced save (data persistence only)
      if (!_scrollSaveTimer) {
        _scrollSaveTimer = setTimeout(function() {
          _scrollSaveTimer = null;
          saveSpeedData(data);
        }, 2000);
      }
    });

    // Non-scroll activity signals
    window.addEventListener('keydown', markActivity);
    window.addEventListener('touchstart', markActivity);
    window.addEventListener('click', markActivity);
    window.addEventListener('wheel', markActivity);

    // Set reader WPM for proportional crediting
    _readerWpm = (data.reader && data.reader.averageWPM) || 225;

    // Restore dwell state: credit paragraphs up to saved maxWordsRead
    // so returning to a book doesn't re-count already-read content
    var savedMax = data.books[bookPath].maxWordsRead || 0;
    if (savedMax > 0 && _wordMap && _wordMap.length > 0) {
      var restored = 0;
      for (var ri = 0; ri < _wordMap.length; ri++) {
        var remaining = savedMax - restored;
        if (remaining <= 0) break;
        var credit = Math.min(_wordMap[ri].words, remaining);
        _wordMap[ri].credited = credit;
        _wordMap[ri].visSec = credit >= _wordMap[ri].words ? 9999 : 0;
        restored += credit;
        if (credit < _wordMap[ri].words) break;
      }
    }

    // Tick every 1 second — three independent clocks:
    // 1. Active time (30s idle gate) — drives WPM/speed model
    // 2. Dwell (2min idle gate) — credits words proportionally
    // 3. ETA display — always updates when tab visible
    var DWELL_IDLE = 120000; // 2 min — stop crediting if away
    setInterval(function() {
      if (document.hidden) return;
      var sinceActivity = Date.now() - lastActivity;
      // Active time: tight gate for accurate WPM
      if (sinceActivity < IDLE_THRESHOLD) {
        activeTime += 1000;
      }
      // Dwell: looser gate — reading without touching is normal,
      // but 2+ minutes idle means you probably left
      if (sinceActivity < DWELL_IDLE) {
        tickDwell();
        // Persist maxWordsRead from dwell credits (not just scroll)
        var liveWords = getWordsRead();
        var savedWords = data.books[bookPath].maxWordsRead || 0;
        if (liveWords > savedWords) {
          data.books[bookPath].maxWordsRead = liveWords;
          data.books[bookPath].updatedAt = Date.now();
        }
      }
      updateEta();
    }, 1000);

    // ETA updates via the 1-second dwell ticker above

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

    function updateReaderModel(sessionWpmVal, wordsInSession) {
      var r = data.reader;
      var clamped = Math.max(
        r.averageWPM * 0.5,
        Math.min(sessionWpmVal, r.averageWPM * 1.5)
      );
      // Weight by session length: longer sessions carry more influence
      // 300 words = baseline weight (0.2), 1500+ words = max weight (0.4)
      var weight = Math.min(0.4,
        0.2 + (Math.min(wordsInSession || 300, 1500) - 300) / 6000
      );
      if (r.samples < 5) {
        r.averageWPM = (r.averageWPM * r.samples + clamped)
          / (r.samples + 1);
      } else {
        r.averageWPM = r.averageWPM * (1 - weight) + clamped * weight;
      }
      r.samples++;
      r.averageWPM = Math.round(r.averageWPM);
      _readerWpm = r.averageWPM;
    }

    // ── Session save (content-based) ──
    var lastSavedWords = sessionWordsStart;
    var lastSavedTime = 0;

    function saveSession() {
      var timeDelta = activeTime - lastSavedTime;
      if (timeDelta < 60000) { saveSpeedData(data); return; }

      var currentMaxWords = data.books[bookPath].maxWordsRead || 0;
      var wordsDelta = Math.max(0, currentMaxWords - lastSavedWords);

      // Lower threshold near end of book: if <500 words remain,
      // accept any reading progress for model update
      var wordsRemaining = totalWords - currentMaxWords;
      var minWords = wordsRemaining < 500 ? 50 : 300;
      if (wordsDelta < minWords) { saveSpeedData(data); return; }

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
        updateReaderModel(wpm, wordsDelta);
        // Accumulate lifetime stats
        var r = data.reader;
        r.totalWordsRead = (r.totalWordsRead || 0) + Math.round(wordsDelta);
        r.totalMinutesRead = (r.totalMinutesRead || 0) + Math.round(minutes);
      }

      // Check if book is finished (>95% read)
      if (currentMaxWords / totalWords > 0.95) {
        var r = data.reader;
        if (!r._finished) r._finished = {};
        if (!r._finished[bookPath]) {
          r._finished[bookPath] = true;
          r.totalBooksFinished = (r.totalBooksFinished || 0) + 1;
        }
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

    // ── Reset reading progress button ──
    var resetBtn = document.createElement('button');
    resetBtn.className = 'bm-clear bm-reset';
    resetBtn.textContent = 'Reset book progress';
    resetBtn.title = 'Reset reading progress and bookmark for this book';
    resetBtn.onclick = function(e) {
      e.stopPropagation();
      if (!confirm(
        'Reset reading progress and remove the bookmark for this book?'
      )) return;
      var book = data.books[bookPath];
      book.maxWordsRead = 0;
      book.maxScroll = 0;
      book.updatedAt = Date.now();
      book.resetAt = book.updatedAt;
      // Reset dwell state on all paragraphs
      if (_wordMap) {
        for (var i = 0; i < _wordMap.length; i++) {
          _wordMap[i].credited = 0;
          _wordMap[i].visSec = 0;
        }
      }
      // Clear sessions for this book
      data.sessions = (data.sessions || []).filter(function(s) {
        return s.book !== bookPath;
      });
      sessionWordsStart = 0;
      lastSavedWords = 0;
      lastSavedTime = 0;
      activeTime = 0;
      _snapshots = [{ words: 0, time: 0 }];
      _lastSnapshotWords = 0;
      sessionWpm = 0;
      saveSpeedData(data, true);
      // Also clear the bookmark so resume bar doesn't restore
      localStorage.removeItem(BM_KEY);
      jsonpFetch(
        SYNC_URL + '?action=set_bookmark&key=' +
        encodeURIComponent(BM_KEY) + '&data=',
        function(){}
      );
      if (bar) bar.style.display = 'none';
      updateProgress();
      updateEta();
      showToast('Progress and bookmark reset');
    };
    // Place reset button at top of page, after first h1 or h2
    var topAnchor = document.querySelector('h1') ||
      document.querySelector('h2');
    if (topAnchor && topAnchor.parentNode) {
      topAnchor.parentNode.insertBefore(resetBtn, topAnchor.nextSibling);
    } else {
      document.body.insertBefore(resetBtn, document.body.firstChild);
    }

    // Show bookmark bar if it was hidden, so ETA is visible
    // (only if there's a bookmark or meaningful progress)
    setTimeout(function() {
      updateEta();
      if (etaEl.textContent && bmBar) {
        bmBar.style.display = 'flex';
      }
    }, 3000);
  })();

  // ── Reader Settings ──
  (function initReaderSettings() {
    var SETTINGS_KEY = 'book-reader-settings';
    var defaults = {fontSize:16, lineSpacing:1.7, maxWidth:900, font:'serif', theme:'warm'};
    var s;
    try { s = JSON.parse(localStorage.getItem(SETTINGS_KEY)) || {}; } catch(e) { s = {}; }
    var fontSize = s.fontSize || defaults.fontSize;
    var lineSpacing = s.lineSpacing || defaults.lineSpacing;
    var maxWidth = s.maxWidth || defaults.maxWidth;
    var currentFont = s.font || defaults.font;
    var currentTheme = s.theme || defaults.theme;

    // Inject CSS
    var style = document.createElement('style');
    style.textContent = [
      '.rs-toggle{background:rgba(0,0,0,0.05);border:1px solid var(--border,#e8e2d6);color:var(--muted,#8a7e6b);padding:4px 14px;border-radius:16px;cursor:pointer;font-family:"Inter",sans-serif;font-size:12px;font-weight:500;transition:all 0.2s;margin:10px auto 0;display:block}',
      '.rs-toggle:hover{background:rgba(0,0,0,0.08);color:var(--text,#2c2416)}',
      '.rs-toggle.active{background:#8b6914;color:#fff;border-color:#8b6914}',
      '.rs-panel{max-width:800px;margin:10px auto 0;background:var(--bg,#faf8f4);border:1px solid var(--border,#e8e2d6);border-radius:8px;display:none;padding:14px 18px;font-family:"Inter",sans-serif}',
      '.rs-panel.open{display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center}',
      '.rs-row{display:flex;align-items:center;gap:8px}',
      '.rs-label{font-size:12px;color:var(--muted,#8a7e6b);font-weight:500}',
      '.rs-controls{display:flex;align-items:center;gap:6px}',
      '.rs-btn{width:28px;height:28px;border-radius:6px;border:1px solid var(--border,#e8e2d6);background:var(--bg,#faf8f4);color:var(--text,#2c2416);font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center;font-weight:600}',
      '.rs-btn:hover{opacity:0.8}',
      '.rs-val{font-size:12px;color:var(--text,#2c2416);min-width:32px;text-align:center;font-weight:600}',
      '.rs-swatches{display:flex;gap:6px}',
      '.rs-swatch{width:28px;height:28px;border-radius:50%;border:2px solid transparent;cursor:pointer;transition:border-color 0.2s}',
      '.rs-swatch:hover{border-color:#8b6914}',
      '.rs-swatch.active{border-color:#8b6914;box-shadow:0 0 0 2px rgba(139,105,20,0.2)}',
      '.rs-swatch.t-warm{background:#faf8f4;border-color:#e8e2d6}',
      '.rs-swatch.t-warm.active{border-color:#8b6914}',
      '.rs-swatch.t-cool{background:#f4f6fa}',
      '.rs-swatch.t-dark{background:#1a1a2e}',
      '.rs-swatch.t-sepia{background:#f1e7d0}',
      '.rs-fonts{display:flex;gap:4px}',
      '.rs-font{padding:3px 10px;border-radius:12px;border:1px solid var(--border,#e8e2d6);background:var(--bg,#faf8f4);font-size:11px;cursor:pointer;color:var(--text,#2c2416)}',
      '.rs-font:hover{opacity:0.8}',
      '.rs-font.active{background:#8b6914;color:#fff;border-color:#8b6914}',
      'body.rs-dark{--bg:#1a1a2e;--text:#e0ddd5;--muted:#8a8a9a;--accent:#c4a33a;--border:#333348}',
      'body.rs-dark .rs-panel{background:#22223a;border-color:#333348}',
      'body.rs-dark .rs-panel h3{color:#e0ddd5}',
      'body.rs-dark .rs-btn{background:#2a2a3e;color:#e0ddd5;border-color:#333348}',
      'body.rs-dark .rs-val{color:#e0ddd5}',
      'body.rs-dark .rs-font{background:#2a2a3e;color:#e0ddd5;border-color:#333348}',
      'body.rs-dark .rs-toggle{background:#c4a33a}',
      'body.rs-cool{--bg:#f4f6fa;--text:#1e2a3a;--muted:#6b7a8e;--accent:#2a6cb6;--border:#d0d8e4}',
      'body.rs-cool .rs-toggle{background:#2a6cb6}',
      'body.rs-sepia{--bg:#f1e7d0;--text:#3a2e1a;--muted:#7a6b52;--accent:#8b5e14;--border:#d4c8a8}'
    ].join('\n');
    document.head.appendChild(style);

    // Inject HTML
    var gear = document.createElement('button');
    gear.className = 'rs-toggle';
    gear.textContent = '\u2699 Settings';
    // Insert at top of page, after first h1
    var topH1 = document.querySelector('h1');
    if (topH1 && topH1.parentNode) {
      topH1.parentNode.insertBefore(gear, topH1.nextSibling);
    } else {
      document.body.insertBefore(gear, document.body.firstChild);
    }

    var panel = document.createElement('div');
    panel.className = 'rs-panel';
    panel.innerHTML = ''
      + '<div class="rs-row"><span class="rs-label">Size</span><div class="rs-controls">'
      + '<button class="rs-btn" data-action="size" data-d="-1">-</button>'
      + '<span class="rs-val" id="rsSizeVal"></span>'
      + '<button class="rs-btn" data-action="size" data-d="1">+</button></div></div>'
      + '<div class="rs-row"><span class="rs-label">Spacing</span><div class="rs-controls">'
      + '<button class="rs-btn" data-action="spacing" data-d="-0.1">-</button>'
      + '<span class="rs-val" id="rsSpacingVal"></span>'
      + '<button class="rs-btn" data-action="spacing" data-d="0.1">+</button></div></div>'
      + '<div class="rs-row"><span class="rs-label">Width</span><div class="rs-controls">'
      + '<button class="rs-btn" data-action="width" data-d="-50">-</button>'
      + '<span class="rs-val" id="rsWidthVal"></span>'
      + '<button class="rs-btn" data-action="width" data-d="50">+</button></div></div>'
      + '<div class="rs-row"><span class="rs-label">Font</span><div class="rs-fonts">'
      + '<button class="rs-font" data-font="serif" style="font-family:Playfair Display,serif">Serif</button>'
      + '<button class="rs-font" data-font="sans" style="font-family:Inter,sans-serif">Sans</button>'
      + '<button class="rs-font" data-font="mono" style="font-family:Courier New,monospace">Mono</button></div></div>'
      + '<div class="rs-row"><span class="rs-label">Theme</span><div class="rs-swatches">'
      + '<div class="rs-swatch t-warm" data-theme="warm" title="Warm"></div>'
      + '<div class="rs-swatch t-cool" data-theme="cool" title="Cool"></div>'
      + '<div class="rs-swatch t-sepia" data-theme="sepia" title="Sepia"></div>'
      + '<div class="rs-swatch t-dark" data-theme="dark" title="Dark"></div></div></div>';
    gear.parentNode.insertBefore(panel, gear.nextSibling);

    function save() {
      localStorage.setItem(SETTINGS_KEY, JSON.stringify({
        fontSize:fontSize, lineSpacing:lineSpacing, maxWidth:maxWidth,
        font:currentFont, theme:currentTheme
      }));
    }

    function applyAll() {
      document.body.style.fontSize = fontSize + 'px';
      document.body.style.lineHeight = lineSpacing;
      document.body.style.maxWidth = maxWidth + 'px';
      document.body.style.margin = '0 auto';
      var fonts = {
        serif: "'Playfair Display', Georgia, serif",
        sans: "'Inter', -apple-system, sans-serif",
        mono: "'Courier New', monospace"
      };
      document.body.style.fontFamily = fonts[currentFont];
      document.getElementById('rsSizeVal').textContent = fontSize + 'px';
      document.getElementById('rsSpacingVal').textContent = lineSpacing.toFixed(1);
      document.getElementById('rsWidthVal').textContent = maxWidth;
      // Theme class
      document.body.classList.remove('rs-dark','rs-cool','rs-sepia');
      if (currentTheme !== 'warm') document.body.classList.add('rs-' + currentTheme);
      // Active states
      panel.querySelectorAll('.rs-swatch').forEach(function(sw) {
        sw.classList.toggle('active', sw.dataset.theme === currentTheme);
      });
      panel.querySelectorAll('.rs-font').forEach(function(b) {
        b.classList.toggle('active', b.dataset.font === currentFont);
      });
    }

    gear.addEventListener('click', function() {
      panel.classList.toggle('open');
      gear.classList.toggle('active');
    });

    panel.addEventListener('click', function(e) {
      var btn = e.target.closest('.rs-btn');
      if (btn) {
        var action = btn.dataset.action;
        var d = parseFloat(btn.dataset.d);
        if (action === 'size') fontSize = Math.max(10, Math.min(24, fontSize + d));
        if (action === 'spacing') lineSpacing = Math.max(1.0, Math.min(2.5, +(lineSpacing + d).toFixed(1)));
        if (action === 'width') maxWidth = Math.max(500, Math.min(1400, maxWidth + d));
        applyAll(); save();
        return;
      }
      var font = e.target.closest('.rs-font');
      if (font) { currentFont = font.dataset.font; applyAll(); save(); return; }
      var swatch = e.target.closest('.rs-swatch');
      if (swatch) { currentTheme = swatch.dataset.theme; applyAll(); save(); return; }
    });

    applyAll();
  })();

  // ── Glossary Tooltips ──
  // Parses the glossary section, then highlights matching terms
  // in chapter text with tap/hover tooltips showing definitions.
  (function initGlossary() {
    var glossaryH2 = document.getElementById('glossary');
    if (!glossaryH2) return;

    // Collect terms from glossary lists
    var terms = [];
    var sibling = glossaryH2.nextElementSibling;
    while (sibling) {
      // Stop at the next h2 (end of glossary section)
      if (sibling.tagName === 'H2') break;
      if (sibling.tagName === 'UL') {
        sibling.querySelectorAll('li').forEach(function(li) {
          var strong = li.querySelector('strong');
          if (!strong) return;
          var rawTerm = strong.textContent.replace(/:$/, '').trim();
          // Get definition: everything after the strong tag
          var def = li.textContent
            .replace(strong.textContent, '').trim();
          if (rawTerm && def) {
            terms.push({ term: rawTerm, def: def });
          }
        });
      }
      sibling = sibling.nextElementSibling;
    }

    if (terms.length === 0) return;

    // Sort by length descending so longer terms match first
    // (e.g. "comparative advantage" before "advantage")
    terms.sort(function(a, b) {
      return b.term.length - a.term.length;
    });

    // Build regex matching all terms (case-insensitive, word boundary)
    var escaped = terms.map(function(t) {
      return t.term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    });
    var re = new RegExp(
      '\\b(' + escaped.join('|') + ')\\b', 'gi'
    );

    // Build term→def lookup (lowercase keys)
    var lookup = {};
    terms.forEach(function(t) {
      lookup[t.term.toLowerCase()] = t;
    });

    // Walk text nodes in chapter content (skip glossary itself,
    // headings, blockquotes with cite, and existing glossary spans)
    var container = document.querySelector('body');
    var glossarySection = glossaryH2.parentElement === container
      ? null : glossaryH2.parentElement;

    function shouldSkip(node) {
      var el = node.parentElement;
      while (el && el !== container) {
        if (el === glossaryH2) return true;
        if (el.id === 'glossary') return true;
        if (el.classList && el.classList.contains('gloss')) return true;
        if (el.tagName === 'A') return true;
        if (el.tagName === 'H1' || el.tagName === 'H2') return true;
        // Skip inside the glossary ULs
        if (glossarySection && el === glossarySection) return true;
        el = el.parentElement;
      }
      return false;
    }

    // Track which terms have already been linked (first occurrence only)
    var linked = {};

    // Find the end of the glossary section (next h2 after glossary)
    var glossaryEnd = glossaryH2.nextElementSibling;
    while (glossaryEnd && glossaryEnd.tagName !== 'H2') {
      glossaryEnd = glossaryEnd.nextElementSibling;
    }

    // Get all paragraphs — skip those inside the glossary
    var paras = document.querySelectorAll('p');
    paras.forEach(function(p) {
      // Skip if inside glossary (between glossary h2 and next h2)
      if (shouldSkip(p)) return;

      var walker = document.createTreeWalker(
        p, NodeFilter.SHOW_TEXT, null, false
      );
      var textNodes = [];
      while (walker.nextNode()) textNodes.push(walker.currentNode);

      textNodes.forEach(function(textNode) {
        if (shouldSkip(textNode)) return;
        var text = textNode.textContent;
        re.lastIndex = 0;
        if (!re.test(text)) return;
        re.lastIndex = 0;

        var frag = document.createDocumentFragment();
        var lastIdx = 0;
        var match;

        re.lastIndex = 0;
        while ((match = re.exec(text)) !== null) {
          var termKey = match[1].toLowerCase();
          // Only link first occurrence of each term
          if (linked[termKey]) continue;
          linked[termKey] = true;

          var entry = lookup[termKey];
          if (!entry) continue;

          // Text before match
          if (match.index > lastIdx) {
            frag.appendChild(
              document.createTextNode(text.slice(lastIdx, match.index))
            );
          }

          // Glossary span
          var span = document.createElement('span');
          span.className = 'gloss';
          span.setAttribute('data-term', entry.term);
          span.setAttribute('data-def', entry.def);
          span.textContent = match[0];
          frag.appendChild(span);

          lastIdx = match.index + match[0].length;
        }

        if (lastIdx === 0) return; // no new matches
        if (lastIdx < text.length) {
          frag.appendChild(
            document.createTextNode(text.slice(lastIdx))
          );
        }
        textNode.parentNode.replaceChild(frag, textNode);
      });
    });

    // Tooltip element (shared, repositioned on each hover/tap)
    var tip = document.createElement('div');
    tip.className = 'gloss-tip';
    document.body.appendChild(tip);

    var hideTimer = null;

    function showTip(span) {
      clearTimeout(hideTimer);
      var term = span.getAttribute('data-term');
      var def = span.getAttribute('data-def');
      tip.replaceChildren();
      var termEl = document.createElement('div');
      termEl.className = 'gloss-tip-term';
      termEl.textContent = term;
      var defEl = document.createElement('div');
      defEl.textContent = def;
      tip.append(termEl, defEl);
      tip.classList.add('show');

      // Position below the term
      var rect = span.getBoundingClientRect();
      var tipW = 320;
      var left = rect.left + window.scrollX;
      // Keep within viewport
      if (left + tipW > window.innerWidth - 16) {
        left = window.innerWidth - tipW - 16;
      }
      if (left < 8) left = 8;
      tip.style.left = left + 'px';
      tip.style.top = (rect.bottom + window.scrollY + 8) + 'px';
    }

    function hideTip() {
      hideTimer = setTimeout(function() {
        tip.classList.remove('show');
      }, 200);
    }

    // Desktop: hover
    document.addEventListener('mouseover', function(e) {
      var g = e.target.closest('.gloss');
      if (g) showTip(g);
    });
    document.addEventListener('mouseout', function(e) {
      var g = e.target.closest('.gloss');
      if (g) hideTip();
    });

    // Mobile: tap to toggle
    document.addEventListener('click', function(e) {
      var g = e.target.closest('.gloss');
      if (g) {
        e.preventDefault();
        if (tip.classList.contains('show') &&
            tip.querySelector('.gloss-tip-term').textContent ===
            g.getAttribute('data-term')) {
          tip.classList.remove('show');
        } else {
          showTip(g);
        }
      } else if (!e.target.closest('.gloss-tip')) {
        tip.classList.remove('show');
      }
    });
  })();
})();
