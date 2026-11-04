// node tools/check.cjs [--file index.html | --url https://…] [--shots DIR] [--write-ids FILE] [--hash id,id,…]
// Loads the book in light/dark at 1280px and 390px and fails on: page errors, console errors, contents links
// that don't open, missing ids from tools/ids-baseline.txt, empty demos, rule switches that don't switch,
// horizontal overflow, deep links that don't land. With --shots it saves screenshots of fixed spots per theme/width.
// Checking a local file also runs tools/export.py --check, so exports that lag behind index.html fail too.
const path = require('path');
const fs = require('fs');
let chromium;
for (const p of ['@playwright/test', process.env.PW_PATH, '/Users/ryan/Documents/Comfy/ComfyUI_frontend/node_modules/@playwright/test'].filter(Boolean)) {
  try { ({ chromium } = require(p)); break; } catch (e) { /* try next */ }
}
if (!chromium) { console.error('Playwright not found: npm i -D @playwright/test, or set PW_PATH'); process.exit(2); }

const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const root = path.resolve(__dirname, '..');
const url = arg('--url') || 'file://' + path.resolve(root, arg('--file', 'index.html'));
const shots = arg('--shots');
const writeIds = arg('--write-ids');
const hashes = (arg('--hash', '') || '').split(',').filter(Boolean);
const SPOTS = ['top', 'part-1', 'good-problem-framing', 'good-heuristic-review', 'ch-patterns-cheat', 'toast', 'ch-choose', 'eff-loop', 'eff-brief', 'eff-worked-example', 'ch-eff-checklist'];
const extraSpots = (arg('--spots', '') || '').split(',').filter(Boolean);
const CONFIGS = [[1280, 'light'], [1280, 'dark'], [390, 'light'], [390, 'dark']];

