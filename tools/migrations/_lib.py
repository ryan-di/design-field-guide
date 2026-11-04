"""Helpers shared by the migrations. Every edit asserts what it expects to find, so a migration fails instead of half-applying."""
import html
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INDEX = os.path.join(ROOT, 'index.html')


class Book:
    def __init__(self, path=INDEX):
        self.path = path
        self.s = open(path, encoding='utf-8').read()

    def save(self):
        open(self.path, 'w', encoding='utf-8').write(self.s)

    def count(self, old):
        return self.s.count(old)

    def once(self, old, new):
        """Replace a string that must occur exactly once."""
        n = self.s.count(old)
        assert n == 1, 'expected 1 match, found %d: %r' % (n, old[:120])
        self.s = self.s.replace(old, new)

    def within(self, start_marker, end_marker, old, new):
        """Replace `old` (exactly once) inside the span from start_marker to the next end_marker."""
        i = self.s.index(start_marker)
        j = self.s.index(end_marker, i)
        span = self.s[i:j]
        n = span.count(old)
        assert n == 1, 'expected 1 match in %r, found %d: %r' % (start_marker[:60], n, old[:120])
        self.s = self.s[:i] + span.replace(old, new) + self.s[j:]

    def before(self, marker, text):
        self.once(marker, text + marker)

    def after(self, marker, text):
        self.once(marker, marker + text)

    def entry(self, eid):
        """(start, end) of an entry article."""
        i = self.s.index('<article class="entry" id="%s"' % eid)
        return i, self.s.index('</article>', i)

    def entry_sub(self, eid, pattern, repl, count=1, flags=re.S):
        i, j = self.entry(eid)
        span, n = re.subn(pattern, repl, self.s[i:j], flags=flags)
        assert n == count, '%s: expected %d match(es) of %r, found %d' % (eid, count, pattern[:80], n)
        self.s = self.s[:i] + span + self.s[j:]


def rule(eid, n, title, prose, cap_b, cap_f, broken_label='Common mistake', try_shared=None, extra=''):
    """A rule with a break/fix demo, in the same markup as the book's rules. The demos are filled by D('<eid>-<n>b'|'f', …)."""
    bar_try = '<p class="fig-cap cs-try"><b>Try:</b> %s</p>' % try_shared if try_shared else ''
    side = lambda m, k, cap: ('<section class="cs-side" data-mode="%s"><div class="cs-demo" data-d="%s-%d%s"></div><div class="cs-foot">'
                              '<p class="fig-cap">%s</p><button class="cs-reset" type="button">Reset</button></div></section>') % (m, eid, n, k, cap)
    t = strip(title)
    return ('<section class="rule" id="%s-rule-%d"><h5><span class="n">%d</span>%s</h5><p class="prose">%s</p>\n%s'
            '<div class="cs-case" aria-label="%s"><div class="cs-panel"><div class="cs-bar"><div class="cs-switch" role="radiogroup" aria-label="Show">'
            '<button type="button" role="radio" class="b" data-mode="broken"><span class="dot"></span>%s</button>'
            '<button type="button" role="radio" class="f" data-mode="fixed"><span class="dot"></span>Do this instead</button></div>%s</div>%s%s</div></div></section>\n'
            ) % (eid, n, n, title, prose, extra, html.escape(t, quote=True), broken_label, bar_try, side('broken', 'b', cap_b), side('fixed', 'f', cap_f))


def strip(h):
    return html.unescape(re.sub(r'<[^>]+>', '', h))


def table(tid, rubric, cols, rows, label_first=False):
    """A reference table in the book's table style. Cells are HTML. Rows may be (cells, tr_attrs) tuples."""
    head = ''.join('<th scope="col">%s</th>' % c for c in cols)
    body = []
    for r in rows:
        attrs = ''
        if isinstance(r, tuple):
            r, attrs = r
        tds = []
        for k, cell in enumerate(r):
            lab = '' if (k == 0 and not label_first) else ' data-label="%s"' % html.escape(strip(cols[k]), quote=True)
            tds.append('<td%s>%s</td>' % (lab, cell))
        body.append('<tr%s>%s</tr>' % (attrs, ''.join(tds)))
    return ('<div class="table-wrap ref" id="%s" data-rubric="%s"><table class="cheat">'
            '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>\n') % (tid, rubric, head, ''.join(body))
