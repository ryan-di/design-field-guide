# Tesler’s law

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 15 · Lean on how people already behave
Live: https://ryan-di.github.io/design-field-guide/#pat-teslers-law
Kind: pattern
Cite as: Design Field Guide v35, #pat-teslers-law

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Tesler’s law says every task holds some complexity that can’t be removed, only moved. When a photo app imports pictures, it still has to save them to a folder. Either people type the full folder path, or the app offers the folders they used recently. The design question is who carries that work: the system or the person.

Usually the system should carry it, because the team solves the hard part once instead of every person solving it every time. But moved complexity always lands somewhere, such as an error message, the help pages or the next screen, so when you simplify a step, check where the work went.

## Rules

Three rules help you put complexity in the right place.

### 1. Keep control within reach

https://ryan-di.github.io/design-field-guide/#pat-teslers-law-rule-1

Some complexity exists because people need the choice. One fixed export size works for sharing a photo but not for a print shop that needs the full size, and if the app hides that choice, people can’t finish the task at all. Keep the simple path as the default, and put the full controls in an [advanced layer](https://ryan-di.github.io/design-field-guide/#pat-layered-ui) one click away.

### 2. Solve it once in the product

https://ryan-di.github.io/design-field-guide/#pat-teslers-law-rule-2

Some complexity lands on people only because the team didn’t handle it. A phone field that accepts one exact format makes every person reformat their number, often after an error. [Accept the formats people type](https://ryan-di.github.io/design-field-guide/#pat-forgiving-input) and tidy them up in the product, so the team does the work once.

### 3. Test the simple version with real data

https://ryan-di.github.io/design-field-guide/#pat-teslers-law-rule-3

A simple flow often works only for the sample data it was built with. Real photos have odd names, other file types and huge sizes, and when those fail, the complexity comes back as error messages people can’t act on. Before you call a flow simple, [try the messy cases](https://ryan-di.github.io/design-field-guide/#good-edge-cases): large files, unusual names, hundreds of items.

## In real products

Notice which hard part each product carries for people, and where it still lets them take over.

- Uber: sets the pickup point from your location, so the only thing to type is where you’re going. You can still change the pickup if it’s off. `pat-teslers-law-example-01`
- iOS: when a sign-in code arrives by text, it’s offered above the keyboard. The security step stays, but nobody copies digits by hand. `pat-teslers-law-example-02`
- Lightroom: Auto sets exposure, contrast and more in one click, and moves the regular sliders, so you can see what it did and adjust any of it. `pat-teslers-law-example-03`

## Related entries

[good-edge-cases](good-edge-cases.md), [pat-forgiving-input](pat-forgiving-input.md), [pat-layered-ui](pat-layered-ui.md)
