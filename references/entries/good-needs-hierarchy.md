# Hierarchy of needs

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 1 · Get the problem right first
Live: https://ryan-di.github.io/design-field-guide/#good-needs-hierarchy
Kind: principle
Cite as: Design Field Guide v35, #good-needs-hierarchy

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

The hierarchy of needs is an order for building a feature. First it has to work, then work every time, then be easy to use. Only after that does delight count, like a small animation or a friendly line of text.

Each layer rests on the ones below it, so a pleasant touch on a feature that sometimes fails doesn’t feel pleasant: it feels like nobody checked. Easy to use includes people who use a keyboard or a screen reader, so accessibility belongs in that layer and can’t wait for the polish.

## Rules

Four rules keep the layers in order.

### 1. Make it work before you polish it

https://ryan-di.github.io/design-field-guide/#good-needs-hierarchy-rule-1

When the animation is done before the feature, people get the nice moment and then find nothing behind it. The polish makes the failure feel worse, because it promised something. Build from the bottom up, and add the polish last.

### 2. Check more than the happy path

https://ryan-di.github.io/design-field-guide/#good-needs-hierarchy-rule-2

A feature can work when everything goes right and still fail people often, because networks are slow, lists are empty and servers return errors. If those cases show a blank screen, people can’t tell whether to wait or leave. Try each case before you call the feature done, and give each one a clear state.

### 3. Make room for delight once it holds

https://ryan-di.github.io/design-field-guide/#good-needs-hierarchy-rule-3

There is always another bug, so delight can wait forever. The product then works but feels flat: finishing something feels the same as nothing happening. Once the base holds, plan small moments of care, like a friendly confirmation or a smooth transition, as part of the work.

### 4. Don’t cover a failure with a joke

https://ryan-di.github.io/design-field-guide/#good-needs-hierarchy-rule-4

A cheerful message on a failed payment leaves people with no idea what went wrong, and it can feel like the product doesn’t take their money seriously. Say plainly what failed and what they can do about it. Keep the playful touches for moments that went well.

## In real products

Notice that each product shows its base is dependable before it adds anything playful.

- Dropbox: each file in the synced folder shows a small icon, arrows while it syncs and a check once it’s up to date. People trust it with work files because they can see that each one is safe. `good-needs-hierarchy-example-01`
- WhatsApp: a message shows a clock until it has really left the phone, then one tick when it’s sent and two when it’s delivered. It never claims a message went out when it didn’t. `good-needs-hierarchy-example-02`
- Asana: finishing a task now and then sends a cartoon creature across the screen. It’s a small, rare treat on top of a task list that already works. `good-needs-hierarchy-example-03`
- Duolingo: the cheerful end-of-lesson screen also shows the XP you earned and your accuracy. The fun celebrates progress that was really counted. `good-needs-hierarchy-example-04`
