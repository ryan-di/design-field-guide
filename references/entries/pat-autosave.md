# Autosave

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 13 · Prevent, explain, recover
Live: https://ryan-di.github.io/design-field-guide/#pat-autosave
Kind: pattern
Cite as: Design Field Guide v35, #pat-autosave

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Autosave keeps people’s work without them asking. Each change is saved a moment after it’s made, and a small status says so. If the app crashes or the tab closes, the work is waiting when people come back.

Autosave keeps only the latest state, so it belongs together with [version history](https://ryan-di.github.io/design-field-guide/#pat-version-history), which keeps the earlier ones.

## Ways to do it

Autosave takes a few forms. A document saves as people type and shows the save state. A settings page saves each change the moment it’s made. A message box keeps unsent text when people move somewhere else. After a crash, the app offers the work it kept on the device.

- **As you type.** Use it for documents people write over time.
- **Each change.** Use it for settings, where each change is small and easy to reverse.
- **Unsent text.** Use it for message boxes, where people often switch away mid-sentence.
- **After a crash.** Use it for apps that keep work on the device between saves.

## Rules

Four rules keep autosave useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Show that work is saved

https://ryan-di.github.io/design-field-guide/#pat-autosave-rule-1

If people can’t see that their work is saved, they don’t trust it: they keep saving by hand, or they lose work when a save fails without a word. Show a [save status](https://ryan-di.github.io/design-field-guide/#pat-instant-feedback) where they already look. If a save fails, say so plainly, keep the work on the device and send it once the connection is back.

### 2. Keep earlier versions

https://ryan-di.github.io/design-field-guide/#pat-autosave-rule-2

Autosave saves mistakes too: if someone deletes a paragraph by accident, the save goes through a second later and the old text is gone. Pair autosave with version history, so any earlier version is one step back. A recovered draft should also wait until people choose Restore or Discard.

### 3. Catch edits from another tab

https://ryan-di.github.io/design-field-guide/#pat-autosave-rule-3

The same document can be open in two tabs or on two devices. Each copy saves its own text, so the last save replaces the other without a word, and people notice much later that what they added in the other place is gone. Detect the clash and ask before one copy replaces the other.

### 4. Offer recovery only when something was lost

https://ryan-di.github.io/design-field-guide/#pat-autosave-rule-4

A recovery prompt that shows up every time teaches people to dismiss it, so the one time it matters, they press Discard without reading. Offer recovery only when the draft differs from what was saved. Clear old drafts after a while, and let Discard be undone for a moment.

## In real products

Notice how each product shows that work is safe, and what comes back after a close or a crash.

- Google Docs: saves as you type, so there’s no Save button to forget, only “Saved to Drive” next to the title. `pat-autosave-example-01`
- Word: after a crash, a recovery pane lists the autosaved copy next to the last saved one, so you choose which to keep. `pat-autosave-example-02`
- VS Code: quit with unsaved files and they reopen next time, still marked unsaved. Nothing is lost, and nothing is written to the file until you save. `pat-autosave-example-03`
- Telegram: leave a chat mid-message and the chat list marks it as a draft. The text is still there when you come back, even on another device. `pat-autosave-example-04`

## Related entries

[pat-instant-feedback](pat-instant-feedback.md), [pat-version-history](pat-version-history.md)
