// Books, Zercher, Taper, Scalp & Finance Guide Sync — Google Apps Script
// Deploy as Web App: Execute as Me, Access: Anyone.
// Every request is a GET (POST fails under Apps Script CORS redirects);
// add &callback=funcName to any request for JSONP.
//
// v2 (2026-09-20)
//   - Bookmarks + reading progress stored ONE ROW PER KEY in sheet
//     "BookmarkRows" instead of a single cell. The old Bookmarks!A1 blob hit
//     the 50,000-character cell limit and every growing write failed.
//   - Legacy Bookmarks!A1 is migrated automatically on first use and left in
//     place as a backup.
//   - Script lock around every write (two devices / tabs can no longer lose
//     each other's updates).
//   - Any thrown error comes back as JSON {status:'error', message} instead
//     of an HTML error page, so clients can tell the write failed.
//   - Cleared bookmarks leave a 30-day tombstone (returned in `deleted`) so
//     another device does not resurrect them from localStorage.
//   - Reader model precedence: newest `updatedAt` wins (a reset can propagate).
//   - Reading records are only kept for real book pages
//     (<Folder>/index.html or <Folder>/plain.html).
//
// Books actions:
//   ?action=ping
//   ?action=get_read                     → { status, books_read }        Settings!A1
//   ?action=set_read&data=               (whole-object replace; legacy)
//   ?action=toggle_read&book=&read=true|false
//   ?action=get_bookmarks                → { status, bookmarks, deleted:{key:ts} }
//   ?action=set_bookmark&key=&data=      (empty data= deletes → tombstone)
//   ?action=get_masterlist / toggle_masterlist&book=&read=              Settings!C1
//   ?action=get_moved / move_to_shelf&book=&section= / unmove_from_shelf&book=   Settings!D1
// Scalp journal:   scalp_get / scalp_save&data= / scalp_add&data= / scalp_delete&date=   Settings!E1
// Finance guide:   fg_get_done / fg_toggle_done&slug=&done=                              Settings!F1
// Taper:           taper_get / taper_save&data= / taper_save_chunk&i=&cd= / taper_save_done&n=   Settings!G1 (+H col temp)
// Zercher:         zercher_save_config / zercher_save_chunk / zercher_save_done / zercher_save_extra /
//                  zercher_log_workout / zercher_log_run / zercher_load                   sheet "Zercher"

var VERSION = 2;
var BM_SHEET = 'BookmarkRows';       // A=key, B=json, C=updated (ms)
var LEGACY_BM_SHEET = 'Bookmarks';   // old single-cell store (A1)
var RS_KEY = 'reading_speed_data';
var BOOK_PAGE_RE = /^[^\/]+\/(index|plain)\.html$/;
var TOMBSTONE_TTL_MS = 30 * 24 * 3600 * 1000;
var MAX_SESSIONS = 50;

var WRITE_ACTIONS = {
  set_read: 1, toggle_read: 1, set_bookmark: 1, toggle_masterlist: 1,
  move_to_shelf: 1, unmove_from_shelf: 1,
  scalp_save: 1, scalp_add: 1, scalp_delete: 1, fg_toggle_done: 1,
  taper_save: 1, taper_save_chunk: 1, taper_save_done: 1,
  zercher_save_config: 1, zercher_save_chunk: 1, zercher_save_done: 1,
  zercher_save_extra: 1, zercher_log_workout: 1, zercher_log_run: 1
};

