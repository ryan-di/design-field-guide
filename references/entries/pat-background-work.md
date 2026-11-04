# Background work

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 10 · Did it work?
Live: https://ryan-di.github.io/design-field-guide/#pat-background-work
Kind: pattern
Cite as: Design Field Guide v35, #pat-background-work

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Some work takes longer than people want to wait, such as an upload, an export or a backup. Background work lets it run while people keep doing other things. A small indicator shows that it’s still going, a toast says when it’s done, and finished results wait in a list until people look at them.

That is what separates it from a [progress bar](https://ryan-di.github.io/design-field-guide/#progress-bar) in a dialog, which makes people sit and watch: here people keep working while the progress stays on screen. Tell screen readers when the work starts and when it ends, not at every step of progress.

## Ways to do it

There are four common ways to keep background work in view. They differ in how much room the work takes and in how people hear that it’s done. Many products combine two, like an indicator while it runs and a toast at the end.

- **Indicator.** A small status in a bar that stays on screen.
- **Panel.** A corner panel with one row per item, which people can shrink.
- **Toast when done.** A short toast when the work finishes, with a way to open the result.
- **Email when ready.** For work that takes many minutes or hours.

## Rules

Four rules keep background work useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Keep progress on screen

https://ryan-di.github.io/design-field-guide/#pat-background-work-rule-1

People rarely stay on the screen where they started a long job, and once they move on, progress that lived on that screen is gone. They can’t tell if the work is still running, stuck or done, so they go back to check or start it again. Put a small indicator in a bar that stays on every screen.

### 2. Keep finished work in a list

https://ryan-di.github.io/design-field-guide/#pat-background-work-rule-2

A toast that says “ready” is easy to miss, because people look away or it fades before they finish what they’re doing. If that toast was the only way to the result, the result is lost to them. Keep finished work in a list they can open later, and mark new items until they’ve been opened.

### 3. Group notices that come together

https://ryan-di.github.io/design-field-guide/#pat-background-work-rule-3

When many items finish close together, one toast per item piles up. The toasts cover the screen and all say nearly the same thing, and people have to read or close each one. Send one toast for the whole batch, with a link to the items.

### 4. Make failures louder than success

https://ryan-di.github.io/design-field-guide/#pat-background-work-rule-4

A failure that looks like a success goes unnoticed until someone needs the file, and by then it may be too late to redo the work. Keep a failure on screen until it’s dealt with: mark it clearly, say what went wrong, and offer a way to fix it.

## In real products

Notice where progress lives while the work runs, and where the result waits once it’s done.

- Google Drive: uploads run in a small panel in the corner, one row per file, while you keep browsing. Finished files keep their check until you close the panel. `pat-background-work-example-01`
- Lightroom Classic: imports and exports show a thin progress bar in the top-left corner, so you can keep editing photos while they run. `pat-background-work-example-02`
- Instagram: after you share a post, you land back in the feed, and a strip at the top shows your photo with a progress bar until it’s posted. `pat-background-work-example-03`
- Safari: the downloads button in the toolbar shows progress, and its list keeps finished files, so a download you missed is still one click away. `pat-background-work-example-04`

## Related entries

[progress-bar](progress-bar.md)
