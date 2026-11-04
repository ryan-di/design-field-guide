"""v35-0: give the page a real document shell and give every rule and entry section a stable id.

Run once on the v34 index.html (commit 232f7cc): python3 tools/migrations/v35_0_shell_anchors.py
- Wraps the page in <!doctype html>, <html lang="en">, <head> (charset, viewport) and <body>.
- Adds ids: <entry>-rule-N on every rule, and <entry>-forms / -ways / -kinds / -rules / -products on entry sections.
- Lets checklist links wrap on phones (they pushed the page wider than the screen).
- Adds a small script that shows a "#" link next to entry titles, rule titles and section titles.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, 'index.html')
s = open(P, encoding='utf-8').read()
assert not s.lstrip().lower().startswith('<!doctype'), 'already migrated'

# 1. Document shell. Everything before the icon sprite is head content (title, font links, the main style).
cut = s.index('<svg width="0" height="0" style="position:absolute" aria-hidden="true">')
head, body = s[:cut], s[cut:]
assert re.fullmatch(r'\s*<title>.*?</title>\s*(<link[^>]*>\s*)+<style>.*</style>\s*', head, re.S), 'unexpected head content'
s = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
     '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + head.rstrip() + '\n</head>\n<body>\n'
     + body.rstrip() + '\n</body>\n</html>\n')

# 2. Ids inside entries.
VARIANT = {'Forms': 'forms', 'Ways to do it': 'ways', 'Kinds of critique': 'kinds', 'Kinds of tokens': 'kinds',
           'Ways to move with the keyboard': 'ways', 'Rules': 'rules', 'In real products': 'products'}
out, pos, rules = [], 0, 0
for m in re.finditer(r'<article class="entry" id="([^"]+)"', s):
    start, eid = m.start(), m.group(1)
    end = s.index('</article>', start)
    out.append(s[pos:start])
    art = s[start:end]

    def rule(mm):
        return '<section class="rule" id="%s-rule-%s"><h5><span class="n">%s</span>' % (eid, mm.group(1), mm.group(1))
    art, n = re.subn(r'<section class="rule"><h5><span class="n">(\d+)</span>', rule, art)
    rules += n

    def h4(mm):
        return '<h4 class="ess-h" id="%s-%s">%s</h4>' % (eid, VARIANT[mm.group(1)], mm.group(1))
    art = re.sub(r'<h4 class="ess-h">([^<]+)</h4>', h4, art)
    out.append(art)
    pos = end
out.append(s[pos:])
s = ''.join(out)
assert rules == 372, rules
assert '<section class="rule"><h5>' not in s

# 3. Section links and rule scroll margin.
CSS = ('.rule{scroll-margin-top:16px}.ess-h{scroll-margin-top:16px}'
       '.sec-link{margin-left:8px;color:var(--muted);text-decoration:none;font-weight:500;opacity:0;transition:opacity .12s}'
       'h3:hover>.sec-link,h4:hover>.sec-link,h5:hover>.sec-link,.sec-link:focus-visible{opacity:1}'
       '@media (hover:none){.sec-link{display:none}}'
       '@media (max-width:520px){.sec-link{display:none}.checklist .check a{white-space:normal}}')
anchor = '.essay .cw-wrap > p:first-of-type{font-size:18px;line-height:1.65;color:var(--body);max-width:64ch}\n</style>'
assert s.count(anchor) == 1
s = s.replace(anchor, anchor.replace('\n</style>', '\n' + CSS + '\n</style>'))

JS = '''<script>
(() => {
  // A "#" link after each entry, section and rule title, so readers (and skills) can copy a precise link.
  const add = (h, id) => { if (!id || h.querySelector('.sec-link')) return; const a = document.createElement('a'); a.className = 'sec-link'; a.href = '#' + id; a.textContent = '#'; a.setAttribute('aria-label', 'Link to “' + h.textContent.trim() + '”'); h.appendChild(a); };
  document.querySelectorAll('article.entry[id] > .entry-head h3').forEach(h => add(h, h.closest('article').id));
  document.querySelectorAll('h4.ess-h[id]').forEach(h => add(h, h.id));
  document.querySelectorAll('section.rule[id] > h5').forEach(h => add(h, h.parentElement.id));
})();
</script>
'''
end_main = '\n</main>\n</div>\n'
assert s.count(end_main) == 1
s = s.replace(end_main, '\n' + JS + '</main>\n</div>\n')

open(P, 'w', encoding='utf-8').write(s)
print('v35-0 applied: rules', rules)
