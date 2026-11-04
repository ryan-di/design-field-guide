# Definition of done

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 26 · Write the brief agents build from
Live: https://ryan-di.github.io/design-field-guide/#eff-definition-of-done
Kind: workflow
Cite as: Design Field Guide v35, #eff-definition-of-done

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A definition of done is the list of checks a change must pass before you call it finished. Write each one as something you could see or run, such as a behavior, a state or a test that passes, and mark who checks it. An agent can prove many of them with a test run or a screenshot, but some need your judgment, such as whether the wording reads well.

Where [Define “good” before building](https://ryan-di.github.io/design-field-guide/#good-success-criteria) decides what a good result is, this entry turns it into checks for one change, so you and the agent agree on when it’s finished.

## Rules

Four rules keep a definition of done useful. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Ask for proof, not a report

https://ryan-di.github.io/design-field-guide/#eff-definition-of-done-rule-1

An agent says a change is done when it believes it is, and that message doesn’t tell you whether any check passed. If you approve on its word, the bugs reach people first. Ask for the test run and the screenshots in the pull request, and look at them before you approve.

### 2. Name what you’d see

https://ryan-di.github.io/design-field-guide/#eff-definition-of-done-rule-2

“It feels intuitive” can’t pass or fail, so it gets marked done without a check. Write what you’d see instead, as in [the problem brief](https://ryan-di.github.io/design-field-guide/#eff-brief), such as which result shows first. Keep the calls that need judgment, labeled as yours, and look yourself: a screenshot proves a state exists, not that it reads well.

### 3. Cover the other states

https://ryan-di.github.io/design-field-guide/#eff-definition-of-done-rule-3

Criteria often describe only the path where everything works, so nobody checks what happens when a save fails or several tabs are unsaved, which is where people lose work. List the other states too: several unsaved tabs, a failed save, keyboard only, a narrow window.

### 4. Put the tests in the brief

https://ryan-di.github.io/design-field-guide/#eff-definition-of-done-rule-4

Tests planned for later rarely get written, so the next change can break this one without anyone noticing, and people find out first. Name the tests in the brief, such as a Playwright spec (a test that clicks through the app in a real browser) for the new behavior, so they ship in the same pull request.

## In real products

- GitHub: branch protection can require passing status checks and an approving review before a pull request merges. Machines prove the tests pass; a person approves the change itself. `eff-definition-of-done-example-01`
- Chromatic: visual tests compare each Storybook story with its last accepted screenshot. The tool finds what changed, and a person accepts or denies it, because only they know if the change was meant. `eff-definition-of-done-example-02`
- DoorDash: when an order is left at the door, the courier takes a photo at drop-off and the app shows it to you. “Delivered” comes with proof you can check, not just a status. `eff-definition-of-done-example-03`

## Related entries

[eff-brief](eff-brief.md), [good-success-criteria](good-success-criteria.md)
