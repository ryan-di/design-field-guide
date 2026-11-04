# Search with filters

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 11 · Can’t find it
Live: https://ryan-di.github.io/design-field-guide/#pat-search-filters
Kind: pattern
Cite as: Design Field Guide v35, #pat-search-filters

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Search with filters helps people narrow a long list fast, such as products, emails or files. The search box takes words, and filters narrow by kind, like size, date or type. Recent items cover the common case of coming back for something used before.

Unlike a [command palette](https://ryan-di.github.io/design-field-guide/#pat-command-palette), which runs actions, search finds things. It works only when people can see what the search and the filters leave out. Tell screen readers the result count once typing pauses, not on every key.

## Ways to do it

There are four common shapes. Chips and a panel narrow the results, a scope picks where to search, and recents help before anyone types.

- **Filter chips.** A row of toggles above the list.
- **Filter panel.** Groups of checkboxes, each with a count of the items it matches.
- **Search scope.** A choice of where to search, like this folder or everywhere.
- **Recents and suggestions.** Places from before show as soon as the box gets focus, and suggestions narrow as people type.

## Rules

Four rules keep search with filters useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Show what the filters hide

https://ryan-di.github.io/design-field-guide/#pat-search-filters-rule-1

Filters often stay on from an earlier visit, and if people can’t see them, they search, find nothing and decide the item doesn’t exist. Keep active filters in view and show the result count. Say how many matches sit outside the filters, and offer one click to see them.

### 2. Don’t stop at “No results”

https://ryan-di.github.io/design-field-guide/#pat-search-filters-rule-2

An empty page with only “No results” leaves people stuck, because they can’t tell if they misspelled a word, used the wrong term or filtered too much. Repeat what they searched for, offer a close spelling, and offer to clear filters. [Empty state](https://ryan-di.github.io/design-field-guide/#empty-state) covers how “no results” differs from “nothing yet”.

### 3. Start with a few filters

https://ryan-di.github.io/design-field-guide/#pat-search-filters-rule-3

Each filter is one more thing to read, so with fifteen, the filter panel turns into a form and the results drop out of view. Start with three to five filters that match how people already choose, like price and breakfast for a hotel. Put the rest behind “More filters”, and add new ones when people ask for them.

### 4. Show recent items before anyone types

https://ryan-di.github.io/design-field-guide/#pat-search-filters-rule-4

People often search for something they used a short while ago, and an empty box makes them type the name again and remember how it’s spelled. Show recent items as soon as the box gets focus. When filters are on, show only the recent items that fit them.

## In real products

- Spotify: the library has type chips, like Playlists or Artists, above a list sorted by Recents, so “the one I played yesterday” is near the top and “I know it’s an album” is one tap. `pat-search-filters-example-01`
- Airbnb: the button at the bottom of the filter panel says how many places match and updates as you change filters, so you see the effect before you apply it. `pat-search-filters-example-02`
- GitHub: the filters you pick are written into the search box as text, like “is:open label:bug”, so you can always see what’s applied and edit it. `pat-search-filters-example-03`
- Gmail: after a search, chips under the box, like “Has attachment” or a date range, narrow the results with one click, without learning search operators. `pat-search-filters-example-04`

## Related entries

[empty-state](empty-state.md), [pat-command-palette](pat-command-palette.md)
