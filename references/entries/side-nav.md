# Side navigation

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 23 · Navigation
Live: https://ryan-di.github.io/design-field-guide/#side-nav
Kind: component
Cite as: Design Field Guide v35, #side-nav

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A side navigation is a list of an app’s main places, down the left edge: Home, Documents, Shared, Settings. People use it to move between those places, and it always marks the one they’re in. It stays in the same spot while the page beside it changes.

Where [tabs](https://ryan-di.github.io/design-field-guide/#tabs) split one thing into parts, like the details and the reviews of a product, a side navigation moves between separate areas of the app, and it can hold more of them.

## Forms

Side navigation comes in four common forms. A full sidebar shows an icon and a label for each place. A nested one lets places open to show their own pages. A rail is a narrow strip of icons with short labels, for pages that need the width. On phones, the list moves into a drawer that opens over the page.

- **Full.** Use it when the app has a handful of main areas and the screen has room.
- **Nested.** Use it when areas have their own pages, like a help center or a big settings page.
- **Rail.** Use it when the page needs most of the width, like a photo grid or a map.
- **Drawer.** Use it on phones, where there’s no room to keep the list open.

## Rules

Four rules keep side navigation useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Keep it to places

https://ryan-di.github.io/design-field-guide/#side-nav-rule-1

People read every item in the sidebar as a place to go, so when one of them runs an action instead, like New folder, pressing it takes them away from the page they were on. The new folder then lands somewhere else, and they have to go looking for it. Put actions on buttons in the page, where they act on what people are looking at.

### 2. Group long lists

https://ryan-di.github.io/design-field-guide/#side-nav-rule-2

When every area sits in one long list, all of them look equally important, so people read the whole list each time, and daily work sits next to setup pages they open once a year. Group items under short headings so people can skip to the right group, fold away the groups people rarely need, and move setup pages into Settings.

### 3. Show labels with icons

https://ryan-di.github.io/design-field-guide/#side-nav-rule-3

Most icons don’t say what they are, so with icons alone people point at one after another to read the tooltips, and next time they do it again. A short label with each icon lets them find a place at a glance and remember it. If space is tight, let the rail expand to show the labels. Icons alone can work in a tool people use all day, like VS Code, where there are few icons to learn and the open view’s name heads the panel beside them.

### 4. Mark the current place

https://ryan-di.github.io/design-field-guide/#side-nav-rule-4

If nothing in the sidebar is marked, people have to work out where they are from the page, and when the page title also uses different words from the item, they can’t match the two at all. Highlight the current item and give the page the same name, so people can tell where they are from either side of the screen.

## In real products

Notice how each one marks the current place and makes room for more items.

- Gmail: the open folder gets a filled background and bold text, unread counts sit beside each name, and rarely used labels wait under More. Compose is a button above the list, not a place in it. `side-nav-example-01`
- Slack: channels sit in sections you can name and collapse. Unread channels turn bold and the open one is highlighted, so a long list stays easy to scan. `side-nav-example-02`
- VS Code: the activity bar is icons only, but the active view is marked on its edge and its name heads the side bar. Badges add counts, like changed files. `side-nav-example-03`
- YouTube: on narrower windows the side menu shrinks to a rail but keeps a short label under each icon, so places stay findable without hovering. `side-nav-example-04`

## Related entries

[tabs](tabs.md)
