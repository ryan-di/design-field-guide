# Segmented control

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 20 · Inputs
Live: https://ryan-di.github.io/design-field-guide/#segmented
Kind: component
Cite as: Design Field Guide v35, #segmented

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A segmented control is a row of two to five buttons joined into one. Exactly one segment is on, and picking another changes the view or mode right away, with no Save button.

That is what separates it from [tabs](https://ryan-di.github.io/design-field-guide/#tabs), which move between different content, like Overview and Reviews. A segmented control shows the same content in another way, like a day, a week or a month of the same calendar.

## Forms

Most segmented controls use short text labels, and well-known views can use icons instead. On a phone, the control often spans the full width under the page title. With exactly two options, it works like a switch that names both sides.

- **Text.** Use it for two to five views of the same thing, like Years, Months and All in a photo library. Keep each label to one short word so the row fits on one line.
- **Icons.** Use it when the icons are well known, like list and grid. Give each segment a name that shows on hover and is read out by screen readers.
- **Full width.** Use it on a phone, where a row of small segments is hard to tap. The segments share the width equally, so each one is a big target.
- **Two options.** Use it for a pair of choices, like monthly and yearly billing. People can read both, so they know what they’ll get before they switch.

## Rules

Three rules keep segmented controls useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Keep it to a few short labels

https://ryan-di.github.io/design-field-guide/#segmented-rule-1

Long labels or more than five options don’t fit on one line, so the control wraps into a block of buttons that is hard to scan and no longer looks like one switch. Use tabs for views like these, because they stay on one line and scroll sideways. For a value rather than a view, use a [select](https://ryan-di.github.io/design-field-guide/#combobox).

### 2. Use it only for changes that apply at once

https://ryan-di.github.io/design-field-guide/#segmented-rule-2

People expect a segmented control to take effect the moment they click it, so if the choice waits for a Save button, they leave and the change is lost. When a choice needs saving, use a [radio group](https://ryan-di.github.io/design-field-guide/#radio), which reads as part of a form.

### 3. Make the selected segment stand out

https://ryan-di.github.io/design-field-guide/#segmented-rule-3

The selected segment is the only thing that tells people what they’re looking at. With a faint tint, they can’t tell if the chart shows a day, a week or a month, and on a dim screen or in bright light the tint disappears. Give the selected segment a solid fill and bold text, so it reads at a glance.

## In real products

- macOS Calendar: four short segments switch the same events between day, week, month and year. `segmented-example-01`
- Blender: four small buttons in the viewport header switch how the same scene is drawn, from wireframe to fully rendered. They change only the view, never the model. `segmented-example-02`
- Google Maps: the travel modes at the top of directions switch the same trip between driving, transit, walking and cycling. Each shows its time, so people can compare before they pick. `segmented-example-03`
- Google Calendar: with six views to choose from, the view switch is a dropdown in the header instead of a long row of segments. `segmented-example-04`

## Related entries

[combobox](combobox.md), [radio](radio.md), [tabs](tabs.md)
