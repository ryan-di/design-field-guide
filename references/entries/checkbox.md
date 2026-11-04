# Checkbox

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 20 · Inputs
Live: https://ryan-di.github.io/design-field-guide/#checkbox
Kind: component
Cite as: Design Field Guide v35, #checkbox

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A checkbox marks a yes or no choice. In a group, people can check any number of boxes, from none to all, and nothing happens until they press a button such as Save or Place order.

That separates it from a [switch](https://ryan-di.github.io/design-field-guide/#switch), which acts the moment it’s flipped, and from radio buttons, which allow only one choice in a group.

## Forms

Checkboxes come in four common forms: a single box, a group, a card and a box on each row of a list. They differ in how many choices there are and which button acts on them.

- **Single.** Use it for one yes or no question, like getting emails about an order.
- **Group.** Use it when people can pick any number of options from a short list.
- **Card.** Use it for extras that need a price or a short detail, like add-ons for a flight.
- **In a list.** Use it to pick items for one action, like moving or deleting files.

## Rules

Four rules keep checkboxes useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Use radio buttons for one choice

https://ryan-di.github.io/design-field-guide/#checkbox-rule-1

Square boxes say “pick any”, so when only one option is allowed, checking a second one leaves the first checked too, and people learn the rule only when the next step shows an error. [Radio buttons](https://ryan-di.github.io/design-field-guide/#radio) say “pick one”, and choosing one clears the other by itself.

### 2. Use a switch when it applies now

https://ryan-di.github.io/design-field-guide/#checkbox-rule-2

Checkboxes usually wait for a Save or Done button, so when a change happens at once with no button, people aren’t sure it worked. Use a [switch](https://ryan-di.github.io/design-field-guide/#switch) there, with “On” next to it to confirm the change.

### 3. Make checked mean yes

https://ryan-di.github.io/design-field-guide/#checkbox-rule-3

With a label like “Don’t send me updates”, people have to leave the box empty to say yes, so people who skim see “send me updates”, check it, and get the opposite. Write the label as the thing they can choose, like “Send me updates”, so checking the box gives them what they want.

### 4. Add search and Select all to long lists

https://ryan-di.github.io/design-field-guide/#checkbox-rule-4

In a long list, people have to scroll and read every name to find the ones they want, which is slow and makes it easy to miss one. A search box cuts the list down, and Select all checks what’s left in one click. When only some are checked, Select all shows a dash.

## In real products

- Gmail: checking emails only selects them, for an action like Archive or Delete. The box at the top shows a dash when just some are checked. `checkbox-example-01`
- Lightroom Classic: the export dialog lists independent options, like resizing, sharpening and adding a watermark, as checkboxes that apply when you press Export. `checkbox-example-02`
- Google Photos: each photo has a check circle, and the one beside a date selects every photo from that day. The top bar counts what’s picked. `checkbox-example-03`

## Related entries

[radio](radio.md), [switch](switch.md)
