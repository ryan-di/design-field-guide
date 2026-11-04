# Spinner

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 17 · Loading & progress
Live: https://ryan-di.github.io/design-field-guide/#spinner
Kind: component
Cite as: Design Field Guide v35, #spinner

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A spinner is a small turning circle that says “working on it”. It’s for short waits, up to about ten seconds: sending a message, loading search results, saving a change. It sits on the thing that’s busy.

Where a spinner says only that work is happening, a progress bar also shows how much is done, so it’s the better choice for longer waits.

## Forms

Spinners come in four forms, set by how much is waiting: in a button, inline next to a field, in one section, and over the full page. Use the smallest one that covers what’s loading, so the rest of the page stays usable.

- **Button.** Use it when one action is waiting, like sending an email.
- **Inline.** Use it next to a field or a line that’s updating, like a search box.
- **Section.** Use it when one part of the page is reloading.
- **Full page.** Use it only when there’s nothing to show yet, like while an app first opens.

## Rules

Four rules keep spinners useful.

### 1. Wait before showing it

https://ryan-di.github.io/design-field-guide/#spinner-rule-1

When results come back in a fraction of a second, the spinner only blinks, which looks like a glitch and makes the app feel slower than it is. Hold it back for about 400 ms, so fast results just appear and a spinner means there’s a real wait.

### 2. Use a progress bar for long waits

https://ryan-di.github.io/design-field-guide/#spinner-rule-2

A spinner can’t say how much is done or how long is left, so after a while people wonder if it’s stuck, and they cancel or reload. Once a wait can run past about ten seconds, show a progress bar and what’s happening, so people can choose to wait or go do something else.

### 3. Keep the rest of the app working

https://ryan-di.github.io/design-field-guide/#spinner-rule-3

A spinner over the whole screen locks everything, even the parts that aren’t loading, so someone writing a reply has to stop and wait for a folder list. Put the spinner on the part that’s loading, so it shows what’s busy and everything else stays usable.

### 4. Hold the content’s space

https://ryan-di.github.io/design-field-guide/#spinner-rule-4

A spinner is usually smaller than the content that replaces it, so the page jumps when the content arrives, like any [content that loads late](https://ryan-di.github.io/design-field-guide/#good-edge-cases). Show a skeleton in the shape of the coming content instead, so nothing below it moves.

## In real products

- Chrome: a loading tab swaps its icon for a small spinner. Only that tab is busy, so you keep reading in the others. `spinner-example-01`
- Stripe Checkout: after you press Pay, the button itself shows a spinner, then a check mark. The feedback sits where you clicked, so you know the press landed. `spinner-example-02`
- iOS Mail: pull the inbox down and a spinner shows above it while it checks for new mail. The messages already there stay put and readable. `spinner-example-03`

## Related entries

[good-edge-cases](good-edge-cases.md)
