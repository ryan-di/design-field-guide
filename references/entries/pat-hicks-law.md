# Hick’s law

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 15 · Lean on how people already behave
Live: https://ryan-di.github.io/design-field-guide/#pat-hicks-law
Kind: pattern
Cite as: Design Field Guide v35, #pat-hicks-law

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Hick’s law says that the more choices people see, the longer it takes them to pick one, because each extra option is one more thing to read and compare. The effect is strongest when people don’t know the list yet and have to scan it.

It doesn’t mean a product should offer less, but that it should show the likely choices first and keep the rest easy to reach. When people already know what they want, a search box beats any list. A screen reader reads options one at a time, so a long list costs even more there.

## Rules

Three rules put Hick’s law to work. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Group long lists, or let people search

https://ryan-di.github.io/design-field-guide/#pat-hicks-law-rule-1

In a long flat list, people read item after item until they find theirs, because nothing tells them where to look. Put recent choices first, group the rest, or add search that narrows the list as they type. See [Combobox](https://ryan-di.github.io/design-field-guide/#combobox).

### 2. Make the likely choice stand out

https://ryan-di.github.io/design-field-guide/#pat-hicks-law-rule-2

When every option looks the same, people have to read and weigh all of them, even when one is the usual answer, which slows them down and leads to wrong picks. Make the likely choice stand out: a sensible default, one primary button, the most used item at the top.

### 3. Tuck rare options away, don’t delete them

https://ryan-di.github.io/design-field-guide/#pat-hicks-law-rule-3

Cutting options makes a menu shorter, but someone needed each one, and those people now can’t do their task at all. Keep the common options in view, and put the rare ones behind “More” or in an advanced section.

## In real products

Notice how each one cuts a long list down to a few likely choices before people have to pick.

- Slack: the quick switcher opens with your recent channels and people, and narrows to a few matches as you type. `pat-hicks-law-example-01`
- Photoshop: the toolbar shows one tool from each group. Hold a tool to see its relatives, so dozens of tools fit in one short column. `pat-hicks-law-example-02`
- Duolingo: the home screen is a path with one lesson marked as next. Opening the app leads to one obvious tap, not a menu of lessons. `pat-hicks-law-example-03`

## Related entries

[combobox](combobox.md)
