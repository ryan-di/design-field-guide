"""v35-1: put the rubrics that lived only in demo code into the text, and give each one scale and one set of names.

Run once after v35-0: python3 tools/migrations/v35_1_rubrics.py
Tables are generated from the demo data they replace, and the demos then read their lists back from the tables
(the vague words, the brief check, the loop stages, the ownership split), so the text and the demos can't drift.
"""
import html
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Book, table  # noqa: E402

b = Book()
assert 'data-rubric=' not in b.s, 'already migrated'
esc = lambda t: html.escape(t, quote=False)

# --- Shared style for reference tables: the book's table, stacked into rows on phones.
CSS = ('.ref .cheat{min-width:0;font-size:15px}.ref .cheat td,.ref .cheat td:nth-child(2){font-weight:400;color:var(--body)}'
       '.ref .cheat td:first-child{color:var(--ink);font-weight:600}.ref .cheat td:nth-child(2) a{color:var(--blue)}'
       '.ref var{font:500 .86em var(--font-mono);padding:0 4px;border-radius:4px;background:var(--paper-2);color:var(--ink)}'
       '@media (max-width:640px){.ref .cheat thead{display:none}.ref .cheat tr{display:block;padding:10px 14px}'
       '.ref .cheat tbody tr+tr{border-top:1px solid var(--line)}.ref .cheat td{display:block;border:0;padding:2px 0}'
       '.ref .cheat td[data-label]::before{content:attr(data-label);display:block;margin-top:6px;font:600 10.5px var(--font-mono);'
       'letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}')
b.after('@media (max-width:520px){.sec-link{display:none}.checklist .check a{white-space:normal}}', CSS)

# --- 1.2 One list of vague words, with a checkable rewrite for each group (Ch1 · success criteria, rule 4).
GROUPS = [
    ('easy easier simple simpler intuitive user-friendly', 'People find <var>X</var> without help, in under <var>N</var> clicks.'),
    ('good better improve improved improves improvement nice nicer', 'Fewer support questions about <var>Y</var>, or fewer retries when people do it.'),
    ('clean cleaner clearer modern', 'People spot the main action in a five-second look at <var>X</var>.'),
    ('seamless smooth smoother', 'Nobody gets stuck or asks for help between <var>X</var> and <var>Y</var>.'),
    ('somehow etc', 'List what you mean: <var>X</var>, <var>Y</var> and <var>Z</var>.'),
]
old_sc = ['easier', 'easy', 'simpler', 'simple', 'intuitive', 'user-friendly', 'better', 'improve', 'improved', 'improves', 'improvement',
          'nice', 'nicer', 'cleaner', 'clean', 'clearer', 'seamless', 'smooth', 'smoother']
old_brief = ['better', 'intuitive', 'easy', 'easier', 'simple', 'simpler', 'clean', 'cleaner', 'nice', 'nicer', 'modern', 'seamless', 'smooth',
             'user-friendly', 'improve', 'improved', 'etc', 'somehow', 'good']
union = {w for g, _ in GROUPS for w in g.split()}
assert union == set(old_sc) | set(old_brief), sorted(union ^ (set(old_sc) | set(old_brief)))
vague = table('good-success-criteria-words', 'vague-words', ['Vague word', 'Write instead, for example'],
              [([', '.join(g.split()), rw], ' data-words="%s"' % g) for g, rw in GROUPS])
b.entry_sub('good-success-criteria', r'(<section class="rule" id="good-success-criteria-rule-4">.*?</p>)',
            lambda m: m.group(1) + '\n<p class="prose">The demo at the top of this entry marks these words, and the '
            '<a href="#eff-brief-check">brief check</a> in Part 4 flags the same ones. Fill the slots with your own task and numbers.</p>\n' + vague)
