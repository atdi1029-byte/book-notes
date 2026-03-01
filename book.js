/* Book Notes — Shared Bookmark & Progress Script
   Usage: set BM_KEY before loading this script, e.g.:
   <script>var BM_KEY = 'bm_my_book';</script>
   <script src="../book.js"></script>
*/

(function() {
  var bar = document.getElementById('bookmarkBar');
  var label = document.getElementById('bmLabel');
  var toast = document.getElementById('bmToast');

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
      if (!h.id) h.id = 'bm_' + Math.random().toString(36).slice(2);
      var btn = document.createElement('span');
      btn.className = 'bm-btn';
      btn.textContent = '\u{1F516}';
      btn.onclick = function(e) { e.stopPropagation(); setBookmark(h); };
      h.appendChild(btn);
    });
  }

  window.setBookmark = function(el) {
    var id = el.id || 'bm_' + Math.random().toString(36).slice(2);
    if (!el.id) el.id = id;
    var d = { id: id, title: el.textContent.replace('\u{1F516}','').trim(), y: window.scrollY };
    localStorage.setItem(BM_KEY, JSON.stringify(d));
    bar.style.display = 'flex';
    label.textContent = 'Resume: ' + d.title;
    showToast('Bookmark saved');
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
  };

  function showToast(msg) {
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(function() { toast.classList.remove('show'); }, 1500);
  }

  // Progress bar
  window.addEventListener('scroll', function() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    document.getElementById('progressBar').style.width = h > 0 ? (window.scrollY / h * 100) + '%' : '0%';
  });

  initBookmark();

  // Auto-scroll to bookmark on load
  var savedBm = localStorage.getItem(BM_KEY);
  if (savedBm) {
    try {
      var d = JSON.parse(savedBm);
      var target = document.getElementById(d.id);
      if (target) setTimeout(function() { target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 300);
    } catch(e) {}
  }
})();
