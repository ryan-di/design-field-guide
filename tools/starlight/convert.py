"""Builds the Starlight pilot (site/) from index.html.

Prose becomes MDX, so it reads and edits like a book. Everything interactive (demos, tables the demos read, their
styles and scripts) is copied byte for byte into src/fragments/ and placed with <Raw>, so the demos run unchanged.
Every element that had an id keeps it: entries, rules and chapters are wrappers with their old id, so old #anchors
and the demos' id-scoped CSS still match.

Chapters not yet converted stay links to the live book in the sidebar.

Run: python3 tools/starlight/convert.py
"""
import json
import os
import re
import shutil
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = os.path.join(ROOT, 'site')
LIVE = 'https://ryan-di.github.io/design-field-guide/'
PILOT = None  # chapter ids to convert; None converts every chapter
# tools/export.py writes these at the repo root; they are copied into site/public so the book's links to them stay on the site.
SITE_FILES = ('llms.txt', 'CHANGELOG.md', 'references')
# Prose that describes the one-page book's own controls, reworded for what the site shows.
SITE_WORDING = {
    'press the # next to its title': 'use the link icon that appears next to its title',
}


def converted(ch):
    return PILOT is None or ch.get('id') in PILOT

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}


class N:
    __slots__ = ('tag', 'attrs', 'children', 'parent', 'start', 'end')

    def __init__(self, tag, attrs, parent, start):
        self.tag, self.attrs, self.children, self.parent, self.start, self.end = tag, dict(attrs), [], parent, start, None

    def get(self, k):
        return self.attrs.get(k) or ''

    @property
    def cls(self):
        return set(self.get('class').split())

    def kids(self):
        return [c for c in self.children if isinstance(c, N)]

    def iter(self):
        for c in self.kids():
            yield c
            yield from c.iter()

    def find(self, pred):
        return next((n for n in self.iter() if pred(n)), None)

    def text(self):
        return re.sub(r'\s+', ' ', ''.join(c if isinstance(c, str) else ('' if c.tag in ('script', 'style') else c.text()) for c in self.children)).strip()


class Parser(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=True)
        self.src = src
        self.lines = [0] + [m.end() for m in re.finditer('\n', src)]
        self.root = self.cur = N('#root', {}, None, 0)

    def off(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attrs):
        st = self.off()
        n = N(tag, attrs, self.cur, st)
        self.cur.children.append(n)
        if tag in VOID:
            n.end = st + len(self.get_starttag_text())
        else:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        st = self.off()
        n = N(tag, attrs, self.cur, st)
        n.end = st + len(self.get_starttag_text())
        self.cur.children.append(n)

    def handle_endtag(self, tag):
        st = self.off()
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is self.root:
            return
        x = self.cur
        while x is not n:
            x.end = x.end or st
            x = x.parent
        n.end = self.src.index('>', st) + 1
        self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


# ------------------------------------------------------------------ CSS

DROP = re.compile(r'^(html|body|\.page|\.main\b|\.rail|\.hero|\.lede|\.chapter\b|\.chapter-head|\.part-divider|\.part-title|\.part-sub|#toc|\.toc|\.pg-|\.view-toggle|\.endnote|\.essay\s*$|\.essay p\.prose|\.ess-h|\.sec-link|h[3-5]:hover>\.sec-link)')
BARE = re.compile(r'^(a|h[1-6]|p|code|pre|:focus-visible)(?=$|[\s:.\[>,+~])')
ROOT_SEL = re.compile(r'^(:root|html)(\[[^\]]*\]|:not\([^)]*\))*')
SCOPE = ':where(.sl-markdown-content) '


def scope(sel):
    """Keep the book's rules inside page content; Starlight's chrome shares class names like .icon and .label."""
    m = ROOT_SEL.match(sel)
    if m and m.end():
        rest = sel[m.end():]
        return sel if not rest.strip() or not rest[0].isspace() else sel[:m.end()] + ' ' + scope(rest.lstrip())
    return SCOPE + ('.dfg-raw ' + sel if BARE.match(sel) else sel)