function jsonpWrap_(json, callback) {
  if (callback) {
    return ContentService.createTextOutput(callback + '(' + json + ')')
      .setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return ContentService.createTextOutput(json)
    .setMimeType(ContentService.MimeType.JSON);
}

function doGet(e) {
  var p = (e && e.parameter) || {};
  var action = String(p.action || '').toLowerCase();
  var callback = String(p.callback || '');
  var lock = null;
  try {
    if (WRITE_ACTIONS[action]) {
      lock = LockService.getScriptLock();
      lock.waitLock(20000);
    }
    var result = handle_(action, p);
    return jsonpWrap_(JSON.stringify(result), callback);
  } catch (err) {
    var msg = (err && err.message) ? err.message : String(err);
    return jsonpWrap_(JSON.stringify({ status: 'error', action: action, message: msg }), callback);
  } finally {
    if (lock) { try { lock.releaseLock(); } catch (ignore) {} }
  }
}

// ── helpers ──────────────────────────────────────────────────────────────

function parseJson_(raw, fallback) {
  if (raw === '' || raw === null || raw === undefined) return fallback;
  try { return JSON.parse(raw); } catch (err) { return fallback; }
}

function cellJson_(sheet, a1, fallback) {
  return parseJson_(sheet.getRange(a1).getValue(), fallback);
}

function settings_(ss) {
  var sh = ss.getSheetByName('Settings');
  if (!sh) sh = ss.insertSheet('Settings');
  return sh;
}

// ── router ───────────────────────────────────────────────────────────────

function handle_(action, p) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();

  if (action === 'ping') {
    return { status: 'ok', version: VERSION, ts: Date.now() };
  }

  // ── BOOKS: read state ──
  if (action === 'get_read') {
    return { status: 'ok', books_read: cellJson_(settings_(ss), 'A1', {}) };
  }
  if (action === 'set_read') {
    var incomingRead = JSON.parse(p.data || '{}');
    if (Object.keys(incomingRead).length === 0) return { status: 'ok', skipped: true };
    settings_(ss).getRange('A1').setValue(JSON.stringify(incomingRead));
    return { status: 'ok' };
  }
  if (action === 'toggle_read') {
    var rsh = settings_(ss);
    var readMap = cellJson_(rsh, 'A1', {});
    var book = p.book || '';
    if (p.read === 'true') readMap[book] = true; else delete readMap[book];
    rsh.getRange('A1').setValue(JSON.stringify(readMap));
    return { status: 'ok', books_read: readMap };
  }

  // ── BOOKMARKS + READING PROGRESS ──
  if (action === 'get_bookmarks') return getBookmarks_(ss);
  if (action === 'set_bookmark') return setBookmark_(ss, String(p.key || ''), String(p.data || ''));

  // ── MASTER LIST ──
  if (action === 'get_masterlist') {
    return { status: 'ok', masterlist_read: cellJson_(settings_(ss), 'C1', {}) };
  }
  if (action === 'toggle_masterlist') {
    var msh = settings_(ss);
    var ml = cellJson_(msh, 'C1', {});
    var mlBook = p.book || '';
    if (p.read === 'true') ml[mlBook] = true; else delete ml[mlBook];
    msh.getRange('C1').setValue(JSON.stringify(ml));
    return { status: 'ok', masterlist_read: ml };
  }

  // ── MOVED TO SHELF ──
  if (action === 'get_moved') {
    return { status: 'ok', moved: cellJson_(settings_(ss), 'D1', {}) };
  }
  if (action === 'move_to_shelf') {
    var mvsh = settings_(ss);
    var moved = cellJson_(mvsh, 'D1', {});
    moved[p.book || ''] = { ts: Date.now(), section: p.section || '' };
    mvsh.getRange('D1').setValue(JSON.stringify(moved));
    return { status: 'ok', moved: moved };
  }
  if (action === 'unmove_from_shelf') {
    var umsh = settings_(ss);
    var moved2 = cellJson_(umsh, 'D1', {});
    delete moved2[p.book || ''];
    umsh.getRange('D1').setValue(JSON.stringify(moved2));
    return { status: 'ok', moved: moved2 };
  }

  // ── SCALP JOURNAL ──
  if (action === 'scalp_get') {
    return { status: 'ok', entries: cellJson_(settings_(ss), 'E1', []) };
  }
  if (action === 'scalp_save') {
    var scalpData = p.data || '[]';
    JSON.parse(scalpData); // validate
    settings_(ss).getRange('E1').setValue(scalpData);
    return { status: 'ok' };
  }
  if (action === 'scalp_add') {
    var ssh = settings_(ss);
    var entries = cellJson_(ssh, 'E1', []);
    var entry = JSON.parse(p.data || '{}');
    var idx = -1;
    for (var i = 0; i < entries.length; i++) {
      if (entries[i].date === entry.date) { idx = i; break; }
    }
    if (idx >= 0) entries[idx] = entry; else entries.push(entry);
    entries.sort(function (a, b) { return a.date < b.date ? -1 : 1; });
    ssh.getRange('E1').setValue(JSON.stringify(entries));
    return { status: 'ok', entries: entries };
  }
  if (action === 'scalp_delete') {
    var dsh = settings_(ss);
    var delDate = p.date || '';
    var kept = cellJson_(dsh, 'E1', []).filter(function (en) { return en.date !== delDate; });
    dsh.getRange('E1').setValue(JSON.stringify(kept));
    return { status: 'ok', entries: kept };
  }

  // ── FINANCE GUIDE DONE ── Settings!F1 = { slug: true, ... }
  if (action === 'fg_get_done') {
    return { status: 'ok', fg_done: cellJson_(settings_(ss), 'F1', {}) };
  }
  if (action === 'fg_toggle_done') {
    var fsh = settings_(ss);
    var fg = cellJson_(fsh, 'F1', {});
    var slug = p.slug || '';
    if (p.done === 'true') fg[slug] = true; else delete fg[slug];
    fsh.getRange('F1').setValue(JSON.stringify(fg));
    return { status: 'ok', fg_done: fg };
  }

  // ── TAPER ── Settings!G1 = JSON blob, H column = temp chunks
  if (action === 'taper_get') {
    return { status: 'ok', taper: cellJson_(settings_(ss), 'G1', {}) };
  }
  if (action === 'taper_save') {
    var taperData = p.data || '{}';
    JSON.parse(taperData); // validate
    settings_(ss).getRange('G1').setValue(taperData);
    return { status: 'ok' };
  }
  if (action === 'taper_save_chunk') {
    var tIdx = parseInt(p.i || '0', 10);
    settings_(ss).getRange('H' + (tIdx + 1)).setValue(p.cd || '');
    return { status: 'ok', ok: true, chunk: tIdx };
  }
  if (action === 'taper_save_done') {
    var tsh = settings_(ss);
    var tTotal = parseInt(p.n || '1', 10);
    var tFull = '';
    for (var ti = 0; ti < tTotal; ti++) tFull += (tsh.getRange('H' + (ti + 1)).getValue() || '');
    tsh.getRange('G1').setValue(tFull);
    for (var tj = 0; tj < tTotal; tj++) tsh.getRange('H' + (tj + 1)).clearContent();
    return { status: 'ok', ok: true };
  }

  // ── ZERCHER ──
  if (action.indexOf('zercher') === 0) return zercher_(ss, action, p);

  return { status: 'error', message: 'Unknown action: ' + action };
}

