# Badge

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 16 · Feedback & status
Live: https://ryan-di.github.io/design-field-guide/#badge
Kind: component
Cite as: Design Field Guide v35, #badge

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A badge is a small mark on another item: a dot or a number on an icon, a tab or a button. It tells people at a glance that something there is new or needs them, like 3 unread messages or 1 update. It goes away once they’ve looked.

Where a toast interrupts to say something just happened, then fades, a badge doesn’t interrupt. It waits on the item until people are ready to look.

## Forms

Badges come in four forms, set by what people need to know. A dot says only that something is new. A count says how many. A label names the kind of thing, like “New” or “Beta”. A status mark shows a live state, like who is online.

- **Dot.** Use it when “something new is here” is all people need to know.
- **Count.** Use it when the number changes what people do, like unread messages.
- **Label.** Use a short word, like “New” or “Beta”, when the kind of thing matters more than how many.
- **Status.** Use it for a live state, like who is online.

## Rules

Four rules keep badges useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Clear it once people look

https://ryan-di.github.io/design-field-guide/#badge-rule-1

A badge that still says 3 after someone has seen all 3 is out of date, so people stop trusting it and miss the next one that matters. Remove it as soon as they view what it points to, so a badge always means there’s something they haven’t seen yet.

### 2. Badge only what needs attention

https://ryan-di.github.io/design-field-guide/#badge-rule-2

When every row has a bright number, none of them stands out, and people open folders one by one to find what changed. Keep badges for what’s new or needs action, and show totals as plain text next to the item, where they don’t compete.

### 3. Cap the number

https://ryan-di.github.io/design-field-guide/#badge-rule-3

A big number makes the badge wider than the icon it sits on and crowds the icons next to it. Past a point, nobody reads the exact number anyway: it just means “a lot”. Show “99+” instead, and put the exact count at the top of the list it opens.

### 4. Say what the number means

https://ryan-di.github.io/design-field-guide/#badge-rule-4

A red 3 on a gear could mean errors, warnings or updates, and red also reads as danger, so people either worry or ignore it. Put what it counts in the button’s label and a tooltip, like “3 updates available”, so people can decide whether to look now without opening anything.

## In real products

Notice that each badge stays small, and only shows a number when the number matters.

- Slack: a channel with new messages turns bold, and only mentions and direct messages get a number. Bold says something’s new, and a number says someone wants you. `badge-example-01`
- GitHub: the notifications icon shows a small dot when something’s unread, not a count. The exact number waits in the inbox it opens. `badge-example-02`
- YouTube: the count on the bell stops at 9+. Past that, the exact number wouldn’t change what you do, so the badge stays small. `badge-example-03`
- iOS: apps can put a count on their home screen icon, like unread mail. People can turn badges off for each app in notification settings, so a noisy app loses its badge. `badge-example-04`
