#!/usr/bin/env python3
"""Export the book for agents, from index.html only.

python3 tools/export.py           write llms.txt and references/ (entries, chapters, index.json, rubrics.json)
python3 tools/export.py --check   fail if any export is stale, or links to an anchor the page doesn't have

The exports are generated, never edited by hand: change index.html, then rerun this.
Literal `cap:`/`use:` strings in the demo scripts are read as text; nothing is executed.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://ryan-di.github.io/design-field-guide/'
EVIDENCE = ('Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, '
            'not verified product documentation, so check a product’s own docs before citing how it behaves. '
            'Tools named in it are 2026 examples, not endorsements.')

# Seed search tags, carried over from the v34 catalog (catalog/build_catalog.py); entries without one get tags from their text.
TAGS = {
    'pat-undo': 'recovery delete remove unsaved tab close reversible time limit history undo toast',
    'pat-autosave': 'draft persistence unsaved tab close restore storage write failure data loss autosave',
    'pat-version-history': 'recovery restore soft delete draft retention data loss version history',
    'pat-preview': 'commit changes before after consequences apply cancel preview',
    'pat-optimistic-ui': 'async race server write stale response concurrency rollback optimistic',
    'pat-instant-feedback': 'status saving saved duplicate submission progress feedback',
    'pat-background-work': 'long task download upload notifications progress background',
    'dialog': 'modal confirm unsaved close cancel save focus dialog',
    'toast': 'undo recovery notification time limit toast',
    'banner': 'persistent notice restore draft recovery banner',
    'pat-shortcuts': 'keyboard single character speech dictation accessibility shortcuts',
    'tooltip': 'hover focus supplementary help noninteractive tooltip',
    'switch': 'on off setting immediate commit checkbox switch',
    'checkbox': 'selection independent boolean commit form checkbox',
    'radio': 'mutually exclusive choices default deliberate answer radio',
    'buttons': 'primary secondary destructive action submit cancel button',
    'eff-loop': 'loop frame explore decide build check learn agent workflow cycle brief',
    'eff-ownership': 'ownership agent judgment framing decide human accountable design role',
    'eff-brief': 'brief problem who goal constraints non-goals success criteria ticket agent',
    'eff-context-pack': 'context pack tokens components copy repo conventions examples materials agent',
    'eff-definition-of-done': 'definition of done checks finished acceptance criteria verification agent',
    'eff-explore-wide': 'explore wide directions alternatives subagent options cheap variations',
    'eff-axes': 'axes named dimensions vary options explore tradeoffs loud silent',
    'eff-prototype-in-code': 'prototype code fidelity clickable artifact real material build explore',
    'eff-decision-matrix': 'decision matrix mandatory requirements eligibility alternatives tradeoffs score weight criteria brief',
    'eff-spot-plausible': 'plausible finished looking agent critique keyboard accessibility state polish',
    'eff-cut-combine': 'cut combine best parts directions synthesize choose decide',
    'eff-small-steps': 'small steps plan mode reviewable incremental build agent',
    'eff-agent-verification': 'agent verification proof tests screenshots e2e unit check done',
    'eff-ux-calls': 'ux calls design decision copy spacing dialog visible change call out',
    'eff-quick-sessions': 'research severity single observation sampling usability watch people sessions',
    'eff-measure': 'measure metrics success criteria brief numbers evaluate',
    'eff-design-qa': 'design qa light dark responsive states agent check evaluate',
    'eff-worked-example': 'worked example end to end unsaved tab brief release walkthrough',
    'eff-toolkit': 'toolkit tools frame explore decide build check share agent',
}
STOP = set('the a an and or to of in on for with is are be as it this that you your from when then than into its by at if not can will '
           'each their them they we our so do does did has have had but'.split())

# ---------------------------------------------------------------- DOM

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
BLOCKS = {'p', 'div', 'section', 'article', 'table', 'ul', 'ol', 'fieldset', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}
AUTOCLOSE = {'p': BLOCKS, 'li': {'li'}, 'td': {'td', 'th', 'tr'}, 'th': {'td', 'th', 'tr'}, 'tr': {'tr'}}


class Node:
    __slots__ = ('tag', 'attrs', 'children', 'parent')

    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.children, self.parent = tag, dict(attrs), [], parent

    @property
    def cls(self):
        return set((self.attrs.get('class') or '').split())

    def get(self, k):
        return self.attrs.get(k) or ''

    def has(self, k):
        return k in self.attrs

    def iter(self):
        for c in self.children:
            if isinstance(c, Node):
                yield c
                yield from c.iter()

    def find_all(self, pred):
        return [n for n in self.iter() if pred(n)]

    def find(self, pred):
        return next((n for n in self.iter() if pred(n)), None)

    def kids(self):
        return [c for c in self.children if isinstance(c, Node)]

    def raw(self):
        return ''.join(c if isinstance(c, str) else c.raw() for c in self.children)

    def text(self):
        return ws(''.join(c if isinstance(c, str) else ('' if c.tag in ('script', 'style') else c.text() + ' ' * (c.tag in BLOCKS or c.tag == 'br'))
                          for c in self.children))


class _Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = self.cur = Node('#root', {}, None)

    def handle_starttag(self, tag, attrs):
        while self.cur.tag in AUTOCLOSE and tag in AUTOCLOSE[self.cur.tag]:
            self.cur = self.cur.parent
        n = Node(tag, attrs, self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def parse(src):
    b = _Builder()
    b.feed(src)
    b.close()
    return b.root


def ws(s):
    return re.sub(r'\s+', ' ', s).strip()


def first_sentence(t):
    m = re.match(r'(.+?[.!?])(?=\s+[A-Z“"(]|$)', t)
    return m.group(1) if m else t

# ---------------------------------------------------------------- markdown

SKIP_TAGS = {'script', 'style', 'button', 'input', 'svg', 'template', 'select', 'textarea', 'canvas', 'noscript', 'nav'}
SKIP_CLASSES = {'cs-case', 'cs-demo', 'fm-stage', 'try', 'fig-cap', 'seg', 'cw-seg', 'cw', 'cw-cap', 'cl-head', 'sec-link',
                'ladder-axis', 'entry-head', 'learned', 'hero-meta', 'part-divider', 'chapter-head', 'p31-split'}


LISTISH = BLOCKS | {'li', 'dl', 'dt', 'dd', 'figure', 'tr', 'td', 'th'}


def label_rest(md, node, head_tags=('h4', 'b')):
    h = node.find(lambda x: x.tag in head_tags)
    rest = Node('div', {}, None)
    rest.children = [x for x in node.children if x is not h]
    return md.line(h) if h else '', md.line(rest).strip()


class Md:
    """Renders book markup as markdown and records every in-page anchor it links to."""

    def __init__(self):
        self.anchors = set()
        self.rich = False
        self.examples = []
        self.eid = ''

    def skipped(self, n):
        c = n.cls
        if n.tag == 'label' and n.find(lambda x: x.tag == 'input'):
            return True
        return (n.tag in SKIP_TAGS or (n.has('hidden') and not self.rich) or c & SKIP_CLASSES or any('stage' in k for k in c))

    def url(self, anchor):
        self.anchors.add(anchor)
        return SITE + '#' + anchor

    def inline(self, n):
        out = []
        prev_el = False
        for c in n.children:
            if isinstance(c, str):
                out.append(re.sub(r'\s+', ' ', c))
                prev_el = False
                continue
            if c.tag in ('script', 'style', 'input', 'button', 'svg') or 'sec-link' in c.cls or c.has('hidden'):
                continue
            if prev_el and out and not out[-1].endswith(' '):
                out.append(' ')
            prev_el = True
            t = self.inline(c)
            if c.tag in ('b', 'strong') and t.strip():
                out.append('**%s**' % t.strip())
            elif c.tag in ('em', 'i', 'var') and t.strip():
                out.append('*%s*' % t.strip())
            elif c.tag in ('code', 'kbd'):
                out.append('`%s`' % t.strip())
            elif c.tag == 'a':
                href = c.get('href')
                if href.startswith('#') and len(href) > 1:
                    out.append('[%s](%s)' % (t.strip(), self.url(href[1:])))
                elif href.startswith('http'):
                    out.append('[%s](%s)' % (t.strip(), href))
                else:
                    out.append(t)
            elif c.tag == 'br':
                out.append(' ')
            else:
                out.append(t)
        return re.sub(r' {2,}', ' ', ''.join(out))

    def line(self, n):
        return self.inline(n).strip()

    def table(self, t):
        head = [self.line(th) for th in t.find_all(lambda x: x.tag == 'th' and x.parent.parent.tag == 'thead')]
        rows = []
        for tr in t.find_all(lambda x: x.tag == 'tr' and x.parent.tag != 'thead'):
            cells = [self.line(td) or ('%s of 5' % td.get('data-s') if td.get('data-s') else '') for td in tr.kids() if td.tag in ('td', 'th')]
            if any(cells[1:]):
                rows.append([c.replace('|', '\\|') for c in cells])
        if not head:
            head, rows = rows[0], rows[1:]
        out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
        out += ['| ' + ' | '.join(r) + ' |' for r in rows]
        return '\n'.join(out)

    def blocks(self, n, depth):
        """depth: markdown level for an h4 at this point."""
        out = []
        for c in n.kids():
            if c.get('data-demo') in SPECIAL_DEMOS:
                out += SPECIAL_DEMOS[c.get('data-demo')](self, c, depth)
                continue
            if self.skipped(c):
                continue
            cl = c.cls
            if c.tag == 'dl':
                pairs = zip([x for x in c.kids() if x.tag == 'dt'], [x for x in c.kids() if x.tag == 'dd'])
                out.append('\n'.join('- **%s**: %s' % (self.line(dt), self.line(dd)) for dt, dd in pairs))
            elif c.tag == 'figure':
                h, rest = label_rest(self, c.find(lambda x: x.tag == 'figcaption') or c)
                out.append('- **%s**: %s' % (h, rest) if h else '- ' + rest)
            elif 'p31-tally' in cl:
                out.append('\n'.join('- %s' % ' '.join(self.line(x) for x in d.kids()) for d in c.kids()))
            elif c.tag == 'p':
                t = self.line(c)
                if t:
                    out.append(t)
            elif c.tag in ('h2', 'h3', 'h4', 'h5', 'h6'):
                lvl = min(6, depth + {'h2': -2, 'h3': -1, 'h4': 0, 'h5': 1, 'h6': 2}[c.tag])
                t = self.line(c)
                if c.get('id'):
                    self.anchors.add(c.get('id'))
                out.append('%s %s' % ('#' * max(lvl, 2), t))
            elif c.tag in ('ul', 'ol'):
                items = [t for t in (self.line(li) for li in c.kids() if li.tag == 'li') if t]
                if items:
                    out.append('\n'.join(('1. ' if c.tag == 'ol' else '- ') + i for i in items))
            elif c.tag == 'table':
                out.append(self.table(c))
            elif 'table-wrap' in cl:
                t = c.find(lambda x: x.tag == 'table')
                if c.get('id'):
                    out.append('Table: %s' % self.url(c.get('id')))
                out.append(self.table(t))
            elif c.tag == 'section' and 'rule' in cl:
                out += self.rule(c, depth)
            elif 'fm' in cl and c.tag == 'div':
                out += self.forms(c)
            elif 'cw-wrap' in cl:
                out += self.products(c)
            elif 'ladder' in cl:
                out.append('\n'.join('- [%s](%s): %s' % (self.line(a.find(lambda x: x.tag == 'b')), self.url(a.get('href')[1:]),
                                                         self.line(a.find(lambda x: x.tag == 'span'))) for a in c.kids() if a.tag == 'a'))
            elif cl & {'three', 'flow'}:
                out.append('\n'.join('- **%s**: %s' % label_rest(self, d) for d in c.kids()))
            elif c.tag == 'fieldset':
                leg = c.find(lambda x: x.tag == 'legend')
                items = ['- [ ] ' + self.line(lb) for lb in c.find_all(lambda x: x.tag == 'label')]
                out.append('**%s**\n\n%s' % (self.line(leg), '\n'.join(items)))
            elif not any(k.tag in LISTISH for k in c.iter()):
                t = self.line(c)
                if t:
                    out.append(t)
            else:
                out += self.blocks(c, depth)
        return out

    def rule(self, s, depth):
        h = s.find(lambda x: x.tag == 'h5')
        n = h.find(lambda x: 'n' in x.cls)
        title = self.line(h)[len(n.text()):].strip() if n else self.line(h)
        out = ['%s %s. %s' % ('#' * (depth + 1), n.text() if n else '', title), self.url(s.get('id'))]
        rest = Node('section', {}, None)
        rest.children = [c for c in s.children if c is not h]
        return out + self.blocks(rest, depth + 1)

    def forms(self, fm):
        seg = fm.find(lambda x: 'fm-seg' in x.cls)
        labels = []
        if seg:
            for inp in seg.find_all(lambda x: x.tag == 'input'):
                lb = seg.find(lambda x, i=inp: x.tag == 'label' and x.get('for') == i.get('id'))
                labels.append((inp.get('value'), self.line(lb) if lb else inp.get('value')))
        src = ''.join(sc.raw() for sc in fm.find_all(lambda x: x.tag == 'script'))
        pos = sorted((m.start(), k) for k, _ in labels for m in [re.search(r'(?<![\w.])%s\s*:\s*\{' % re.escape(k or '-'), src)] if m)
        texts = {}
        for i, (p, k) in enumerate(pos):
            seg_src = src[p:pos[i + 1][0] if i + 1 < len(pos) else len(src)]
            bits = [unq(v) for v in re.findall(r"\b(?:use|cost|note|how|why|when|tip)\s*:\s*'((?:[^'\\]|\\.)*)'", seg_src)]
            texts[k] = ' '.join(b for b in bits if '<' not in b)
        items = ['- **%s.** %s' % (lab, texts.get(k, '')) if texts.get(k) else '- **%s**' % lab for k, lab in labels]
        return ['\n'.join(items)] if items else []

    def products(self, cw):
        out = [self.line(p) for p in cw.kids() if p.tag == 'p' and not p.cls and self.line(p)]
        src = ''.join(sc.raw() for sc in cw.find_all(lambda x: x.tag == 'script'))
        caps = [unq(v) for v in re.findall(r"\bcap:\s*'((?:[^'\\]|\\.)*)'", src)]
        start = len(self.examples)
        self.examples += caps
        if caps:
            out.append('\n'.join('- %s `%s-example-%02d`' % (c, self.eid, start + i) for i, c in enumerate(caps, 1)))
        return out


def unq(v):
    v = re.sub(r"\\(['\"\\])", r'\1', v).replace('\\n', ' ')
    return ws(re.sub(r'<[^>]+>', '', v))


JS_STR = r"'((?:[^'\\]|\\.)*)'"


def chapter_js(n):
    sec = next(a for a in ancestors(n) if a.tag == 'section' and a.has('data-chapter'))
    return ''.join(s.raw() for s in sec.find_all(lambda x: x.tag == 'script'))


def worked_example(md, demo, depth):
    """The seven stages are the substance of this entry; their names and who-does-what lines live in the stepper script."""
    js = chapter_js(demo)
    names = [unq(v) for v in re.findall(JS_STR, re.search(r'const names = \[(.*?)\];', js, re.S).group(1))]
    who = re.findall(r'\[\s*' + JS_STR + r',\s*' + JS_STR + r'\s*\]', re.search(r'const who = \[(.*?)\n    \];', js, re.S).group(1))
    verdict = re.search(r'verdict\.textContent = w\s*\?\s*' + JS_STR + r'\s*:\s*' + JS_STR, js)
    panes = demo.find_all(lambda x: 'p31-pane' in x.cls)
    assert len(names) == len(who) == len(panes) == 7, 'worked example: expected 7 stages'
    md.rich, out = True, []
    for i, (name, (you, agents), pane) in enumerate(zip(names, who, panes)):
        out.append('%s Stage %d · %s' % ('#' * (depth + 1), i + 1, name))
        out += md.blocks(pane, depth + 1)
        table = pane.find(lambda x: x.tag == 'table')
        if table:
            rows = [tr for tr in table.find_all(lambda x: x.tag == 'tr' and x.parent.tag == 'tbody')]
            cols = [md.line(th) for th in table.find_all(lambda x: x.tag == 'th' and x.parent.parent.tag == 'thead')][1:]
            tot = lambda w: [sum(int(td.get('data-s')) * (2 if w and tr.has('data-w') else 1) for tr in rows
                                 for k, td in enumerate([x for x in tr.kids() if x.tag == 'td']) if k == c) for c in range(len(cols))]
            out.append('Totals: %s. Counting “never loses work” twice: %s.' % (
                ', '.join('%s %d' % x for x in zip(cols, tot(False))), ', '.join('%s %d' % x for x in zip(cols, tot(True)))))
            out.append('Counted once: %s Counted twice: %s' % (unq(verdict.group(2)), unq(verdict.group(1))))
        out.append('- **You**: %s\n- **Agents**: %s' % (unq(you), unq(agents)))
    md.rich = False
    return out


def toolkit(md, demo, depth):
    js = chapter_js(demo)
    tools = {li.get('data-tool'): md.line(li) for li in demo.find_all(lambda x: x.get('data-tool'))}
    jobs = [(b.get('data-job'), md.line(b)) for b in demo.find_all(lambda x: x.get('data-job'))]
    out = []
    for key, label in jobs:
        m = re.search(r'\b%s: \{ t: \[([^\]]*)\], how: %s, eg: %s' % (re.escape(key), JS_STR, JS_STR), js)
        assert m, 'toolkit: no data for job %s' % key
        names = ', '.join(tools[t] for t in re.findall(r"'(\w+)'", m.group(1)))
        out.append('- **%s** (%s): %s For the tab-close problem: %s' % (label, names, unq(m.group(2)), unq(m.group(3))))
    return ['\n'.join(out)]


SPECIAL_DEMOS = {'eff-worked-example': worked_example, 'eff-toolkit': toolkit}

# ---------------------------------------------------------------- book model


def kind_of(eid):
    if eid.startswith('pat-'):
        return 'pattern'
    if eid.startswith('eff-'):
        return 'workflow'
    if eid.startswith(('good-', 'design-')):
        return 'principle'
    return 'component'


def auto_tags(title, text, kind, chapter):
    seen = []
    for w in re.findall(r'[a-z0-9-]{3,}', (title + ' ' + ' '.join(text.split()[:80])).lower()):
        if w not in STOP and w not in seen:
            seen.append(w)
        if len(seen) >= 18:
            break
    extras = [kind, chapter.replace('ch-', ''), 'guide'] + (['part4', 'effective', 'agent', 'workflow'] if kind == 'workflow' else [])
    return ' '.join(dict.fromkeys(extras + seen))


def build():
    src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    root = parse(src)
    meta = {m.get('name'): m.get('content') for m in root.find_all(lambda x: x.tag == 'meta' and x.get('name'))}
    version, date, desc = meta['dfg-version'], meta['dfg-date'], meta['description']
    ids = {n.get('id') for n in root.iter() if n.get('id')}
    cite = 'Design Field Guide %s, #<anchor>' % version
    md = Md()
    files = {}

    parts, chapters, entries, part = [], [], [], None
    for n in root.iter():
        if 'part-divider' in n.cls:
            part = {'id': n.get('id'), 'title': n.get('data-part'),
                    'summary': ws((n.find(lambda x: 'part-sub' in x.cls) or Node('p', {}, None)).text()), 'chapters': []}
            parts.append(part)
        elif n.tag == 'section' and n.has('data-chapter'):
            head = n.find(lambda x: 'chapter-head' in x.cls)
            eyebrow = ws(head.find(lambda x: 'eyebrow' in x.cls).text()) if head else ''
            title = ws(head.find(lambda x: x.tag == 'h2').text()) if head else n.get('data-short')
            label = '%s · %s' % (eyebrow, title) if eyebrow.startswith('Chapter') else title
            ch = {'id': n.get('id'), 'title': title, 'label': label, 'short': n.get('data-short'), 'part': part['id'] if part else None,
                  'node': n, 'entries': []}
            if part:
                part['chapters'].append(ch['id'])
            chapters.append(ch)
        elif n.tag == 'article' and n.has('data-entry'):
            entries.append({'id': n.get('id'), 'title': n.get('data-name'), 'node': n, 'chapter': chapters[-1]['id']})
            chapters[-1]['entries'].append(n.get('id'))
    assert len(entries) == 99, 'expected 99 entries, found %d' % len(entries)
    P = {p['id']: p for p in parts}
    C = {c['id']: c for c in chapters}
    E = {e['id'] for e in entries}

    def header(title, part_id, ch, anchor, extra=()):
        where = ' · '.join(x for x in [P[part_id]['title'] if part_id else 'Front matter', ch['label'] if ch else ''] if x)
        return ['# ' + title, '',
                'Design Field Guide %s (%s) · %s' % (version, date, where),
                'Live: %s' % md.url(anchor)] + list(extra) + ['Cite as: Design Field Guide %s, #%s' % (version, anchor), '', '> ' + EVIDENCE, '']

    index_entries = []
    for e in entries:
        n, ch = e['node'], C[e['chapter']]
        md.anchors, md.examples, md.eid = set(), [], e['id']
        body = md.blocks(n.find(lambda x: 'essay' in x.cls) or n, 2)
        kind = kind_of(e['id'])
        intro = next((md.line(p) for p in n.find_all(lambda x: x.tag == 'p' and 'prose' in x.cls)), '')
        examples = ['%s-example-%02d' % (e['id'], i) for i in range(1, len(md.examples) + 1)]
        related = sorted(a for a in md.anchors if a in E and a != e['id'])
        text = ws(re.sub(r'\]\([^)]*\)|https?://\S+|`[\w-]+-example-\d+`|[#*\[`|]|-{3,}', ' ', e['title'] + ' ' + ' '.join(body)))
        rules = [{'id': r.get('id'), 'n': int(ws(r.find(lambda x: 'n' in x.cls).text())),
                  'title': ws(r.find(lambda x: x.tag == 'h5').text())[len(ws(r.find(lambda x: 'n' in x.cls).text())):].strip(),
                  'url': SITE + '#' + r.get('id')} for r in n.find_all(lambda x: x.tag == 'section' and 'rule' in x.cls)]
        sections = [{'id': h.get('id'), 'title': ws(h.text()), 'url': SITE + '#' + h.get('id')}
                    for h in n.find_all(lambda x: x.tag == 'h4' and 'ess-h' in x.cls and x.get('id'))]
        tables = [{'id': t.get('id'), 'rubric': t.get('data-rubric') or None, 'url': SITE + '#' + t.get('id')}
                  for t in n.find_all(lambda x: 'table-wrap' in x.cls and x.get('id'))]
        md.anchors.add(e['id'])
        lines = header(e['title'], ch['part'], ch, e['id'], ['Kind: %s' % kind]) + ['\n\n'.join(body)]
        if related:
            lines += ['', '## Related entries', '', ', '.join('[%s](%s.md)' % (r, r) for r in related)]
        path = 'references/entries/%s.md' % e['id']
        files[path] = '\n'.join(lines).rstrip() + '\n'
        tags = TAGS.get(e['id'], '')
        if not tags or kind == 'workflow':
            tags = ' '.join(dict.fromkeys((tags + ' ' + auto_tags(e['title'], text, kind, ch['id'])).split()))
        index_entries.append({'id': e['id'], 'title': e['title'], 'kind': kind, 'part': ch['part'], 'chapter': ch['id'],
                              'url': SITE + '#' + e['id'], 'path': path, 'summary': first_sentence(intro),
                              'sections': sections, 'rules': rules, 'tables': tables, 'related': related,
                              'example_ids': examples, 'tags': tags, 'search_text': text})
        e['summary'] = first_sentence(intro)

    for ch in chapters:
        n = ch['node']
        own = Node('section', {}, None)
        own.children = [c for c in n.children if not (isinstance(c, Node) and c.tag == 'article')]
        md.anchors = set()
        body = md.blocks(own, 2)
        prose = n.find(lambda x: 'prose' in x.cls and x.parent is n)
        ch['summary'] = first_sentence(md.line(prose.find(lambda x: x.tag == 'p') or prose)) if prose else ''
        listing = ['## Entries', ''] + ['- [%s](../entries/%s.md): %s' % (next(x['title'] for x in entries if x['id'] == i), i,
                                                                          next(x['summary'] for x in entries if x['id'] == i)) for i in ch['entries']]
        lines = header(ch['label'], ch['part'], None, ch['id']) + ['\n\n'.join(body)]
        if ch['entries']:
            lines += [''] + listing
        files['references/chapters/%s.md' % ch['id']] = '\n'.join(lines).rstrip() + '\n'

    rubrics = []
    for t in root.find_all(lambda x: x.has('data-rubric')):
        owner = next((a for a in ancestors(t) if a.tag == 'article' and a.has('data-entry')), None)
        cols = [ws(th.text()) for th in t.find_all(lambda x: x.tag == 'th' and x.parent.parent.tag == 'thead')]
        rows = []
        for tr in t.find_all(lambda x: x.tag == 'tr' and x.parent.tag == 'tbody'):
            r = {'cells': [ws(td.text()) for td in tr.kids() if td.tag in ('td', 'th')]}
            if tr.get('data-words'):
                r['words'] = tr.get('data-words').split()
            lists = {s.get('data-words'): s.get('data-list').split('|') for s in tr.find_all(lambda x: x.get('data-list'))}
            if lists:
                r['lists'] = lists
            rows.append(r)
        rubrics.append({'name': t.get('data-rubric'), 'id': t.get('id'), 'url': SITE + '#' + t.get('id'),
                        'entry': owner.get('id') if owner else None, 'columns': cols, 'rows': rows})
    files['references/rubrics.json'] = dumps({'book': 'Design Field Guide', 'version': version, 'date': date, 'site': SITE, 'cite': cite,
                                              'note': 'Generated from the reference tables in the book; each rubric links to its table.',
                                              'rubrics': rubrics})

    files['references/index.json'] = dumps({
        'book': 'Design Field Guide', 'version': version, 'date': date, 'site': SITE, 'cite': cite, 'evidence': EVIDENCE,
        'parts': [{k: p[k] for k in ('id', 'title', 'summary', 'chapters')} | {'url': SITE + '#' + p['id']} for p in parts],
        'chapters': [{'id': c['id'], 'title': c['title'], 'label': c['label'], 'part': c['part'], 'url': SITE + '#' + c['id'],
                      'path': 'references/chapters/%s.md' % c['id'], 'summary': c['summary'], 'entries': c['entries']} for c in chapters],
        'entries': index_entries})

    L = ['# Design Field Guide', '',
         '> %s Version %s (%s). The book is one page with live demos at %s' % (desc, version, date, SITE), '',
         'Every entry is also exported as markdown, generated from the same page, so you don’t need to load the 4 MB HTML:', '',
         '- One file per entry: %sreferences/entries/<id>.md, with links to each section and rule' % SITE,
         '- Index of parts, chapters, entries, rules and anchors: %sreferences/index.json' % SITE,
         '- Rubrics (word lists, severity scale, heuristics, accessibility pass, loop stages and more): %sreferences/rubrics.json' % SITE,
         '- What changed between versions: %sCHANGELOG.md' % SITE, '',
         'Cite as “Design Field Guide %s, #<anchor>” with the link %s#<anchor>. An entry is #<id>, its rules are #<id>-rules, '
         'and rule N is #<id>-rule-N. Anchors stay valid across versions.' % (version, SITE), '',
         EVIDENCE, '']
    front = [c for c in chapters if not c['part']]
    if front:
        L += ['## Front matter', ''] + ['- [%s](%sreferences/chapters/%s.md)%s' % (c['label'], SITE, c['id'], ': ' + c['summary'] if c['summary'] else '')
                                        for c in front] + ['']
    for p in parts:
        L += ['## %s' % p['title'], '']
        if p['summary']:
            L += [p['summary'], '']
        for cid in p['chapters']:
            c = C[cid]
            L.append('- [%s](%sreferences/chapters/%s.md)%s' % (c['label'], SITE, cid, ': ' + c['summary'] if c['summary'] else ''))
            for eid in c['entries']:
                e = next(x for x in entries if x['id'] == eid)
                L.append('  - [%s](%sreferences/entries/%s.md): %s' % (e['title'], SITE, eid, e['summary']))
        L.append('')
    L += ['## Optional', '', '- [Rubrics](%sreferences/rubrics.json): the book’s reference tables as data' % SITE,
          '- [Index](%sreferences/index.json): every entry with its rules, tables, related entries and search tags' % SITE,
          '- [Changelog](%sCHANGELOG.md)' % SITE]
    files['llms.txt'] = '\n'.join(L).rstrip() + '\n'
    return files, ids, version


def ancestors(n):
    p = n.parent
    while p is not None:
        yield p
        p = p.parent


def dumps(o):
    return json.dumps(o, ensure_ascii=False, indent=1) + '\n'


def main():
    files, ids, version = build()
    problems = []
    for path, content in files.items():
        for a in re.findall(re.escape(SITE) + r'#([\w-]+)', content):
            if a not in ids:
                problems.append('%s links to #%s, which index.html does not have' % (path, a))
        for rel in re.findall(re.escape(SITE) + r'((?:references|CHANGELOG)[\w./-]*\.(?:md|json))', content):
            if rel not in files and not os.path.exists(os.path.join(ROOT, rel)):
                problems.append('%s links to %s, which does not exist' % (path, rel))
        for rel in re.findall(r'\]\(((?:\.\./)?[\w-]+(?:/[\w-]+)?\.md)\)', content):
            target = os.path.normpath(os.path.join(os.path.dirname(path), rel))
            if target not in files:
                problems.append('%s links to %s, which does not exist' % (path, rel))
    changelog = os.path.join(ROOT, 'CHANGELOG.md')
    if not os.path.exists(changelog) or ('## ' + version) not in open(changelog, encoding='utf-8').read():
        problems.append('CHANGELOG.md has no "## %s" section' % version)
    existing = {os.path.relpath(os.path.join(d, f), ROOT) for sub in ('references/entries', 'references/chapters')
                for d, _, fs in os.walk(os.path.join(ROOT, sub)) for f in fs}
    if '--check' in sys.argv:
        for path, content in files.items():
            p = os.path.join(ROOT, path)
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != content:
                problems.append('%s is stale: run python3 tools/export.py' % path)
        for path in sorted(existing - set(files)):
            problems.append('%s is no longer generated: run python3 tools/export.py' % path)
    else:
        for path in existing - set(files):
            os.remove(os.path.join(ROOT, path))
        for path, content in files.items():
            p = os.path.join(ROOT, path)
            os.makedirs(os.path.dirname(p) or ROOT, exist_ok=True)
            open(p, 'w', encoding='utf-8').write(content)
        print('wrote %d files (%d entries)' % (len(files), sum(k.startswith('references/entries/') for k in files)))
    for pr in problems:
        print('FAIL', pr)
    if problems:
        sys.exit(1)
    if '--check' in sys.argv:
        print('exports up to date: %d files, every anchor exists' % len(files))


if __name__ == '__main__':
    main()
