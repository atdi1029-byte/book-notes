// Books Read Sync — Google Apps Script
// Deploy as Web App: Execute as Me, Access: Anyone
//
// Actions:
//   ?action=get_read        → returns { status:"ok", books_read: { ... } }
//   ?action=set_read&data=  → saves JSON string to Settings!A1

function doGet(e) {
  var action = (e.parameter.action || '').toLowerCase();
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('Settings');
  if (!sheet) {
    sheet = ss.insertSheet('Settings');
  }

  if (action === 'get_read') {
    var raw = sheet.getRange('A1').getValue() || '{}';
    return ContentService.createTextOutput(
      JSON.stringify({ status: 'ok', books_read: JSON.parse(raw) })
    ).setMimeType(ContentService.MimeType.JSON);
  }

  if (action === 'set_read') {
    var data = e.parameter.data || '{}';
    // Validate it's proper JSON
    JSON.parse(data);
    sheet.getRange('A1').setValue(data);
    return ContentService.createTextOutput(
      JSON.stringify({ status: 'ok' })
    ).setMimeType(ContentService.MimeType.JSON);
  }

  return ContentService.createTextOutput(
    JSON.stringify({ status: 'error', message: 'Unknown action' })
  ).setMimeType(ContentService.MimeType.JSON);
}
