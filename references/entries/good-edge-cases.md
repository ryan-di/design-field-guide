# Edge cases

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 5 · Sweat the states and the edges
Live: https://ryan-di.github.io/design-field-guide/#good-edge-cases
Kind: principle
Cite as: Design Field Guide v35, #good-edge-cases

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Real data is long, missing, huge and empty. Names run past the edge, images fail to load, counts reach the millions, and fields come back blank. A design made only with tidy sample data breaks on the first day of real use, and people see those cases every day after that.

For every field, decide what happens when it is very long, missing, very large, empty, or squeezed into a narrow space. [Checking more than the happy path](https://ryan-di.github.io/design-field-guide/#good-needs-hierarchy) covers slow, empty and failed loads. This entry is about the data itself.

## Rules

Four rules keep a design working with real data. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Test with the extremes from the start

https://ryan-di.github.io/design-field-guide/#good-edge-cases-rule-1

A mockup filled with a short name, a perfect image and a tidy number always looks finished, so the problems show up only after launch, when real people bring real data. Put the extremes in the mockups, the stories and the test data from the start, so they get designed instead of discovered.

### 2. Keep the part that tells items apart

https://ryan-di.github.io/design-field-guide/#good-edge-cases-rule-2

When long names are cut at the end, items that differ only at the end look the same: three files all read “Quarterly report dra…”, and people pick the wrong one. Cut the middle to keep the end, or let the text wrap to two lines. Keep the full text in the page so screen readers read it, and show it on hover and on focus.

### 3. Reserve space for what loads later

https://ryan-di.github.io/design-field-guide/#good-edge-cases-rule-3

When something loads late, it pushes everything below it down, and a click aimed at a button lands on the wrong thing. Reserve the space before the content arrives: give images a fixed aspect ratio, and make [skeletons](https://ryan-di.github.io/design-field-guide/#skeleton) the same size as the content they stand in for.

### 4. Format values for people

https://ryan-di.github.io/design-field-guide/#good-edge-cases-rule-4

Raw values like “1234567”, “null” and “undefined” show that nobody planned for this case: a long number is hard to read at a glance, and “null” looks like a bug. Format numbers and dates for reading, like “1.2M followers”, with the exact value one step away, and write a fallback for every field that can be empty.

## In real products

- VS Code: when two open tabs have the same file name, each tab adds the part of its path that tells them apart, in lighter text. Tabs with unique names stay short. `good-edge-cases-example-01`
- macOS Finder: long file names are cut in the middle, not at the end. The start and the ending both stay visible, so “final v2.pdf” and “final v3.pdf” still look different. `good-edge-cases-example-02`
- YouTube: big view counts are rounded, like “1.2M views”, and dates are relative, like “3 years ago”. Long titles wrap to two lines before they’re cut. The exact count and date show when you open the description. `good-edge-cases-example-03`
- Airbnb: a listing without enough reviews shows “New” where the star rating goes. There’s no zero-star rating and no empty gap. `good-edge-cases-example-04`

## Related entries

[good-needs-hierarchy](good-needs-hierarchy.md), [skeleton](skeleton.md)
