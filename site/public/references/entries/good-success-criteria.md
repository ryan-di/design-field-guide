# Success criteria

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 1 · Get the problem right first
Live: https://ryan-di.github.io/design-field-guide/#good-success-criteria
Kind: principle
Cite as: Design Field Guide v35, #good-success-criteria

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Success criteria say what you would see or count if a change worked. Where the [problem frame](https://ryan-di.github.io/design-field-guide/#good-problem-framing) says what to solve, they say what “done” looks like.

Good criteria describe what people do, not how the design feels. “People find Export without help” can be checked, but “Export is more intuitive” can’t. Include the other ways people work too, for example “people using only a keyboard can finish checkout”.

## Rules

Four rules keep success criteria useful.

### 1. Count people who got it done

https://ryan-di.github.io/design-field-guide/#good-success-criteria-rule-1

Views, clicks and time on page can all go up when a design gets worse, because a confusing page makes people click around and stay longer. Count what people came to do instead: how many finished the task, how long it took and how many errors they hit.

### 2. Watch people, not only numbers

https://ryan-di.github.io/design-field-guide/#good-success-criteria-rule-2

A number tells you that something changed, not why: a drop in sign-ups could come from any field on the form. Watch a few people use it. Five short sessions often show the exact place where people stop, which no dashboard will.

### 3. Write them down before you build

https://ryan-di.github.io/design-field-guide/#good-success-criteria-rule-3

Without criteria, a change is done when it ships: nobody can say whether it helped, and the review only checks that it looks fine. Write the criteria in the ticket or the brief before work starts, so the review can test the change against them.

### 4. Turn feelings into things you can see

https://ryan-di.github.io/design-field-guide/#good-success-criteria-rule-4

Words like easier, cleaner and more intuitive sound like goals, but nobody can check them, so after a test people argue about whether it felt easier. Turn each feeling into something you can watch: found without help, finished on the first try, fewer questions to support.

The demo at the top of this entry marks these words, and the [brief check](https://ryan-di.github.io/design-field-guide/#eff-brief-check) in Part 4 flags the same ones. Fill the slots with your own task and numbers.

Table: https://ryan-di.github.io/design-field-guide/#good-success-criteria-words

| Vague word | Write instead, for example |
|---|---|
| easy, easier, simple, simpler, intuitive, user-friendly | People find *X* without help, in under *N* clicks. |
| good, better, improve, improved, improves, improvement, nice, nicer | Fewer support questions about *Y*, or fewer retries when people do it. |
| clean, cleaner, clearer, modern | People spot the main action in a five-second look at *X*. |
| seamless, smooth, smoother | Nobody gets stuck or asks for help between *X* and *Y*. |
| somehow, etc | List what you mean: *X*, *Y* and *Z*. |

## In real products

- GitHub: a repo can require named checks to pass before a pull request can merge, and every change is held to them. `good-success-criteria-example-01`
- YouTube Studio: next to views, it shows how long people watched and where they dropped off. Views can climb while most people leave in the first seconds. `good-success-criteria-example-02`
- Apple Watch: each Activity ring is a daily goal you can count, like minutes of exercise. One glance shows how close you are, with nothing left to judge by feel. `good-success-criteria-example-03`

## Related entries

[good-problem-framing](good-problem-framing.md)
