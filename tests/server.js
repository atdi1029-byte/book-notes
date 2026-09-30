// Local copy of the site for the tests.
//   /…            files from the Books folder, with SYNC_URL pointed at /exec
//   /exec?…       the real apps_script.gs (in gas_harness), JSONP like Google
// Switches (all return "ok"):
//   /__offline?on=1|0          drop every request, like having no connection
//   /__slow?ms=6000            delay every file response
//   /__delay?action=…&ms=…&n=1 delay the next n calls of one backend action
//   /__patch?path=…&marker=…   append <!--marker--> to that file from now on
//   /__reset                   fresh backend, clear switches
//   /__log                     backend calls so far (JSON)
const http = require('http');
const fs = require('fs');
const path = require('path');
const { loadGas } = require('./gas_harness');

// BOOKS_ROOT lets the tests run against another checkout (e.g. an old version).
const ROOT = process.env.BOOKS_ROOT || path.resolve(__dirname, '..');
const GAS_FILE = path.join(ROOT, 'apps_script.gs');
const TYPES = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css',
  '.json': 'application/json', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.png': 'image/png', '.gif': 'image/gif', '.webp': 'image/webp', '.svg': 'image/svg+xml',
};

function start(port) {
  let gas = loadGas(GAS_FILE);
  let offline = false, slowMs = 0;
  const delay = {}, patches = {}, log = [];
  const execUrl = 'http://localhost:' + port + '/exec';

  const server = http.createServer((req, res) => {
    const u = new URL(req.url, 'http://localhost');
    const q = Object.fromEntries(u.searchParams);
    const ok = () => { res.writeHead(200); res.end('ok'); };

    if (u.pathname === '/__offline') { offline = q.on === '1'; return ok(); }
    if (u.pathname === '/__slow') { slowMs = Number(q.ms || 0); return ok(); }
    if (u.pathname === '/__delay') { delay[q.action] = { ms: Number(q.ms), n: Number(q.n || 1) }; return ok(); }
    if (u.pathname === '/__patch') { patches[q.path] = q.marker; return ok(); }
    if (u.pathname === '/__reset') {
      gas = loadGas(GAS_FILE); offline = false; slowMs = 0; log.length = 0;
      for (const k in delay) delete delay[k];
      for (const k in patches) delete patches[k];
      return ok();
    }
    if (u.pathname === '/__log') { res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify(log)); return; }

    if (offline) { req.socket.destroy(); return; }

    if (u.pathname === '/exec') {
      const action = String(q.action || '').toLowerCase();
      let wait = 20;
      if (delay[action] && delay[action].n > 0) { delay[action].n--; wait += delay[action].ms; }
      setTimeout(() => {
        const text = gas.doGet(q);
        log.push({ action, params: q, t: Date.now() });
        res.writeHead(200, { 'Content-Type': 'text/javascript' });
        res.end(text);
      }, wait);
      return;
    }

    let rel = decodeURIComponent(u.pathname).replace(/^\/+/, '');
    if (rel === '' || rel.endsWith('/')) rel += 'index.html';
    const file = path.join(ROOT, rel);
    if (!file.startsWith(ROOT) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
      if (fs.existsSync(file) && fs.statSync(file).isDirectory()) {
        res.writeHead(301, { Location: u.pathname + '/' }); res.end(); return;
      }
      res.writeHead(404); res.end('not found'); return;
    }
    setTimeout(() => {
      let body = fs.readFileSync(file);
      const ext = path.extname(file).toLowerCase();
      if (ext === '.html' || ext === '.js') {
        body = body.toString().replace(/var SYNC_URL = '[^']*';/g, "var SYNC_URL = '" + execUrl + "';");
        if (patches[rel]) body += '\n<!--' + patches[rel] + '-->\n';
      }
      res.writeHead(200, { 'Content-Type': TYPES[ext] || 'application/octet-stream', 'Cache-Control': 'no-cache' });
      res.end(body);
    }, slowMs);
  });

  return new Promise(resolve => server.listen(port, () => resolve({
    base: 'http://localhost:' + port + '/',
    get gas() { return gas; },
    log,
    close: () => new Promise(r => { server.closeAllConnections(); server.close(r); }),
  })));
}

module.exports = { start };
