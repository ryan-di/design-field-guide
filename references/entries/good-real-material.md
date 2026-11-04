# Real material

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 7 · Train your eye, design in the real material
Live: https://ryan-di.github.io/design-field-guide/#good-real-material
Kind: principle
Cite as: Design Field Guide v35, #good-real-material

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Prototyping in the real material means building the risky parts of a design in code, early. A mockup shows one still moment with tidy text, while code shows what happens when the message is long, the response is slow or the window is narrow. It also lets you test what a picture can’t: keyboard use, focus, screen readers and reduced motion.

A prototype is not the feature. It answers one question, like “Can people read the toast before it goes?”, and then it’s thrown away. Keep mockups for what they answer faster, such as layout ideas and wording.

## Rules

Four rules keep prototypes useful. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Try the risky part in code early

https://ryan-di.github.io/design-field-guide/#good-real-material-rule-1

A mockup uses short names and answers at once. The real build gets long names and slow responses, and nobody sees that until weeks later, when the design is signed off and changing it costs more. Build the risky part in code first, with real data and real timing, so problems show up while the design can still change.

### 2. Mark throwaway code as throwaway

https://ryan-di.github.io/design-field-guide/#good-real-material-rule-2

Prototype code is written fast, with fake delays, hard-coded colors and no tests. If nobody says so, it gets merged and ships, and months later someone has to work out which parts were real. Say it’s a prototype in the branch name and at the top of the file, then rebuild the idea properly.

### 3. Decide what “good” means before you tune

https://ryan-di.github.io/design-field-guide/#good-real-material-rule-3

Tuning without a goal never ends: each value looks a little off, so you keep nudging it and stop when you’re tired rather than when it works. [Write down what has to be true](https://ryan-di.github.io/design-field-guide/#good-success-criteria) first, like “people can read the caption before the slide changes”, then tune until it passes and stop.

### 4. Try the messy cases on purpose

https://ryan-di.github.io/design-field-guide/#good-real-material-rule-4

On your own laptop, with tidy sample data, everything looks fine, and people find the [messy cases](https://ryan-di.github.io/design-field-guide/#good-edge-cases) for you after launch: long names, empty lists, slow connections and small screens. Go through each one before you ship, and design what people see in it.

## In real products

- Storybook: each state of a component is a story you can open on its own, like Long text or Error, and the Controls panel changes its data live. `good-real-material-example-01`
- Xcode: SwiftUI previews render the view next to its code and update as you type. Variants show it at several text sizes or orientations side by side. `good-real-material-example-02`
- Chrome DevTools: slow the network, narrow the viewport and turn on reduced motion, so a prototype meets slow responses and small screens before people do. `good-real-material-example-03`
- CodePen: code and result sit together and update as you type, so you can tune an animation’s timing by feel, then share a link others can fork. `good-real-material-example-04`

## Related entries

[good-edge-cases](good-edge-cases.md), [good-success-criteria](good-success-criteria.md)
