# Optimistic UI

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 10 · Did it work?
Live: https://ryan-di.github.io/design-field-guide/#pat-optimistic-ui
Kind: pattern
Cite as: Design Field Guide v35, #pat-optimistic-ui

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Optimistic UI shows the result of an action before the server confirms it. The app assumes the action will work, updates the screen at once, and sends the request in the background. If the request fails, it puts things back and says so.

It goes one step further than [instant feedback](https://ryan-di.github.io/design-field-guide/#pat-instant-feedback), which only shows that the action has started: here the result itself shows at once. That suits small actions that almost always succeed, such as a like, a star or a status change.

## Ways to do it

Four kinds of actions often use it, and each needs its own way to show a failure. Tick “Make the next request fail” to see it.

- **Toggle.** Use it for on and off actions, such as liking a song. The heart fills the moment it’s tapped. If saving fails, it empties again on that row, with a reason and Retry.
- **New item.** Use it when people add something, such as a message. It appears in the list at once, slightly faded until it’s saved. If it fails, it stays in place, marked “Not sent”, with Retry.
- **Move.** Use it when people move something, such as a task to Done. The card moves at once. If saving fails, it moves back to where it was, and a line under the board says so.
- **Rename.** Use it when people edit text, such as an album name. The new name shows at once. If saving fails, the old name comes back and the typed name stays in the field, so nothing is lost.

## Rules

Three rules keep optimistic UI honest. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Show failures where they happened

https://ryan-di.github.io/design-field-guide/#pat-optimistic-ui-rule-1

Sometimes the request fails after the screen has changed. If nothing says so, the change quietly vanishes later or looks saved when it isn’t, and people find out much later, when it matters. Roll the change back where people can see it, say what failed, and offer Retry. Announce the rollback in text too, because a heart that empties again is invisible to a screen reader.

### 2. Wait when it matters

https://ryan-di.github.io/design-field-guide/#pat-optimistic-ui-rule-2

Some actions often fail or carry a real cost, like payments or deletes. Showing success at once and taking it back a moment later is worse than waiting, because people may already have closed the app, sure it worked. For these, wait for the server’s answer and show progress. Keep optimism for small, reversible actions that almost always succeed.

### 3. Let the latest request decide

https://ryan-di.github.io/design-field-guide/#pat-optimistic-ui-rule-3

Two quick clicks send two requests, and the answers can come back in the wrong order. If the screen follows whichever answer arrives last, it can show a state the person didn’t choose. Treat the server’s answer as the truth, but let only the latest request decide what’s shown.

## In real products

- Linear: changing an issue’s status, assignee or priority shows at once, and the change syncs in the background. Nothing waits on a spinner. `pat-optimistic-ui-example-01`
- Instagram: the heart fills and the count goes up the moment you tap. `pat-optimistic-ui-example-02`
- iMessage: a sent message appears in the thread at once. If it fails, it stays in place, marked Not Delivered with a red icon, and tapping it offers to try again. `pat-optimistic-ui-example-03`

## Related entries

[pat-instant-feedback](pat-instant-feedback.md)
