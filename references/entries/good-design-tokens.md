# Design tokens

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 3 · Same thing, same look, same place
Live: https://ryan-di.github.io/design-field-guide/#good-design-tokens
Kind: principle
Cite as: Design Field Guide v35, #good-design-tokens

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A design token is a shared value with a name, such as a corner radius, a spacing step, a color or a text size. Components point at the name instead of holding their own number, so when the token changes, every component that uses it changes with it.

Tokens are how [Spacing rhythm](https://ryan-di.github.io/design-field-guide/#good-spacing-rhythm) and [consistency](https://ryan-di.github.io/design-field-guide/#good-consistency) hold up in a large team. They can carry [contrast](https://ryan-di.github.io/design-field-guide/#good-contrast) too: give every background token a matching text token, like “accent” and “on-accent”, and check each pair once, so no component can pick a pair that fails.

## Kinds of tokens

Most systems have three layers of tokens: base, role and component. Each layer points at the one before it, so a change happens in one place.

- **Base.** Raw values, like blue-600 = #2F5DA8. Components never use them directly.
- **Role.** A name for a job, like accent or danger. This is the layer components use.
- **Component.** For one component that has to differ from its role, like a play button in the text color.

## Rules

Three rules keep tokens useful. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Point components at tokens

https://ryan-di.github.io/design-field-guide/#good-design-tokens-rule-1

When each component holds its own numbers, a change has to be made in every component. Someone always misses one, and the product drifts: a 6 px corner here, an 8 px corner there. Point every component at a token instead, so a change in one place reaches all of them.

### 2. Name tokens by their job

https://ryan-di.github.io/design-field-guide/#good-design-tokens-rule-2

A token named after its value, like blue-500, can’t change without becoming wrong: to rebrand, you either edit every component, or make blue-500 green and turn everything else that used it green too. Name tokens by their job, such as accent or rain. Only the job token knows which blue it is, so a rebrand changes one line.

### 3. Keep the set small

https://ryan-di.github.io/design-field-guide/#good-design-tokens-rule-3

Tokens that are close, like radius-7, radius-8 and radius-9, look the same on screen. People can’t choose between them, so they pick one at random, and the product drifts anyway. Keep a few clear steps, each with a job. When two tokens are close and used for the same job, merge them.

## In real products

- Figma: layers can point at a variable, like accent, instead of a raw color. Change the variable once and every layer that uses it updates. Modes, like Light and Dark, swap a whole set of values at once. `good-design-tokens-example-01`
- VS Code: every part of the window reads a named theme color, like editor.background or statusBar.background. A theme only fills in those names. Extensions use the same names, so they follow every theme too. `good-design-tokens-example-02`
- iOS: apps set text by role, like Headline, Body and Caption, not by pixel size. Move the Text Size slider in Settings and every app that uses these roles scales all its text together. `good-design-tokens-example-03`
- X (Twitter): the display settings let you pick one accent color, and buttons, links and highlights across the app switch to it at once. `good-design-tokens-example-04`

## Related entries

[good-consistency](good-consistency.md), [good-contrast](good-contrast.md), [good-spacing-rhythm](good-spacing-rhythm.md)