// ── Bookmark rows ────────────────────────────────────────────────────────

function bmSheet_(ss) {
  var sh = ss.getSheetByName(BM_SHEET);
  if (sh) return sh;
  sh = ss.insertSheet(BM_SHEET);
  sh.getRange(1, 1, 1, 3).setValues([['key', 'data', 'updated']]);
  migrateLegacyBookmarks_(ss, sh);
  return sh;
}

function normalizePath_(path) {
  path = String(path || '');
  if (path.charAt(path.length - 1) === '/') path += 'index.html';
  return path;
}

function recordTime_(b) {
  return (b && (b.updatedAt || b.resetAt)) || 0;
}

// One-time: explode the legacy Bookmarks!A1 blob into rows. A1 is left as a backup.
function migrateLegacyBookmarks_(ss, sh) {
  var legacy = ss.getSheetByName(LEGACY_BM_SHEET);
  if (!legacy) return;
  var all = parseJson_(legacy.getRange('A1').getValue(), null);
  if (!all || typeof all !== 'object') return;
  var now = Date.now();
  var rows = [];
  var bookRows = {};
  Object.keys(all).forEach(function (key) {
    var v = all[key];
    if (v === null || v === undefined) return;
    if (key !== RS_KEY) { rows.push([key, JSON.stringify(v), now]); return; }
    if (typeof v !== 'object') return;
    Object.keys(v.books || {}).forEach(function (rawPath) {
      var path = normalizePath_(rawPath);
      if (!BOOK_PAGE_RE.test(path)) return;      // drops debug/guide/junk records
      var b = v.books[rawPath];
      if (!b || typeof b !== 'object') return;
      delete b._lastJumpAt;
      var prev = bookRows[path];
      if (!prev || recordTime_(b) > recordTime_(prev) ||
          (!recordTime_(b) && !recordTime_(prev) && (b.maxScroll || 0) > (prev.maxScroll || 0))) {
        if (prev) b.words = Math.max(b.words || 0, prev.words || 0);
        bookRows[path] = b;
      }
    });
    if (v.reader && typeof v.reader === 'object') rows.push(['rs:reader', JSON.stringify(v.reader), now]);
    if (v.sessions && v.sessions.length) {
      rows.push(['rs:sessions', JSON.stringify(v.sessions.slice(-MAX_SESSIONS)), now]);
    }
  });
  Object.keys(bookRows).forEach(function (path) {
    rows.push(['rs:book:' + path, JSON.stringify(bookRows[path]), now]);
  });
  if (rows.length) sh.getRange(2, 1, rows.length, 3).setValues(rows);
  legacy.getRange('B1').setValue('Migrated ' + rows.length + ' rows to sheet "' + BM_SHEET +
    '" on ' + new Date().toISOString() + '. A1 is kept only as a backup and is no longer read.');
}

