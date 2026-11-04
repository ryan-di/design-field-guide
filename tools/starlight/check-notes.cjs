// node tools/starlight/check-notes.cjs [--base http://localhost:4321] [--only ch-a,ch-b] [--shots DIR]
// Checks the notes in site/annotations/ against the built pages. For each annotated comparison it fails on:
// notes that break the book's writing rules, selectors that match nothing, notes without "wait" whose element
// isn't showing at first, "wait" notes whose "reveal" steps don't bring their element out, numbers outside the
// comparison, demos wider than their column, and page errors. Reveal steps run inside that side's demo:
// ["click", sel], ["fill", sel, text], ["select", sel, value], ["press", sel, key], ["check", sel], ["hover", sel], ["wait", ms].
const fs = require('fs');
const path = require('path');
let chromium;
for (const p of ['@playwright/test', process.env.PW_PATH, '/Users/ryan/Documents/Comfy/ComfyUI_frontend/node_modules/@playwright/test'].filter(Boolean)) {
  try { ({ chromium } = require(p)); break; } catch (e) { /* try next */ }
}
if (!chromium) { console.error('Playwright not found: npm i -D @playwright/test, or set PW_PATH'); process.exit(2); }

const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const site = path.resolve(__dirname, '..', '..', 'site');
const base = arg('--base', 'http://localhost:4321').replace(/\/$/, '');
const only = (arg('--only', '') || '').split(',').filter(Boolean);
const shots = arg('--shots');
const anchors = JSON.parse(fs.readFileSync(path.join(site, 'public', 'anchors.json'), 'utf8'));
const dir = path.join(site, 'annotations');
const files = fs.readdirSync(dir).filter(f => f.endsWith('.json')).map(f => f.slice(0, -5)).filter(c => !only.length || only.includes(c));

