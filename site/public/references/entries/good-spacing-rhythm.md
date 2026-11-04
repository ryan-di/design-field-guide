# Spacing rhythm

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 2 · Make the important thing obvious
Live: https://ryan-di.github.io/design-field-guide/#good-spacing-rhythm
Kind: principle
Cite as: Design Field Guide v35, #good-spacing-rhythm

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Spacing rhythm means every gap on a screen comes from a short scale of sizes, such as 4, 8, 16, 24 and 32 pixels, and the edges of things line up. People never measure the gaps, but they notice when gaps vary for no reason: the screen looks untidy, and it takes longer to see what belongs together.

It works together with [Proximity](https://ryan-di.github.io/design-field-guide/#good-proximity): Proximity decides which gaps should be small and which large, and rhythm decides which sizes those gaps can be. Set the steps in rem, so the gaps grow when people make their text larger.

## Rules

Three rules keep spacing steady.

### 1. Take every gap from one scale

https://ryan-di.github.io/design-field-guide/#good-spacing-rhythm-rule-1

When each gap is picked by eye, a screen ends up with many sizes that are almost the same. People can’t tell 11 from 13, so the small differences only look like mistakes. Give the team a short scale and use only its steps, so a review can ask “which step?” instead of “why 13?”.

### 2. Line edges up, or offset them clearly

https://ryan-di.github.io/design-field-guide/#good-spacing-rhythm-rule-2

Edges that sit a few pixels apart look like an error, so people see a ragged column and trust the screen a little less. Put shared edges on the same line. When something should stand apart, like a note under a price, indent it by a full step or more so it reads as a choice.

### 3. Choose density on purpose

https://ryan-di.github.io/design-field-guide/#good-spacing-rhythm-rule-3

When each panel gets its own padding, one list is cramped and the next one is roomy, so people have to adjust at every panel and the cramped rows are harder to tap. Pick a density for each kind of screen, such as compact for a busy settings page and roomy for a welcome dialog, and build both from the same steps.

## In real products

Notice the few gap sizes that repeat, and the edges that line up. Dashed lines mark the shared edges.

- Notion: every block, from headings to to-dos, starts on the same left edge. The + and the drag handle appear in the margin on hover, so the edge never moves. `good-spacing-rhythm-example-01`
- GitHub: its design system, Primer, takes every gap from a short spacing scale. Lists, cards and dialogs use the same few steps, so pages feel related. `good-spacing-rhythm-example-02`
- iOS Mail: the unread dot sits in the margin, and each divider line starts where the text starts. Every row shares one text edge. `good-spacing-rhythm-example-03`
- Pinterest: pins have different heights, but every column is the same width and every gap is the same size. The steady gutters keep a busy grid calm. `good-spacing-rhythm-example-04`

## Related entries

[good-proximity](good-proximity.md)
