# Proximity

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 2 · Make the important thing obvious
Live: https://ryan-di.github.io/design-field-guide/#good-proximity
Kind: principle
Cite as: Design Field Guide v35, #good-proximity

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Proximity means that things close together look like they belong together. People read the space between items before they read the words, so the gaps on a screen tell them what goes with what.

Space only groups things for people who can see it, so give assistive tech the same groups: a real label for every field, and a named group around each set of fields.

## Rules

Four rules keep spacing honest. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Use more space between groups than inside them

https://ryan-di.github.io/design-field-guide/#good-proximity-rule-1

When every gap is the same, people can’t tell where one group ends and the next begins, so a caption between two photos could belong to either. Make the space between groups clearly bigger than the space inside them. About twice as much is a good start.

### 2. Try space before boxes and lines

https://ryan-di.github.io/design-field-guide/#good-proximity-rule-2

Borders and divider lines around every group give people a lot of lines to read past: the page looks busy, and the lines compete with the content. Group with space first, and add a line or a box only when space alone isn’t enough, like in a long, dense list.

### 3. Put a control next to what it changes

https://ryan-di.github.io/design-field-guide/#good-proximity-rule-3

When a setting sits at the top and the button that applies it sits far below, people don’t see that they belong together: they change the setting and nothing happens, or they hunt for the button. Keep a control next to the thing it changes, and its action next to the control.

### 4. Keep help text tight under its field

https://ryan-di.github.io/design-field-guide/#good-proximity-rule-4

A message that sits closer to the next field than to its own seems to be about the next field, so people fix the wrong thing or miss the message. Keep help and error text close under their field, with the bigger gap after them, as in [Text field](https://ryan-di.github.io/design-field-guide/#text-field).

## In real products

Notice where the bigger gaps fall: between groups, never inside them.

- iOS Settings: rows sit in rounded groups, with a clear gap between groups. Wi-Fi and Bluetooth read as one set and Notifications starts the next, with no heading needed. `good-proximity-example-01`
- Slack: messages one person sends in a row stack under a single name, with tight spacing. A new person gets a name, a picture and more space above. `good-proximity-example-02`
- Instagram: under a post, like, comment and share sit together on the left, and save sits alone on the right. The gap says save is a different kind of action. `good-proximity-example-03`
- YouTube: a video’s thumbnail, title, channel and view count sit tight together, with wider gaps between videos. The grid reads as separate cards without any borders. `good-proximity-example-04`

## Related entries

[text-field](text-field.md)