const words = s => s.trim().split(/\s+/).length;
const lint = (where, n) => {
  const bad = [];
  for (const k of ['at', 'title', 'text']) if (typeof n[k] !== 'string' || !n[k].trim()) bad.push(`${where}: missing ${k}`);
  for (const k of ['title', 'text', 'wait']) {
    const v = n[k];
    if (typeof v !== 'string') continue;
    // Text quoted from the demo, inside “ ”, may keep its own "!" or ";".
    if (/[—–]/.test(v) || /[;!]/.test(v.replace(/“[^”]*”/g, ''))) bad.push(`${where}: ${k} uses a dash, semicolon or "!": ${v}`);
    if (/['"]/.test(v)) bad.push(`${where}: ${k} uses straight quotes: ${v}`);
    if (/\s{2,}|^\s|\s$/.test(v)) bad.push(`${where}: ${k} has stray spaces`);
  }
  if (n.title && words(n.title) > 8) bad.push(`${where}: title over 8 words: ${n.title}`);
  if (n.title && /[.]$/.test(n.title)) bad.push(`${where}: title ends with a period`);
  if (n.text && words(n.text) > 24) bad.push(`${where}: text over 24 words: ${n.text}`);
  if (n.text && !/[.?”’)…]$/.test(n.text)) bad.push(`${where}: text should end like a sentence`);
  if (n.wait && !/^[A-Z].*\.$/.test(n.wait)) bad.push(`${where}: wait should be one sentence, like "Pick Custom… to see this."`);
  if (n.wait && !Array.isArray(n.reveal)) bad.push(`${where}: wait without reveal steps`);
  if (n.reveal && !n.wait) bad.push(`${where}: reveal without wait`);
  return bad;
};

(async () => {
  const b = await chromium.launch();
  let fails = 0, cases = 0, notes = 0;
  const report = (m) => { fails++; console.log('  ✗ ' + m); };
  for (const ch of files) {
    const data = JSON.parse(fs.readFileSync(path.join(dir, ch + '.json'), 'utf8'));
    const slug = anchors[ch];
    console.log(`${ch} (${Object.keys(data).length} comparisons)`);
    if (!slug) { report(`${ch}: no such chapter`); continue; }
    for (const [key, c] of Object.entries(data)) {
      for (const tone of ['bad', 'good']) {
        const list = c[tone];
        if (!Array.isArray(list) || list.length < 1 || list.length > 4) report(`${key} ${tone}: wants 1 to 4 notes`);
        (list || []).forEach((n, i) => lint(`${key} ${tone} ${i + 1}`, n).forEach(report));
        const ats = (list || []).map(n => n.at);
        if (new Set(ats).size !== ats.length) report(`${key} ${tone}: two notes point at the same selector`);
      }
    }
    for (const [w, scheme] of [[1280, 'light'], [390, 'dark']]) {
      const ctx = await b.newContext({ viewport: { width: w, height: 900 }, colorScheme: scheme, deviceScaleFactor: shots ? 2 : 1 });
      const p = await ctx.newPage();
      const errs = [];
      p.on('pageerror', e => errs.push(e.message));
      p.on('console', m => { if (m.type() === 'error' || (m.type() === 'warning' && m.text().startsWith('annotated'))) errs.push(m.text()); });
      await p.goto(`${base}/${slug}/`, { waitUntil: 'networkidle' });
      await p.addStyleTag({ content: 'header.header, mobile-starlight-toc { display: none !important }' });
      await p.waitForTimeout(500);
      for (const [key, c] of Object.entries(data)) {
        const box = p.locator(`[data-ac="${key}"]`);
        if (!(await box.count())) { report(`${key}: not on the page (does the key match a comparison?)`); continue; }
        if (w === 1280) cases++;
        await box.scrollIntoViewIfNeeded();
        await p.waitForTimeout(150);
        const state = await box.evaluate(el => {
          const cr = el.getBoundingClientRect();
          return [...el.querySelectorAll('.ac-side')].map(s => {
            const d = s.querySelector('.cs-demo');
            return {
              overflow: d.scrollWidth - d.clientWidth,
              notes: [...s.querySelectorAll('.ac-note')].map((n, k) => {
                const pin = s.querySelectorAll('.ac-pin')[k];
                if (!pin) return { wait: true, count: 0, noPin: true };
                const r = pin.getBoundingClientRect();
                let count = 0;
                try { count = d.querySelectorAll(n.dataset.at).length; } catch (e) { count = -1; }
                return { wait: n.classList.contains('is-wait'), count, pinOut: !pin.hidden && (r.left < cr.left || r.right > cr.right || r.top < cr.top - 4 || r.bottom > cr.bottom + 4) };
              }),
            };
          });
        });
        for (const [si, tone] of [[0, 'bad'], [1, 'good']]) {
          const s = state[si], list = c[tone] || [];
          if (s.overflow > 1 && c.layout !== 'stack') report(`${key} ${tone} @${w}: demo is ${s.overflow}px wider than its column; try "layout": "stack"`);
          for (const [k, n] of list.entries()) {
            const st = s.notes[k], where = `${key} ${tone} ${k + 1} @${w}`;
            if (st.noPin) { report(`${where}: the annotation script didn't set up this side`); continue; }
            if (st.count < 0) { report(`${where}: invalid selector ${n.at}`); continue; }
            if (!n.wait && st.wait) report(`${where}: ${n.at} isn't showing at first (${st.count} matches); add "wait" and "reveal", or fix the selector`);
            if (st.pinOut) report(`${where}: the number sits outside the comparison`);
            if (n.wait && w === 1280) {
              const side = box.locator('.ac-side').nth(si), demo = side.locator('.cs-demo');
              await side.locator('.cs-reset').click();
              await p.waitForTimeout(100);
              try {
                for (const [op, sel, v] of n.reveal) {
                  const t = () => demo.locator(sel).first();
                  if (op === 'wait') await p.waitForTimeout(sel);
                  else if (op === 'click') await t().click({ timeout: 2000 });
                  else if (op === 'fill') await t().fill(v, { timeout: 2000 });
                  else if (op === 'select') await t().selectOption(v, { timeout: 2000 });
                  else if (op === 'press') await t().press(v, { timeout: 2000 });
                  else if (op === 'check') await t().check({ timeout: 2000 });
                  else if (op === 'hover') await t().hover({ timeout: 2000 });
                  else throw new Error('unknown step ' + op);
                }
                await p.waitForTimeout(250);
                const ok = await side.locator('.ac-note').nth(k).evaluate(el => !el.classList.contains('is-wait'));
                if (!ok) report(`${where}: after the reveal steps ${n.at} still isn't showing`);
              } catch (e) { report(`${where}: reveal step failed: ${e.message.split('\n')[0]}`); }
              await side.locator('.cs-reset').click();
              await p.mouse.move(0, 0);
            }
            if (w === 1280) notes++;
          }
        }
        if (shots && w === 1280) {
          fs.mkdirSync(shots, { recursive: true });
          await box.screenshot({ path: path.join(shots, `${key}.png`) });
        }
      }
      errs.forEach(e => report(`${ch} @${w}: ${e}`));
      await ctx.close();
    }
  }
  await b.close();
  console.log(`\n${cases} comparisons, ${notes} notes, ${fails ? fails + ' problems' : 'all OK'}`);
  process.exit(fails ? 1 : 0);
})();