// Returns { rows: [{key,data,updated,row}], byKey: {key: entry} }
function readBmRows_(sh) {
  var last = sh.getLastRow();
  var byKey = {};
  var rows = [];
  if (last < 2) return { rows: rows, byKey: byKey };
  var values = sh.getRange(2, 1, last - 1, 3).getValues();
  for (var i = 0; i < values.length; i++) {
    var key = String(values[i][0] || '');
    if (!key) continue;
    var entry = {
      key: key,
      data: parseJson_(values[i][1], null),
      updated: Number(values[i][2]) || 0,
      row: i + 2
    };
    rows.push(entry);
    byKey[key] = entry;
  }
  return { rows: rows, byKey: byKey };
}

function writeBmRow_(sh, byKey, key, obj) {
  var json = JSON.stringify(obj);
  var now = Date.now();
  var entry = byKey[key];
  if (entry) {
    sh.getRange(entry.row, 2, 1, 2).setValues([[json, now]]);
    entry.data = obj;
    entry.updated = now;
  } else {
    sh.appendRow([key, json, now]);
    byKey[key] = { key: key, data: obj, updated: now, row: sh.getLastRow() };
  }
}

function deleteBmRow_(sh, byKey, key) {
  var entry = byKey[key];
  if (!entry) return;
  sh.deleteRow(entry.row);
  delete byKey[key];
  for (var k in byKey) if (byKey[k].row > entry.row) byKey[k].row--;
}

// Response shape is identical to v1 (bookmarks[key] and
// bookmarks.reading_speed_data = {books, sessions, reader}) plus `deleted`.
function getBookmarks_(ss) {
  var sh = bmSheet_(ss);
  var rows = readBmRows_(sh).rows;
  var bookmarks = {};
  var deleted = {};
  var rs = { books: {}, sessions: [] };
  var hasRs = false;
  var now = Date.now();
  rows.forEach(function (r) {
    if (r.data === null) return;
    if (r.key === 'rs:reader') { rs.reader = r.data; hasRs = true; }
    else if (r.key === 'rs:sessions') { rs.sessions = Array.isArray(r.data) ? r.data : []; hasRs = true; }
    else if (r.key.indexOf('rs:book:') === 0) { rs.books[r.key.slice(8)] = r.data; hasRs = true; }
    else if (r.data && r.data.deleted) {
      if (now - (r.data.ts || 0) < TOMBSTONE_TTL_MS) deleted[r.key] = r.data.ts || 0;
    }
    else bookmarks[r.key] = r.data;
  });
  if (hasRs) bookmarks[RS_KEY] = rs;
  return { status: 'ok', bookmarks: bookmarks, deleted: deleted };
}

