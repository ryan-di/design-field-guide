# Spot the plausible

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 28 · Decide with judgment, not by polish
Live: https://ryan-di.github.io/design-field-guide/#eff-spot-plausible
Kind: workflow
Cite as: Design Field Guide v35, #eff-spot-plausible

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Agent-made screens often look finished and still have problems: vague copy, a broken keyboard path, a missing state, or a color a little off the design tokens. A screenshot hides all of these, so you find them by using the screen the way people will.

In [Let agents prove their work](https://ryan-di.github.io/design-field-guide/#eff-agent-verification) the agent runs checks and shows you the results; here you use the result yourself and catch what no check covered.

## Rules

Four rules keep this check useful.

### 1. Use it, don’t just look at it

https://ryan-di.github.io/design-field-guide/#eff-spot-plausible-rule-1

A screenshot shows how a screen looks, not how it works: it can’t show that Tab skips a button, that an empty name gets saved, or that text is too faint to read. If you approve from the picture, people find these problems after release. Open the real thing: Tab through it, trigger the errors and read the copy out loud.

### 2. Look at every state

https://ryan-di.github.io/design-field-guide/#eff-spot-plausible-rule-2

Agents build the state they were shown, usually the one with data, but people also see the screen empty, loading and failing. A blank panel on a first visit looks broken, and a spinner that never stops leaves people stuck. Ask for each state and look at each one before you approve.

### 3. Check values against the tokens

https://ryan-di.github.io/design-field-guide/#eff-spot-plausible-rule-3

A padding of 15 instead of 16, or a color that’s almost the brand color, looks fine by eye. Each one is small, but the next change copies it, and the product slowly stops matching itself. Check spacing, corners and color against the design tokens. Ask the agent for token names, not raw values.

### 4. Collect problems, then send one list

https://ryan-di.github.io/design-field-guide/#eff-spot-plausible-rule-4

Sending problems to the agent one at a time takes many rounds, and a fix for one can bring back an earlier one, so you end up checking the same thing again. Collect everything you found in one list first, and send it back with the checks the agent should run, such as a Playwright test for the keyboard path and screenshots in both themes.

## In real products

- GitHub: a repository can require status checks, like tests and lint (automatic checks for code mistakes), to pass before a pull request can merge. A change that looks right in review still can’t land until they pass. `eff-spot-plausible-example-01`
- Chromatic: it highlights the pixels that changed in every Storybook story since the last accepted version, so a small shift in spacing or color can’t slip in unseen. `eff-spot-plausible-example-02`
- Lighthouse: an audit built into Chrome’s developer tools checks a page for problems a screenshot hides, like low contrast or buttons with no name. Each failed check lists the exact elements to fix. `eff-spot-plausible-example-03`
- Gmail: if a message says something is attached but nothing is, it asks before sending. The email reads as finished, and the check catches the one thing it promised but doesn’t have. `eff-spot-plausible-example-04`

## Related entries

[eff-agent-verification](eff-agent-verification.md)
