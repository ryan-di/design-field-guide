"""v35-2: four new rules the skills rely on, each with a break/fix demo, plus the sentences that connect them.

Run once after v35-1: python3 tools/migrations/v35_2_principles.py
- Ch1 problem framing, rule 5: leave what you don't know empty (and look before you guess).
- Ch6 critique, rule 4: hear their read first.
- Ch6 heuristic review, rule 4: say what a mock can't show, with a fidelity table. Rule 2: when an agent counts as a reviewer.
- Ch25 the loop, rule 5: frame a hunch as a question.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Book, table, rule  # noqa: E402

b = Book()
assert 'id="good-critique-rule-4"' not in b.s, 'already migrated'
WORDS = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six']


def add_rule(eid, n, title, prose, cap_b, cap_f, js, extra='', try_shared=None):
    i, j = b.entry(eid)
    a = b.s[i:j]
    label = re.search(r'class="b" data-mode="broken"><span class="dot"></span>([^<]+)</button>', a).group(1)
    assert 'id="%s-rule-%d"' % (eid, n - 1) in a and 'id="%s-rule-%d"' % (eid, n) not in a
    tail = '</div></div></section>\n'
    marker = tail + "<script>\n(() => {\n  const cs = document.currentScript.closest('.cs');"
    assert a.count(marker) == 1, eid
    a = a.replace(marker, tail + rule(eid, n, title, prose, cap_b, cap_f, label, try_shared, extra) + marker[len(tail):])
    assert a.count('\n  csInit(cs);') == 1, eid
    a = a.replace('\n  csInit(cs);', '\n' + js.strip('\n') + '\n\n  csInit(cs);')
    old = '<p class="prose">%s rules keep' % WORDS[n - 1]
    assert a.count(old) == 1, (eid, old)
    a = a.replace(old, '<p class="prose">%s rules keep' % WORDS[n])
    b.s = b.s[:i] + a + b.s[j:]


# --- Small styles the new demos need (the rest reuse each entry's own demo classes).
CSS = ('#good-problem-framing .nf-row{display:grid;grid-template-columns:84px minmax(0,1fr);gap:8px;align-items:baseline;padding:6px 0;border-top:1px solid var(--ui-border)}'
       '#good-problem-framing .nf-row em{font-style:normal;color:var(--ui-muted)}'
       '#good-problem-framing .nf-tag{display:inline-block;margin-top:3px;font:600 10.5px var(--font-mono);letter-spacing:.03em;padding:1px 7px;border-radius:999px;background:var(--ui-hover);color:var(--ui-muted)}'
       '#good-problem-framing .nf-tag.g{background:var(--ui-sel-soft);color:var(--ui-sel)}'
       '#good-problem-framing .nf-out{margin:0;font-size:13.5px;line-height:1.45}#good-problem-framing .nf-out:empty{display:none}')
b.after('.ref .cheat td[data-label]::before{content:attr(data-label);display:block;margin-top:6px;font:600 10.5px var(--font-mono);'
        'letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}', CSS)

# --- 2.2 Ch1 · problem framing, rule 5.
add_rule('good-problem-framing', 5, 'Leave what you don’t know empty',
         'A frame filled with guesses reads like fact, so nobody checks it, and the team builds for a problem that may not exist. '
         'Say where each part came from: something people told you, something you read or saw, or your own guess. '
         'Look before you guess, in the support threads, tickets and notes that already exist. When nobody knows yet, leave the part empty '
         'and add it to a list of things to check. Label any guess with how you’ll check it, and when two sources disagree, show both.',
         'Every part is filled in, and nothing says where it came from. <b>Try:</b> press Share with the team.',
         'Each part says where it came from, and the unknowns are a list. <b>Try:</b> press Share with the team.', r"""
  /* 5. Guesses that read like facts */
  const nfRow = (k, v, tag, g) => '<div class="nf-row"><span class="pf-k">' + k + '</span><span>' + v + (tag ? '<br><span class="nf-tag' + (g ? ' g' : '') + '">' + tag + '</span>' : '') + '</span></div>';
  const nfHtml = rows => '<div class="pf-card"><span class="pf-k">Problem frame · Export</span><div>' + rows + '</div>' +
    '<div class="pf-opts"><button class="btn btn-secondary cs-sm" type="button" data-go>Share with the team</button></div><p class="nf-out" data-out></p></div>';
  const nfWire = msg => d => { const o = d.querySelector('[data-out]'), g = d.querySelector('[data-go]'); g.addEventListener('click', () => { o.innerHTML = msg; g.disabled = true; }); };
  D('good-problem-framing-5b', nfHtml(nfRow('Who', 'Photographers on a deadline') + nfRow('Trying to', 'Send a finished album to a client') +
    nfRow('In the way', 'Export is slow and confusing') + nfRow('How often', 'All the time')),
    nfWire('<b>Ben:</b> Where does “on a deadline” come from? And “all the time”? Nobody can tell what was seen and what was guessed, so the team argues instead of checking.'));
  D('good-problem-framing-5f', nfHtml(nfRow('Who', 'People exporting albums for clients', 'Support · 14 threads') +
    nfRow('Trying to', 'Send a finished album to a client', 'They said so') +
    nfRow('In the way', 'Export overwrites a file with the same name', 'Seen in 2 of 5 sessions') +
    nfRow('How often', '<em>Unknown</em>', 'To check · export logs', true) +
    nfRow('Why', 'Guess: they export late, close to a deadline', 'Guess · ask in the next sessions', true)),
    nfWire('<b>Ben:</b> I can pull the export logs today. The rest we can build on, and the guess gets checked in Thursday’s sessions.'));""")
b.once('A longer one likely covers more than one problem, so split it.',
         'A longer one likely covers more than one problem, so split it. Say where each part came from, and '
         '<a href="#good-problem-framing-rule-5">leave what you don’t know empty</a>.')
b.once('<dt>Evidence</dt><dd>Say where you saw it: a support thread, a session you watched, your own runs.</dd>',
       '<dt>Evidence</dt><dd>Three support threads this month, and you lost work the same way in your own runs. To check: how often it happens.</dd>')

# --- 2.1 Ch6 · critique, rule 4, and the two places that share the order.
add_rule('good-critique', 4, 'Hear their read first',
         'When the reviewer speaks first, the designer’s view bends toward theirs: they defend the design or take every note, '
         'and the doubt they already had never comes up. Ask the designer what works for them and what worries them, then give your critique, '
         'and say where the two agree and where they don’t. The same goes for an agent’s review: get the designer’s read before you show it.',
         'The reviewer opens with her notes. <b>Try:</b> press Two weeks later.',
         'The reviewer asks for the designer’s read first. <b>Try:</b> press Write down the next steps.', r"""
  /* 4. Reviewer first vs designer first */
  const bookApp = '<div class="cr-app"><div class="cr-bar"><span>Book a table</span><span class="cs-meta">Sketch v2</span></div><div class="cr-body">' +
    '<span class="cr-fld">Date<span class="cr-in">Today</span></span><span class="cr-fld">Time<span class="cr-acts">' +
    ['18:00', '18:30', '19:00', '19:30'].map(t => '<span class="cr-in">' + t + '</span>').join('') + '</span></span>' +
    '<span class="btn btn-primary cs-sm" style="justify-content:center">Book</span></div></div>';
  const readBtn = label => '<div class="cr-acts"><button class="btn btn-secondary cs-sm" type="button" data-go>' + label + '</button></div><p class="cs-meta" data-out></p>';
  const readWire = msg => d => { const o = d.querySelector('[data-out]'), g = d.querySelector('[data-go]'); g.addEventListener('click', () => { o.textContent = msg; g.disabled = true; }); };
  D('good-critique-4b', '<div class="cr-col">' + bookApp + C('Ana', 'The time slots are tiny on a phone. Make them bigger.') + C('Kai', 'Good point, making them bigger.') + readBtn('Two weeks later') + '</div>',
    readWire('People still book for the wrong day. Kai had wondered whether “Today” was easy to miss, but the review never got there.'));
  D('good-critique-4f', '<div class="cr-col">' + bookApp + C('Ana', 'Before I start: what works for you, and what worries you?') +
    C('Kai', 'The slots work. I’m not sure people notice the date is set to today.') +
    C('Ana', 'I missed that. Agreed on the slots, and one more thing: they’re tiny on a phone.') + readBtn('Write down the next steps') + '</div>',
    readWire('Two changes, both named: make the date stand out, and make the slots bigger on phones. One came from Kai, one from Ana.'));""")
b.within('id="eff-ownership-rule-1"', '</p>', 'then make the choice yourself.',
         'then make the choice yourself. If you already lean one way, write it down first, so the agent’s confident answer doesn’t become yours, '
         'as <a href="#good-critique-rule-4">Hear their read first</a> explains.')
b.within('id="eff-decision-matrix-rule-2"', '</p>', 'Write the weights down from the brief first, then score.',
         'Write the weights down from the brief first, then score on your own before you read anyone else’s scores, an agent’s included, '
         'so <a href="#good-critique-rule-4">their read doesn’t become yours</a>.')
b.once("['Pick the criteria from the brief, then decide.', 'Draft the scores. You check every one you disagree with.']",
       "['Pick the criteria from the brief, score the directions yourself, then decide.', 'Score them separately. You look again wherever the two disagree.']")

# --- 2.3 Ch6 · heuristic review, rule 4: what each fidelity can show.
Y, N = 'Yes', 'No'
fid = table('good-heuristic-review-fidelity', 'fidelity', ['What you check', 'Sketch', 'Static mock', 'Clickable page', 'Branch in the app'], [
    ['Whether it solves the problem', Y, Y, Y, Y],
    ['Hierarchy and layout', 'Roughly', Y, Y, Y],
    ['Words and labels', 'If written', Y, Y, Y],
    ['Contrast and color', N, Y, Y, Y],
    ['States: loading, empty, error', 'Only if drawn', 'Only if drawn', 'Only if built', Y],
    ['Real data: long names, empty lists', N, 'Only if drawn', 'Sample data only', Y],
    ['Timing and motion', N, N, Y, Y],
    ['Keyboard, focus and screen readers', N, N, 'With real controls', Y],
    ['Speed with real data', N, N, N, Y]])
add_rule('good-heuristic-review', 4, 'Say what a mock can’t show',
         'A review of a static mock can only judge what’s drawn. Timing, focus, screen readers and real data don’t show, so a clean review reads as a pass '
         'for things nobody checked. List what the mock can’t show next to the findings, and check those parts in a running build. '
         'The table shows what each stage of a <a href="#eff-prototype-in-code">prototype</a> can show.',
         'The review of a mock ends with “everything else passes”. <b>Try:</b> press Ship it.',
         'The review lists what the mock can’t show. <b>Try:</b> press Check them in the build.', r"""
  /* 4. What a mock can't show */
  const mockFinds = [['Cancel is grayed out while it prepares', 3], ['“OK” doesn’t say what it does', 2], ['The only help is a tiny “?”', 2]];
  const mockHtml = fixed => '<div class="hr-col"><div class="hr-card"><span class="hr-h">Review · export dialog · static mock</span>' +
    mockFinds.map(f => '<div class="hr-li"><span class="hr-sev s' + f[1] + '">' + f[1] + '</span><span class="grow">' + f[0] + '</span></div>').join('') +
    (fixed ? '<span class="hr-h">Not checked: a mock can’t show these</span>' + ['Focus order, and Escape to close', 'How the progress moves over time', 'What an error looks like', 'What a screen reader says'].map(t => '<div class="hr-li"><span class="hr-tag">?</span><span class="grow">' + t + '</span></div>').join('')
      : '<div class="hr-li"><span class="hr-tag">✓</span><span class="grow">Everything else passes</span></div>') +
    '</div><div class="hr-acts"><button class="btn btn-primary cs-sm" type="button" data-go>' + (fixed ? 'Check them in the build' : 'Ship it') + '</button></div><p class="hr-out" data-out></p></div>';
  const mockWire = msg => d => { const o = d.querySelector('[data-out]'), g = d.querySelector('[data-go]'); g.addEventListener('click', () => { o.textContent = msg; g.disabled = true; }); };
  D('good-heuristic-review-4b', mockHtml(false), mockWire('After release: focus stays behind the dialog, and the progress never moves. Neither could show in a mock, but the review said everything else passed.'));
  D('good-heuristic-review-4f', mockHtml(true), mockWire('Two of the four fail in the build: focus stays behind the dialog, and the progress never moves. Both are fixed before release.'));""",
         extra=fid)
b.within('id="good-heuristic-review-rule-2"', '</p>', 'Past five, each new reviewer adds little.',
         'Past five, each new reviewer adds little. An agent’s review counts as another reviewer only if it looks through a different lens or runs '
         'on a different model, because one model asked twice repeats its own blind spots.')
b.once('A session shows the why, one person at a time.',
         'A session shows the why, one person at a time. An agent’s review can’t stand in for one: it predicts what people might do, and a session shows what they do.')

# --- 2.4 Ch25 · the loop, rule 5.
add_rule('eff-loop', 5, 'Frame a hunch as a question',
         'Some work starts from a hunch, with no evidence yet and a goal that’s still moving. Written as a spec, the hunch gets built as if it were known, '
         'and a whole round passes before anyone learns it was wrong. Write the brief as a question instead: what you want to find out, what you believe now '
         'and what would change your mind. Keep the rounds short, and let each Learn rewrite the brief.',
         'The hunch is written as a spec. <b>Try:</b> press Ship it.',
         'The brief is a question, with what would change your mind. <b>Try:</b> press Finish round 1.', r"""
  /* 5. A hunch as a spec vs as a question */
  const hunchHtml = fixed => '<div class="lp-card"><span class="lp-k">Brief · templates for new people</span><div class="lp-doc">' +
    (fixed ? '<b>Do new people reach a first result faster from a template than from a blank canvas?</b><span>We think: yes, for their first workflow.</span><span>We’d change our minds if: people pick a template, then delete most of it.</span>'
      : '<b>Build a template gallery for new people.</b><span>Done when: the gallery ships.</span>') + '</div>' +
    (fixed ? '<span class="lp-pill ev">Round 1 · two days, five people</span>' : '') +
    '<div class="lp-acts"><button class="btn btn-primary cs-sm" type="button" data-go>' + (fixed ? 'Finish round 1' : 'Ship it') + '</button></div><div class="lp-res" data-res></div></div>';
  const hunchWire = fixed => d => {
    const res = d.querySelector('[data-res]'), g = d.querySelector('[data-go]');
    g.addEventListener('click', () => {
      g.disabled = true;
      res.innerHTML = fixed ? '<span class="lp-good">Learn: people kept the layout, but replaced most of the nodes.</span><span>New brief: would a starter with only the layout work better? Round 2, two days.</span>'
        : '<span class="lp-bad">Two weeks later, the gallery ships. Few people open it, and nobody can say whether templates were the wrong idea or only in the wrong place.</span>';
    });
  };
  D('eff-loop-5b', hunchHtml(false), hunchWire(false));
  D('eff-loop-5f', hunchHtml(true), hunchWire(true));""")

b.save()
print('v35-2 applied')
