# Undo

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 9 · Scared to click
Live: https://ryan-di.github.io/design-field-guide/#pat-undo
Kind: pattern
Cite as: Design Field Guide v35, #pat-undo

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Undo lets people act at once and take the action back afterwards. The app deletes, moves or sends right away and keeps a way back open, so a wrong click costs a second instead of lost work.

A confirm dialog asks “Are you sure?” before the action, when people haven’t seen the result yet, and after a few of them people click through without reading. Undo works after the action, when people can see what they did.

## Ways to do it

Undo comes in four common forms. They differ in how long the way back stays open and where people find it.

- **Undo toast.** Use it right after a single action, such as removing a song. A toast offers Undo for a few seconds, then leaves.
- **Undo history.** Use it in editors where people make many small changes. Each Undo steps back one change, in order. Redo steps forward again, and the buttons name the step.
- **Trash.** Use it when people may notice a mistake days later. Deleted items wait in the trash for a set time, and people can put them back from there.
- **Delay.** Use it for actions that can’t be taken back once they happen, such as sending. The app waits a few seconds before it really acts, and Undo cancels it.

## Rules

Four rules keep undo useful.

### 1. Plan where deleted things go

https://ryan-di.github.io/design-field-guide/#pat-undo-rule-1

Undo only works if the deleted thing still exists somewhere. If the app removes it for real and Undo is added later, Undo can only rebuild a rough copy, and people get back a name without the details they cared about. Plan for it in the data model from the start: mark items as deleted and keep them until the way back closes. [Version history](https://ryan-di.github.io/design-field-guide/#pat-version-history) uses the same idea.

### 2. Keep Undo open long enough

https://ryan-di.github.io/design-field-guide/#pat-undo-rule-2

People often notice a mistake a few seconds late, after they look back at the screen, so an Undo that leaves after two seconds is already gone. Keep it until the next action, or for several seconds after people return to the page. Pause any timer while the pointer or focus is on the toast.

### 3. Keep a confirm for what can’t be undone

https://ryan-di.github.io/design-field-guide/#pat-undo-rule-3

Some actions can’t be reversed, such as emptying the trash, sending money or sharing with other people, and without a question one slip loses things for good. Ask first for these actions, and only these. Name the consequence in the question and put the action on the button, such as “Delete 12 files”. See [Dialog](https://ryan-di.github.io/design-field-guide/#dialog).

### 4. Give more than one way back

https://ryan-di.github.io/design-field-guide/#pat-undo-rule-4

A [toast](https://ryan-di.github.io/design-field-guide/#toast) is easy to miss and leaves after a while, so if Undo lives only there, people who missed it have no way back. Also support Ctrl+Z (⌘Z on Mac) and an Undo item in a menu that names what it will undo. After Undo, put focus on the restored item so keyboard users can carry on.

## In real products

Notice where each way back lives: on screen, on the keyboard or in a menu.

- Gmail: after Send, the message waits a few seconds with Undo on screen. Even sending, which is normally final, gets a way back. `pat-undo-example-01`
- macOS Finder: Move to Trash happens without a question. ⌘Z puts the file back, and the Edit menu names exactly what will be undone. `pat-undo-example-02`
- YouTube: choosing “Not interested” removes a video from the feed at once. The empty spot offers Undo, right where the tap happened. `pat-undo-example-03`

## Related entries

[dialog](dialog.md), [pat-version-history](pat-version-history.md), [toast](toast.md)
