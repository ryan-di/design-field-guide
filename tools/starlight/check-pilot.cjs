// node tools/starlight/check-pilot.cjs [--base http://localhost:4321] [--shots DIR]
// Compares each pilot page with the same chapter in index.html: ids, demo counts, rendered demo size after load,
// and errors while every rule switch, segmented control and stage button is clicked. Light/dark at 1280px and 390px.
const path = require('path');
const fs = require('fs');
let chromium;
for (const p of ['@playwright/test', process.env.PW_PATH, '/Users/ryan/Documents/Comfy/ComfyUI_frontend/node_modules/@playwright/test'].filter(Boolean)) {
  try { ({ chromium } = require(p)); break; } catch (e) { /* try next */ }
}
if (!chromium) { console.error('Playwright not found'); process.exit(2); }

const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const root = path.resolve(__dirname, '../..');
const base = arg('--base', 'http://localhost:4321');
const shots = arg('--shots');
const book = 'file://' + path.join(root, 'index.html');
const only = (arg('--only', '') || '').split(',').filter(Boolean);
const PAGES = JSON.parse(fs.readFileSync(path.join(root, 'site/src/sidebar.json'), 'utf8'))
  .flatMap(g => g.items).filter(i => i.slug).map(i => ['ch-' + i.slug.split('/').pop(), '/' + i.slug + '/'])
  .filter(([ch]) => !only.length || only.includes(ch));
const CONFIGS = arg('--quick') !== undefined || process.argv.includes('--quick') ? [[1280, 'light']] : [[1280, 'light'], [1280, 'dark'], [390, 'light']];

const survey = (scope) => {
  const el = scope ? document.getElementById(scope) : document.querySelector('main');
  const ids = [...el.querySelectorAll('[id]')].map(e => e.id).concat(el.id ? [el.id] : []);
  const size = s => [...el.querySelectorAll(s)].map(d => d.innerHTML.length);
  return {
    ids: [...new Set(ids)],
    stages: size('[data-demo]'),
    cases: el.querySelectorAll('.cs-case').length,
    cw: el.querySelectorAll('.cw-wrap').length,
    rules: el.querySelectorAll('section.rule[id]').length,
  };
};

const exercise = () => {
  const bad = [];
  const main = document.querySelector('main') || document.body;
  for (const c of main.querySelectorAll('.cs-case')) {
    const fixed = c.querySelector('.cs-switch [data-mode="fixed"]');
    if (!fixed) continue;
    fixed.click();
    const side = c.querySelector('.cs-side[data-mode="fixed"]');
    if (!side || side.hidden || !side.getClientRects().length) bad.push('switch ' + c.getAttribute('aria-label'));
    c.querySelector('.cs-switch [data-mode="broken"]').click();
  }
  for (const wr of main.querySelectorAll('.cw-wrap')) for (const r of wr.querySelectorAll('.cw-seg input')) {
    r.checked = true; r.dispatchEvent(new Event('change', { bubbles: true }));
    const v = wr.querySelector('[data-cw-view]');
    if (!v || !v.innerHTML.trim()) bad.push('cw view empty ' + (wr.closest('.entry') || {}).id);
  }
  let clicks = 0;
  for (const st of main.querySelectorAll('[data-demo]')) for (const b of st.querySelectorAll('button:not([disabled])')) { b.click(); clicks++; }
  return { bad, clicks };
};

