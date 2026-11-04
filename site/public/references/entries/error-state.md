# Error state

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 24 · States
Live: https://ryan-di.github.io/design-field-guide/#error-state
Kind: component
Cite as: Design Field Guide v35, #error-state

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

An error state is what a screen, or part of one, shows when something failed: a page didn’t load, a save didn’t go through, a link is broken. It says what went wrong in plain words and offers the next step.

It sits where content would be, like an [empty state](https://ryan-di.github.io/design-field-guide/#empty-state), but it means the opposite: something failed, and people need to know what and what to do about it.

## Forms

Error states come in four common kinds, set by what failed: content that didn’t load, an action that didn’t go through, a link to something that’s gone, and a page people aren’t allowed to open. Each kind needs a different next step.

- **Couldn’t load.** Use it when part of a page can’t get its content, often because of the connection.
- **Couldn’t send.** Use it when something people did didn’t go through, like sending an email.
- **Not found.** Use it when a link leads to something that was deleted or never existed.
- **No access.** Use it when the thing exists but people aren’t allowed to open it.

## Rules

Four rules keep error states useful.

### 1. Say what failed

https://ryan-di.github.io/design-field-guide/#error-state-rule-1

When every problem gets the same words, people can’t tell if they made a mistake, lost their connection or hit a bug, so they don’t know what to fix. Name the thing that failed, and say where the cause lies: in what they entered, in the connection, or on the product’s side. People then know whether to change their input, wait for the connection or try again later.

### 2. Offer the next step

https://ryan-di.github.io/design-field-guide/#error-state-rule-2

An error with only an OK button closes and leaves the problem where it was. Put the next step on buttons in the message, such as Try again or Get help, as in [Error messages](https://ryan-di.github.io/design-field-guide/#good-error-copy). Most failures go away on a second try, and help is there when they don’t.

### 3. Keep people’s work

https://ryan-di.github.io/design-field-guide/#error-state-rule-3

When an upload of 40 photos fails halfway and the error clears the selection, people have to pick all 40 again, and the 18 that already uploaded get sent a second time. Keep what people chose and what already finished, so Retry continues from where it stopped.

### 4. Don’t lead with the code

https://ryan-di.github.io/design-field-guide/#error-state-rule-4

“Error 500” means nothing to most people, who can’t tell whose fault it is, or whether to retry or wait. [Lead with plain words](https://ryan-di.github.io/design-field-guide/#good-error-copy): say what didn’t load, that it isn’t their fault, and what to do. The code can stay below in small text, for when they contact support.

## In real products

Notice that each one names what failed, keeps the work, and offers the fix right there.

- Figma: a file that uses fonts you don’t have still opens. Figma lists the missing fonts and lets you pick replacements, so nothing is lost and the fix is one step. `error-state-example-01`
- GitHub: when a pull request can’t merge, it says the branch has conflicts, lists the files, and offers a Resolve conflicts button. Merge stays off until they’re fixed. `error-state-example-02`
- iPhone Messages: a message that fails keeps its text, gets a red mark and “Not Delivered”, and tapping the mark offers Try Again. Nothing has to be retyped. `error-state-example-03`
- Chrome: when a page can’t load, it says why in plain words, lists a few things to check, and keeps the error code small at the bottom, for support. `error-state-example-04`

## Related entries

[empty-state](empty-state.md), [good-error-copy](good-error-copy.md)
