// Finance Guide — completion tracking, filter, cloud sync
(function() {
  var DONE_KEY = 'fg_done', FILTER_KEY = 'fg_filter', HIDE_KEY = 'fg_hide_done';
  var SYNC_URL = 'https://script.google.com/macros/s/AKfycbwt438APIycBc534W6T66O3IgtxLUU9cczw-PZAN6Mc9p2xfU2ySsND_wEMJDHUvrXyUg/exec';
  var done = JSON.parse(localStorage.getItem(DONE_KEY) || '{}');
  var filter = localStorage.getItem(FILTER_KEY) || 'all';
  var syncReady = false;

  // Auto-hide: restore preference on load
  if (localStorage.getItem(HIDE_KEY) === '1') {
    document.body.classList.add('hide-done');
  }

  function visible(flag) {
    if (filter === 'star') return flag === 'star';
    return true;
  }

  function apply() {
    var shown = 0, total = 0, hidden = 0;
    document.querySelectorAll('.concept-row').forEach(function(r) {
      var slug = r.dataset.slug, flag = r.dataset.flag;
      total++;
      if (done[slug]) r.classList.add('done'); else r.classList.remove('done');
      if (visible(flag)) { r.classList.remove('fg-hidden'); shown++; }
      else { r.classList.add('fg-hidden'); hidden++; }
    });
    document.querySelectorAll('.cat-card').forEach(function(card) {
      var slugs = card.dataset.slugs ? card.dataset.slugs.split(',') : [];
      var flags = card.dataset.flags ? card.dataset.flags.split(',') : [];
      var vis = 0, allDone = slugs.length > 0;
      slugs.forEach(function(sl, i) {
        if (visible(flags[i])) vis++;
        if (!done[sl]) allDone = false;
      });
      total += slugs.length; shown += vis;
      var c = card.querySelector('.cat-count');
      if (c) c.textContent = vis + (vis !== slugs.length ? ' of ' + slugs.length : '') + ' concepts' +
        (card.dataset.stars ? ' \u00b7 ' + card.dataset.stars + ' \u2605' : '');
      if (vis === 0) card.classList.add('fg-empty'); else card.classList.remove('fg-empty');
      if (allDone) card.classList.add('done'); else card.classList.remove('done');
    });
    document.querySelectorAll('[data-filter]').forEach(function(b) {
      b.classList.toggle('active', b.dataset.filter === filter);
    });
    // Update hide button state
    var hideBtn = document.querySelector('.fg-btn-hide');
    if (hideBtn) {
      var hiding = document.body.classList.contains('hide-done');
      hideBtn.classList.toggle('active', hiding);
      hideBtn.textContent = hiding ? 'Show completed' : 'Hide completed';
    }
    var n = document.getElementById('fgCount');
    if (n) n.textContent = shown + ' of ' + total + ' shown';
    var h = document.getElementById('fgHiddenNote');
    if (h) h.textContent = hidden ? hidden + ' hidden by the filter.' : '';
    var btn = document.querySelector('.concept-done');
    if (btn) {
      var on = !!done[btn.dataset.slug];
      btn.classList.toggle('on', on);
      btn.textContent = on ? '\u2713 Completed' : '\u2713 Mark complete';
    }
  }

  // JSONP helper (same pattern as book shelf)
  function jsonpFetch(url, cb) {
    var cbName = '_fgCb_' + Date.now() + '_' + Math.random().toString(36).substr(2, 5);
    var script = document.createElement('script');
    var fired = false;
    window[cbName] = function(resp) { fired = true; delete window[cbName]; script.remove(); cb(null, resp); };
    script.src = url + (url.includes('?') ? '&' : '?') + 'callback=' + cbName;
    script.onerror = function() { if (!fired) { delete window[cbName]; script.remove(); cb('Failed'); } };
    setTimeout(function() { if (!fired) { delete window[cbName]; script.remove(); cb('Timeout'); } }, 15000);
    document.head.appendChild(script);
  }

  // Cloud sync: pull on load
  function syncFromCloud() {
    jsonpFetch(SYNC_URL + '?action=fg_get_done', function(err, data) {
      if (!err && data && data.status === 'ok' && data.fg_done) {
        // Merge: remote wins for additions, union of both
        var remote = data.fg_done;
        var changed = false;
        for (var k in remote) {
          if (!done[k]) { done[k] = true; changed = true; }
        }
        if (changed) {
          localStorage.setItem(DONE_KEY, JSON.stringify(done));
          apply();
        }
      }
      syncReady = true;
    });
  }
  syncFromCloud();

  // Re-sync when page becomes visible (tab switch, phone wake)
  document.addEventListener('visibilitychange', function() {
    if (document.visibilityState === 'visible') syncFromCloud();
  });

  window.setFilter = function(f) {
    filter = f; localStorage.setItem(FILTER_KEY, f); apply();
  };

  window.toggleDone = function(slug) {
    var nowDone;
    if (done[slug]) { delete done[slug]; nowDone = false; }
    else { done[slug] = true; nowDone = true; }
    localStorage.setItem(DONE_KEY, JSON.stringify(done));
    apply();
    // Push individual toggle to cloud
    if (syncReady) {
      jsonpFetch(SYNC_URL + '?action=fg_toggle_done&slug=' +
        encodeURIComponent(slug) + '&done=' + nowDone, function(){});
    }
  };

  window.toggleHideDone = function() {
    var hiding = document.body.classList.toggle('hide-done');
    localStorage.setItem(HIDE_KEY, hiding ? '1' : '0');
    apply();
  };

  apply();
})();
