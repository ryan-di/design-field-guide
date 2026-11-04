# Read every component as a promise

Design Field Guide v35 (2026-11) · Part 3 · Components
Live: https://ryan-di.github.io/design-field-guide/#ch-start
Cite as: Design Field Guide v35, #ch-start

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Every component makes a promise to the person using it, about three things.

- **Attention**: How much it interrupts. A badge waits to be noticed. A dialog stops everything until it gets an answer.
- **Lifetime**: How long it stays. A toast is gone in seconds. A banner stays until the state behind it changes.
- **Control**: What people can do with it. A tooltip can only be read. A popover can hold buttons and fields.

## How each entry reads

Each component is a short article. It says what the component is for, with a demo. Then its forms, and the rules: each shows how the component breaks and what to do instead, with a demo you can switch between the two. Last, real products that use it.

## The interruption ladder

For anything the product needs to tell people, use the lowest step that still does the job. Each step up costs more attention, so it has to be worth more. Click a step to jump to it.

- [Inline message](https://ryan-di.github.io/design-field-guide/#inline-message): Next to the thing
- [Badge](https://ryan-di.github.io/design-field-guide/#badge): Waits to be seen
- [Toast](https://ryan-di.github.io/design-field-guide/#toast): Says it, then goes
- [Banner](https://ryan-di.github.io/design-field-guide/#banner): Stays while true
- [Dialog](https://ryan-di.github.io/design-field-guide/#dialog): Stops everything
