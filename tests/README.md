# Book Notes app tests

Headless tests for the shelf (`index.html`), `book.js`, the offline service
worker (`service-worker.js`) and the sync backend (`apps_script.gs`).
Run them before changing any of those files.

```
cd tests
npm install            # puppeteer-core only; it drives the Chrome you already have
node sync_test.js      # merge rules, backend, shelf/book sync, glossary (~1 min)
node offline_test.js   # save the library, then read it with no connection (~30 s)
node pages_test.js     # every shelf page loads without a JavaScript error (~2 min)
```

- `server.js` serves this folder on localhost with `SYNC_URL` pointed at a local
  copy of the real `apps_script.gs` (run by `gas_harness.js`). Switches:
  `/__offline?on=1`, `/__slow?ms=`, `/__delay?action=&ms=`, `/__patch?path=&marker=`.
- Chrome is started with every host except localhost unreachable, so a test can
  never touch the real backend or your reading data.
- `BOOKS_ROOT=/path/to/old/checkout node sync_test.js` runs the same checks
  against another version (used to confirm each test fails on the old code).
- The merge rules exist three times (`book.js`, `index.html`, `apps_script.gs`);
  `sync_test.js` fails if they ever disagree.

`apps_script.gs` is a copy of the deployed script. The deploy copy lives in
`Documents/Code/Claude/.clasp/books/Code.js`; keep the two identical.
