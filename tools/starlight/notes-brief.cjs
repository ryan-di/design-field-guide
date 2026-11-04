// node tools/starlight/notes-brief.cjs OUTDIR [--base http://localhost:4321] [--only ch-a,ch-b]
// Writes one Markdown brief per chapter for drafting site/annotations/: each comparison's rule, captions, where its
// demo code sits in index.html, and both demos' rendered markup at first load, to pick selectors from.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
let chromium;
for (const p of ['@playwright/test', process.env.PW_PATH, '/Users/ryan/Documents/Comfy/ComfyUI_frontend/node_modules/@playwright/test'].filter(Boolean)) {
  try { ({ chromium } = require(p)); break; } catch (e) { /* try next */ }
}
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const out = process.argv[2];
const base = arg('--base', 'http://localhost:4321').replace(/\/$/, '');
const only = (arg('--only', '') || '').split(',').filter(Boolean);
const root = path.resolve(__dirname, '..', '..');
const book = fs.readFileSync(path.join(root, 'index.html'), 'utf8').split('\n');
const lineOf = s => book.findIndex(l => l.includes(s)) + 1;
const chapters = JSON.parse(execFileSync('python3', ['-c', `
import sys, json; sys.path.insert(0, 'tools/starlight')
import convert as c
b = c.Book()
print(json.dumps([[ch.get('id'), b.slug(ch), [c.case_key(x) for x in ch.iter() if 'cs-case' in x.cls]] for ch in b.chapters]))
`], { cwd: root, encoding: 'utf8' })).filter(([id, , keys]) => keys.length && (!only.length || only.includes(id)));

(async () => {
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
  for (const [id, slug, keys] of chapters) {
    await p.goto(`${base}/${slug}/`, { waitUntil: 'networkidle' });
    await p.waitForTimeout(600);
    const cases = await p.evaluate(keys => keys.map(key => {
      const demo = side => document.querySelector(`.cs-demo[data-d="${key}${side}"]`);
      const cs = demo('b').closest('.cs-case'), rule = cs.closest('.rule');
      const keep = /^(class|id|role|type|hidden|disabled|checked|selected|value|placeholder|for|name|href|open|tabindex|inputmode|contenteditable|data-.*|aria-.*)$/;
      const clean = el => {
        const c = el.cloneNode(true);
        c.querySelectorAll('style,script').forEach(x => x.remove());
        c.querySelectorAll('svg').forEach(x => { x.innerHTML = ''; });
        c.querySelectorAll('.ac-layer').forEach(x => x.remove());
        [c, ...c.querySelectorAll('*')].forEach(x => {
          [...x.attributes].forEach(a => { if (!keep.test(a.name) || a.name === 'data-ac-plain') x.removeAttribute(a.name); });
          if (x.style) x.removeAttribute('style');
        });
        const w = document.createTreeWalker(c, NodeFilter.SHOW_TEXT);
        for (let t; (t = w.nextNode());) { const v = t.nodeValue.replace(/\s+/g, ' '); t.nodeValue = v.length > 90 ? v.slice(0, 87) + '…' : v; }
        return c.innerHTML;
      };
      const cap = side => { const s = demo(side).closest('.cs-side'); const f = s.querySelector('.cs-foot .fig-cap, .ac-cap'); return f ? f.textContent.trim() : ''; };
      const labels = [...cs.querySelectorAll('.cs-switch button, .ac-chip')].map(x => x.textContent.trim());
      const tri = cs.querySelector('.cs-try, .ac-try');
      return {
        key, rule: rule ? rule.id : '', title: rule ? rule.querySelector('h4, h5').textContent.replace(/^\s*\d+\.\s*/, '').trim() : cs.getAttribute('aria-label'),
        prose: rule ? [...rule.querySelectorAll(':scope > p')].map(x => x.textContent.trim()).join(' ') : '',
        labels, tryText: tri ? tri.textContent.trim() : '', bad: { cap: cap('b'), html: clean(demo('b')) }, good: { cap: cap('f'), html: clean(demo('f')) },
      };
    }), keys);
    const md = [`# ${id} (${slug})`, '', `Page: ${base}/${slug}/  `, `Notes file: site/annotations/${id}.json`, ''];
    for (const c of cases) {
      const at = lineOf(`data-d="${c.key}b"`), code = lineOf(`D('${c.key}b'`) || lineOf(`'${c.key}b'`);
      md.push(`## ${c.key}`, '', `Rule: ${c.title}${c.rule ? ` (#${c.rule})` : ''}  `, `Prose: ${c.prose}  `,
        `Chips: ${c.labels.join(' / ')}  `, c.tryText ? `Shared try line: ${c.tryText}  ` : '', `Markup: index.html line ${at}. Demo code: index.html line ${code || '?'} (search for \`${c.key}b\`; the html and wire functions it passes are defined above it).`, '',
        `### Bad side (\`${c.key}b\`)`, '', `Caption: ${c.bad.cap}`, '', '```html', c.bad.html, '```', '',
        `### Good side (\`${c.key}f\`)`, '', `Caption: ${c.good.cap}`, '', '```html', c.good.html, '```', '');
    }
    fs.writeFileSync(path.join(out, id + '.md'), md.filter(x => x !== '').join('\n').replace(/\n(#+ )/g, '\n\n$1') + '\n');
    console.log('wrote', id, cases.length);
  }
  await b.close();
})();