(async () => {
  const b = await chromium.launch();
  let failed = 0;
  for (const [w, scheme] of CONFIGS) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, colorScheme: scheme });
    const ref = await ctx.newPage();
    await ref.goto(book, { waitUntil: 'load' });
    await ref.waitForTimeout(500);
    for (const [ch, route] of PAGES) {
      const want = await ref.evaluate(survey, ch);
      const p = await ctx.newPage();
      const errs = [];
      p.on('pageerror', e => errs.push('pageerror: ' + e.message));
      p.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
      await p.goto(base + route, { waitUntil: 'load' });
      await p.waitForTimeout(800);
      const got = await p.evaluate(survey, ch);
      const bad = [];
      const missing = want.ids.filter(id => !got.ids.includes(id));
      if (missing.length) bad.push(`missing ids (${missing.length}): ${missing.slice(0, 12).join(' ')}`);
      for (const k of ['cases', 'cw', 'rules']) if (want[k] !== got[k]) bad.push(`${k} ${got[k]}/${want[k]}`);
      if (want.stages.length !== got.stages.length) bad.push(`stages ${got.stages.length}/${want.stages.length}`);
      want.stages.forEach((n, i) => { const g = got.stages[i] || 0; if (Math.abs(g - n) > Math.max(40, n * 0.1)) bad.push(`stage ${i} html ${g} vs ${n}`); });
      const dup = await p.evaluate(() => { const d = {}; document.querySelectorAll('[id]').forEach(e => { d[e.id] = (d[e.id] || 0) + 1; }); return Object.keys(d).filter(k => d[k] > 1); });
      if (dup.length) bad.push('duplicate ids: ' + dup.slice(0, 10).join(' '));
      const links = await p.evaluate(() => [...document.querySelectorAll('main a[href^="#"]')].map(a => decodeURIComponent(a.getAttribute('href').slice(1))).filter(id => id && !document.getElementById(id)));
      if (links.length) bad.push('dead in-page links: ' + links.slice(0, 10).join(' '));
      const ex = await p.evaluate(exercise);
      bad.push(...ex.bad);
      await p.waitForTimeout(300);
      const learned = await p.evaluate(() => { const i = document.querySelector('[data-learned]'); if (!i) return 'none'; i.click(); return i.checked; });
      await p.reload({ waitUntil: 'load' });
      await p.waitForTimeout(500);
      const kept = await p.evaluate(() => { const i = document.querySelector('[data-learned]'); if (!i) return 'none'; const v = i.checked; if (v) i.click(); return v; });
      if (learned !== 'none' && kept !== true) bad.push('learned did not persist');
      const sw = await p.evaluate(() => [document.documentElement.scrollWidth, innerWidth]);
      if (sw[0] > sw[1] + 1) bad.push('horizontal overflow ' + sw.join('/'));
      if (shots) {
        const dir = path.join(shots, w + '-' + scheme);
        fs.mkdirSync(dir, { recursive: true });
        const name = route.replace(/\W+/g, '-').replace(/^-|-$/g, '');
        await p.evaluate(() => scrollTo(0, 0));
        await p.screenshot({ path: path.join(dir, name + '-top.png') });
        for (const s of ['good-needs-hierarchy', 'good-needs-hierarchy-rules', 'good-problem-framing', 'good-success-criteria', 'ch-problem-in-short']) {
          const ok = await p.evaluate(s => { const t = document.getElementById(s); if (!t) return false; t.scrollIntoView({ block: 'start' }); return true; }, s);
          if (!ok) continue;
          await p.waitForTimeout(150);
          await p.screenshot({ path: path.join(dir, name + '-' + s + '.png') });
        }
      }
      const all = bad.length + errs.length;
      if (all) failed++;
      console.log(`${w} ${scheme} ${route}: ids ${got.ids.length}/${want.ids.length}, stages ${got.stages.length}, switches ${got.cases}, cw ${got.cw}, rules ${got.rules}, clicks ${ex.clicks}` +
        (all ? `\n  FAIL ${JSON.stringify(bad)}\n  errors ${JSON.stringify(errs.slice(0, 8))}` : '  OK'));
      await p.close();
    }
    await ctx.close();
  }
  // Old one-page links (/#id) should land on the id in its new page, below the sticky header.
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } });
  const p = await ctx.newPage();
  for (const [id, want] of [['good-problem-framing-rule-2', '/part-1/problem/'], ['ch-problem-in-short', '/part-1/problem/'], ['ch-preface', '/front/preface/'], ['good-visual-hierarchy', '/part-1/clarity/'], ['part-3', '/part-3/start/']]) {
    await p.goto(base + '/#' + id, { waitUntil: 'load' }).catch(() => {});
    await p.waitForTimeout(1200);
    const at = p.url();
    const [top, end] = want.startsWith('/') ? await p.evaluate(id => {
      const t = document.getElementById(id);
      return [t ? Math.round(t.getBoundingClientRect().top) : null, Math.ceil(scrollY + innerHeight) >= document.documentElement.scrollHeight - 2];
    }, id) : [0, false];
    const ok = at.includes(want) && at.endsWith('#' + id) && top !== null && top >= 0 && (top < 160 || end);
    if (!ok) failed++;
    console.log(`/#${id} -> ${at.replace(base, '')} top ${top}  ${ok ? 'OK' : 'FAIL'}`);
  }
  await ctx.close();
  await b.close();
  process.exit(failed ? 1 : 0);
})();
