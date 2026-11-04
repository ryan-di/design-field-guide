# Version history

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 9 · Scared to click
Live: https://ryan-di.github.io/design-field-guide/#pat-version-history
Kind: pattern
Cite as: Design Field Guide v35, #pat-version-history

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Version history keeps earlier versions of a document so people can go back to one. A trash does the same for deleted items, which wait there for a while before they’re gone. Both let people make big changes without fear of losing what worked.

Where [undo](https://ryan-di.github.io/design-field-guide/#pat-undo) covers the last few seconds, version history covers days and weeks, and it still works after the app was closed.

## Ways to do it

There are four common forms, which differ in what they cover: a whole document, one value or deleted items.

- **Automatic.** Use it for documents people edit over days. The app saves versions on its own, lists them by time and author, and shows what each one changed.
- **Named.** Use it when some moments matter more than others. People save a version with a name, and it stands out among the automatic ones.
- **One value.** Use it when people care about one value more than the whole document, such as a cell in a spreadsheet. Its own history shows who changed it, when, and from what.
- **Trash.** Use it for anything people delete. Each item in the trash shows how many days it has left.

## Rules

Four rules keep version history useful.

### 1. Name versions by what changed

https://ryan-di.github.io/design-field-guide/#pat-version-history-rule-1

A list of times says when something changed, not what changed, so people open one version after another to find the one they want. Describe each version by its change, such as “Added the menu”. Write that line automatically, and let people rename the versions that matter.

### 2. Restore as a new version

https://ryan-di.github.io/design-field-guide/#pat-version-history-rule-2

If restoring an old version deletes everything newer, one wrong restore loses days of work, and people avoid restoring at all. Add the restored version on top as the newest one, so everything newer stays in the history and the restore itself can be undone.

### 3. Say what restoring will change

https://ryan-di.github.io/design-field-guide/#pat-version-history-rule-3

A time doesn’t say what will happen to the current document, so people restore and then find parts missing that they wanted to keep. Show a short summary of the difference next to the Restore button, such as “Removes 2 slides and brings back the old title”. Put it in text, so screen readers read it too.

### 4. Say when the trash empties

https://ryan-di.github.io/design-field-guide/#pat-version-history-rule-4

A trash that empties without warning removes things people still expect to find, and one that never empties grows until nobody can find anything in it. Empty it after a set time, such as 30 days, say so in the trash itself, and show how long each item has left.

## In real products

- Google Docs: version history lists versions by time and author, and important ones can be named. Restoring one adds it as the newest version, so later edits stay in the list. `pat-version-history-example-01`
- Figma: besides automatic saves, people can save a version with a title and a short description. The history then reads as named milestones, not just times. `pat-version-history-example-02`
- GitHub: a merged pull request has a Revert button. It opens a new pull request that undoes the change, so the history keeps both. `pat-version-history-example-03`
- iPhone Photos: deleted photos wait in Recently Deleted, and each one shows how many days it has left before it’s gone for good. `pat-version-history-example-04`

## Related entries

[pat-undo](pat-undo.md)
