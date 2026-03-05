// Books & Zercher Sync — Google Apps Script
// Deploy as Web App: Execute as Me, Access: Anyone
//
// Books Actions:
//   ?action=get_read            → returns { status:"ok", books_read: { ... } }
//   ?action=set_read&data=      → saves JSON string to Settings!A1
//   ?action=get_bookmarks       → returns { status:"ok", bookmarks: { ... } }
//   ?action=set_bookmark&key=&data= → merges single bookmark into Bookmarks!A1
//
// Zercher Actions:
//   ?action=zercher_save_config&data=  → saves config JSON to Zercher!A1
//   ?action=zercher_log_workout&data=  → appends workout log to Zercher!A2+
//   ?action=zercher_save_extra&data=   → saves holds/notes/starts to Zercher!B1
//   ?action=zercher_load               → returns all zercher data

function doGet(e) {
  var action = (e.parameter.action || '').toLowerCase();
  var ss = SpreadsheetApp.getActiveSpreadsheet();

  // ── BOOKS ──
  if (action === 'get_read' || action === 'set_read') {
    var sheet = ss.getSheetByName('Settings');
    if (!sheet) sheet = ss.insertSheet('Settings');

    if (action === 'get_read') {
      var raw = sheet.getRange('A1').getValue() || '{}';
      return ContentService.createTextOutput(
        JSON.stringify({ status: 'ok', books_read: JSON.parse(raw) })
      ).setMimeType(ContentService.MimeType.JSON);
    }

    if (action === 'set_read') {
      var data = e.parameter.data || '{}';
      JSON.parse(data);
      sheet.getRange('A1').setValue(data);
      return ContentService.createTextOutput(
        JSON.stringify({ status: 'ok' })
      ).setMimeType(ContentService.MimeType.JSON);
    }
  }

  // ── BOOKMARKS ──
  if (action === 'get_bookmarks' || action === 'set_bookmark') {
    var bmSheet = ss.getSheetByName('Bookmarks');
    if (!bmSheet) bmSheet = ss.insertSheet('Bookmarks');

    if (action === 'get_bookmarks') {
      var raw = bmSheet.getRange('A1').getValue() || '{}';
      return ContentService.createTextOutput(
        JSON.stringify({ status: 'ok', bookmarks: JSON.parse(raw) })
      ).setMimeType(ContentService.MimeType.JSON);
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
      return ContentService.createTextOutput(
        JSON.stringify({ status: 'ok' })
      ).setMimeType(ContentService.MimeType.JSON);
    }
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
    return ContentService.createTextOutput(
      JSON.stringify({ status: 'ok' })
    ).setMimeType(ContentService.MimeType.JSON);
  }

  if (action === 'zercher_save_extra') {
    var extraData = e.parameter.data || '{}';
    JSON.parse(extraData); // validate
    zSheet.getRange('B1').setValue(extraData);
    return ContentService.createTextOutput(
      JSON.stringify({ status: 'ok' })
    ).setMimeType(ContentService.MimeType.JSON);
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
            // Already exists, update in place
            zSheet.getRange(i + 2, 1).setValue(logData);
            return ContentService.createTextOutput(
              JSON.stringify({ status: 'ok', updated: true })
            ).setMimeType(ContentService.MimeType.JSON);
          }
        } catch(err) {}
      }
    }
    // Append new
    zSheet.getRange(lastRow + 1, 1).setValue(logData);
    return ContentService.createTextOutput(
      JSON.stringify({ status: 'ok' })
    ).setMimeType(ContentService.MimeType.JSON);
  }

  if (action === 'zercher_load') {
    var config = {};
    var extra = {};
    var logs = [];
    var prs = {};
    try { config = JSON.parse(zSheet.getRange('A1').getValue() || '{}'); } catch(err) {}
    try { extra = JSON.parse(zSheet.getRange('B1').getValue() || '{}'); } catch(err) {}
    var lastRow = zSheet.getLastRow();
    if (lastRow >= 2) {
      var rows = zSheet.getRange(2, 1, lastRow - 1, 1).getValues();
      for (var i = 0; i < rows.length; i++) {
        try {
          var log = JSON.parse(rows[i][0]);
          logs.push(log);
        } catch(err) {}
      }
    }
    return ContentService.createTextOutput(
      JSON.stringify({ status: 'ok', config: config, extra: extra, logs: logs, prs: config.prs || {} })
    ).setMimeType(ContentService.MimeType.JSON);
  }

  return ContentService.createTextOutput(
    JSON.stringify({ status: 'error', message: 'Unknown action' })
  ).setMimeType(ContentService.MimeType.JSON);
}
