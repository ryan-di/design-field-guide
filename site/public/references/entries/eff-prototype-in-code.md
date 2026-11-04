# Prototype in code

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 27 · Explore wide before you narrow
Live: https://ryan-di.github.io/design-field-guide/#eff-prototype-in-code
Kind: workflow
Cite as: Design Field Guide v35, #eff-prototype-in-code

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A prototype answers a question about a design. Build it in code, at the fidelity the question needs and no higher. A clickable artifact page answers questions about feel and timing, and a branch in the app answers questions about real storage, real data and real speed.

Code also lets you try the prototype with a keyboard and a screen reader, which a static mock can’t. Do that before you pick a direction, not after it ships.

## Rules

Four rules keep prototypes useful.

### 1. Make timing questions clickable

https://ryan-di.github.io/design-field-guide/#eff-prototype-in-code-rule-1

Some questions are about time: is a toast up long enough, does a reply feel slow. A static mock can show a toast, but not how long it stays. Make a clickable page with a real timer and real keyboard behavior, and try it yourself.

### 2. Sketch before you branch

https://ryan-di.github.io/design-field-guide/#eff-prototype-in-code-rule-2

A branch in the app takes days and is slow to throw away, so if you build one per direction just to compare them, most of that work goes in the bin. Compare directions as sketches first, and build in the app once the question is about the real thing.

### 3. Write the question at the top

https://ryan-di.github.io/design-field-guide/#eff-prototype-in-code-rule-3

A prototype without a question has no point where it’s finished, so it keeps growing and nobody can say what it showed. Write the question at the top of the prototype, add only what helps answer it, and stop when it’s answered.

### 4. Decide what happens to the branch

https://ryan-di.github.io/design-field-guide/#eff-prototype-in-code-rule-4

A prototype branch is built to answer a question fast, so it skips tests and takes shortcuts. If it ships as it is, those shortcuts reach people. Decide on purpose: rewrite it with tests, or keep it only after it passes the same review as any other change.

## In real products

Notice how far each one goes: one page, one component, a real branch, real people.

- CodePen: a pen is one page of HTML, CSS and JavaScript with the result running underneath. It’s enough for a question about feel, like how long a toast should stay, without touching the real app. `eff-prototype-in-code-example-01`
- Storybook: each story renders one real component in one state, outside the app. You can check the error and long-text states in real code, and change props live, before any screen uses it. `eff-prototype-in-code-example-02`
- Vercel: every pull request gets its own live preview link. Reviewers click through the real branch in a browser instead of judging screenshots. `eff-prototype-in-code-example-03`
- Instagram: it tested hiding like counts with real accounts in several countries before deciding, because how people would feel about it could only be learned from real use, not from a mock. It later became a setting people can turn on. `eff-prototype-in-code-example-04`
