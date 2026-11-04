# Toast

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 16 · Feedback & status
Live: https://ryan-di.github.io/design-field-guide/#toast
Kind: component
Cite as: Design Field Guide v35, #toast

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A toast is a short message that appears near the edge of the screen after people do something. It confirms that the action worked, such as “Email archived”, and often offers Undo. It leaves on its own after a few seconds, and people can keep working while it’s there.

Where a banner describes a state that lasts, like being offline, and stays until the state ends, a toast reports one moment and fades. So it can’t carry anything people must see.

## Forms

Toasts come in three common forms: a plain toast only confirms, a toast with Undo lets people reverse what they just did, and a progress toast reports a short task while it runs. All three leave on their own.

- **Plain.** Use it to confirm something that worked, when nothing else needs doing.
- **With Undo.** Use it after an action people may want to reverse, like removing something from a cart.
- **Progress.** Use it for a short task that runs in the background, like sending invitations.

## Rules

Five rules keep toasts useful.

### 1. Don’t put errors in a toast

https://ryan-di.github.io/design-field-guide/#toast-rule-1

A toast leaves after a few seconds, whether anyone read it or not, so people who looked away never learn that the photo didn’t upload. Put the error next to the file it’s about, or in a banner that lasts until the problem is solved, where it has room to explain the limit and offer a way forward.

### 2. Don’t make it the only way to act

https://ryan-di.github.io/design-field-guide/#toast-rule-2

When a toast holds the only Restart button, the button leaves with it, and people who miss it have no way left to finish the update. Put requests like this in a banner or a notification that stays until people choose, so “Later” is a real choice and not a missed chance.

### 3. Combine messages into one

https://ryan-di.github.io/design-field-guide/#toast-rule-3

When several things finish at once, each can fire its own toast, and they pile up, cover the page and repeat the same news. Use one toast that updates as things finish, such as “3 photos uploaded”, so people get one clear result and the page stays usable.

### 4. Leave a trace that lasts

https://ryan-di.github.io/design-field-guide/#toast-rule-4

A toast only helps if people are looking when it appears. If the export finishes while they’re in another part of the app, they come back to no sign that it’s done. Also mark the result somewhere that waits, such as a badge on Files or an entry in a notifications list, where people find it whenever they look.

### 5. Offer Undo instead of asking first

https://ryan-di.github.io/design-field-guide/#toast-rule-5

A confirm dialog on every delete gets clicked through without reading, as [the Undo pattern](https://ryan-di.github.io/design-field-guide/#pat-undo) explains. For actions that can be reversed, act right away and show a toast with Undo: it takes fewer clicks, and a mistake is one press to fix.

## In real products

- Gmail: after you send, a toast offers Undo for a few seconds, and the email only goes out once that time is up. A slip costs one click instead of a follow-up email. `toast-example-01`
- macOS: after a screenshot, a thumbnail slides into the corner. Click it to mark up or share, or ignore it and it saves on its own a few seconds later. `toast-example-02`
- Spotify: adding a song to a playlist from a menu shows a short toast with the playlist’s name. The menu has already closed, so the toast is how you know it worked. `toast-example-03`

## Related entries

[pat-undo](pat-undo.md)
