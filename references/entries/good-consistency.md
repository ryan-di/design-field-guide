# Internal & external

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 3 · Same thing, same look, same place
Live: https://ryan-di.github.io/design-field-guide/#good-consistency
Kind: principle
Cite as: Design Field Guide v35, #good-consistency

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Consistency means one action has one look, one concept has one name, and the same buttons sit in the same order everywhere. People learn a product by noticing patterns, so when the patterns hold, what they learned on one screen works on the next. When they don’t, people slow down and wonder whether two things that look different do different things.

There are two kinds. Internal consistency is about your own product: the same thing looks and works the same on every screen. External consistency is about everything else people use, the platform and other common products, as in [Jakob’s law](https://ryan-di.github.io/design-field-guide/#pat-jakobs-law). Keyboard and screen-reader users lean on both, because they can’t take in a whole screen at a glance.

## Rules

Three rules keep a product consistent. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Give one action one look

https://ryan-di.github.io/design-field-guide/#good-consistency-rule-1

When Add to cart is a filled button on one page and a plain link on another, people wonder whether the two do different things: a link usually opens a page, so some expect to see the item rather than add it. Build the action once as a component and use it everywhere. If two places really need different styles, they probably need different names too.

### 2. Give one thing one name

https://ryan-di.github.io/design-field-guide/#good-consistency-rule-2

When one thing has two names, people assume there are two things, so they look in the wrong place or doubt that their action worked. Pick one word for each concept and keep a short glossary. Use the same word in buttons, menus, messages and help.

### 3. Follow the platform’s conventions

https://ryan-di.github.io/design-field-guide/#good-consistency-rule-3

People bring habits from every other app they use. Most dialogs put the main button at the right end, with Cancel just before it, so when a product flips that order, people press by position and hit the wrong button. Follow the convention unless you can show a clear win for a real task, and if you do break it, break it the same way everywhere.

## In real products

Notice what stays the same from screen to screen, and which habits people bring from other products.

- Google Docs: Docs, Sheets and Slides share one menu order and keep Share in the top-right corner. Only a few menus differ, so learning one teaches the others. `good-consistency-example-01`
- macOS: dialogs put the main button at the right end, with Cancel just before it. Apps that keep the platform’s order let people answer without rereading the buttons. `good-consistency-example-02`
- Linear: Cmd+K opens a command menu, the same shortcut Slack and GitHub use to jump around or run commands. People bring that habit from tool to tool. `good-consistency-example-03`
- YouTube: every video in a feed or search results has the same ⋮ menu beside its title, with the same actions. Learn it once and it works on every video. `good-consistency-example-04`

## Related entries

[pat-jakobs-law](pat-jakobs-law.md)
