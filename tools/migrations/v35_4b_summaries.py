"""v35-4b: "In short" at the end of every chapter with rules, and a short bridge at the end of Parts 1 to 3.

"In short" lists the chapter's rule titles, each linked to its rule. It is built in the page from the rules
themselves (like the contents rail), so it can't drift from them. The bridges are prose.

Run once after v35-4a: python3 tools/migrations/v35_4b_summaries.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Book  # noqa: E402

b = Book()
assert 'in-short' not in b.s, 'already migrated'

BRIDGES = {
    'ch-good-checklist': ('part-1-next', 'Part 2',
                          'This part was about judgment: telling whether a design is good, and why. The next part starts from problems '
                          'instead of principles. Every pattern in it has a cost, and the judgment from this part tells you when it’s worth paying.'),
    'ch-patterns-cheat': ('part-2-next', 'Part 3',
                          'Patterns describe what should happen, and the next part is about the pieces you build them from. The wrong piece can '
                          'undo a good pattern: an error in a toast is gone before anyone reads it.'),
    'ch-choose': ('part-3-next', 'Part 4',
                  'Parts 1 to 3 are about what to build and how to judge it. The next part puts them to work on one problem, and links '
                  'back to them where they apply.'),
}
for cid, (bid, part, text) in BRIDGES.items():
    i = b.s.index('<section class="chapter" id="%s"' % cid)
    j = b.s.index('\n</section>', i)
    block = ('\n  <div class="prose part-bridge" id="%s">\n    <p class="eyebrow">Next · %s</p>\n    <p>%s</p>\n  </div>' % (bid, part, text))
    b.s = b.s[:j].rstrip('\n') + block + b.s[j:]

SCRIPT = '''<style>
.in-short{margin-top:44px;padding:20px 22px;border:1px solid var(--line);border-radius:12px;background:var(--paper-2)}
.in-short h4{font:600 13px/1.3 var(--font-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 14px}
.in-short .is-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px 28px}
.in-short .is-e{display:block;font:600 15px/1.35 var(--font-body);color:var(--ink);text-decoration:none}
.in-short ol{margin:6px 0 0;padding-left:20px;font-size:14.5px;line-height:1.45;color:var(--body)}
.in-short li{margin-top:3px}
.in-short ol a{color:inherit;text-decoration:none}
.in-short a:hover,.in-short a:focus-visible{text-decoration:underline}
.part-bridge{margin-top:40px;padding-top:20px;border-top:1px solid var(--line)}
.part-bridge .eyebrow{margin-bottom:6px}
@media (max-width:520px){.in-short{padding:16px}}
</style>
<script>
(() => {
  // "In short": each chapter's rule titles, linked to the rules. Built from the rules so it always matches them.
  const title = h => { const c = h.cloneNode(true); c.querySelectorAll('.n, .sec-link').forEach(x => x.remove()); return c.textContent.trim(); };
  document.querySelectorAll('section.chapter[data-chapter]').forEach(ch => {
    const groups = [...ch.querySelectorAll('article.entry[data-entry]')]
      .map(e => ({ e, rules: [...e.querySelectorAll('section.rule[id]')] })).filter(g => g.rules.length);
    if (!groups.length) return;
    const box = document.createElement('aside');
    box.className = 'in-short';
    box.id = ch.id + '-in-short';
    box.setAttribute('aria-labelledby', box.id + '-h');
    const h = document.createElement('h4'); h.id = box.id + '-h'; h.textContent = 'In short';
    const grid = document.createElement('div'); grid.className = 'is-grid';
    groups.forEach(({ e, rules }) => {
      const g = document.createElement('div');
      const a = document.createElement('a'); a.className = 'is-e'; a.href = '#' + e.id; a.textContent = title(e.querySelector('.entry-head h3'));
      const ol = document.createElement('ol');
      rules.forEach(r => { const li = document.createElement('li'), ra = document.createElement('a'); ra.href = '#' + r.id; ra.textContent = title(r.querySelector('h5')); li.appendChild(ra); ol.appendChild(li); });
      g.append(a, ol);
      grid.appendChild(g);
    });
    box.append(h, grid);
    const bridge = ch.querySelector(':scope > .part-bridge');
    ch.insertBefore(box, bridge);
  });
})();
</script>
'''
b.before('<script>\n(() => {\n  // A "#" link after each entry, section and rule title', SCRIPT)
b.save()
print('v35-4b applied')
