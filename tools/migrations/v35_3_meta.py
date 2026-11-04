"""v35-3: page metadata the exports read (version, date, description) and a pointer to llms.txt. Nothing visible changes.

Run once after v35-2: python3 tools/migrations/v35_3_meta.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Book  # noqa: E402

b = Book()
assert 'name="dfg-version"' not in b.s, 'already migrated'
b.after('<title>Design Field Guide</title>\n',
        '<meta name="description" content="An interactive book about design: how to tell good design, the patterns and components it is built from, and how to work with agents on it.">\n'
        '<meta name="dfg-version" content="v35">\n'
        '<meta name="dfg-date" content="2026-11">\n'
        '<link rel="alternate" type="text/markdown" href="llms.txt" title="Plain-text guide for agents">\n')
b.save()
print('v35-3 applied')
