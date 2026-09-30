// Runs the real apps_script.gs in Node with in-memory fakes for the Google
// services it uses (Sheets, locks, text output). Same idea as Cadence/tests.
const fs = require('fs');
const vm = require('vm');

function makeSheet(name) {
  const cells = new Map();
  const key = (r, c) => r + ':' + c;
  function a1(s) {
    const m = /^([A-Z]+)(\d+)$/.exec(s);
    let c = 0;
    for (const ch of m[1]) c = c * 26 + (ch.charCodeAt(0) - 64);
    return [Number(m[2]), c];
  }
  // Sheets turns number-looking text into numbers; JSON cells stay text.
  function convert(v) {
    if (typeof v === 'string' && /^[+-]?\d+(\.\d+)?$/.test(v.trim())) return Number(v);
    return v;
  }
  function range(r, c, nr = 1, nc = 1) {
    return {
      getValue() { const v = cells.get(key(r, c)); return v === undefined ? '' : v; },
      getValues() {
        const out = [];
        for (let i = 0; i < nr; i++) {
          const row = [];
          for (let j = 0; j < nc; j++) { const v = cells.get(key(r + i, c + j)); row.push(v === undefined ? '' : v); }
          out.push(row);
        }
        return out;
      },
      setValue(v) { cells.set(key(r, c), convert(v)); return this; },
      setValues(vals) {
        for (let i = 0; i < nr; i++) for (let j = 0; j < nc; j++) cells.set(key(r + i, c + j), convert(vals[i][j]));
        return this;
      },
      clearContent() {
        for (let i = 0; i < nr; i++) for (let j = 0; j < nc; j++) cells.delete(key(r + i, c + j));
        return this;
      },
    };
  }
  const sheet = {
    name, cells,
    getRange(a, b, c, d) {
      if (typeof a === 'string') { const [r, col] = a1(a); return range(r, col); }
      return range(a, b, c, d);
    },
    getLastRow() { let m = 0; for (const k of cells.keys()) m = Math.max(m, Number(k.split(':')[0])); return m; },
    getLastColumn() { let m = 0; for (const k of cells.keys()) m = Math.max(m, Number(k.split(':')[1])); return m; },
    appendRow(vals) { const r = sheet.getLastRow() + 1; vals.forEach((v, j) => cells.set(key(r, j + 1), convert(v))); return sheet; },
    deleteRow(row) {
      const moved = new Map();
      for (const [k, v] of cells) {
        const [r, c] = k.split(':').map(Number);
        if (r < row) moved.set(k, v);
        else if (r > row) moved.set((r - 1) + ':' + c, v);
      }
      cells.clear();
      for (const [k, v] of moved) cells.set(k, v);
    },
  };
  return sheet;
}

function loadGas(file) {
  const sheets = new Map();
  const ss = {
    getSheetByName(n) { return sheets.get(n) || null; },
    insertSheet(n) { const s = makeSheet(n); sheets.set(n, s); return s; },
  };
  const ctx = {
    SpreadsheetApp: { getActiveSpreadsheet: () => ss, flush() {} },
    LockService: { getScriptLock: () => ({ waitLock() {}, tryLock() { return true; }, releaseLock() {} }) },
    ContentService: {
      MimeType: { JSON: 'json', JAVASCRIPT: 'js' },
      createTextOutput(t) { return { _t: t, setMimeType() { return this; }, getContent() { return this._t; } }; },
    },
    console,
  };
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(file, 'utf8'), ctx, { filename: file });
  return {
    ctx, sheets,
    // Same as hitting the web app: returns the response body text.
    doGet(params) { return ctx.doGet({ parameter: params }).getContent(); },
    call(params) { return JSON.parse(ctx.doGet({ parameter: params }).getContent()); },
  };
}

module.exports = { loadGas };
