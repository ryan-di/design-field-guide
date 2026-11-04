# Contrast

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 2 · Make the important thing obvious
Live: https://ryan-di.github.io/design-field-guide/#good-contrast
Kind: principle
Cite as: Design Field Guide v35, #good-contrast

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Contrast is how clearly text and controls stand apart from what’s behind them. With too little, people squint, miss things, or can’t read the screen at all in sunlight. WCAG asks for at least 4.5 : 1 for body text, and 3 : 1 for large text and for the edges and icons people need to see.

The second half of the idea is about meaning. Color can make a status quicker to spot, but it can’t be the only clue, because some people can’t tell certain colors apart and some screens show everything in gray. Pair every color with a shape, an icon or a word.

## Rules

Four rules keep text readable and meaning clear. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Give text enough contrast

https://ryan-di.github.io/design-field-guide/#good-contrast-rule-1

Pale gray text looks calm in a mockup on a good monitor, but on a phone in sunlight, or for someone with weaker eyes, it fades away. Give body text at least 4.5 : 1 against its background, and large text at least 3 : 1. Check the quiet text too: captions, placeholders and hints.

### 2. Don’t carry meaning with color alone

https://ryan-di.github.io/design-field-guide/#good-contrast-rule-2

A green or red amount only tells something to people who see the color. For everyone else, money in and money out look the same. Add a sign, an arrow or a word, such as “+” and “Received”, so color still helps people scan and the meaning stays when the color is gone.

### 3. Pick colors that differ in lightness

https://ryan-di.github.io/design-field-guide/#good-contrast-rule-3

Many people can’t tell red from green, especially when the two are equally light, so a seat map in those colors becomes one muddy shade. Choose colors that are also clearly lighter and darker than each other, and add a mark and a word to each state.

### 4. Check both themes

https://ryan-di.github.io/design-field-guide/#good-contrast-rule-4

A gray that passes on white can fail on dark gray. This happens when colors are picked in the light theme and copied into the dark one, which leaves dim text on a dim background. Measure every text and background pair in each theme, and give the dark theme its own values.

## In real products

Notice that every state has its own shape or word. Each sketch is shown twice, the second time without color.

- Linear: each issue status has its own icon shape, from a dashed circle for backlog to a half-filled one in progress and a check for done. Without color, the shapes still tell them apart. `good-contrast-example-01`
- GitHub: a pull request’s state is a colored label with an icon and a word: Open, Merged, Closed or Draft. Without color, the word and the icon still say it. `good-contrast-example-02`
- Slack: an active person gets a filled dot and an away person an empty ring. Filled versus hollow carries the meaning, not just green versus gray. `good-contrast-example-03`
- Duolingo: after you check an answer, the panel turns green with a check and praise, or red with a cross and the right answer written out. The icon, the words and a sound carry the meaning too, so color is never alone. `good-contrast-example-04`
