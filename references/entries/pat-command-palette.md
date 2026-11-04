# Command palette

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 11 · Can’t find it
Live: https://ryan-di.github.io/design-field-guide/#pat-command-palette
Kind: pattern
Cite as: Design Field Guide v35, #pat-command-palette

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A command palette is a search box for actions. People press a shortcut, usually Ctrl+K (⌘K on Mac), type what they want to do and press Enter. They don’t need to know which menu holds the command, only a word for it.

That is what separates it from [search](https://ryan-di.github.io/design-field-guide/#pat-search-filters): search finds things, like a file or an email, and a palette runs commands, like “Export to PDF”. It adds a fast path for people who know what they want, and it doesn’t replace the menus.

## Ways to do it

Palettes differ in what they search and when they open.

- **All commands.** One box for every command in the app, opened with Ctrl+K or ⌘K.
- **Commands and pages.** The same box also finds pages and files.
- **For the selection.** Only the commands that fit the selected item.
- **Slash in text.** Typing “/” at the start of a line opens a short menu of things to add.

## Rules

Four rules keep a command palette useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Give it a visible way in

https://ryan-di.github.io/design-field-guide/#pat-command-palette-rule-1

A palette that opens only with a shortcut is hidden from anyone who doesn’t know the shortcut, so newcomers never find it and keep hunting through menus. Give the palette a button people can see, with the shortcut written on it. Keep the menus too, and show each command’s shortcut there, so people learn the keys over time.

### 2. Match the words people type

https://ryan-di.github.io/design-field-guide/#pat-command-palette-rule-2

People type the word in their head, not the command’s official name. With strict matching, “dark mode” finds nothing when the command is called “Change theme”, and people decide the app can’t do it. Match loosely: letters in order, plus a few synonyms for each command. Show why a result matched, so people learn the real name.

### 3. Name commands as a verb and an object

https://ryan-di.github.io/design-field-guide/#pat-command-palette-rule-3

A palette full of one-word entries is hard to scan: “PDF” and “Export” could each mean several things, so people try them one by one. Name every command as a verb and an object, like “Export to PDF”. Group them, and show recent commands first when the box is empty.

### 4. Use one well-known shortcut

https://ryan-di.github.io/design-field-guide/#pat-command-palette-rule-4

A shortcut that is also a normal key gets in the way of typing: if “/” opens the palette everywhere, people can’t type “and/or” in a note. Use the shortcut most apps share, Ctrl+K (⌘K on Mac), listen for it only where it applies, and never take keys people need for typing.

## In real products

Notice what each palette teaches on the side: a shortcut, the current selection, or where the command lives in the menus.

- VS Code: the Command Palette lists commands with their keyboard shortcuts beside them and puts recently used ones first, so using it slowly teaches the shortcuts. `pat-command-palette-example-01`
- Linear: with an issue selected, ⌘K offers actions for that issue, like changing its status or assignee, each with the one-key shortcut that does the same. `pat-command-palette-example-02`
- Notion: typing “/” in a page opens a menu of blocks you filter by name, so adding a heading or a table never leaves the keyboard. It’s a palette pointed at the things you can add. `pat-command-palette-example-03`
- macOS: the search field in an app’s Help menu finds menu commands by name, and pointing at a result opens the real menu with an arrow on the command, so you learn where it lives. `pat-command-palette-example-04`

## Related entries

[pat-search-filters](pat-search-filters.md)
