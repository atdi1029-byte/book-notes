// Books & Zercher Sync — Google Apps Script
// Deploy as Web App: Execute as Me, Access: Anyone
// Supports JSONP: add &callback=funcName to any request

function jsonpWrap_(json, callback) {
  if (callback) {
    return ContentService.createTextOutput(callback + '(' + json + ')')
      .setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return ContentService.createTextOutput(json)
    .setMimeType(ContentService.MimeType.JSON);
}
//
// Books Actions:
//   ?action=get_read            → returns { status:"ok", books_read: { ... } }
//   ?action=set_read&data=      → saves JSON string to Settings!A1
//   ?action=get_bookmarks       → returns { status:"ok", bookmarks: { ... } }
//   ?action=set_bookmark&key=&data= → merges single bookmark into Bookmarks!A1
//
// Zercher Actions:
//   ?action=zercher_save_config&data=  → saves config JSON to Zercher!A1
//   ?action=zercher_log_workout&data=  → appends workout log to Zercher!A2+ (col A)
//   ?action=zercher_log_run&data=      → appends run log to Zercher!C2+ (col C)
//   ?action=zercher_save_extra&data=   → saves holds/notes/starts to Zercher!B1
//   ?action=zercher_load               → returns all zercher data (logs + runLogs)

function doGet(e) {
  var action = (e.parameter.action || '').toLowerCase();
  var callback = e.parameter.callback || '';
  var ss = SpreadsheetApp.getActiveSpreadsheet();

  // ── BOOKS ──
  if (action === 'get_read' || action === 'set_read') {
    var sheet = ss.getSheetByName('Settings');
    if (!sheet) sheet = ss.insertSheet('Settings');

    if (action === 'get_read') {
      var raw = sheet.getRange('A1').getValue() || '{}';
      return jsonpWrap_(JSON.stringify({ status: 'ok', books_read: JSON.parse(raw) }), callback);
    }

    if (action === 'set_read') {
      var data = e.parameter.data || '{}';
      var incoming = JSON.parse(data);
      if (Object.keys(incoming).length === 0) {
        return jsonpWrap_(JSON.stringify({ status: 'ok', skipped: true }), callback);
      }
      sheet.getRange('A1').setValue(data);
      return jsonpWrap_(JSON.stringify({ status: 'ok' }), callback);
    }
  }

  // Toggle a single book's read status (safe — never wipes other data)
  if (action === 'toggle_read') {
    var sheet = ss.getSheetByName('Settings');
    if (!sheet) sheet = ss.insertSheet('Settings');
    var book = e.parameter.book || '';
    var read = e.parameter.read === 'true';
    var existing = {};
    try { existing = JSON.parse(sheet.getRange('A1').getValue() || '{}'); } catch(err) {}
    if (read) { existing[book] = true; } else { delete existing[book]; }
    sheet.getRange('A1').setValue(JSON.stringify(existing));
    return jsonpWrap_(JSON.stringify({ status: 'ok', books_read: existing }), callback);
  }

  // ── BOOKMARKS ──
  if (action === 'get_bookmarks' || action === 'set_bookmark') {
    var bmSheet = ss.getSheetByName('Bookmarks');
    if (!bmSheet) bmSheet = ss.insertSheet('Bookmarks');

    if (action === 'get_bookmarks') {
      var raw = bmSheet.getRange('A1').getValue() || '{}';
      return jsonpWrap_(JSON.stringify({ status: 'ok', bookmarks: JSON.parse(raw) }), callback);
    }

    if (action === 'set_bookmark') {
      var key = e.parameter.key || '';
      var bmData = e.parameter.data || '';
      var all = {};
      try { all = JSON.parse(bmSheet.getRange('A1').getValue() || '{}'); } catch(err) {}
      if (bmData) {
        all[key] = JSON.parse(bmData);
      } else {
        delete all[key];
      }
      bmSheet.getRange('A1').setValue(JSON.stringify(all));
      return jsonpWrap_(JSON.stringify({ status: 'ok' }), callback);
    }
  }

  // ── MASTER LIST ──
  if (action === 'get_masterlist') {
    var mlSheet = ss.getSheetByName('Settings');
    if (!mlSheet) mlSheet = ss.insertSheet('Settings');
    var raw = mlSheet.getRange('C1').getValue() || '{}';
    return jsonpWrap_(JSON.stringify({ status: 'ok', masterlist_read: JSON.parse(raw) }), callback);
  }

  if (action === 'toggle_masterlist') {
    var mlSheet = ss.getSheetByName('Settings');
    if (!mlSheet) mlSheet = ss.insertSheet('Settings');
    var mlBook = e.parameter.book || '';
    var mlRead = e.parameter.read === 'true';
    var mlExisting = {};
    try { mlExisting = JSON.parse(mlSheet.getRange('C1').getValue() || '{}'); } catch(err) {}
    if (mlRead) { mlExisting[mlBook] = true; } else { delete mlExisting[mlBook]; }
    mlSheet.getRange('C1').setValue(JSON.stringify(mlExisting));
    return jsonpWrap_(JSON.stringify({ status: 'ok', masterlist_read: mlExisting }), callback);
  }

  // ── ZERCHER ──
  var zSheet = ss.getSheetByName('Zercher');
  if (!zSheet && action.indexOf('zercher') === 0) {
    zSheet = ss.insertSheet('Zercher');
    zSheet.getRange('A1').setValue('{}');  // config
    zSheet.getRange('B1').setValue('{}');  // extra (holds/notes/starts)
    // A2+ = workout logs (one JSON per row)
  }

  if (action === 'zercher_save_config') {
    var configData = e.parameter.data || '{}';
    JSON.parse(configData); // validate
    zSheet.getRange('A1').setValue(configData);
    return jsonpWrap_(JSON.stringify({ status: 'ok' }), callback);
  }

  // Chunked config save (JSONP GET — works with AdBlock Plus)
  if (action === 'zercher_save_chunk') {
    var idx = parseInt(e.parameter.i || '0');
    var chunk = e.parameter.cd || '';
    zSheet.getRange('D' + (idx + 1)).setValue(chunk);
    return jsonpWrap_(JSON.stringify({ ok: true, chunk: idx }), callback);
  }

  if (action === 'zercher_save_done') {
    var target = e.parameter.target || 'config'; // 'config' or 'extra'
    var total = parseInt(e.parameter.n || '1');
    var fullData = '';
    for (var i = 0; i < total; i++) {
      fullData += (zSheet.getRange('D' + (i + 1)).getValue() || '');
    }
    var targetCell = target === 'extra' ? 'B1' : 'A1';
    zSheet.getRange(targetCell).setValue(fullData);
    for (var i = 0; i < total; i++) {
      zSheet.getRange('D' + (i + 1)).clearContent();
    }
    return jsonpWrap_(JSON.stringify({ ok: true }), callback);
  }

  if (action === 'zercher_save_extra') {
    var extraData = e.parameter.data || '{}';
    JSON.parse(extraData); // validate
    zSheet.getRange('B1').setValue(extraData);
    return jsonpWrap_(JSON.stringify({ status: 'ok' }), callback);
  }

  if (action === 'zercher_log_workout') {
    var logData = e.parameter.data || '{}';
    var logObj = JSON.parse(logData);
    // Check for duplicate by ID
    var lastRow = zSheet.getLastRow();
    if (lastRow >= 2) {
      var existing = zSheet.getRange(2, 1, lastRow - 1, 1).getValues();
      for (var i = 0; i < existing.length; i++) {
        try {
          var ex = JSON.parse(existing[i][0]);
          if (ex.id === logObj.id) {
            zSheet.getRange(i + 2, 1).setValue(logData);
            return jsonpWrap_(JSON.stringify({ status: 'ok', updated: true }), callback);
          }
        } catch(err) {}
      }
    }
    zSheet.getRange(lastRow + 1, 1).setValue(logData);
    return jsonpWrap_(JSON.stringify({ status: 'ok' }), callback);
  }

  if (action === 'zercher_log_run') {
    var runData = e.parameter.data || '{}';
    var runObj = JSON.parse(runData);
    var lastRow = zSheet.getLastRow();
    var lastRunRow = 1;
    if (lastRow >= 2) {
      var existing = zSheet.getRange(2, 3, lastRow - 1, 1).getValues();
      for (var i = 0; i < existing.length; i++) {
        if (existing[i][0]) lastRunRow = i + 2;
        try {
          var ex = JSON.parse(existing[i][0]);
          if (ex.id === runObj.id) {
            zSheet.getRange(i + 2, 3).setValue(runData);
            return jsonpWrap_(JSON.stringify({ status: 'ok', updated: true }), callback);
          }
        } catch(err) {}
      }
    }
    var newRow = Math.max(lastRunRow + 1, 2);
    zSheet.getRange(newRow, 3).setValue(runData);
    return jsonpWrap_(JSON.stringify({ status: 'ok' }), callback);
  }

  if (action === 'zercher_load') {
    var config = {};
    var extra = {};
    var logs = [];
    var runLogs = [];
    var prs = {};
    try { config = JSON.parse(zSheet.getRange('A1').getValue() || '{}'); } catch(err) {}
    try { extra = JSON.parse(zSheet.getRange('B1').getValue() || '{}'); } catch(err) {}
    var lastRow = zSheet.getLastRow();
    if (lastRow >= 2) {
      var rows = zSheet.getRange(2, 1, lastRow - 1, 3).getValues();
      for (var i = 0; i < rows.length; i++) {
        try {
          var log = JSON.parse(rows[i][0]);
          logs.push(log);
        } catch(err) {}
        try {
          if (rows[i][2]) {
            var rlog = JSON.parse(rows[i][2]);
            runLogs.push(rlog);
          }
        } catch(err) {}
      }
    }
    return jsonpWrap_(JSON.stringify({ status: 'ok', config: config, extra: extra, logs: logs, runLogs: runLogs, prs: config.prs || {} }), callback);
  }

  return jsonpWrap_(JSON.stringify({ status: 'error', message: 'Unknown action' }), callback);
}
