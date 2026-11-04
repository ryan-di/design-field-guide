# Popover

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 18 · Overlays
Live: https://ryan-di.github.io/design-field-guide/#popover
Kind: component
Cite as: Design Field Guide v35, #popover

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A popover is a small box that opens next to the button people pressed. It holds a few related controls or details, such as view options, a guest count or a contact card. It stays open until people click outside it, press Esc or press the button again.

Unlike a [tooltip](https://ryan-di.github.io/design-field-guide/#tooltip), it opens on a click and can hold buttons, fields and links. Unlike a dialog, it doesn’t block the page behind it.

## Forms

The common forms are options, a picker, a details card and a tip. Options and pickers change something on the page, a details card shows more about a person or a link, and a tip points at something new once.

- **Options.** Use it for a few settings that change the view, like size or filters.
- **Picker.** Use it to set one value, like dates or the number of guests.
- **Details.** Use it to show more about a person, a place or a link without leaving the page.
- **Tip.** Use it once, to point out something new right where it is.

## Rules

Four rules keep popovers useful.

### 1. Keep it to a few controls

https://ryan-di.github.io/design-field-guide/#popover-rule-1

A popover has room for only a few controls, so with seven fields in it, people scroll inside the box to find a field, then scroll again to find Save. When a task needs more fields than that, use a side panel or a page, where the fields can be grouped and Save stays in view.

### 2. Don’t lose work when it closes

https://ryan-di.github.io/design-field-guide/#popover-rule-2

People close popovers by clicking outside them, often without thinking, so if that also throws away what they typed, their work is gone without a word. Save each change the moment it’s made, so nothing is lost however the popover closes. If people need to review changes before they count, use a dialog with Save and Cancel instead.

### 3. Don’t open popovers from popovers

https://ryan-di.github.io/design-field-guide/#popover-rule-3

Each popover that opens another adds a layer on top, so people lose track of where they are, and one choice can close every layer at once. The next change then starts again from the first button. Put related choices side by side in one popover or panel, and apply them as people click.

### 4. Keep the result in view

https://ryan-di.github.io/design-field-guide/#popover-rule-4

When a popover covers what it changes, people adjust blind: they close it to see the result, then open it again to adjust some more. Place it beside the thing being changed, or, if there isn’t room, use a side panel and leave the thing itself in full view.

## In real products

- Figma: clicking a fill swatch opens a small color picker beside the properties panel. The selected shape updates as you drag, and clicking away just closes the picker. `popover-example-01`
- Google Docs: putting the cursor in a link shows a small card under it, with the address and buttons to copy, edit or remove the link. The page around it doesn’t change. `popover-example-02`
- Airbnb: the guests field opens a small panel of plus and minus steppers. Each change shows up in the search bar right away, so there’s nothing to confirm before closing it. `popover-example-03`
- YouTube: in the player’s settings panel, picking playback speed swaps the list for the speeds, with a back arrow, instead of stacking a second layer. The new speed applies at once. `popover-example-04`

## Related entries

[tooltip](tooltip.md)