function setBookmark_(ss, key, dataStr) {
  if (!key) return { status: 'error', message: 'set_bookmark: missing key' };
  var sh = bmSheet_(ss);
  var state = readBmRows_(sh);
  var now = Date.now();

  // Prune expired tombstones (bottom-up so row numbers stay valid).
  state.rows
    .filter(function (r) { return r.data && r.data.deleted && now - (r.data.ts || 0) >= TOMBSTONE_TTL_MS; })
    .sort(function (a, b) { return b.row - a.row; })
    .forEach(function (r) { deleteBmRow_(sh, state.byKey, r.key); });

  if (key === RS_KEY) {
    if (!dataStr) return { status: 'ok', skipped: true };   // never wipe reading data
    var written = mergeReadingData_(sh, state.byKey, JSON.parse(dataStr));
    return { status: 'ok', written: written };
  }

  var existing = state.byKey[key] ? state.byKey[key].data : null;
  if (!dataStr) {
    // Clear → tombstone (kept 30 days so other devices drop their local copy).
    writeBmRow_(sh, state.byKey, key, { deleted: true, ts: now });
    return { status: 'ok', deleted: key };
  }
  var incoming = JSON.parse(dataStr);
  var incTs = (incoming && incoming.ts) || 0;
  if (existing && (existing.ts || 0) > incTs) {
    // Stored bookmark (or tombstone) is newer than what this device has.
    return { status: 'ok', ignored: true, reason: existing.deleted ? 'cleared_elsewhere' : 'newer_on_server' };
  }
  writeBmRow_(sh, state.byKey, key, incoming);
  return { status: 'ok' };
}

// Merge a client's reading-progress payload ({books:{path:rec}, reader, sessions})
// into per-key rows. Returns the number of rows written.
function mergeReadingData_(sh, byKey, inc) {
  if (!inc || typeof inc !== 'object') return 0;
  var written = 0;
  var books = inc.books || {};
  Object.keys(books).forEach(function (rawPath) {
    var path = normalizePath_(rawPath);
    if (!BOOK_PAGE_RE.test(path)) return;         // ignore non-book pages
    var b = books[rawPath];
    if (!b || typeof b !== 'object') return;
    delete b._lastJumpAt;
    var k = 'rs:book:' + path;
    var ex = byKey[k] ? byKey[k].data : null;
    if (ex) {
      var incTime = recordTime_(b), exTime = recordTime_(ex);
      if (incTime || exTime) {
        if (incTime <= exTime) return;             // server copy is as new or newer
        b.words = Math.max(b.words || 0, ex.words || 0);
      } else if ((b.maxScroll || 0) <= (ex.maxScroll || 0)) {
        return;                                    // legacy records: highest wins
      }
    }
    writeBmRow_(sh, byKey, k, b);
    written++;
  });

  if (inc.reader && typeof inc.reader === 'object') {
    var exR = byKey['rs:reader'] ? byKey['rs:reader'].data : null;
    if (readerIsNewer_(inc.reader, exR)) { writeBmRow_(sh, byKey, 'rs:reader', inc.reader); written++; }
  }

  if (inc.sessions && inc.sessions.length) {
    var exS = byKey['rs:sessions'] ? byKey['rs:sessions'].data : [];
    if (!Array.isArray(exS)) exS = [];
    var seen = {};
    exS.forEach(function (s) { seen[s.ts || s.date] = true; });
    var added = 0;
    inc.sessions.forEach(function (s) {
      var id = s.ts || s.date;
      if (!seen[id]) { seen[id] = true; exS.push(s); added++; }
    });
    if (added) {
      if (exS.length > MAX_SESSIONS) exS = exS.slice(-MAX_SESSIONS);
      writeBmRow_(sh, byKey, 'rs:sessions', exS);
      written++;
    }
  }
  return written;
}

// Reader model precedence: newest updatedAt wins (so a reset propagates);
// legacy models without timestamps fall back to "more samples wins".
function readerIsNewer_(inc, ex) {
  if (!ex) return true;
  var it = inc.updatedAt || 0, et = ex.updatedAt || 0;
  if (it || et) return it > et;
  return (inc.samples || 0) > (ex.samples || 0);
}

