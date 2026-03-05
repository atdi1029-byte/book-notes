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
    document.querySelectorAll('h2[id], h3').forEach(function(h) {
      if (!h.id) h.id = stableId(h.textContent);
      var btn = document.createElement('span');
      btn.className = 'bm-btn';
      btn.textContent = '\u{1F516}';
      btn.onclick = function(e) { e.stopPropagation(); setBookmark(h); };
      h.appendChild(btn);
    });
  }

  window.setBookmark = function(el) {
    var id = el.id || stableId(el.textContent);
    if (!el.id) el.id = id;
    var d = { id: id, title: el.textContent.replace('\u{1F516}','').trim(), y: window.scrollY };
    localStorage.setItem(BM_KEY, JSON.stringify(d));
    bar.style.display = 'flex';
    label.textContent = 'Resume: ' + d.title;
    showToast('Bookmark saved');
    // Sync to backend
    fetch(SYNC_URL + '?action=set_bookmark&key=' + encodeURIComponent(BM_KEY) + '&data=' + encodeURIComponent(JSON.stringify(d))).catch(function() {});
    document.querySelectorAll('.bm-btn').forEach(function(b) { b.classList.remove('active'); });
    var activeBtn = el.querySelector('.bm-btn');
    if (activeBtn) activeBtn.classList.add('active');
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
    fetch(SYNC_URL + '?action=set_bookmark&key=' + encodeURIComponent(BM_KEY) + '&data=').catch(function() {});
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
  fetch(SYNC_URL + '?action=get_bookmarks').then(function(r) { return r.json(); }).then(function(json) {
    if (json.status === 'ok' && json.bookmarks && json.bookmarks[BM_KEY]) {
      var remote = json.bookmarks[BM_KEY];
      localStorage.setItem(BM_KEY, JSON.stringify(remote));
      applyBookmark(remote);
    } else {
      // No remote bookmark — use local if exists
      var local = localStorage.getItem(BM_KEY);
      if (local) applyBookmark(JSON.parse(local));
    }
  }).catch(function() {
    // Offline — use local
    var local = localStorage.getItem(BM_KEY);
    if (local) applyBookmark(JSON.parse(local));
  });

  // Initialize progress bar on load
  setTimeout(updateProgress, 100);
})();
