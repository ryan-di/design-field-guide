# Layered interface

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 14 · Newcomers & experts
Live: https://ryan-di.github.io/design-field-guide/#pat-layered-ui
Kind: pattern
Cite as: Design Field Guide v35, #pat-layered-ui

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A layered interface shows a simple set of controls first and keeps the full set one step away. New and occasional users get the few choices that matter, and experts open the advanced layer to change the rest. Both layers change the same settings, so switching between them loses nothing.

Where [progressive disclosure](https://ryan-di.github.io/design-field-guide/#pat-progressive-disclosure) tucks away the settings few people change, a layered interface gives newcomers and experts each a named layer of the same controls, and people pick the one they work in.

## Ways to do it

There are a few ways to layer. Show more and a separate page work as in [progressive disclosure](https://ryan-di.github.io/design-field-guide/#pat-progressive-disclosure). The other two split the work into two versions: a mode switch flips the whole screen between a basic and a full version, and a quick form handles the common case and opens the full form for the rest.

- **Show more.** Use it when a few extra fields help some people, on the same screen.
- **Mode switch.** Use it when a whole screen has a basic and a full version, and people stay in one for a while.
- **Separate page.** Use it for settings few people ever need, kept out of the main screen.
- **Quick, then full.** Use it when most people need only a title and a time, and some need everything.

## Rules

Four rules keep a layered interface useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Build both layers on one set of settings

https://ryan-di.github.io/design-field-guide/#pat-layered-ui-rule-1

If Simple and Advanced are two separate forms, they drift apart: a value typed in one is missing in the other, and some settings work in only one mode. Build Simple on top of the same settings as Advanced, so it only hides fields and keeps their values.

### 2. Keep the way to more in sight

https://ryan-di.github.io/design-field-guide/#pat-layered-ui-rule-2

If the way to the full controls is hard to find, people assume the simple layer is all there is, and they scroll through everything or leave. Put the way in a fixed, visible place, as a named button or a [segmented control](https://ryan-di.github.io/design-field-guide/#segmented), and [say what’s behind it](https://ryan-di.github.io/design-field-guide/#pat-progressive-disclosure), such as “Filters: size, color, price”.

### 3. Show what changed out of sight

https://ryan-di.github.io/design-field-guide/#pat-layered-ui-rule-3

Settings changed in the advanced layer still apply after people go back to the simple one, and [a change nobody can see](https://ryan-di.github.io/design-field-guide/#pat-progressive-disclosure) makes results look wrong for no clear reason. Show a short summary in the simple layer, such as “1 advanced setting changed”, with a way to show it and a way to reset it.

### 4. Decide where each new option goes

https://ryan-di.github.io/design-field-guide/#pat-layered-ui-rule-4

When nobody decides where a new option goes, it lands in Advanced, which over time becomes a long, unsorted list where settings many people need get buried. For each option, choose the simple layer, the advanced layer, or a better default that makes it unnecessary. Keep Advanced for real expert choices, grouped in a sensible order.

## In real products

- Gmail: the search options button opens fields like From, Subject and Date, and turns them into a query in the same search box. `pat-layered-ui-example-01`
- VS Code: the searchable settings form and the JSON file that experts open from the corner icon edit one file. `pat-layered-ui-example-02`
- Airbnb: the search bar asks only where, when and who. Price, type of place and amenities wait behind Filters for the people who care. `pat-layered-ui-example-03`

## Related entries

[pat-progressive-disclosure](pat-progressive-disclosure.md), [segmented](segmented.md)
