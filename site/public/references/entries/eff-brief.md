# Problem brief

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 26 · Write the brief agents build from
Live: https://ryan-di.github.io/design-field-guide/#eff-brief
Kind: workflow
Cite as: Design Field Guide v35, #eff-brief

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A problem brief is a short note written before anyone builds. It says who has the problem, what should change, what’s off limits and how you’ll know it worked, so an agent can explore answers without guessing what you meant.

Where a ticket often names a fix, a brief names the problem, so better fixes can still turn up. Its neighbors do other jobs: a [context pack](https://ryan-di.github.io/design-field-guide/#eff-context-pack) holds the materials the agent works with, and a [definition of done](https://ryan-di.github.io/design-field-guide/#eff-definition-of-done) lists the checks the change must pass. Keep a brief to one page. A longer one likely covers more than one problem, so split it. Say where each part came from, and [leave what you don’t know empty](https://ryan-di.github.io/design-field-guide/#good-problem-framing-rule-5).

The brief check in the demo flags four things. Passing it doesn’t make a brief clear, but each flag is worth fixing.

Table: https://ryan-di.github.io/design-field-guide/#eff-brief-check

| Flag | Shows when | Fix |
|---|---|---|
| Missing | A field is empty: who, problem, goal, constraints, non-goals or success criteria. | Fill it in. Without [non-goals](https://ryan-di.github.io/design-field-guide/#eff-brief-rule-2), an agent may widen the scope, and without [success criteria](https://ryan-di.github.io/design-field-guide/#eff-brief-rule-3), nobody can say when it’s done. |
| Vague | A field uses a word from the [vague-word table](https://ryan-di.github.io/design-field-guide/#good-success-criteria-words), such as “better” or “intuitive”. | [Say what you’d see happen.](https://ryan-di.github.io/design-field-guide/#eff-brief-rule-4) |
| Too broad | Who is only “users”, “user”, “everyone”, “everybody”, “people”, “all users” or “anyone”. | Name the people and the moment, like “people editing in several tabs”. |
| Solution | The problem names a control: dialog, modal, popup, pop-up, button, toggle, banner, toast, checkbox or menu. | [Describe what goes wrong instead.](https://ryan-di.github.io/design-field-guide/#eff-brief-rule-1) |

## Rules

Four rules keep a brief useful.

### 1. Describe the problem, not the fix

https://ryan-di.github.io/design-field-guide/#eff-brief-rule-1

An agent builds the fix a brief names, and nothing else, so a simpler answer never comes up. [Frame the problem](https://ryan-di.github.io/design-field-guide/#good-problem-framing) instead: state the problem and the goal, and list any fix you have in mind as one option.

### 2. Say what’s out of scope

https://ryan-di.github.io/design-field-guide/#eff-brief-rule-2

An agent that sees nearby problems tends to fix them too. The change grows, you review work you didn’t ask for, and some of it may undo choices made on purpose. List the non-goals, such as the page layout or the button wording, so the change stays the size you meant.

### 3. Say how you’ll know it worked

https://ryan-di.github.io/design-field-guide/#eff-brief-rule-3

Without [success criteria](https://ryan-di.github.io/design-field-guide/#good-success-criteria), “done” means whatever the agent or the reviewer feels, so the review turns into opinions and gaps slip through. Write criteria you can check in the app, such as a time, a step count or a key that must work, and turn them into the definition of done.

### 4. Replace vague words with what you’d see

https://ryan-di.github.io/design-field-guide/#eff-brief-rule-4

Words like “better”, “cleaner” and “intuitive” mean something different to every reader, so each agent fills them in its own way, and none of the results is wrong by the brief. Replace each vague word with something you could watch happen, such as “people pay in three steps or fewer”.

## In real products

Notice that each format makes the writer state the problem and the limits before anyone builds.

- Amazon: in “working backwards”, teams write the press release and FAQ they’d publish at launch before they build. It forces a plain answer to who the customer is and what problem goes away. `eff-brief-example-01`
- Basecamp: a Shape Up pitch names the problem, the appetite (how much time it’s worth), a rough solution, rabbit holes and no-gos. The no-gos are its non-goals, set before anyone starts. `eff-brief-example-02`
- GitHub: issue templates can ask for steps to reproduce, expected and actual behavior before an issue is filed. Whoever finds the bug writes the brief, so nobody has to guess later. `eff-brief-example-03`

## Related entries

[eff-context-pack](eff-context-pack.md), [eff-definition-of-done](eff-definition-of-done.md), [good-problem-framing](good-problem-framing.md), [good-success-criteria](good-success-criteria.md)