// ── Zercher ──────────────────────────────────────────────────────────────

function zercher_(ss, action, p) {
  var zSheet = ss.getSheetByName('Zercher');
  if (!zSheet) {
    zSheet = ss.insertSheet('Zercher');
    zSheet.getRange('A1').setValue('{}');  // config
    zSheet.getRange('B1').setValue('{}');  // extra (holds/notes/starts)
    // A2+ = workout logs (one JSON per row), C2+ = run logs, D = temp chunks
  }

  if (action === 'zercher_save_config') {
    var configData = p.data || '{}';
    JSON.parse(configData); // validate
    zSheet.getRange('A1').setValue(configData);
    return { status: 'ok' };
  }
  if (action === 'zercher_save_chunk') {
    var idx = parseInt(p.i || '0', 10);
    zSheet.getRange('D' + (idx + 1)).setValue(p.cd || '');
    return { status: 'ok', ok: true, chunk: idx };
  }
  if (action === 'zercher_save_done') {
    var target = p.target || 'config';
    var total = parseInt(p.n || '1', 10);
    var fullData = '';
    for (var i = 0; i < total; i++) fullData += (zSheet.getRange('D' + (i + 1)).getValue() || '');
    zSheet.getRange(target === 'extra' ? 'B1' : 'A1').setValue(fullData);
    for (var j = 0; j < total; j++) zSheet.getRange('D' + (j + 1)).clearContent();
    return { status: 'ok', ok: true, ts: new Date().toISOString() };
  }
  if (action === 'zercher_save_extra') {
    var extraData = p.data || '{}';
    JSON.parse(extraData); // validate
    zSheet.getRange('B1').setValue(extraData);
    return { status: 'ok' };
  }
  if (action === 'zercher_log_workout') {
    var logData = p.data || '{}';
    var logObj = JSON.parse(logData);
    var lastRow = zSheet.getLastRow();
    if (lastRow >= 2) {
      var existing = zSheet.getRange(2, 1, lastRow - 1, 1).getValues();
      for (var w = 0; w < existing.length; w++) {
        var ex = parseJson_(existing[w][0], null);
        if (ex && ex.id === logObj.id) {
          zSheet.getRange(w + 2, 1).setValue(logData);
          return { status: 'ok', updated: true };
        }
      }
    }
    zSheet.getRange(lastRow + 1, 1).setValue(logData);
    return { status: 'ok' };
  }
  if (action === 'zercher_log_run') {
    var runData = p.data || '{}';
    var runObj = JSON.parse(runData);
    var lastRow2 = zSheet.getLastRow();
    var lastRunRow = 1;
    if (lastRow2 >= 2) {
      var runs = zSheet.getRange(2, 3, lastRow2 - 1, 1).getValues();
      for (var r = 0; r < runs.length; r++) {
        if (runs[r][0]) lastRunRow = r + 2;
        var exr = parseJson_(runs[r][0], null);
        if (exr && exr.id === runObj.id) {
          zSheet.getRange(r + 2, 3).setValue(runData);
          return { status: 'ok', updated: true };
        }
      }
    }
    zSheet.getRange(Math.max(lastRunRow + 1, 2), 3).setValue(runData);
    return { status: 'ok' };
  }
  if (action === 'zercher_load') {
    var config = cellJson_(zSheet, 'A1', {});
    var extra = cellJson_(zSheet, 'B1', {});
    var logs = [], runLogs = [];
    var lastRow3 = zSheet.getLastRow();
    if (lastRow3 >= 2) {
      var rows = zSheet.getRange(2, 1, lastRow3 - 1, 3).getValues();
      for (var q = 0; q < rows.length; q++) {
        var lg = parseJson_(rows[q][0], null);
        if (lg) logs.push(lg);
        var rl = rows[q][2] ? parseJson_(rows[q][2], null) : null;
        if (rl) runLogs.push(rl);
      }
    }
    return { status: 'ok', config: config, extra: extra, logs: logs, runLogs: runLogs,
      prs: config.prs || {}, ts: new Date().toISOString() };
  }
  return { status: 'error', message: 'Unknown action: ' + action };
}
