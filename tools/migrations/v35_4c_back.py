"""v35-4c: back matter. An afterword, a glossary, sources and a colophon after Part 4; the endnote's companion decks
move into the colophon (its "Go deeper" sentence pointed at sections removed in v33); one title made unique;
US spelling for gray.

Run once after v35-4b: python3 tools/migrations/v35_4c_back.py
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Book  # noqa: E402

b = Book()
assert 'id="ch-glossary"' not in b.s, 'already migrated'


def link(i, t):
    assert 'id="%s"' % i in b.s, 'no #%s' % i
    return '<a href="#%s">%s</a>' % (i, t)


# term, definition (HTML), entry id, entry title
GLOSSARY = [
    ('A/B test', 'A test where each group of people gets a different version, so you can compare what they do. It’s judged on one main number agreed before the test, plus a <a href="#gl-guardrail">guardrail</a>.', 'eff-measure', 'Measure against the brief'),
    ('Artifact', 'Something small a stage of the work leaves for others to read or try, such as a brief, a decision or a plan. In Part 4 it is often an artifact page: one shared web page an agent made.', 'eff-worked-example', 'Follow one problem through'),
    ('Attention, lifetime and control', 'The three things every component promises: how much it interrupts, how long it stays, and what people can do with it.', 'ch-start', 'Read every component as a promise'),
    ('Axis', 'One dimension with two ends that options vary along, such as how loud a message is, from silent to blocking. Two axes make a grid, and each cell is a <a href="#gl-direction">direction</a>.', 'eff-axes', 'Vary along named axes'),
    ('Bet', 'The guess about what people need that a direction is built around, such as “never interrupt” or “make it fixable in one step”.', 'eff-explore-wide', 'Get many directions cheaply'),
    ('Brief', 'A short note written before anyone builds: who has the problem, what should change, what’s off limits and how you’ll know it worked.', 'eff-brief', 'Write the problem brief'),
    ('Context pack', 'What a new teammate would need on their first day: design tokens, components to reuse, copy rules, examples of good screens, repo conventions and the design frames.', 'eff-context-pack', 'Pack the context'),
    ('Critique', 'Judging work against what it is for: start from the goal, say what serves it and what doesn’t, then suggest a fix. It comes in three kinds: direction for early sketches, flow once the steps exist as rough screens, and polish when the screens are close to done.', 'good-critique', 'Critique against the goal'),
    ('Decision matrix', 'A table that scores each direction from 1 to 5 against each criterion in the brief. Each criterion has a <a href="#gl-weight">weight</a>, so what the problem is about counts more.', 'eff-decision-matrix', 'Score directions against the brief'),
    ('Definition of done', 'The list of checks a change must pass before you call it finished. Each is something you could see or run, and says who checks it.', 'eff-definition-of-done', 'Define done so both of you can check it'),
    ('Design rationale', 'The reasoning behind a design decision, written down: the problem, the options you considered, the one you chose and why.', 'good-design-rationale', 'Write down the reasoning'),
    ('Design token', 'A shared value with a name, such as a corner radius, a spacing step, a color or a text size.', 'good-design-tokens', 'Design tokens'),
    ('Diff', 'The lines a change adds and removes, as a pull request shows them. Skim it for new strings, styles and components.', 'eff-ux-calls', 'Call out what people will see'),
    ('Direction', 'One clearly different answer to the brief, explored on its own, so you can lay several side by side and choose.', 'eff-explore-wide', 'Get many directions cheaply'),
    ('End-to-end spec', 'A test that uses the app the way people do, through its screens, such as a Playwright spec. Unit tests check the logic underneath.', 'eff-agent-verification', 'Let agents prove their work'),
    ('Feature flag', 'A switch that keeps new code turned off for people, so a step can merge before the step that completes it lands.', 'eff-small-steps', 'Plan, then take small steps'),
    ('Fidelity', 'How close a sketch, mock or prototype is to the real thing, from a sketch to a branch in the app. Each level shows some things and hides others.', 'good-heuristic-review-fidelity', 'what each fidelity can show'),
    ('Guardrail', 'One number that must not get worse, with a limit you set before looking.', 'eff-measure', 'Measure against the brief'),
    ('Heuristic review', 'A check of a design against a short list of rules of thumb, such as Jakob Nielsen’s ten usability heuristics. It finds likely problems, not proven ones.', 'good-heuristic-review', 'Heuristic review'),
    ('Interruption ladder', 'The ways to tell people something, from quietest to loudest: inline message, badge, toast, banner, dialog. Use the lowest step that still does the job.', 'ch-start', 'Read every component as a promise'),
    ('Loop', 'The stages every change goes through: Problem, Brief, Explore, Decide, Build, Check and Learn. What Learn finds starts the next round.', 'eff-loop', 'The loop'),
    ('MCP', 'A standard way to plug tools into an agent, such as a connector that lets it read Figma frames.', 'eff-context-pack', 'Pack the context'),
    ('Pattern', 'A solution shape that has worked many times before, such as undo instead of a confirm. Every pattern has a <a href="#gl-trade-off">trade-off</a>.', 'ch-patterns-start', 'Name the problem before the fix'),
    ('Plan mode', 'A way of working where the agent proposes a plan and changes nothing until you agree to it, such as Claude Code’s plan mode.', 'eff-small-steps', 'Plan, then take small steps'),
    ('Problem frame', 'Who has the problem, what they’re trying to do and what stops them, written down before anyone draws a screen.', 'good-problem-framing', 'Frame the problem'),
    ('Severity', 'How bad a usability problem is, from 0 to 4: 0 isn’t a problem after all, 1 is cosmetic, 2 minor, 3 major, where people struggle or lose work, and 4 a catastrophe, where they can’t finish the task.', 'good-heuristic-review-severity', 'the severity scale'),
    ('Subagent', 'A helper agent that works alongside the others, such as one for each direction.', 'eff-explore-wide', 'Get many directions cheaply'),
    ('Success criteria', 'What you would see or count if a change worked.', 'good-success-criteria', 'Define “good” before building'),
    ('Trade-off', 'What a pattern costs. Hidden things get forgotten, for example, and experts pay an extra click.', 'ch-patterns-start', 'Name the problem before the fix'),
    ('Usability test', 'Watching real people use a design to do a task, and noting where they stall. It finds problems that a review can only guess at.', 'eff-quick-sessions', 'Watch a few people use it'),
    ('UX call', 'A choice people will see in a change, such as the wording, the spacing or which kind of dialog appears. Decide each one and name it in the pull request.', 'eff-ux-calls', 'Call out what people will see'),
    ('Weight', 'How much a criterion counts in a <a href="#gl-decision-matrix">decision matrix</a>.', 'eff-decision-matrix', 'Score directions against the brief'),
    ('Worktree', 'A separate working copy of the code, made with git, so several agents can work at once without clashing.', 'eff-explore-wide', 'Get many directions cheaply'),
]
slug = lambda t: 'gl-' + re.sub(r'[^a-z0-9]+', '-', t.lower().replace('/', '')).strip('-')
assert [g[0] for g in GLOSSARY] == sorted((g[0] for g in GLOSSARY), key=str.lower), 'keep the glossary alphabetical'
gl_ids = {slug(g[0]) for g in GLOSSARY}
for _, d, _, _ in GLOSSARY:
    for ref in re.findall(r'href="#(gl-[\w-]+)"', d):
        assert ref in gl_ids, ref
glossary = '\n'.join('      <dt id="%s">%s</dt><dd>%s %s</dd>' % (slug(t), html.escape(t, quote=False), d, link(i, 'See ' + lt if lt[0].islower() else lt))
                     for t, d, i, lt in GLOSSARY)

# title, url, who/when/type, entries it supports
SOURCES = [
    ('Part 1 · Good design', [
        ('10 Usability Heuristics for User Interface Design', 'https://www.nngroup.com/articles/ten-usability-heuristics/', 'Jakob Nielsen, Nielsen Norman Group, 1994, updated since · article', [('good-heuristic-review', 'Heuristic review')]),
        ('Severity Ratings for Usability Problems', 'https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/', 'Jakob Nielsen, Nielsen Norman Group, 1994 · article', [('good-heuristic-review-severity', 'the severity scale')]),
        ('Good design', 'https://www.vitsoe.com/us/about/good-design', 'Dieter Rams’ ten principles, Vitsœ · web page', [('good-rams-principles', 'Rams’ ten principles')]),
        ('Web Content Accessibility Guidelines (WCAG) 2.2', 'https://www.w3.org/TR/WCAG22/', 'W3C, 2023 · standard. Explained in Understanding '
         '<a href="https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html">Contrast (Minimum)</a>, '
         '<a href="https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html">Use of Color</a> and '
         '<a href="https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html">Target Size (Minimum)</a>',
         [('good-contrast', 'Contrast, and never color alone'), ('icon-button', 'Icon button')]),
        ('prefers-reduced-motion', 'https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion', 'MDN Web Docs · reference', [('good-motion', 'Motion with a purpose')]),
    ]),
    ('Part 2 · Patterns', [
        ('Laws of UX', 'https://lawsofux.com/', 'Jon Yablonski · website, with pages on '
         '<a href="https://lawsofux.com/jakobs-law/">Jakob’s law</a>, <a href="https://lawsofux.com/fittss-law/">Fitts’s law</a>, '
         '<a href="https://lawsofux.com/hicks-law/">Hick’s law</a> and <a href="https://lawsofux.com/teslers-law/">Tesler’s law</a>',
         [('ch-laws', 'Lean on how people already behave')]),
        ('The information capacity of the human motor system in controlling the amplitude of movement', 'https://doi.org/10.1037/h0055392', 'Paul M. Fitts, Journal of Experimental Psychology, 1954 · paper', [('pat-fitts-law', 'Fitts’s law')]),
        ('On the rate of gain of information', 'https://doi.org/10.1080/17470215208416600', 'W. E. Hick, Quarterly Journal of Experimental Psychology, 1952 · paper', [('pat-hicks-law', 'Hick’s law')]),
    ]),
    ('Part 4 · Effective design', [
        ('Shape Up', 'https://basecamp.com/shapeup', 'Ryan Singer, Basecamp, 2019 · book, free online', [('eff-loop', 'The loop'), ('eff-worked-example', 'Follow one problem through')]),
        ('The Design Sprint', 'https://www.gv.com/sprint/', 'GV · web page; also the book <i>Sprint</i> by Jake Knapp, John Zeratsky and Braden Kowitz, 2016', [('eff-loop', 'The loop'), ('eff-worked-example', 'Follow one problem through')]),
        ('Working Backwards', 'https://www.allthingsdistributed.com/2006/11/working_backwards.html', 'Werner Vogels, All Things Distributed, 2006 · article', [('eff-brief', 'Write the problem brief'), ('eff-worked-example', 'Follow one problem through')]),
    ]),
]
sources = []
for h4, items in SOURCES:
    sources.append('    <h4>%s</h4>\n    <ul class="sources">' % h4)
    for t, u, meta, uses in items:
        used = ' and '.join(link(i, lt) for i, lt in uses)
        sources.append('      <li><a href="%s">%s</a> <span class="src-meta">· %s</span><br>In this book: %s.</li>' % (u, t, meta, used))
    sources.append('    </ul>')
sources = '\n'.join(sources)

ENDNOTE = re.search(r'<p class="endnote">Companion decks in this primer: (.*?)\. Sources named under “Go deeper” are starting points to look up; '
                    r'they’re named from memory, so search by title\.</p>\n', b.s)
assert ENDNOTE, 'endnote not found'
decks = ENDNOTE.group(1)
b.once(ENDNOTE.group(0), '')

BACK = '''

<div class="part-divider" id="back" data-part="Back matter">
  <p class="eyebrow">Back matter</p>
  <p class="part-title">Afterword and reference</p>
  <p class="part-sub">How the parts fit together, the terms this book uses, and where its principles come from.</p>
</div>

<section class="chapter" id="ch-afterword" data-chapter data-short="Afterword">
  <div class="chapter-head">
    <p class="eyebrow">Afterword</p>
    <h2>Where to go from here</h2>
  </div>
  <div class="prose">
    <p>The four parts meet in <a href="#eff-loop">the loop</a>. You frame the problem and set success criteria with Part 1, explore and build with the patterns and components in Parts 2 and 3, and check the result with the critique and review from Part 1 again. What you learn then starts the next round.</p>
    <p>To start, take a ticket you already have. Before you open a design tool or an editor, <a href="#good-problem-framing">frame the problem</a>: who has it, what they’re trying to do, what stops them, and how you’ll know it’s better. Then, before it ships, go through <a href="#ch-good-checklist">Before you ship, ask these</a>.</p>
  </div>
</section>

<section class="chapter" id="ch-glossary" data-chapter data-short="Glossary">
  <div class="chapter-head">
    <p class="eyebrow">Reference</p>
    <h2>Glossary</h2>
  </div>
  <div class="prose">
    <p>Terms this book uses in a specific sense, each with the entry that explains it.</p>
    <dl class="glossary">
%s
    </dl>
  </div>
</section>

<section class="chapter" id="ch-sources" data-chapter data-short="Sources">
  <div class="chapter-head">
    <p class="eyebrow">Reference</p>
    <h2>Sources</h2>
  </div>
  <div class="prose">
    <p>The work behind the principles, laws, standards and methods this book names, each with where the book uses it. The product examples aren’t listed: they’re this book’s own summaries, as <a href="#ch-preface">the preface</a> says.</p>
%s
  </div>
</section>

<section class="chapter" id="ch-colophon" data-chapter data-short="Colophon">
  <div class="chapter-head">
    <p class="eyebrow">Colophon</p>
    <h2>About this edition</h2>
  </div>
  <div class="prose">
    <p>Design Field Guide is Book 1 of the design engineer primer. This is version <span id="colophon-version">v35</span>, from November 2026. The <a href="CHANGELOG.md">changelog</a> lists what changed in each version, and the source is on <a href="https://github.com/ryan-di/design-field-guide">GitHub</a>.</p>
    <p>The book is one HTML file, with every demo built in. Agents can read the same text, generated from this page, starting from <a href="llms.txt">llms.txt</a>.</p>
    <p>Companion decks in this primer: %s.</p>
  </div>
</section>''' % (glossary, sources, decks)

i = b.s.index('<section class="chapter" id="ch-eff-checklist"')
j = b.s.index('\n</section>', i) + len('\n</section>')
b.s = b.s[:j] + BACK + b.s[j:]

b.before('<script>\n(() => {\n  // "In short": each chapter', '''<style>
.glossary{display:grid;grid-template-columns:minmax(140px,210px) minmax(0,1fr);gap:12px 24px;margin:6px 0 0}
.glossary dt{font:600 16px/1.5 var(--font-body);color:var(--ink);scroll-margin-top:24px}
.glossary dd{margin:0;font-size:16px;line-height:1.55;color:var(--body)}
.sources{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:14px}
.sources li{font-size:16px;line-height:1.55;color:var(--body)}
.sources .src-meta{color:var(--muted)}
#ch-colophon .prose{font-size:16px;color:var(--muted)}
@media (max-width:640px){.glossary{grid-template-columns:minmax(0,1fr);gap:2px}.glossary dd{margin-bottom:12px}}
</style>
''')

old = 'data-learned="eff-prototype-in-code"'
b.once('<div class="entry-head"><h3>Prototype in the real material</h3><label class="learned"><input type="checkbox" %s>' % old,
       '<div class="entry-head"><h3>Prototype at the fidelity the question needs</h3><label class="learned"><input type="checkbox" %s>' % old)

JS_NAME = re.compile(r'\s*=\s*\$\(|\.(checked|addEventListener|classList)\b')
n = 0


def gray(m):
    global n
    if JS_NAME.match(b.s, m.end()):
        return m.group(0)
    n += 1
    return m.group(1).replace('e', 'a') + 'ray' + (m.group(2) or '')


b.s = re.sub(r'(?<=[ >(])([Gg])rey(ed)?(?=[ ,.;:)<’])', lambda m: gray(m) if True else m, b.s)
assert n >= 30, 'expected about 33 visible "grey"s, changed %d' % n
b.save()
print('v35-4c applied; %d "grey" -> "gray"' % n)
