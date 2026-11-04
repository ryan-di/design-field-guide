# Empty state

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 24 · States
Live: https://ryan-di.github.io/design-field-guide/#empty-state
Kind: component
Cite as: Design Field Guide v35, #empty-state

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

An empty state is what a screen shows when there’s nothing in it: no albums yet, no search results, no tasks left. Instead of a blank space, it says what belongs here and how to get the first one.

Loading means content is on its way, and an [error](https://ryan-di.github.io/design-field-guide/#error-state) means something failed. Empty means everything worked, and there’s nothing to show.

## Forms

Empty states come in three common kinds, set by why the screen is empty: first use, no results and all done. Each kind needs different words and a different action.

- **First use.** Use it when people haven’t added anything yet.
- **No results.** Use it when a search or filter matched nothing.
- **All done.** Use it when people cleared the list themselves, like an inbox or today’s tasks.

## Rules

Three rules keep empty states useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Say what goes here

https://ryan-di.github.io/design-field-guide/#empty-state-rule-1

“No items” doesn’t say what belongs on the screen or how to add it, so people have to find the small + in the corner on their own. Name what will show up here, and put the button for the first one inside the empty space, where it takes one press.

### 2. Offer one way to start

https://ryan-di.github.io/design-field-guide/#empty-state-rule-2

Five equal buttons make a new person stop and compare them, and none of them looks like the place to start. Give one main action, and at most one quieter one beside it, such as a link to [templates](https://ryan-di.github.io/design-field-guide/#pat-templates) for people who look for them.

### 3. Match the message to the cause

https://ryan-di.github.io/design-field-guide/#empty-state-rule-3

If an empty search and an unstarted wishlist both say “No items”, people can’t tell which problem they have, and a search that’s too narrow needs a different fix than a list that’s new. For no results, name the filter and offer to clear it. For first use, explain how to add the first item.

## In real products

Notice that each empty screen says what belongs there and puts the first step inside the empty space.

- GitHub: a new, empty repository shows the setup commands to copy, so the first push is one paste away. `empty-state-example-01`
- Trello: on a new board, the spot where the first list will go is itself the Add a list button. `empty-state-example-02`
- Spotify: a new, empty playlist puts a song search right where the songs will appear, so adding the first one doesn’t mean going anywhere else. `empty-state-example-03`
- Gmail: a search with no results says nothing matched and points to search options like sender and date. It’s a no-results state, not a first-use one, so it helps you change the search. `empty-state-example-04`

## Related entries

[error-state](error-state.md), [pat-templates](pat-templates.md)
