# Labels in people’s words

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 11 · Can’t find it
Live: https://ryan-di.github.io/design-field-guide/#pat-information-scent
Kind: pattern
Cite as: Design Field Guide v35, #pat-information-scent

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

People scan menus and links for the word already in their head. When a label matches it, they click with confidence, and when it doesn’t, they guess, go back and try again, or give up. This pull of matching words is called information scent.

Labels in people’s words carry that scent: they name things the way customers do, not the way the team does inside the company. Each label should also make sense on its own, because many people, screen reader users among them, jump from label to label without seeing the layout around it.

## Ways to do it

A label can carry more or less scent, and the more alike the options are, the more each label needs to say.

- **Name the thing**
- **Name the task**
- **Add a description**
- **Show what’s inside**

## Rules

Four rules keep labels in people’s words.

### 1. Use people’s words, not the team’s

https://ryan-di.github.io/design-field-guide/#pat-information-scent-rule-1

Teams name things after how the system works: “entities”, “remittance”, a database field. People don’t know those words, so they read every option and guess. Collect the words people use in support questions, reviews and searches before you name things, and use those.

### 2. Name what’s inside, not the brand

https://ryan-di.github.io/design-field-guide/#pat-information-scent-rule-2

Clever or branded names are fun to write, but they don’t say what’s behind them, so people open each one to find out and remember none of them. Use plain names that say what each section holds, and keep personality for empty states and onboarding, where it doesn’t cost a click.

### 3. Use one name for one thing

https://ryan-di.github.io/design-field-guide/#pat-information-scent-rule-3

When one thing has two names, people assume they are two things and wonder whether the cart and the bag hold the same items. As with [consistent naming](https://ryan-di.github.io/design-field-guide/#good-consistency) anywhere in a product, pick one term for each concept, use it everywhere and keep a short glossary.

### 4. Test the whole path with a task

https://ryan-di.github.io/design-field-guide/#pat-information-scent-rule-4

A label can be right and still go unfound, because it sits under a parent nobody opens. People pick a top-level section first, and if that name doesn’t match their goal, they never see what’s inside. Give people a task, like “Where would you add your passport number?”, and watch where they click first, which is called tree testing. Move items to where people look.

## In real products

- GOV.UK: pages are named for the task people come to do, like “Renew your passport”, not for the office that handles it. `pat-information-scent-example-01`
- Blender: menus use plain names like “Cube”. With Python tooltips turned on, the tooltip adds the scripting name under the description, for the people who need it. `pat-information-scent-example-02`
- Uber: the main box asks “Where to?”, the question already in your head, instead of a form label like “Destination”. `pat-information-scent-example-03`
- Windows: searching the old Control Panel name, “Add or remove programs”, still opens the newer Apps page in Settings, so people who learned the old words still get there. `pat-information-scent-example-04`

## Related entries

[good-consistency](good-consistency.md)
