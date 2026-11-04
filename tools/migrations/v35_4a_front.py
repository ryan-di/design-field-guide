"""v35-4a: front matter. A preface on how to read the book, "How each entry reads" for Parts 3 and 4, and the
rule-intro sentence about demos said once in the preface instead of 97 times.

Run once after v35-3: python3 tools/migrations/v35_4a_front.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Book  # noqa: E402

b = Book()
assert 'id="ch-preface"' not in b.s, 'already migrated'

PREFACE = '''<section class="chapter" id="ch-preface" data-chapter data-short="How to read this book">
  <div class="chapter-head">
    <p class="eyebrow">Preface</p>
    <h2>How to read this book</h2>
  </div>
  <div class="prose">
    <p>This book is for anyone who decides how an interface should work, and most of all for design engineers, who make those calls in code. It teaches by showing: every idea comes with a demo you can try on the page.</p>
    <h4>Three ways to read it</h4>
    <p>Read it from the start. Each part builds on the one before, and Part 4 puts the first three to work on one problem. Or start from a question: <a href="#ch-patterns-cheat">When you hear this, try that</a> goes from what people say to a pattern, and <a href="#ch-choose">Before you pick one, ask three questions</a> goes from what people need to a component. Or keep it open while you work: <a href="#ch-good-checklist">Before you ship, ask these</a> and <a href="#ch-eff-checklist">Effective design, step by step</a> turn the book into questions for your next change.</p>
    <h4>How an entry works</h4>
    <p>An entry starts with what the idea is and a demo, with a short “Try it” line that says what to look for. Many entries then show the forms or ways it comes in. Then come the rules, each with its own demo and a switch between two sides: what goes wrong, and “Do this instead”. The first side is called “Common mistake” in Parts 1 and 4, “When it backfires” for patterns, because every pattern has a cost, and “When it breaks” for components. Last, “In real products” shows the idea in products you may know.</p>
    <p>Tick “Learned” when an idea clicks. The contents show how many you’ve ticked, and your progress stays in this browser.</p>
    <h4>What the examples are</h4>
    <p>The product examples are this book’s summaries of how those products worked when it was written, not the companies’ own descriptions, so check the product before you cite how it behaves. Part 4 names the tools of 2026, such as Claude Code, Figma, Linear and Playwright. Each rule says what to do first, so it still holds when a tool changes.</p>
    <h4>How to cite it</h4>
    <p>Every entry, section and rule has its own link: press the # next to its title. To cite one, give the version and the link’s anchor, such as “Design Field Guide v35, #good-problem-framing-rule-2”. Agents can read the same book as plain text, starting from <a href="llms.txt">llms.txt</a>.</p>
  </div>
</section>

'''
b.before('<div class="part-divider" id="start"', PREFACE)

b.within('<section class="chapter" id="ch-start"', '</section>',
         '  <div class="prose">\n    <h4>The interruption ladder</h4>',
         '  <div class="prose">\n    <h4>How each entry reads</h4>\n'
         '    <p>Each component is a short article. It says what the component is for, with a demo. Then its forms, and the rules: '
         'each shows how the component breaks and what to do instead, with a demo you can switch between the two. Last, real products that use it.</p>\n'
         '  </div>\n'
         '  <div class="prose">\n    <h4>The interruption ladder</h4>')

b.within('<section class="chapter" id="ch-eff-start"', '</section>',
         ' The worked example in the last chapter follows it through every stage.</p>\n  </div>',
         ' The worked example in the last chapter follows it through every stage.</p>\n'
         '    <h4>How each entry reads</h4>\n'
         '    <p>Each entry is one step of the work. It says what the step is for, with a demo that most often uses the problem above. '
         'Then the rules: each shows a common mistake and what to do instead, with a demo you can switch between the two. '
         'Last, how real teams and products do it.</p>\n  </div>')

b.s, n = re.subn(r'(<h4 class="ess-h" id="[\w-]+-rules">Rules</h4>\s*<p class="prose">[^<]*?) Each comes with a demo\. '
                 r'Switch between “[^”<]+” and “Do this instead” to see the difference\.</p>', r'\1</p>', b.s)
assert n == 97, 'expected 97 rule intros, found %d' % n
assert 'Each comes with a demo' not in b.s
b.save()
print('v35-4a applied')