b.once("""    const groups = [
      { words: ['easier', 'easy', 'simpler', 'simple', 'intuitive', 'user-friendly'], rewrite: ['People find ', 'X', ' without help, in under ', 'N', ' clicks.'] },
      { words: ['better', 'improve', 'improved', 'improves', 'improvement', 'nice', 'nicer'], rewrite: ['Fewer support questions about ', 'Y', ', or fewer retries when people do it.'] },
      { words: ['cleaner', 'clean', 'clearer'], rewrite: ['People spot the main action in a five-second look at ', 'X', '.'] },
      { words: ['seamless', 'smooth', 'smoother'], rewrite: ['Nobody gets stuck or asks for help between ', 'X', ' and ', 'Y', '.'] }
    ];""", """    const groups = [...document.querySelectorAll('#good-success-criteria-words tbody tr')]
      .map(tr => ({ words: tr.dataset.words.split(' '), rewrite: [...tr.cells[1].childNodes].map(n => n.textContent) }));
    if (!groups.length) throw new Error('Success criteria: the vague-word table is missing');""")

# --- 1.1 What the brief check flags (Ch26 · problem brief).
BROAD = ['users', 'user', 'everyone', 'everybody', 'people', 'all users', 'anyone']
SOL = ['dialog', 'modal', 'popup', 'pop-up', 'button', 'toggle', 'banner', 'toast', 'checkbox', 'menu']
q = lambda ws: ', '.join('“%s”' % w for w in ws[:-1]) + ' or “%s”' % ws[-1]
brief = table('eff-brief-check', 'brief-check', ['Flag', 'Shows when', 'Fix'], [
    ['Missing', 'A field is empty: who, problem, goal, constraints, non-goals or success criteria.',
     'Fill it in. Without <a href="#eff-brief-rule-2">non-goals</a>, an agent may widen the scope, and without '
     '<a href="#eff-brief-rule-3">success criteria</a>, nobody can say when it’s done.'],
    ['Vague', 'A field uses a word from the <a href="#good-success-criteria-words">vague-word table</a>, such as “better” or “intuitive”.',
     '<a href="#eff-brief-rule-4">Say what you’d see happen.</a>'],
    ['Too broad', 'Who is only <span data-words="broad" data-list="%s">%s</span>.' % ('|'.join(BROAD), q(BROAD)),
     'Name the people and the moment, like “people editing in several tabs”.'],
    ['Solution', 'The problem names a control: <span data-words="solution" data-list="%s">%s</span>.' % ('|'.join(SOL), ', '.join(SOL[:-1]) + ' or ' + SOL[-1]),
     '<a href="#eff-brief-rule-1">Describe what goes wrong instead.</a>'],
])
b.before('<h4 class="ess-h" id="eff-brief-rules">Rules</h4>',
         '<p class="prose">The brief check in the demo flags four things. Passing it doesn’t make a brief clear, but each flag is worth fixing.</p>\n' + brief)
b.once("""      const VAGUE = ['better', 'intuitive', 'easy', 'easier', 'simple', 'simpler', 'clean', 'cleaner', 'nice', 'nicer', 'modern', 'seamless', 'smooth', 'user-friendly', 'improve', 'improved', 'etc', 'somehow', 'good'];
      const BROAD = ['users', 'user', 'everyone', 'people', 'all users', 'anyone'];
      const SOL = /\\b(dialog|modal|popup|pop-up|button|toggle|banner|toast|checkbox|menu)\\b/i;""",
       """      const words = sel => {
        const el = document.querySelector(sel);
        if (!el) throw new Error('Brief check: missing ' + sel);
        return el.dataset.list ? el.dataset.list.split('|') : [...el.querySelectorAll('tbody tr')].flatMap(tr => tr.dataset.words.split(' '));
      };
      const VAGUE = words('#good-success-criteria-words');
      const BROAD = words('#eff-brief-check [data-words="broad"]');
      const SOL = new RegExp('\\\\b(' + words('#eff-brief-check [data-words="solution"]').join('|') + ')\\\\b', 'i');""")

# --- 1.3 The two framing tests, in the rules they belong to (Ch1 · problem framing).
b.within('id="good-problem-framing-rule-2"', '</p>', 'If two readers still picture different things, narrow it again.',
         'If two readers still picture different things, narrow it again. A who that’s only a group, like “users” or “everyone”, '
         'is always too broad. The <a href="#eff-brief-check">brief check</a> lists the words to watch for.')
b.within('id="good-problem-framing-rule-4"', '</p>', 'so the frame just repeats the request.',
         'so the frame just repeats the request. Any control name in the problem, like a button, a dialog or a toggle, is the sign to look for.')