def split_top(s, sep=','):
    out, depth, cur = [], 0, ''
    for ch in s:
        if ch in '([':
            depth += 1
        elif ch in ')]':
            depth -= 1
        if ch == sep and depth == 0:
            out.append(cur)
            cur = ''
        else:
            cur += ch
    out.append(cur)
    return out


def blocks(css):
    """Top-level (prelude, body) pairs, by brace matching."""
    i, out = 0, []
    while i < len(css):
        j = css.find('{', i)
        if j < 0:
            break
        depth, k = 1, j + 1
        while depth:
            depth += {'{': 1, '}': -1}.get(css[k], 0)
            k += 1
        out.append((css[i:j].strip(), css[j + 1:k - 1]))
        i = k
    return out


def filter_css(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    out = []
    for pre, body in blocks(css):
        if pre.startswith('@media') or pre.startswith('@supports') or pre.startswith('@container') or pre.startswith('@layer'):
            inner = filter_css(body)
            if inner.strip():
                out.append('%s{%s}' % (pre, inner))
        elif pre.startswith('@'):
            out.append('%s{%s}' % (pre, body))
        else:
            sels = []
            for sel in (x.strip() for x in split_top(pre)):
                if not sel or DROP.match(sel):
                    continue
                sels.append(scope(sel))
            if sels:
                out.append('%s{%s}' % (','.join(sels), body))
    return '\n'.join(out)


# ------------------------------------------------------------------ MDX

def esc(t):
    t = re.sub(r'\s+', ' ', t)
    for a, b in (('\\', '\\\\'), ('{', '\\{'), ('}', '\\}'), ('<', '&lt;'), ('*', '\\*'), ('_', '\\_'), ('`', '\\`'), ('[', '\\['), (']', '\\]')):
        t = t.replace(a, b)
    return t


class Book:
    def __init__(self):
        self.src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
        self.reworded = set()
        p = Parser(self.src)
        p.feed(self.src)
        p.close()
        self.root = p.root
        for n in self.root.iter():
            assert self.src.startswith('<' + n.tag, n.start), n.tag
        self.main = self.root.find(lambda n: n.tag == 'main')
        self.chapters = [n for n in self.main.kids() if n.tag == 'section' and 'chapter' in n.cls]
        self.parts = []
        part = None
        for n in self.main.kids():
            if 'part-divider' in n.cls:
                part = {'id': n.get('id'), 'label': n.get('data-part'), 'chapters': [], 'node': n}
                self.parts.append(part)
            elif n in self.chapters:
                (part or self.front())['chapters'].append(n)
        self.page_of = {}
        for ch in self.chapters:
            if converted(ch):
                for n in [ch] + list(ch.iter()):
                    if n.get('id'):
                        self.page_of[n.get('id')] = self.slug(ch)
        for part in self.parts:
            first = next((c for c in part['chapters'] if converted(c)), None)
            if part.get('node') is not None and first is not None:
                for n in [part['node']] + list(part['node'].iter()):
                    if n.get('id'):
                        self.page_of[n.get('id')] = self.slug(first)

    def front(self):
        if not self.parts or self.parts[0]['id'] != 'front':
            self.parts.insert(0, {'id': 'front', 'label': 'Front matter', 'chapters': []})
        return self.parts[0]

    def raw(self, n):
        return self.src[n.start:n.end]

    def part_slug(self, ch):
        for p in self.parts:
            if ch in p['chapters']:
                return {'front': 'front', 'start': 'start-here', 'back': 'back-matter'}.get(p['id'], p['id'])

    def slug(self, ch):
        return '%s/%s' % (self.part_slug(ch), ch.get('id')[3:])

    def href(self, h, here):
        if h.startswith('#') and len(h) > 1:
            target = h[1:]
            page = self.page_of.get(target)
            if page is None:
                return LIVE + h
            return h if page == here else '/%s/%s' % (page, h)
        if h.startswith('http'):
            return h
        if h.split('/')[0] in SITE_FILES:
            # Relative to the page, so it holds under any base path; pages are served as /part/chapter/.
            return '../' * (here.count('/') + 1) + h
        return LIVE + h

    def inline(self, n, here):
        out = []
        for c in n.children:
            if isinstance(c, str):
                out.append(esc(c))
                continue
            if c.tag in ('script', 'style', 'input', 'button', 'svg') or 'sec-link' in c.cls or 'hidden' in c.attrs:
                continue
            t = self.inline(c, here)
            if c.tag in ('b', 'strong') and t.strip():
                out.append('**%s**' % t.strip())
            elif c.tag in ('em', 'i', 'var') and t.strip():
                out.append('*%s*' % t.strip())
            elif c.tag in ('code', 'kbd'):
                out.append('`%s`' % c.text())
            elif c.tag == 'a' and c.get('href'):
                out.append('[%s](%s)' % (t.strip(), self.href(c.get('href'), here)))
            elif c.tag == 'br':
                out.append(' ')
            elif c.get('id'):
                out.append('<span id="%s">%s</span>' % (c.get('id'), t))
            else:
                out.append(t)
        return re.sub(r' {2,}', ' ', ''.join(out)).strip()


def attr_str(n):
    """The id and non-prose classes a markdown block has to keep."""
    cls = ' '.join(c for c in n.get('class').split() if c != 'prose')
    return ('' if not n.get('id') else ' id="%s"' % n.get('id')) + ('' if not cls else ' class="%s"' % cls)


class Page:
    def __init__(self, book, ch):
        self.b, self.ch, self.here = book, ch, book.slug(ch)
        self.cid = ch.get('id')
        self.frags = []
        self.lines = []

    def frag(self, html):
        html = re.sub(r'<style\b[^>]*>.*?</style>', '', html, flags=re.S)
        html = re.sub(r'href="#([^"]+)"', lambda m: 'href="%s"' % (self.b.href('#' + m.group(1), self.here) if m.group(1) in self.b.page_of else '#' + m.group(1)), html)
        if not html.strip():
            return
        k = len(self.frags)
        self.frags.append(html)
        self.lines += ['<Raw html={F%d} />' % k, '']

    def para(self, n):
        t = self.b.inline(n, self.here)
        if not t:
            return
        for old, new in SITE_WORDING.items():
            if old in t:
                t = t.replace(old, new)
                self.b.reworded.add(old)
        attrs = attr_str(n)
        self.lines += ['<p%s>%s</p>' % (attrs, t) if attrs else t, '']

    def heading(self, lvl, n, hid=None):
        t = self.b.inline(n, self.here)
        self.lines += ['%s %s%s' % ('#' * lvl, t, ' \\{#%s\\}' % hid if hid else ''), '']

    def prose_block(self, n):
        attrs = attr_str(n)
        if attrs:
            self.lines += ['<div%s>' % attrs, '']
        for c in n.kids():
            if c.tag == 'p':
                self.para(c)
            elif c.tag in ('h4', 'h3'):
                self.heading(2 if self.cid == 'ch-preface' else 3, c, c.get('id') or None)
            else:
                self.frag(self.b.raw(c))
        if attrs:
            self.lines += ['</div>', '']

    def rule(self, s):
        h5 = s.find(lambda x: x.tag == 'h5')
        num = h5.find(lambda x: 'n' in x.cls)
        title = N('h5', {}, None, 0)
        title.children = [c for c in h5.children if c is not num]
        self.lines += ['<section class="rule" id="%s">' % s.get('id'), '']
        self.lines += ['#### %s. %s \\{#%s-h\\}' % (num.text(), self.b.inline(title, self.here), s.get('id')), '']
        for c in s.kids():
            if c is h5:
                continue
            if c.tag == 'p' and 'prose' in c.cls:
                self.para(c)
            else:
                self.frag(self.b.raw(c))
        self.lines += ['</section>', '']

    def essay(self, ess):
        for c in ess.kids():
            cl = c.cls
            if c.tag == 'p' and 'prose' in cl:
                self.para(c)
            elif c.tag == 'h4' and 'ess-h' in cl:
                self.heading(3, c, c.get('id') or None)
            elif 'cs' in cl and 'essay-cs' in cl:
                self.lines += ['<div class="cs essay-cs">', '']
                for r in c.kids():
                    if r.tag == 'section' and 'rule' in r.cls:
                        self.rule(r)
                    elif r.tag == 'p' and 'prose' in r.cls:
                        self.para(r)
                    else:
                        self.frag(self.b.raw(r))
                self.lines += ['</div>', '']
            else:
                self.frag(self.b.raw(c))

    def entry(self, art):
        eid = art.get('id')
        h3 = art.find(lambda x: x.tag == 'h3')
        self.lines += ['<article class="entry essay" id="%s" data-entry data-name="%s">' % (eid, art.get('data-name')), '']
        self.lines += ['<div class="entry-head">', '']
        self.heading(2, h3, eid + '-h')
        self.lines += ['<Learned id="%s" />' % eid, '', '</div>', '']
        self.essay(art.find(lambda x: 'essay' in x.cls))
        self.lines += ['</article>', '']

    def in_short(self, entries):
        if not entries:
            return
        box = self.cid + '-in-short'
        self.lines += ['<aside class="in-short" id="%s" aria-labelledby="%s-h" data-pagefind-ignore>' % (box, box), '',
                       '## In short \\{#%s-h\\}' % box, '', '<div class="is-grid">', '']
        for art in entries:
            rules = [x for x in art.iter() if x.tag == 'section' and 'rule' in x.cls and x.get('id')]
            if not rules:
                continue
            h3 = art.find(lambda x: x.tag == 'h3')
            self.lines += ['<div>', '', '<a class="is-e" href="#%s">%s</a>' % (art.get('id'), self.b.inline(h3, self.here)), '']
            for r in rules:
                h5 = r.find(lambda x: x.tag == 'h5')
                num = h5.find(lambda x: 'n' in x.cls)
                t = esc(h5.text()[len(num.text()):].strip())
                self.lines.append('%s. [%s](#%s)' % (num.text(), t, r.get('id')))
            self.lines += ['', '</div>', '']
        self.lines += ['</div>', '', '</aside>', '']

    def borrowed(self):
        """Elements in other chapters that this chapter's inline scripts look up by id, such as word lists kept in the text."""
        js = ''.join(self.b.raw(n) for n in self.ch.iter() if n.tag == 'script')
        own = {n.get('id') for n in self.ch.iter() if n.get('id')}
        ids = sorted({i for i in re.findall(r"['\"]#([A-Za-z][\w-]*)", js) if i not in own and i in self.b.page_of})
        nodes = [n for n in self.b.main.iter() if n.get('id') in ids]
        html = ''.join(re.sub(r'<script\b[^>]*>.*?</script>', '', self.b.raw(n), flags=re.S) for n in nodes)
        return '<div hidden aria-hidden="true" class="dfg-borrowed">%s</div>' % html if html else ''

    def build(self, sidebar_label, eyebrow, part=None):
        head = self.ch.find(lambda x: 'chapter-head' in x.cls)
        title = head.find(lambda x: x.tag == 'h2').text() if head else self.ch.get('data-short')
        entries = []
        self.lines += ['<Runtime at="start" />', '']
        borrowed = self.borrowed()
        if borrowed:
            self.frag(borrowed)
        self.lines += ['<section class="dfg-chapter" id="%s">' % self.cid, '']
        for c in self.ch.kids():
            if c is head:
                continue
            if 'prose' in c.cls and c.tag == 'div':
                self.prose_block(c)
            elif c.tag == 'article' and 'entry' in c.cls:
                entries.append(c)
                self.entry(c)
            else:
                self.frag(self.b.raw(c))
        self.in_short(entries)
        self.lines += ['</section>', '', '<Runtime chapter="%s" />' % self.cid, '']
        first = next((x for x in self.ch.iter() if x.tag == 'p' and 'eyebrow' not in x.cls and x.text()), None)
        desc = re.split(r'(?<=[.!?])\s', first.text())[0] if first else title
        depth = '../' * (self.here.count('/') + 2)
        front = ['---', 'title: %s' % json.dumps(title, ensure_ascii=False), 'description: %s' % json.dumps(desc, ensure_ascii=False)]
        if eyebrow:
            front.append('eyebrow: %s' % json.dumps(eyebrow, ensure_ascii=False))
        if part is not None:
            q = lambda c: next((x.text() for x in part.iter() if c in x.cls), '')
            front += ['part:', '  id: %s' % json.dumps(part.get('id')), '  label: %s' % json.dumps(part.get('data-part'), ensure_ascii=False),
                      '  title: %s' % json.dumps(q('part-title'), ensure_ascii=False), '  sub: %s' % json.dumps(q('part-sub'), ensure_ascii=False)]
        front += ['sidebar:', '  label: %s' % json.dumps(sidebar_label, ensure_ascii=False), '---', '',
                  "import Raw from '%scomponents/Raw.astro';" % depth,
                  "import Learned from '%scomponents/Learned.astro';" % depth,
                  "import Runtime from '%scomponents/Runtime.astro';" % depth]
        front += ["import F%d from '%sfragments/%s/%d.html?raw';" % (k, depth, self.cid, k) for k in range(len(self.frags))]
        return '\n'.join(front + [''] + self.lines)


def runtime(book):
    s = book.src
    sprite = book.raw(book.root.find(lambda n: n.tag == 'svg' and n.parent.tag == 'body'))
    cs = book.raw(next(n for n in book.main.kids() if n.tag == 'script' and 'window.csInit' in book.raw(n)))
    big = next(n for n in book.root.find(lambda n: n.tag == 'body').iter() if n.tag == 'script' and "'use strict';" in book.raw(n)[:60] and '---------- Demos ----------' in book.raw(n))
    js = s[big.start:big.end]
    js = js[js.index('>') + 1:js.rindex('</script>')]
    head = js[:js.index('  /* ---------- Contents rail')]
    helpers = js[js.index('  /* ---------- Review checklist'):js.index('  /* ---------- Demos')]
    demos = js[js.index('  /* ---------- Demos'):js.rindex('})();')]
    parts = re.split(r'(?=\n  /\* js-[\w-]+\.js \*/)', demos)
    core = ('<script>' + head + helpers +
            '  /* ---------- Learned progress ---------- */\n'
            '  const learned = new Set(store.get(KEY, []));\n'
            "  const syncLearned = () => $$('[data-learned]').forEach(cb => { cb.checked = learned.has(cb.dataset.learned); });\n"
            "  document.addEventListener('change', e => {\n"
            "    const cb = e.target.closest && e.target.closest('[data-learned]');\n"
            '    if (!cb) return;\n'
            '    if (cb.checked) learned.add(cb.dataset.learned); else learned.delete(cb.dataset.learned);\n'
            '    store.set(KEY, Array.from(learned));\n'
            '    syncLearned();\n'
            '  });\n'
            '  syncLearned();\n'
            '  window.dfg = { $, $$, store, demo, toast };\n'
            '})();\n</script>')
    return sprite, cs, core, parts


def chapter_js(book, ch, parts):
    names = {n.get('data-demo') for n in ch.iter() if n.get('data-demo')}
    picked = [p for p in parts if any(("demo('%s'" % x) in p for x in names)]
    if not picked:
        return ''
    return '<script>\n(() => {\n  const { $, $$, store, demo, toast } = window.dfg;\n' + ''.join(picked) + '\n})();\n</script>'


def sidebar(book):
    out = []
    for p in book.parts:
        items = []
        for ch in p['chapters']:
            label = ch.get('data-short')
            if converted(ch):
                items.append({'label': label, 'slug': book.slug(ch)})
            else:
                items.append({'label': label + ' ↗', 'link': LIVE + '#' + ch.get('id'), 'attrs': {'class': 'dfg-live'}})
        out.append({'label': p['label'], 'items': items, 'collapsed': p['id'] not in ('front', 'start')})
    return out


def main():
    book = Book()
    frag_dir = os.path.join(SITE, 'src', 'fragments')
    docs = os.path.join(SITE, 'src', 'content', 'docs')
    shutil.rmtree(frag_dir, ignore_errors=True)
    for sub in ('front', 'start-here', 'part-1', 'part-2', 'part-3', 'part-4', 'back-matter', 'guides', 'reference'):
        shutil.rmtree(os.path.join(docs, sub), ignore_errors=True)

    css = []
    for st in [n for n in book.root.iter() if n.tag == 'style']:
        body = book.raw(st)
        css.append(filter_css(body[body.index('>') + 1:body.rindex('</style>')]))
    os.makedirs(os.path.join(SITE, 'src', 'styles'), exist_ok=True)
    open(os.path.join(SITE, 'src', 'styles', 'book.css'), 'w', encoding='utf-8').write(
        '/* Generated by tools/starlight/convert.py from index.html. Edit the book, not this file. */\n' + '\n'.join(css) + '\n')

    sprite, cs, core, parts = runtime(book)
    os.makedirs(frag_dir, exist_ok=True)
    fx = book.main.find(lambda n: n.get('id') == 'fx-shared')
    open(os.path.join(frag_dir, 'runtime-head.html'), 'w', encoding='utf-8').write(sprite + '\n' + (book.raw(fx) + '\n' if fx else '') + cs + '\n')
    open(os.path.join(frag_dir, 'runtime.html'), 'w', encoding='utf-8').write(core + '\n')

    labels = {}
    for ch in book.chapters:
        head = ch.find(lambda x: 'chapter-head' in x.cls)
        eb = head.find(lambda x: 'eyebrow' in x.cls) if head else None
        labels[ch.get('id')] = eb.text() if eb else ''
    for ch in book.chapters:
        if not converted(ch):
            continue
        pg = Page(book, ch)
        part = next((p for p in book.parts if p['chapters'] and p['chapters'][0] is ch), {})
        js = chapter_js(book, ch, parts)
        mdx = pg.build(ch.get('data-short'), labels[ch.get('id')], part.get('node'))
        path = os.path.join(docs, pg.here + '.mdx')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'w', encoding='utf-8').write(mdx)
        d = os.path.join(frag_dir, ch.get('id'))
        os.makedirs(d, exist_ok=True)
        for k, f in enumerate(pg.frags):
            open(os.path.join(d, '%d.html' % k), 'w', encoding='utf-8').write(f)
        open(os.path.join(d, 'demos.html'), 'w', encoding='utf-8').write(js)
        print('wrote', path, len(pg.frags), 'fragments')

    open(os.path.join(SITE, 'src', 'sidebar.json'), 'w', encoding='utf-8').write(json.dumps(sidebar(book), ensure_ascii=False, indent=1) + '\n')
    anchors = dict(book.page_of)
    for ch in book.chapters:
        if converted(ch):
            anchors[ch.get('id') + '-in-short'] = anchors[ch.get('id') + '-in-short-h'] = book.slug(ch)
    os.makedirs(os.path.join(SITE, 'public'), exist_ok=True)
    open(os.path.join(SITE, 'public', 'anchors.json'), 'w', encoding='utf-8').write(json.dumps(anchors, sort_keys=True, separators=(',', ':')) + '\n')
    print('wrote book.css, runtime, sidebar, %d anchors' % len(anchors))
    for old in set(SITE_WORDING) - book.reworded:
        print('warning: SITE_WORDING %r no longer matches the book' % old)

    for name in SITE_FILES:
        src, dst = os.path.join(ROOT, name), os.path.join(SITE, 'public', name)
        if os.path.isdir(src):
            shutil.rmtree(dst, ignore_errors=True)
            shutil.copytree(src, dst)
        else:
            text = open(src, encoding='utf-8').read()
            if name == 'llms.txt':
                # Its links to the exported files become relative, so an agent reading the site's copy stays on the site.
                for f in SITE_FILES:
                    text = text.replace(LIVE + f, f)
            open(dst, 'w', encoding='utf-8').write(text)
    print('copied %s to public/' % ', '.join(SITE_FILES))


if __name__ == '__main__':
    main()
