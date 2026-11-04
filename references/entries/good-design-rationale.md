# Design rationale

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 7 · Train your eye, design in the real material
Live: https://ryan-di.github.io/design-field-guide/#good-design-rationale
Kind: principle
Cite as: Design Field Guide v35, #good-design-rationale

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Design rationale is the reasoning behind a design decision, written down. It says what the problem was, which options you considered, which one you chose and why. The next person reads it before they change the design. Without it, they guess, and may undo a choice that was made for a good reason.

Rationale is not a description of how the design works, which the design itself shows. It records why it works that way, including the options you turned down. Record accessibility decisions too, like the keyboard path, because they are the first thing lost in a later rewrite.

## Rules

Four rules keep design rationale useful.

### 1. Keep it where people will look

https://ryan-di.github.io/design-field-guide/#good-design-rationale-rule-1

Decisions are often made in a chat thread or on a call, and a month later nobody can find them, so a new teammate has to ask again or guess. Put the decision in the pull request description or a short doc, and link it from the issue so it’s one click from the question.

### 2. Include what you rejected

https://ryan-di.github.io/design-field-guide/#good-design-rationale-rule-2

A record that only names the winner answers “what”, not “why not”, so the next person suggests an option you already tried and the team argues it again. List each option you turned down, with one line on why, and the second discussion ends before it starts.

### 3. Write it while you decide

https://ryan-di.github.io/design-field-guide/#good-design-rationale-rule-3

Written weeks later, a record comes from memory. The reasons have faded, so it says “it seemed best”, which helps nobody. Write it while you’re still choosing, because spelling out each option’s trade-off often turns up a better option you hadn’t seen.

### 4. Lead with what changes for people

https://ryan-di.github.io/design-field-guide/#good-design-rationale-rule-4

Reviewers read the top of a pull request description and skim the rest. If it opens with refactors and file names, they can’t tell what people will notice, and the change people will feel gets the least review. Start with what changes for people, then why, then how it’s built.

## In real products

- Material Design: guidelines pair a “Do” with a “Don’t” and a line on why, so the rejected option sits on the page next to the chosen one. `good-design-rationale-example-01`
- GOV.UK Design System: component pages say when not to use them and what research found, so teams see why a component works the way it does before they change it. `good-design-rationale-example-02`
- Python: a proposal to change the language, called a PEP, has a Rejected Ideas section that lists the alternatives raised and why each was turned down. `good-design-rationale-example-03`
- Wikipedia: every article has a talk page that keeps the discussion behind its wording, so a new editor can see what was already proposed and why it was turned down. `good-design-rationale-example-04`