# --- 1.4 The three kinds of critique (Ch6 · critique). The captions now describe the scenario only.
b.once('<p class="prose">Work at different stages needs different feedback, so there is one kind of critique for each stage. '
       'Each kind wastes time when it comes at the wrong stage.</p>',
       '<p class="prose">Work at different stages needs different feedback, so there is one kind of critique for each stage. '
       'Each kind wastes time when it comes at the wrong stage, so <a href="#good-critique-rule-3">ask which one is wanted</a>. '
       'If you can’t ask, go by how finished the work is.</p>\n' +
       table('good-critique-kinds-table', 'critique-kinds', ['Kind', 'When', 'Look at'], [
           ['Direction', 'Early sketches, while the idea can still change', 'Whether it solves the right problem'],
           ['Flow', 'The steps exist as rough screens', 'Whether people can get from start to finish without getting stuck'],
           ['Polish', 'The flow is settled and the screens are close to done', 'Contrast, alignment and wording']]))
for old, new in [
        ('Use it for early sketches, while the idea can still change. Ask whether it solves the right problem.', 'Two early sketches of a shopping list.'),
        ('Use it once the steps exist as rough screens. Ask whether people can get from start to finish without getting stuck.', 'Three rough screens, from a recipe to the list.'),
        ('Use it when the flow is settled and the screens are close to done. Look at contrast, alignment and wording.', 'A shopping list that’s close to done.')]:
    b.once("use: '%s'" % old, "use: '%s'" % new)

# --- 1.5 The loop's seven stages as a table (Ch25 · the loop). The demo reads name, input, output and owner from it.
i = b.s.index("const STAGES = [\n        { name: 'Problem'")
j = b.s.index('      ];\n', i)
block = b.s[i:j]
pat = re.compile(r"\{ name: '([^']*)', owner: '([^']*)', ownerText: '([^']*)',\s*input: '([^']*)',\s*output: '([^']*)',\s*")
stages = pat.findall(block)
assert [st[0] for st in stages] == ['Problem', 'Brief', 'Explore', 'Decide', 'Build', 'Check', 'Learn'], stages
block = pat.sub(lambda m: "{ owner: '%s',\n          " % m.group(2), block)
b.s = b.s[:i] + block + b.s[j:]
b.once("      ];\n      const list = loopStage.querySelector('#p25-stages');",
       "      ];\n      const ST = document.querySelectorAll('#eff-loop-stages tbody tr');\n"
       "      if (ST.length !== STAGES.length) throw new Error('Loop: the stage table is missing');\n"
       "      STAGES.forEach((s, i) => { const c = ST[i].cells; s.name = c[0].textContent; s.input = c[1].textContent; s.output = c[2].textContent; s.ownerText = c[3].textContent; });\n"
       "      const list = loopStage.querySelector('#p25-stages');")
b.before('<h4 class="ess-h" id="eff-loop-rules">Rules</h4>',
         '<p class="prose">Each stage at a glance. <a href="#eff-ownership">What you own, what agents do</a> shows how the split moves with the kind of work.</p>\n' +
         table('eff-loop-stages', 'loop-stages', ['Stage', 'Takes in', 'Hands on', 'Who owns it'],
               [[esc(n), esc(inp), esc(out), esc(ot)] for n, _, ot, inp, out in stages]))

# --- 1.11 Ownership: the split per kind of work, and where drafting stops (Ch25 · ownership).
i = b.s.index('      const K = {\n        fix: {')
j = b.s.index('      const bars = ownStage', i)
block = b.s[i:j]
rows = {}
for k in ['fix', 'feature', 'explore']:
    m = re.search(r'%s: \{ cap: .*?rows: \[(.*?)\] \}' % k, block, re.S)
    rows[k] = re.findall(r"\[(\d+), '([^']*)'\]", m.group(1))
    assert len(rows[k]) == 7, (k, len(rows[k]))
block, n = re.subn(r"\[(\d+), '[^']*'\]", r'[\1]', block)
assert n == 21, n
b.s = b.s[:i] + block + b.s[j:]
b.once('      const bars = ownStage',
       "      const OT = document.querySelector('#eff-ownership-split tbody');\n"
       "      if (!OT || OT.rows.length !== 7) throw new Error('Ownership: the split table is missing');\n"
       "      ['fix', 'feature', 'explore'].forEach((k, j) => K[k].rows.forEach((r, i) => { r[1] = OT.rows[i].cells[j + 1].textContent; }));\n"
       '      const bars = ownStage')
