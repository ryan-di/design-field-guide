"""v35-5: style fixes from Ryan's review, and a one-line lede.

- The contents search box sat on a pale card-colored strip; the strip now matches the page and the field is the lighter surface.
  The placeholder was cut off mid-word, so it's shorter.
- Three demo badges had their icon off center, because a broad selector for the text beside them also matched the badge:
  the sync and check badges in good-needs-hierarchy, the playlist cover in good-problem-framing, the failed-check cross in
  good-success-criteria.
- The lede listed every part, which the part openers, the contents and the preface already do. It's now one line.

Run once after v35-4c: python3 tools/migrations/v35_5_fixes.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Book  # noqa: E402

b = Book()
assert 'Search the book' not in b.s, 'already migrated'

b.once('.toc-search{position:sticky;top:0;z-index:1;background:var(--card);',
       '.toc-search{position:sticky;top:0;z-index:1;background:var(--paper);')
b.once('.toc-search input{width:100%;font:400 15px var(--font-body);color:var(--ink);background:var(--paper);',
       '.toc-search input{width:100%;font:400 15px var(--font-body);color:var(--ink);background:var(--card);')
b.once('.toc-search input:focus{', '.hero .lede{text-wrap:balance}\n.toc-search input:focus{')
b.once('placeholder="Search components, patterns…" aria-label="Search contents"',
       'placeholder="Search the book" aria-label="Search contents"')

b.once('.cw-gnh-key span{display:inline-flex;', '.cw-gnh-key > span{display:inline-flex;')
b.once('.cw-gpf-pl-head span{display:flex;', '.cw-gpf-pl-head > span:not(.cw-gpf-cover){display:flex;')
b.once('.cw-gsc-head > span{display:flex;', '.cw-gsc-head > span:not(.cw-gsc-x){display:flex;')

i = b.s.index('<p class="lede">')
j = b.s.index('</p>', i) + 4
assert 'Play with the demos as you read' in b.s[i:j]
b.s = b.s[:i] + '<p class="lede">How to design interfaces, and why the good ones work, with a live demo for every idea.</p>' + b.s[j:]

b.save()
print('v35-5 applied')