(async () => {
  const b = await chromium.launch();
  let failed = 0;
  const baseline = fs.existsSync(path.join(__dirname, 'ids-baseline.txt')) ? fs.readFileSync(path.join(__dirname, 'ids-baseline.txt'), 'utf8').split('\n').filter(Boolean) : [];
  for (const [w, scheme] of CONFIGS) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, colorScheme: scheme });
    const p = await ctx.newPage();
    const errs = [];
    p.on('pageerror', e => errs.push('pageerror: ' + e.message));
    p.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
    await p.goto(url, { waitUntil: 'load' });
    await p.waitForTimeout(600);
    if (writeIds && w === 1280 && scheme === 'light') {
      const ids = await p.evaluate(() => [...new Set([...document.querySelectorAll('[id]')].map(e => e.id))].sort());
      fs.writeFileSync(writeIds, ids.join('\n') + '\n');
      console.log('wrote', ids.length, 'ids to', writeIds);
    }
    const r = await p.evaluate(async (baseline) => {
      const out = { bad: [] };
      const toc = [...document.querySelectorAll('#toc-list a[href^="#"]')];
      out.toc = toc.length;
      toc.forEach(a => { const t = document.getElementById(a.getAttribute('href').slice(1)); if (!t || !t.getClientRects().length) out.bad.push('toc ' + a.getAttribute('href')); });
      const links = [...document.querySelectorAll('main a[href^="#"]')].filter(a => !a.closest('.cs-demo, .fm-stage, .stage, .cw') && a.getAttribute('href').length > 1);
      out.links = links.length;
      links.forEach(a => { const id = decodeURIComponent(a.getAttribute('href').slice(1)); if (!document.getElementById(id)) out.bad.push('link #' + id); });
      out.missingIds = baseline.filter(id => !document.getElementById(id));
      const dup = {}; document.querySelectorAll('[id]').forEach(e => { dup[e.id] = (dup[e.id] || 0) + 1; });
      out.dupIds = Object.keys(dup).filter(k => dup[k] > 1 && !/^(p\d+|fm|cw|d)-/.test(k)).slice(0, 20);
      const cases = [...document.querySelectorAll('.cs-case')];
      out.cases = cases.length;
      for (const c of cases) {
        const demos = [...c.querySelectorAll('.cs-demo')];
        if (demos.some(d => !d.innerHTML.trim())) out.bad.push('empty demo ' + (c.getAttribute('aria-label') || '?'));
        const fixed = c.querySelector('.cs-switch [data-mode="fixed"]');
        if (fixed) { fixed.click(); const side = c.querySelector('.cs-side[data-mode="fixed"]'); if (!side || side.hidden) out.bad.push('switch ' + c.getAttribute('aria-label')); c.querySelector('.cs-switch [data-mode="broken"]').click(); }
      }
      let cw = 0;
      for (const wr of document.querySelectorAll('.cw-wrap')) for (const rr of wr.querySelectorAll('.cw-seg input')) { rr.checked = true; rr.dispatchEvent(new Event('change', { bubbles: true })); cw++; const v = wr.querySelector('[data-cw-view]'); if (!v || !v.innerHTML.trim()) out.bad.push('cw ' + (wr.closest('.entry,.chapter') || {}).id); }
      out.cw = cw;
      let fm = 0;
      for (const f of document.querySelectorAll('[data-fm]')) for (const rr of f.querySelectorAll('.fm-seg input')) { rr.checked = true; rr.dispatchEvent(new Event('change', { bubbles: true })); fm++; const st = f.querySelector('[data-fm-stage]'); if (!st || !st.innerHTML.trim()) out.bad.push('forms ' + (f.closest('.entry') || {}).id); }
      out.fm = fm;
      out.stages = document.querySelectorAll('.stage').length;
      out.entries = document.querySelectorAll('[data-entry]').length;
      out.sw = document.documentElement.scrollWidth; out.vw = innerWidth;
      out.mode = document.compatMode;
      return out;
    }, baseline);
    // Click a contents link and a rule link the way a reader would.
    const jumpOk = await p.evaluate(() => {
      const a = document.querySelector('#toc-list a[href="#ch-critique"]') || document.querySelector('#toc-list a');
      a.click();
      const t = document.getElementById(a.getAttribute('href').slice(1)).getBoundingClientRect().top;
      return Math.abs(t) < 140;
    });
    if (!jumpOk) r.bad.push('contents click did not land');
    const deep = [];
    for (const h of hashes) {
      const p2 = await ctx.newPage();
      p2.on('pageerror', e => errs.push('pageerror(' + h + '): ' + e.message));
      await p2.goto(url + '#' + h, { waitUntil: 'load' });
      await p2.waitForTimeout(1600);
      const top = await p2.evaluate(h => { const t = document.getElementById(h); return t ? Math.round(t.getBoundingClientRect().top) : null; }, h);
      if (top === null || top < -10 || top > 160) deep.push(h + '@' + top);
      await p2.close();
    }
    if (shots) {
      const dir = path.join(shots, w + '-' + scheme);
      fs.mkdirSync(dir, { recursive: true });
      for (const s of SPOTS.concat(extraSpots)) {
        const ok = await p.evaluate(s => { const t = document.getElementById(s); if (!t) return false; t.scrollIntoView({ block: 'start' }); return true; }, s);
        if (!ok) continue;
        await p.waitForTimeout(120);
        await p.screenshot({ path: path.join(dir, s + '.png') });
      }
    }
    // Demos that read their lists from the text: make sure each still works.
    const probe = await p.evaluate(() => {
      const bad = [], q = s => document.querySelector(s);
      const rubrics = [...document.querySelectorAll('[data-rubric]')];
      rubrics.forEach(t => { if (!t.querySelector('tbody tr')) bad.push('empty rubric ' + t.id); });
      const rough = q('#p26-br-rough');
      if (rough) {
        rough.checked = true; rough.dispatchEvent(new Event('change', { bubbles: true }));
        const t = q('#p26-br-list').textContent;
        ['Missing', 'Vague', 'Too broad', 'Solution'].forEach(f => { if (!t.includes(f)) bad.push('brief check lacks ' + f); });
      }
      const sc = q('#p18-sc-text');
      if (sc) { sc.value = 'the new checkout feels easier, cleaner and more intuitive'; sc.dispatchEvent(new Event('input')); if (q('#p18-sc-sugs').children.length !== 2) bad.push('success criteria rewrites ' + q('#p18-sc-sugs').children.length); }
      if (q('#p25-d-name') && !(q('#p25-d-name').textContent.trim() && q('#p25-d-in').textContent.trim())) bad.push('loop stage empty');
      if (q('#p25-bars') && !/[a-z]{4}/.test(q('#p25-bars').textContent)) bad.push('ownership notes empty');
      const shorts = document.querySelectorAll('.in-short');
      const shortRules = document.querySelectorAll('.in-short ol a').length, rules = document.querySelectorAll('section.rule[id]').length;
      if (shorts.length && (shorts.length !== 31 || shortRules !== rules)) bad.push('in short: ' + shorts.length + ' boxes, ' + shortRules + ' of ' + rules + ' rules');
      return { bad, rubrics: rubrics.length };
    });
    r.bad.push(...probe.bad);
    r.rubrics = probe.rubrics;
    const overflow = r.sw > r.vw + 1;
    const bad = r.bad.length + r.missingIds.length + errs.length + deep.length + (overflow ? 1 : 0) + r.dupIds.length;
    if (bad) failed++;
    console.log(`${w} ${scheme} ${r.mode}: toc ${r.toc}, links ${r.links}, entries ${r.entries}, demos ${r.stages}, rule switches ${r.cases}, cw ${r.cw}, forms ${r.fm}, rubrics ${r.rubrics}, width ${r.sw}/${r.vw}` +
      (bad ? `\n  FAIL bad=${JSON.stringify(r.bad.slice(0, 15))} missingIds=${JSON.stringify(r.missingIds.slice(0, 15))} (${r.missingIds.length}) dupIds=${JSON.stringify(r.dupIds)} deep=${JSON.stringify(deep)} errors=${JSON.stringify(errs.slice(0, 10))}` : '  OK'));
    await ctx.close();
  }
  await b.close();
  if (!arg('--url')) {
    const ex = require('child_process').spawnSync('python3', [path.join(__dirname, 'export.py'), '--check'], { encoding: 'utf8' });
    process.stdout.write('exports: ' + (ex.stdout || '') + (ex.stderr || ''));
    if (ex.status !== 0) failed++;
  }
  process.exit(failed ? 1 : 0);
})();
