# Visual hierarchy

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 2 · Make the important thing obvious
Live: https://ryan-di.github.io/design-field-guide/#good-visual-hierarchy
Kind: principle
Cite as: Design Field Guide v35, #good-visual-hierarchy

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Visual hierarchy is the order in which people notice things on a screen. Size, weight, color, position and space set that order. In each region, one thing should clearly lead and the rest should step down from it.

When the order is clear, people find what matters in one glance and read the rest only if they need it. Build the same order into the markup, with real headings and lists, so people using a screen reader can move through the page the same way.

## Rules

Four rules keep visual hierarchy clear.

### 1. Let one thing lead

https://ryan-di.github.io/design-field-guide/#good-visual-hierarchy-rule-1

When everything is bold, big or bright, nothing stands out, and people have to read every line to find the one they need. Pick one focal point per region, usually the outcome or the next step, and make everything else quieter.

### 2. Don’t rely on color alone

https://ryan-di.github.io/design-field-guide/#good-visual-hierarchy-rule-2

Like any [meaning carried by color alone](https://ryan-di.github.io/design-field-guide/#good-contrast), a title set apart only by its color blends into the text around it in grayscale, in bright sun or for people who see color differently. Set the order with size, weight, position and space, and let color add to it.

### 3. Keep to three or four levels

https://ryan-di.github.io/design-field-guide/#good-visual-hierarchy-rule-3

Eight sizes and four weights, each a little different, don’t read as an order: people can’t tell which level a line is on, so the page looks uneven instead of organized. Three or four levels are enough, for example a title, key facts, body text and small print. Make each step big enough to see at a glance.

### 4. Keep one primary button

https://ryan-di.github.io/design-field-guide/#good-visual-hierarchy-rule-4

Two filled buttons side by side ask for the same attention, so people stop to work out which one is the next step, and some press the wrong one. Keep one primary action per view and make the others secondary, as in [Button hierarchy](https://ryan-di.github.io/design-field-guide/#buttons).

## In real products

Notice the one thing that leads in each, marked with a dashed outline, and how far everything else steps down from it.

- iOS Weather: the current temperature is by far the largest thing on screen. The place, the conditions and the forecast step down below it, so one glance tells you how warm it is. `good-visual-hierarchy-example-01`
- Airbnb: on a listing, the booking card has one filled button, Reserve, with the nightly price in bold above it. Dates, guests and fine print stay quieter. `good-visual-hierarchy-example-02`
- Linear: an issue’s title is the largest, darkest text on the page. Status, priority and assignee sit in a side panel in smaller, lighter text. `good-visual-hierarchy-example-03`
- Gmail: in the compose window, Send is the only filled button. Formatting, attachments and delete are small gray icons, so the next step is never in doubt. `good-visual-hierarchy-example-04`

## Related entries

[buttons](buttons.md), [good-contrast](good-contrast.md)
