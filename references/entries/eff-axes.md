# Named axes

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 27 · Explore wide before you narrow
Live: https://ryan-di.github.io/design-field-guide/#eff-axes
Kind: workflow
Cite as: Design Field Guide v35, #eff-axes

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

When you ask for options, name what should change between them. An axis is one dimension with two ends, such as how loud a message is, from silent to blocking. Lay two axes out as a grid, one across and one down, and each cell becomes a direction. The options then differ in ways you chose, so each difference tells you something.

Where [Get many directions cheaply](https://ryan-di.github.io/design-field-guide/#eff-explore-wide) asks for many directions, this entry decides how they should differ.

## Rules

Four rules keep axes useful. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Name the axis and its ends

https://ryan-di.github.io/design-field-guide/#eff-axes-rule-1

“Make three versions” gives no direction, so you get the same idea three times with small changes. Name the dimension and its two ends instead, such as “how loud, from silent to blocking”, and ask for one direction per point along it.

### 2. Vary what people notice or do

https://ryan-di.github.io/design-field-guide/#eff-axes-rule-2

Color, label and corner radius are easy to vary, but people using the app barely notice them, so options that differ only there can’t teach you anything about the experience. Vary how loud it is, where it shows up and when it happens. If both ends of an axis would look the same to someone using the app, pick another axis.

### 3. Change two things at a time

https://ryan-di.github.io/design-field-guide/#eff-axes-rule-3

When every option differs in every way, a test shows a winner but not the reason. Vary two axes at a time and hold the rest fixed. Then two options that differ on only one axis, such as neighbors in the same row or column, show what that axis does.

### 4. Look at the odd cells

https://ryan-di.github.io/design-field-guide/#eff-axes-rule-4

Some cells look wrong at first, such as a blocking dialog after the fact, and it’s tempting to drop them unread. Look at each one before you drop it, because a strange corner often shows why its neighbor works.

## In real products

- Figma: a component’s variants are set by named properties, like Size and State, each with its values. The set is usually laid out as a grid, one property per direction, so a missing or odd combination is easy to spot. `eff-axes-example-01`
- Tailwind CSS: every default color is named by two axes, a hue and a shade from light to dark, like blue-500. The palette is the full grid, so choosing a color means choosing a position, and its neighbors are easy to compare. `eff-axes-example-02`
- Optimizely: a multivariate test names the parts of a page that change, like the headline and the image, with a few options each. It then tests every combination, so you can tell which part made the difference. `eff-axes-example-03`

## Related entries

[eff-explore-wide](eff-explore-wide.md)
