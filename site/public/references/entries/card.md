# Card

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 22 · Containers
Live: https://ryan-di.github.io/design-field-guide/#card
Kind: component
Cite as: Design Field Guide v35, #card

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A card is a box that holds one item: a photo album, a home to rent, a product. It shows just enough to tell items apart, such as a picture, a name and a detail or two, so people can scan a set of cards, compare them at a glance, and open one to see the rest.

A row in a list lines up the same details in columns, which is better for comparing dates or prices. A card gives each item room for a picture instead, which helps when people know items by how they look.

## Forms

Cards come in a few forms, and the form decides what a click on the card does. A media card leads with a picture, and a horizontal card puts the picture beside the text, so it fits in a list. A summary card shows a few key figures, like an account balance. A choice card is picked instead of opened, like a plan.

- **Media.** Use it when people know items by their picture, like photos, videos or homes to rent.
- **Horizontal.** Use it when the text matters as much as the picture, like hotels in search results.
- **Summary.** Use it on a home screen to show a few key figures, like an account balance.
- **Choice.** Use it when people pick one option that needs a few details to compare, like a plan.

## Rules

Four rules keep cards useful.

### 1. Give each card one main action

https://ryan-di.github.io/design-field-guide/#card-rule-1

Every button on a card takes space from the name and the picture, so a page of busy cards is hard to scan. Risky actions like Delete also end up next to everyday ones, one slip away. Let a click anywhere on the card open it, and put the rarer actions in one ⋯ menu.

### 2. Put the cards in order

https://ryan-di.github.io/design-field-guide/#card-rule-2

With no order and no dates, every card is a guess, and people open them one by one to find the right one. Sort or group them the way people remember the items, such as newest first for albums, and show the date. For comparing details like photo counts, offer a list view, where the values line up in columns.

### 3. Make the whole card one target

https://ryan-di.github.io/design-field-guide/#card-rule-3

When a card holds several click targets, one inside another, people can’t predict what a click will do: a shop name might open the shop, and a heart might save the item and open it too. Make the card one link that always opens the item, and keep the one extra action, like save, outside that link, so it does only its own job.

### 4. Don’t put everything in a card

https://ryan-di.github.io/design-field-guide/#card-rule-4

Cards are for separate items of the same kind, like albums or homes to rent. When every setting sits in its own box, the page fills with borders and shadows, nothing groups, and the boxes look clickable when they aren’t. Use plain rows under headings, and let [the space between them](https://ryan-di.github.io/design-field-guide/#good-proximity) do the grouping.

## In real products

Notice how little each card shows, and that none has more than one extra action.

- YouTube: each video card is a thumbnail, a title, the channel and how old it is. The whole card opens the video, and other actions wait in one ⋮ menu. `card-example-01`
- Airbnb: every listing card puts the same facts in the same order, photo, place, dates, price, so they’re easy to compare. Saving is the one extra action, a heart on the photo. `card-example-02`
- Trello: a card shows only its title, labels and small badges for things like due date and checklist progress. Open it to see everything else. `card-example-03`
- Spotify: album and playlist cards are mostly cover art. A play button appears on hover, so you can play without opening, and the card stays clean the rest of the time. `card-example-04`

## Related entries

[good-proximity](good-proximity.md)
