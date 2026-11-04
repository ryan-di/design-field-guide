# Banner

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 16 · Feedback & status
Live: https://ryan-di.github.io/design-field-guide/#banner
Kind: component
Cite as: Design Field Guide v35, #banner

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A banner is a strip across the top of an app or page. It describes a state that lasts and changes what people can do: they’re offline, the file is read-only, the trial is ending. It stays while the state lasts and leaves when it ends, where a [toast](https://ryan-di.github.io/design-field-guide/#toast) reports one moment and fades.

## Forms

Banners come in three tones, set by how serious the state is: info, warning and error. The tone also decides whether people can close it. A fourth, smaller form covers only one part of a page.

- **Info.** Use it for a state that changes what people can do, when nothing is wrong.
- **Warning.** Use it when something will become a problem soon unless people act.
- **Error.** Use it when something is wrong right now and affects the whole app.
- **In a section.** Use it when the state only affects one part of the page. It sits at the top of that part.

## Rules

Four rules keep banners useful.

### 1. Use it only for what’s happening now

https://ryan-di.github.io/design-field-guide/#banner-rule-1

People learn fast what the top of the screen means. If a banner there always means “something is going on right now”, they read it. If it also carries news and offers, they learn to skip it, and then they skip the offline notice too. Put news somewhere people can open when they want, such as a “What’s new” entry.

### 2. Let information be closed

https://ryan-di.github.io/design-field-guide/#banner-rule-2

Some banners are only information, such as a tip or a note that this is a shared copy, and once read they’ve done their job. If they can’t be closed, they keep taking space and turn into a stripe people look past. Let people close them, and remember that they did.

### 3. Show one at a time

https://ryan-di.github.io/design-field-guide/#banner-rule-3

Several states can be true at once: offline, read-only, a tip. Each banner is short, but stacked they push the page down, and people rarely read past the first. Show the most serious one and put the rest in a notifications list.

### 4. Don’t move the page

https://ryan-di.github.io/design-field-guide/#banner-rule-4

Like [content that loads late](https://ryan-di.github.io/design-field-guide/#good-edge-cases), a banner that appears or leaves pushes everything below it, and a click aimed at a button lands on the wrong thing. Lay the banner over the top edge, or keep its space reserved, so nothing under the pointer moves.

## In real products

- Gmail: while the vacation auto-reply is on, a bar above the inbox says so and offers End now. It’s a mode people forget they switched on. `banner-example-01`
- Notion: a page opened from the trash gets a red bar across the top, with buttons to restore it or delete it for good. `banner-example-02`
- GitHub: an archived repository shows a notice at the top saying it’s read-only, which explains why you can’t push or open issues. `banner-example-03`

## Related entries

[good-edge-cases](good-edge-cases.md), [toast](toast.md)