b.before('<h4 class="ess-h" id="eff-ownership-rules">Rules</h4>',
         '<p class="prose" id="eff-ownership-draft">An agent can draft any part of a brief, and any option or check, as long as it says where each part came from, '
         'such as a support thread, a ticket or a file. Confirming who has the problem, the evidence and the problem itself stays with you, '
         'and so do the choice between options and every judgment call. The table shows the split from the demo for each kind of work.</p>\n' +
         table('eff-ownership-split', 'ownership', ['Stage', 'Small fix', 'New feature', 'Open exploration'],
               [[st[0]] + [esc(rows[k][r][1]) for k in ['fix', 'feature', 'explore']] for r, st in enumerate(stages)]))

# --- 1.6 One set of stage names: the loop's (Ch31 · worked example, Ch30 contents label).
for old, new in [('Directions', 'Explore'), ('Decision', 'Decide'), ('Evaluate', 'Check'), ('Learned', 'Learn')]:
    b.once('<span class="p31-sl">%s</span>' % old, '<span class="p31-sl">%s</span>' % new)
b.once('At Decision, count “never loses work” twice', 'At Decide, count “never loses work” twice')
b.once('a plan, checks and a note on what you learned.</p>',
       'a plan, checks and a note on what you learned. The stages follow <a href="#eff-loop">the loop</a>, with Problem folded into the brief '
       'and the context pack as a step of its own.</p>')
b.once("['Evaluate', 'A three-line evaluation plan.'],\n    ['Learned', 'A session tally.']",
       "['Check', 'A three-line evaluation plan.'],\n    ['Learn', 'A session tally.']")
b.once('id="ch-evaluate" data-chapter data-short="Evaluate"', 'id="ch-evaluate" data-chapter data-short="Check"')

# --- 1.10 One scoring scale, 1 to 5 (Ch28 · decision matrix, Ch31 · worked example: x → 2x − 1 keeps the ranking).
b.once('A decision matrix scores each direction against the criteria in the brief.',
       'A decision matrix scores each direction from 1 to 5 against each criterion in the brief.')
b.once('Sample scores · 1 to 3, criteria from the brief', 'Sample scores · 1 to 5, criteria from the brief')
i = b.s.index('<table class="p31-score">')
j = b.s.index('</table>', i)
sc, n = re.subn(r'data-s="([123])"', lambda m: 'data-s="%d"' % (2 * int(m.group(1)) - 1), b.s[i:j])
assert n == 12, n
b.s = b.s[:i] + sc + b.s[j:]
b.after('.p31-score tfoot td.win{color:var(--ui-ok)}',
        '\n    @media (max-width:520px){.p31-score th,.p31-score td{padding:6px 4px}.p31-score tbody td{letter-spacing:0;font-size:11px}}')
b.once("td.textContent = '●'.repeat(s) + '○'.repeat(3 - s);\n      td.setAttribute('aria-label', s + ' of 3');",
       "td.textContent = '●'.repeat(s) + '○'.repeat(5 - s);\n      td.setAttribute('aria-label', s + ' of 5');")

# --- 1.7 Severity 0–4, with what each level means (Ch6 · heuristic review, rule 3).
b.once('Rate each problem from 1, cosmetic, to 4, catastrophe, and fix from the top.</p>',
       'Rate each problem from 0 to 4 and fix from the top. The rating weighs how many people hit the problem, how much it hurts '
       'and whether it gets in their way every time.</p>\n' +
       table('good-heuristic-review-severity', 'severity', ['Severity', 'Means', 'Example'], [
           ['0 · Not a problem', 'Not a usability problem after all. Drop it and write down why.', '“I’d make it blue”, with no problem behind it'],
           ['1 · Cosmetic', 'Fix it if there’s time left.', 'A typo: “Delivey fee”'],
           ['2 · Minor', 'Low priority: people notice it but get past it.', 'Prices are low contrast'],
           ['3 · Major', 'High priority: people struggle or lose work.', 'The basket empties when you switch restaurant'],
           ['4 · Catastrophe', 'Fix it before release: people can’t finish the task.', 'Card payment fails if the address has an accent']]))

