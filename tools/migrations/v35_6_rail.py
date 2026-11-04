"""v35-6: the contents rail can be hidden.

- Wide screens: a button beside the search box folds the rail to a thin strip and centers the text column. The same
  button brings it back, and so do / and Cmd+K.
- Narrow screens: the contents sit above the text, and "Contents" already folded the list; it now has a chevron so that's
  visible. The wide-screen button isn't shown there.
- The choice is remembered in this browser (dfg-rail).
- On narrow screens the rail is a card, so the search strip there has no fill of its own (v35-5 gave it the page color).

Run once after v35-5: python3 tools/migrations/v35_6_rail.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Book  # noqa: E402

b = Book()
assert 'rail-toggle' not in b.s, 'already migrated'

b.once('.toc-search{position:sticky;top:0;z-index:1;background:var(--paper);padding:4px 0 10px;margin-bottom:4px}',
       '.toc-search{position:sticky;top:0;z-index:1;background:var(--paper);padding:4px 0 10px;margin-bottom:4px;display:flex;flex-wrap:wrap;align-items:center;gap:6px}\n'
       '.toc-search .toc-empty{flex-basis:100%}\n'
       '.rail-toggle{all:unset;cursor:pointer;flex:none;width:38px;height:38px;display:grid;place-items:center;border-radius:9px;color:var(--muted)}\n'
       '.rail-toggle:hover{color:var(--ink);background:var(--paper-2)}\n'
       '.rail-toggle:focus-visible{outline:2px solid var(--blue);outline-offset:1px}\n'
       '.rail-toggle .icon{width:18px;height:18px}\n'
       'body.rail-collapsed .page{grid-template-columns:38px minmax(0,780px);justify-content:center}\n'
       'body.rail-collapsed .rail > :not(.toc-search),body.rail-collapsed .toc-search > :not(.rail-toggle){display:none}\n'
       '#toc-count{margin-left:auto}\n'
       '@media (max-width:900px){\n'
       '  .rail-toggle{display:none}\n'
       '  .toc-search{background:none}\n'
       '  .toc-search input{background:var(--paper)}\n'
       '  body.rail-collapsed .page{grid-template-columns:minmax(0,1fr)}\n'
       '  body.rail-collapsed .rail > :not(.toc-search),body.rail-collapsed .toc-search > :not(.rail-toggle){display:revert}\n'
       '  #toc summary::after{content:"";width:7px;height:7px;border-right:1.5px solid;border-bottom:1.5px solid;transform:translateY(-2px) rotate(45deg);margin-left:4px}\n'
       '  #toc:not([open]) summary::after{transform:rotate(-45deg)}\n'
       '}')
b.once('.toc-search input{width:100%;', '.toc-search input{flex:1;min-width:0;width:auto;')

b.once("  rail.prepend(sbox);\n",
       "  rail.prepend(sbox);\n"
       "  const railBtn = document.createElement('button');\n"
       "  railBtn.type = 'button'; railBtn.className = 'rail-toggle'; railBtn.setAttribute('aria-controls', 'toc');\n"
       "  railBtn.innerHTML = '<svg class=\"icon\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><rect x=\"3\" y=\"4\" width=\"18\" height=\"16\" rx=\"2\"/><path d=\"M9 4v16\"/></svg>';\n"
       "  sbox.querySelector('input').after(railBtn);\n"
       "  const railPref = { get() { try { return localStorage.getItem('dfg-rail'); } catch (e) { return null; } }, set(v) { try { localStorage.setItem('dfg-rail', v); } catch (e) {} } };\n"
       "  // Wide screens hide the whole rail; narrow ones fold the list under \"Contents\".\n"
       "  const railOpen = (on, save) => {\n"
       "    document.body.classList.toggle('rail-collapsed', !on);\n"
       "    railBtn.setAttribute('aria-expanded', String(on));\n"
       "    railBtn.setAttribute('aria-label', on ? 'Hide contents' : 'Show contents');\n"
       "    railBtn.title = on ? 'Hide contents' : 'Show contents';\n"
       "    if (toc && narrow()) toc.open = on;\n"
       "    if (save) railPref.set(on ? 'open' : 'closed');\n"
       "  };\n"
       "  railBtn.addEventListener('click', () => railOpen(document.body.classList.contains('rail-collapsed'), true));\n"
       "  if (toc) {\n"
       "    toc.querySelector('summary').addEventListener('click', e => { if (!narrow()) e.preventDefault(); });\n"
       "    toc.addEventListener('toggle', () => { if (narrow() && toc.open === document.body.classList.contains('rail-collapsed')) railOpen(toc.open, true); });\n"
       "  }\n"
       "  railOpen(railPref.get() !== 'closed');\n")
b.once("|| e.key === '/')) { e.preventDefault(); setToc(true); }",
       "|| e.key === '/')) { e.preventDefault(); railOpen(true, true); setToc(true); }")

b.save()
print('v35-6 applied')
