# Progress bar

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 17 · Loading & progress
Live: https://ryan-di.github.io/design-field-guide/#progress-bar
Kind: component
Cite as: Design Field Guide v35, #progress-bar

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A progress bar is a line that fills as long work gets done: an upload, a download, an export, a backup. It shows how far along the work is, and often what it’s doing and how much is left. Unlike a [spinner](https://ryan-di.github.io/design-field-guide/#spinner), it lets people decide whether to wait or do something else.

## Forms

Progress bars come in four forms. A bar of known length fills as work gets done, and a bar of unknown length moves without filling. A small ring sits on one item in a list, and a background strip tracks long work while people do something else.

- **Known.** Use it when the work can be counted, like songs in an album.
- **Unknown.** Use it when the total isn’t known yet, like a search across many airlines.
- **Ring.** Use it when several things download at once, like podcast episodes.
- **Background.** Use it for long work people don’t need to watch, like a photo backup.

## Rules

Four rules keep progress bars useful.

### 1. Show stages when you can’t measure

https://ryan-di.github.io/design-field-guide/#progress-bar-rule-1

Some work has nothing to count, so the bar sits at 0% and then jumps to done, and until then people can’t tell if it’s working or stuck. Use a moving bar to show it’s alive, with a label that names each stage as it starts, so people see it’s getting somewhere.

### 2. Count real work

https://ryan-di.github.io/design-field-guide/#progress-bar-rule-2

A bar that isn’t tied to real work often races ahead, then sits at 99% for most of the wait, so people think it froze and stop believing it. Move it by real units, like photos exported, and if one part can’t be counted, say so with a label like “Finishing up…”.

### 3. Let people keep working

https://ryan-di.github.io/design-field-guide/#progress-bar-rule-3

When an export locks the whole app, people can only sit and watch the bar, and if they change their mind, there’s no way to stop it. Run long work in a small strip, as [background work](https://ryan-di.github.io/design-field-guide/#pat-background-work), let people carry on, always offer Cancel, and tell them when it’s done.

### 4. Put it on the item

https://ryan-di.github.io/design-field-guide/#progress-bar-rule-4

A new file can look ready in the list while it’s still uploading, and a tiny bar in a corner goes unseen. Show progress on the item itself, where people are already looking, and add a summary, like an uploads count in the top bar.

## In real products

- Blender: while rendering, the render window counts samples and shows the time left. Samples are real units of work, so the count is honest, and Esc stops the render. `progress-bar-example-01`
- Finder: a long copy shows how much is done, about how long is left, and a button to stop it. You can keep using Finder while it runs. `progress-bar-example-02`
- YouTube: while a video uploads, the dialog shows the percent and time left at the bottom, and you fill in the title and description meanwhile. `progress-bar-example-03`
- WhatsApp: a photo or video you send shows a ring around a cancel button, right on the message, so stopping takes one tap. `progress-bar-example-04`

## Related entries

[pat-background-work](pat-background-work.md), [spinner](spinner.md)
