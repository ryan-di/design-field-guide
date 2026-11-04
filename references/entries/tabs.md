# Tabs

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 22 · Containers
Live: https://ryan-di.github.io/design-field-guide/#tabs
Kind: component
Cite as: Design Field Guide v35, #tabs

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Tabs split one thing into a few parts and show one part at a time. A hotel page might have Overview, Rooms and Reviews. The tab names sit in a row with the selected one marked, and picking a tab swaps the panel below it while the rest of the page stays where it is.

Each tab holds different content, where a [segmented control](https://ryan-di.github.io/design-field-guide/#segmented) changes how the same content is shown, such as a list or a grid.

## Forms

Tabs come in three common forms, which differ in who decides what the tabs are and in what each tab remembers. Line tabs split one section of a page, a tab bar holds the main sections of a phone app, and document tabs are ones people open and close themselves, like browser tabs.

- **Line tabs.** Use them when one section of a page has a few parts people read one at a time.
- **Tab bar.** Use it for the three to five main sections of a phone app.
- **Document tabs.** Use them when people open their own items side by side, like web pages.

## Rules

Four rules keep tabs useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Put things to compare side by side

https://ryan-di.github.io/design-field-guide/#tabs-rule-1

Tabs show one panel at a time, so when people need to compare, such as rooms and their prices, they flip back and forth and keep the numbers in their head. That is slow and easy to get wrong. Put the options side by side, or in one table with a column per option, so the eye does the comparing and the answer takes one look.

### 2. Keep to a few tabs

https://ryan-di.github.io/design-field-guide/#tabs-rule-2

Only so many tabs fit in a row, so the rest hide past the edge, often behind a faint fade, and people miss them or scroll sideways to look. For more than about six sections, list them top to bottom in [side navigation](https://ryan-di.github.io/design-field-guide/#side-nav), where every section is visible and the list has room to grow. Or keep a few tabs and put the rarely used sections in a select.

### 3. Use a stepper for steps

https://ryan-di.github.io/design-field-guide/#tabs-rule-3

Tabs tell people they can open them in any order, so when the parts have to happen in order, people jump ahead and only learn at the end that something earlier was needed. A [stepper](https://ryan-di.github.io/design-field-guide/#stepper) shows the order and where people are, and it checks each step before the next one, so nothing fails at the last moment.

### 4. Keep short content on one page

https://ryan-di.github.io/design-field-guide/#tabs-rule-4

When each tab holds a field or two, checking them all costs a click per tab, and people never see the whole thing before they save. On one short page with headings, they check everything at a glance and save with one click.

## In real products

Notice when products use tabs, and what they do instead when there are too many.

- Figma: the right panel splits into Design and Prototype tabs. Both describe the same selection, and people work in one at a time. `tabs-example-01`
- Instagram: a profile has a row of icon tabs for posts, reels and tagged photos, each a different collection from the same person. `tabs-example-02`
- GitHub: a repository’s tabs show counts, like open issues. When the window is narrow, the tabs that don’t fit move into a menu at the end of the row instead of being cut off. `tabs-example-03`
- Slack: preferences have many sections, so they’re a list down the side instead of tabs. `tabs-example-04`

## Related entries

[segmented](segmented.md), [side-nav](side-nav.md), [stepper](stepper.md)
