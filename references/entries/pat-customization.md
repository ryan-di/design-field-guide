# Customization

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 14 · Newcomers & experts
Live: https://ryan-di.github.io/design-field-guide/#pat-customization
Kind: pattern
Cite as: Design Field Guide v35, #pat-customization

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Customization lets people shape a product around the few things they use most, such as starring a contact, pinning a chat or adding a button to a toolbar. The full list stays as it was, and their own picks sit on top of it, one step away.

It differs from personalization, where the product guesses, like a “Recently used” list that changes by itself. With customization people choose, so it only changes when they change it.

## Ways to do it

There are four common ways, which differ in what people pick: an item to star, an item to pin at the top of a list sorted by date, the buttons a toolbar shows, or the sections of a home screen.

- **Favorites.** Use it when people return to a few items in a long list. Starring adds a copy at the top. The item also stays in its usual place.
- **Pin to top.** Use it in a list sorted by date, so one item doesn’t sink as new ones arrive. Pin a note, then write a new one. The pinned note stays first.
- **Toolbar.** Use it when different people rely on different tools from a large set. Each person keeps the buttons they use and hides the rest. Every tool is still in the menu.
- **Home sections.** Use it for a home screen made of sections that matter more to some people than others. People move the sections they read up, and hide the ones they don’t.

## Rules

Four rules keep customization useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Fix the defaults first

https://ryan-di.github.io/design-field-guide/#pat-customization-rule-1

It’s tempting to leave a weak screen as it is, because “people can set it up themselves”, but most people never do: they keep the screen they were given and work around it. Make the default right for most people first, and offer customization on top for the rest.

### 2. Offer it when it helps

https://ryan-di.github.io/design-field-guide/#pat-customization-rule-2

A setting nobody finds doesn’t help anybody, and few people go looking in Settings. The best moment to offer customization is when someone keeps doing the same thing: after they share with the same person a few times, offer to make that person a favorite, right there.

### 3. Add on top, don’t reorder

https://ryan-di.github.io/design-field-guide/#pat-customization-rule-3

Help articles and support staff say things like “open the third item”. If customizing moves items around in the main list, those directions no longer match what people see. Keep pins in a separate place at the top and leave the full list in its usual order, with “Reset to default” in one obvious place.

### 4. Keep the pinned list short

https://ryan-di.github.io/design-field-guide/#pat-customization-rule-4

Pins are added in a second but often removed only from a settings page, so the pinned section keeps growing until it is as long as the list it was meant to shorten. Let people unpin right where the pin appears, and when nothing is pinned, show an [empty state](https://ryan-di.github.io/design-field-guide/#empty-state) that explains how pinning works.

## In real products

- Notion: add a page to Favorites and it shows up at the top of the sidebar. It also stays in its place in the page tree. `pat-customization-example-01`
- Chrome: the extensions menu lists everything installed. Pin the few you use often and they get their own button in the toolbar. `pat-customization-example-02`
- WhatsApp: pin a few chats and they stay at the top, even when newer messages arrive elsewhere. The rest keep sorting by the latest message. `pat-customization-example-03`

## Related entries

[empty-state](empty-state.md)
