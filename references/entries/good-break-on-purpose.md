# Break it on purpose

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 3 · Same thing, same look, same place
Live: https://ryan-di.github.io/design-field-guide/#good-break-on-purpose
Kind: principle
Cite as: Design Field Guide v35, #good-break-on-purpose

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Consistency doesn’t mean everything looks the same. When one thing really is different, such as an action that destroys work, it should look different, and it should be the only thing that does. People notice the one element that breaks a pattern, but only while the pattern holds everywhere else.

This is the other half of [Internal and external consistency](https://ryan-di.github.io/design-field-guide/#good-consistency). Like any [meaning carried by color](https://ryan-di.github.io/design-field-guide/#good-contrast), an exception needs a second cue: an icon, a divider, a place at the end of the list, or the word itself, like “Delete”.

## Rules

Three rules keep exceptions meaningful. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Keep exceptions rare

https://ryan-di.github.io/design-field-guide/#good-break-on-purpose-rule-1

When every action gets its own color, weight or badge, nothing stands out, and people have to read every item to find the one they need, as on a [screen where everything is bold](https://ryan-di.github.io/design-field-guide/#good-visual-hierarchy). Keep about one exception per screen, for the one thing that really differs, and give everything else the normal style.

### 2. Write down the reason

https://ryan-di.github.io/design-field-guide/#good-break-on-purpose-rule-2

An exception without a reason looks like any other style choice, so the next person copies it to places where it doesn’t belong, and soon it means nothing. Write the reason next to the rule, like “red only for actions that destroy data”. If you can’t write a reason, follow the rule.

### 3. Audit for drift

https://ryan-di.github.io/design-field-guide/#good-break-on-purpose-rule-3

Not every difference is a choice: someone copies an old screen or picks a value that’s close enough, and small variants pile up release after release. Check the product now and then. Fold drift back into the system, and if a variant has a real job, give it a name and add it.

## In real products

- GitHub: a repository’s settings page stays plain until the bottom. The few actions that are hard to undo, like Archive and Delete, sit together in a red-bordered “Danger Zone” with its own heading. `good-break-on-purpose-example-01`
- Gmail: Compose is the only big filled button in the sidebar. Inbox, Starred, Sent and the rest are plain rows, so the one way to start something new is easy to find. `good-break-on-purpose-example-02`
- Spotify: a playlist page has one big round Play button. Save, download and more options are small plain icons next to it, because playing is what most people came for. `good-break-on-purpose-example-03`
- iOS: in a photo’s long-press menu, every item is plain except Delete. It’s red, has a trash icon and comes last, so it stands apart even without the color. `good-break-on-purpose-example-04`

## Related entries

[good-consistency](good-consistency.md), [good-contrast](good-contrast.md), [good-visual-hierarchy](good-visual-hierarchy.md)
