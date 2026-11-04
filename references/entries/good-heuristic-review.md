# Heuristic review

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 6 · Judge work against its goal
Live: https://ryan-di.github.io/design-field-guide/#good-heuristic-review
Kind: principle
Cite as: Design Field Guide v35, #good-heuristic-review

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A heuristic review checks a design against a short list of rules of thumb. The best-known list is Jakob Nielsen’s ten usability heuristics. One person can run it in an hour, before anyone outside the team sees the design.

It finds likely problems, not proven ones, which separates it from a usability test, where you watch real people use the design. The ten heuristics also leave out accessibility, so add a separate pass for keyboard, focus, contrast and screen readers.

The dialog in the demo breaks six of the ten. Here are all ten, each with a question to ask and the entries that cover it.

Table: https://ryan-di.github.io/design-field-guide/#good-heuristic-review-ten

| Heuristic | Ask | In this book |
|---|---|---|
| 1 · Visibility of system status | Does the screen always show what’s happening, and how long it will take? | [Instant feedback](https://ryan-di.github.io/design-field-guide/#pat-instant-feedback), [Progress bar](https://ryan-di.github.io/design-field-guide/#progress-bar) |
| 2 · Match between the system and the real world | Does it use the words people use, in the order they think of things? | [Labels in people’s words](https://ryan-di.github.io/design-field-guide/#pat-information-scent), [Plain words, one term per concept](https://ryan-di.github.io/design-field-guide/#good-plain-language) |
| 3 · User control and freedom | Can people back out of every step, even halfway through? | [Undo instead of “Are you sure?”](https://ryan-di.github.io/design-field-guide/#pat-undo), [Dialog](https://ryan-di.github.io/design-field-guide/#dialog) |
| 4 · Consistency and standards | Does the same thing look and work the same here and in the apps people already use? | [Internal and external consistency](https://ryan-di.github.io/design-field-guide/#good-consistency), [Jakob’s law](https://ryan-di.github.io/design-field-guide/#pat-jakobs-law) |
| 5 · Error prevention | Does the design stop the mistake before it happens? | [Constraints that prevent errors](https://ryan-di.github.io/design-field-guide/#pat-constraints), [Forgiving input](https://ryan-di.github.io/design-field-guide/#pat-forgiving-input) |
| 6 · Recognition rather than recall | Can people see their options instead of remembering them? | [Labels that say what happens](https://ryan-di.github.io/design-field-guide/#good-labels), [Search with filters and recents](https://ryan-di.github.io/design-field-guide/#pat-search-filters), [Command palette](https://ryan-di.github.io/design-field-guide/#pat-command-palette) |
| 7 · Flexibility and efficiency of use | Do frequent users get faster paths that newcomers never have to learn? | [Keyboard shortcuts and accelerators](https://ryan-di.github.io/design-field-guide/#pat-shortcuts), [Layered interface](https://ryan-di.github.io/design-field-guide/#pat-layered-ui) |
| 8 · Aesthetic and minimalist design | Does anything on the screen compete with what matters? | [Visual hierarchy](https://ryan-di.github.io/design-field-guide/#good-visual-hierarchy), [Rams’ ten principles](https://ryan-di.github.io/design-field-guide/#good-rams-principles) |
| 9 · Help users recognize, diagnose, and recover from errors | Does each error say what went wrong and what to do next, in plain words? | [Error messages that help](https://ryan-di.github.io/design-field-guide/#good-error-copy), [Error state](https://ryan-di.github.io/design-field-guide/#error-state) |
| 10 · Help and documentation | Is the help right where the question comes up? | [Contextual hints over tours](https://ryan-di.github.io/design-field-guide/#pat-contextual-hints) |

Then make the accessibility pass. A mock shows only some of it, so most of these checks need a running build.

Table: https://ryan-di.github.io/design-field-guide/#good-heuristic-review-a11y

| Check | Passes when | Shows in a mock? | In this book |
|---|---|---|---|
| Keyboard | You can finish the whole task with the keyboard alone, in reading order. | No, it needs a running build | [Keyboard paths are craft](https://ryan-di.github.io/design-field-guide/#good-keyboard-focus) |
| Focus | Focus is always visible, moves into a dialog when it opens and back when it closes. | No | [Move focus with what opens and closes](https://ryan-di.github.io/design-field-guide/#good-keyboard-focus-rule-4) |
| Contrast | Body text is at least 4.5 : 1 against its background; large text, edges and icons people need are at least 3 : 1. | Yes | [Contrast, and never color alone](https://ryan-di.github.io/design-field-guide/#good-contrast) |
| Color | No meaning is carried by color alone. | Yes | [Don’t carry meaning with color alone](https://ryan-di.github.io/design-field-guide/#good-contrast-rule-2) |
| Names | Every control says what it does, and is a real button or link that a screen reader can name. | Partly: the words show, the roles only in code | [Labels that say what happens](https://ryan-di.github.io/design-field-guide/#good-labels), [Use real buttons and links](https://ryan-di.github.io/design-field-guide/#good-keyboard-focus-rule-3) |
| Announcements | Errors, toasts and finished work appear in text that screen readers announce. | No | [Instant feedback](https://ryan-di.github.io/design-field-guide/#pat-instant-feedback) |
| Motion | With reduce motion on, slides and zooms become an instant change or a short fade. | No | [Respect reduced motion](https://ryan-di.github.io/design-field-guide/#good-motion-rule-3) |

## Rules

Four rules keep a heuristic review useful.

### 1. Pair it with watching people

https://ryan-di.github.io/design-field-guide/#good-heuristic-review-rule-1

A review finds what reviewers expect to go wrong, but real people trip over things no list predicts and breeze past some problems the review rated high. If the review is the only test, the team fixes guesses. [Watch a few people](https://ryan-di.github.io/design-field-guide/#good-success-criteria) try the same flow, and let what they do decide which findings matter.

### 2. Ask three to five reviewers

https://ryan-di.github.io/design-field-guide/#good-heuristic-review-rule-2

One reviewer finds only part of the problems, because each person notices different things. Ask three to five people to review on their own, then merge the lists. Past five, each new reviewer adds little. An agent’s review counts as another reviewer only if it looks through a different lens or runs on a different model, because one model asked twice repeats its own blind spots.

### 3. Rate each problem by severity

https://ryan-di.github.io/design-field-guide/#good-heuristic-review-rule-3

A flat list of problems gives the team no order, so they fix the quick ones first and the problem that stops people from paying waits. Rate each problem from 0 to 4 and fix from the top. The rating weighs how many people hit the problem, how much it hurts and whether it gets in their way every time.

Table: https://ryan-di.github.io/design-field-guide/#good-heuristic-review-severity

| Severity | Means | Example |
|---|---|---|
| 0 · Not a problem | Not a usability problem after all. Drop it and write down why. | “I’d make it blue”, with no problem behind it |
| 1 · Cosmetic | Fix it if there’s time left. | A typo: “Delivey fee” |
| 2 · Minor | Low priority: people notice it but get past it. | Prices are low contrast |
| 3 · Major | High priority: people struggle or lose work. | The basket empties when you switch restaurant |
| 4 · Catastrophe | Fix it before release: people can’t finish the task. | Card payment fails if the address has an accent |

### 4. Say what a mock can’t show

https://ryan-di.github.io/design-field-guide/#good-heuristic-review-rule-4

A review of a static mock can only judge what’s drawn. Timing, focus, screen readers and real data don’t show, so a clean review reads as a pass for things nobody checked. List what the mock can’t show next to the findings, and check those parts in a running build. The table shows what each stage of a [prototype](https://ryan-di.github.io/design-field-guide/#eff-prototype-in-code) can show.

Table: https://ryan-di.github.io/design-field-guide/#good-heuristic-review-fidelity

| What you check | Sketch | Static mock | Clickable page | Branch in the app |
|---|---|---|---|---|
| Whether it solves the problem | Yes | Yes | Yes | Yes |
| Hierarchy and layout | Roughly | Yes | Yes | Yes |
| Words and labels | If written | Yes | Yes | Yes |
| Contrast and color | No | Yes | Yes | Yes |
| States: loading, empty, error | Only if drawn | Only if drawn | Only if built | Yes |
| Real data: long names, empty lists | No | Only if drawn | Sample data only | Yes |
| Timing and motion | No | No | Yes | Yes |
| Keyboard, focus and screen readers | No | No | With real controls | Yes |
| Speed with real data | No | No | No | Yes |

## In real products

Each one gets a different heuristic right. Naming the heuristic when you see it done well makes it easier to spot when it’s missing.

- Uber: after you book, the map shows the car moving toward you and the arrival time keeps updating, so you never wonder whether anything is happening. Heuristic 1, visibility of system status. `good-heuristic-review-example-01`
- Gmail: if a message mentions an attachment but has no file, Gmail asks before sending. It catches the slip at the last moment it can still be fixed. Heuristic 5, error prevention. `good-heuristic-review-example-02`
- macOS: menus list every command by name with its shortcut beside it. People find a command by looking instead of remembering, and pick up the faster key along the way. Heuristics 6 and 7. `good-heuristic-review-example-03`
- Google Search: a misspelled query gets results for the likely spelling, with a link to search for exactly what you typed. Heuristic 9, help users recognize, diagnose and recover from errors. `good-heuristic-review-example-04`

## Related entries

[dialog](dialog.md), [eff-prototype-in-code](eff-prototype-in-code.md), [error-state](error-state.md), [good-consistency](good-consistency.md), [good-contrast](good-contrast.md), [good-error-copy](good-error-copy.md), [good-keyboard-focus](good-keyboard-focus.md), [good-labels](good-labels.md), [good-plain-language](good-plain-language.md), [good-rams-principles](good-rams-principles.md), [good-success-criteria](good-success-criteria.md), [good-visual-hierarchy](good-visual-hierarchy.md), [pat-command-palette](pat-command-palette.md), [pat-constraints](pat-constraints.md), [pat-contextual-hints](pat-contextual-hints.md), [pat-forgiving-input](pat-forgiving-input.md), [pat-information-scent](pat-information-scent.md), [pat-instant-feedback](pat-instant-feedback.md), [pat-jakobs-law](pat-jakobs-law.md), [pat-layered-ui](pat-layered-ui.md), [pat-search-filters](pat-search-filters.md), [pat-shortcuts](pat-shortcuts.md), [pat-undo](pat-undo.md), [progress-bar](progress-bar.md)