# --- 1.8 All ten heuristics, and 1.9 the accessibility pass (Ch6 · heuristic review).
A = lambda h, t: '<a href="#%s">%s</a>' % (h, t)
ten = table('good-heuristic-review-ten', 'heuristics', ['Heuristic', 'Ask', 'In this book'], [
    ['1 · Visibility of system status', 'Does the screen always show what’s happening, and how long it will take?',
     A('pat-instant-feedback', 'Instant feedback') + ', ' + A('progress-bar', 'Progress bar')],
    ['2 · Match between the system and the real world', 'Does it use the words people use, in the order they think of things?',
     A('pat-information-scent', 'Labels in people’s words') + ', ' + A('good-plain-language', 'Plain words, one term per concept')],
    ['3 · User control and freedom', 'Can people back out of every step, even halfway through?',
     A('pat-undo', 'Undo instead of “Are you sure?”') + ', ' + A('dialog', 'Dialog')],
    ['4 · Consistency and standards', 'Does the same thing look and work the same here and in the apps people already use?',
     A('good-consistency', 'Internal and external consistency') + ', ' + A('pat-jakobs-law', 'Jakob’s law')],
    ['5 · Error prevention', 'Does the design stop the mistake before it happens?',
     A('pat-constraints', 'Constraints that prevent errors') + ', ' + A('pat-forgiving-input', 'Forgiving input')],
    ['6 · Recognition rather than recall', 'Can people see their options instead of remembering them?',
     A('good-labels', 'Labels that say what happens') + ', ' + A('pat-search-filters', 'Search with filters and recents') + ', ' + A('pat-command-palette', 'Command palette')],
    ['7 · Flexibility and efficiency of use', 'Do frequent users get faster paths that newcomers never have to learn?',
     A('pat-shortcuts', 'Keyboard shortcuts and accelerators') + ', ' + A('pat-layered-ui', 'Layered interface')],
    ['8 · Aesthetic and minimalist design', 'Does anything on the screen compete with what matters?',
     A('good-visual-hierarchy', 'Visual hierarchy') + ', ' + A('good-rams-principles', 'Rams’ ten principles')],
    ['9 · Help users recognize, diagnose, and recover from errors', 'Does each error say what went wrong and what to do next, in plain words?',
     A('good-error-copy', 'Error messages that help') + ', ' + A('error-state', 'Error state')],
    ['10 · Help and documentation', 'Is the help right where the question comes up?', A('pat-contextual-hints', 'Contextual hints over tours')]])
a11y = table('good-heuristic-review-a11y', 'a11y-pass', ['Check', 'Passes when', 'Shows in a mock?', 'In this book'], [
    ['Keyboard', 'You can finish the whole task with the keyboard alone, in reading order.', 'No, it needs a running build', A('good-keyboard-focus', 'Keyboard paths are craft')],
    ['Focus', 'Focus is always visible, moves into a dialog when it opens and back when it closes.', 'No', A('good-keyboard-focus-rule-4', 'Move focus with what opens and closes')],
    ['Contrast', 'Body text is at least 4.5 : 1 against its background; large text, edges and icons people need are at least 3 : 1.', 'Yes', A('good-contrast', 'Contrast, and never color alone')],
    ['Color', 'No meaning is carried by color alone.', 'Yes', A('good-contrast-rule-2', 'Don’t carry meaning with color alone')],
    ['Names', 'Every control says what it does, and is a real button or link that a screen reader can name.', 'Partly: the words show, the roles only in code',
     A('good-labels', 'Labels that say what happens') + ', ' + A('good-keyboard-focus-rule-3', 'Use real buttons and links')],
    ['Announcements', 'Errors, toasts and finished work appear in text that screen readers announce.', 'No', A('pat-instant-feedback', 'Instant feedback')],
    ['Motion', 'With reduce motion on, slides and zooms become an instant change or a short fade.', 'No', A('good-motion-rule-3', 'Respect reduced motion')]])
b.before('<h4 class="ess-h" id="good-heuristic-review-rules">Rules</h4>',
         '<p class="prose">The dialog in the demo breaks six of the ten. Here are all ten, each with a question to ask and the entries that cover it.</p>\n' + ten +
         '<p class="prose">Then make the accessibility pass. A mock shows only some of it, so most of these checks need a running build.</p>\n' + a11y)

b.save()
print('v35-1 applied')
