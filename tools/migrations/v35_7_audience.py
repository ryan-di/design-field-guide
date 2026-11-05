"""v35-7: who the book is for. Agents write most of the code now, so the book is framed around the calls they don't make
for you: how an interface should work, and whether what got built is right. It was written for design engineers; it's now
for anyone who makes those calls.

- The series is "a design primer for the agent era" instead of "the design engineer primer" (hero and colophon).
- The preface opens with that framing.
- Start here: the second essay was "What design engineering is". It's now "Design when agents build", with the role table
  replaced by what you own and what the agent does. The entry id stays design-engineering, since it's in the id baseline.
- Craft and Practice no longer speak to "a design engineer".
- The colophon says the site is generated from the one-file source.

Run once after v35-6: python3 tools/migrations/v35_7_audience.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Book  # noqa: E402

b = Book()
assert 'Design primer for the agent era' not in b.s, 'already migrated'

b.once('<p class="eyebrow">Design engineer primer · Book 1</p>',
       '<p class="eyebrow">Design primer for the agent era · Book 1</p>')

b.once('<p>This book is for anyone who decides how an interface should work, and most of all for design engineers, who make '
       'those calls in code. It teaches by showing',
       '<p>This book is about the part of making software that agents don’t do for you: deciding how an interface should '
       'work, and telling whether what got built is any good. Agents can write most of the code now, so these calls are what '
       'make a product good. The book is for anyone who makes them, whether you design, write code, run the product or '
       'direct the agents that do. It teaches by showing')

b.once('<p class="part-title">Design and design engineering</p>\n'
       '  <p class="part-sub">Two short definitions before the rest of the book: what design is, and what a design engineer does.</p>',
       '<p class="part-title">Design, and what agents change</p>\n'
       '  <p class="part-sub">Two short essays before the rest of the book: what design is, and what’s left for you when agents write the code.</p>')
b.once('<section class="chapter" id="ch-intro" data-chapter data-short="Two definitions">',
       '<section class="chapter" id="ch-intro" data-chapter data-short="Two ideas">')

i, j = b.entry('design-engineering')
old = b.s[i:j]
new = old
for a, z in [
    ('data-name="What design engineering is"', 'data-name="Design when agents build"'),
    ('<h3>What design engineering is</h3>', '<h3>Design when agents build</h3>'),
    ('<p class="prose">A design engineer designs in the material the product is made of: code. Instead of handing over '
     'pictures, they build the thing, try it, and change it until it works.</p>',
     '<p class="prose">Agents can turn a clear description into working code in minutes. Building used to be the slow, costly '
     'part of making a product. Now the slow part is knowing what to ask for, and seeing what’s wrong with what comes back.</p>'),
    ('<p class="prose">The role exists because many design decisions only show up when something runs. How long should a '
     'spinner wait before it appears? What happens to a 40-character name? Where does focus go when a dialog closes? A mockup '
     'rarely answers these, but a prototype in code answers them in minutes.</p>',
     '<p class="prose">The details matter as much as ever. How long should a spinner wait before it appears? What happens to a '
     '40-character name? Where does focus go when a dialog closes? An agent answers each of these with a guess, most often the '
     'common choice, and the guess usually looks fine in a demo. Whether it fits your product is a design call, and you can '
     'only make it if you know what good looks like.</p>'),
    ('<div><h4>Prototypes</h4><p>Quick working versions that answer a design question, so the team decides on evidence '
     'instead of opinions.</p></div>',
     '<div><h4>What to build</h4><p>A problem and a behavior clear enough that an agent builds the right thing, not only a '
     'working one.</p></div>'),
    ('<div><h4>The details</h4><p>States, timing, motion, edge cases and the keyboard path. Mockups skip them, but people '
     'notice all of them.</p></div>',
     '<div><h4>What good looks like</h4><p>States, timing, motion, edge cases and the keyboard path. Agents skip them unless '
     'asked, and people notice all of them.</p></div>'),
    ('<div><h4>What ships</h4><p>Keeping what was designed and what ships the same, through components, tokens and review '
     'of the built thing.</p></div>',
     '<div><h4>Whether it’s right</h4><p>Checking the built thing in every state, because a build can pass every test and '
     'still feel wrong.</p></div>'),
    ('<p class="prose">It sits between two roles that already exist. The three differ mostly in where each one starts and '
     'what each one is judged on.</p>',
     '<p class="prose">The work splits by what each side is good at. The agent is fast at what can be written down, and you '
     'own what needs judgment.</p>'),
    ('<thead><tr><th></th><th>Designer</th><th>Design engineer</th><th>Frontend engineer</th></tr></thead>',
     '<thead><tr><th></th><th>You</th><th>The agent</th></tr></thead>'),
    ('<tr><td>Starts from</td><td>A problem and the people who have it</td><td>A design question, or a design that has to '
     'work for real</td><td>A spec and a codebase</td></tr>',
     '<tr><td>Starts from</td><td>A problem and the people who have it</td><td>Your brief and the codebase</td></tr>'),
    ('<tr><td>Produces</td><td>Flows, mockups, the design system</td><td>Working prototypes, interface details, '
     'components</td><td>Features that ship, are tested and can be maintained</td></tr>',
     '<tr><td>Produces</td><td>The brief, the decisions and the review</td><td>Plans, prototypes and code</td></tr>'),
    ('<tr><td>Judged on</td><td>Whether it solves the right problem clearly</td><td>Whether the built thing feels as '
     'intended, in every state</td><td>Whether it works, is fast and lasts</td></tr>',
     '<tr><td>Judged on</td><td>Whether the right problem is solved, in every state</td><td>Whether the result does what '
     'the brief asks</td></tr>'),
    ('<p class="prose">The rest of the book follows that work, from judging the problem to shipping the solution.</p>',
     '<p class="prose">Parts 1 to 3 train that judgment: what makes a product and its interactions good, and why. Part 4 '
     'puts it to work with agents, from framing the problem to shipping the solution.</p>'),
]:
    assert new.count(a) == 1, 'design-engineering: expected 1 match of %r' % a[:80]
    new = new.replace(a, z)
b.s = b.s[:i] + new + b.s[j:]

b.once('It lives in code, which is why it’s where a design engineer earns their keep.',
       'It lives in code, and agents leave it out unless someone asks for it, so it’s where your judgment shows most.')
b.once('As a design engineer, you also have an edge: you can design in the real material,',
       'Agents also give you an edge: building is cheap now, so you can design in the real material,')

b.once('Design Field Guide is Book 1 of the design engineer primer.',
       'Design Field Guide is Book 1 of a design primer for the agent era.')
b.once('<p>The book is one HTML file, with every demo built in. Agents can read the same text, generated from this page, '
       'starting from <a href="llms.txt">llms.txt</a>.</p>',
       '<p>The book’s source is one HTML file, with every demo built in, and this site is generated from it. Agents can read '
       'the same text as plain files, starting from <a href="llms.txt">llms.txt</a>.</p>')

assert 'design engineer' not in b.s.lower().replace('design-engineering', ''), 'a "design engineer" mention is left'
b.save()
print('v35-7 applied')
