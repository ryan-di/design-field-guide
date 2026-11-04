# Breadcrumbs

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 23 · Navigation
Live: https://ryan-di.github.io/design-field-guide/#breadcrumbs
Kind: component
Cite as: Design Field Guide v35, #breadcrumbs

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Breadcrumbs are a short line of links above a page title, like My drive / Family / Holidays. They show where the page sits in a structure, from the top level down, and let people jump to any level above in one click.

A Back link goes up one level at a time. Breadcrumbs show every level at once, so people can skip several in one go.

## Forms

Most breadcrumbs show the full path, with a link for each level. Some add a small menu after each level, so people can move sideways to a neighbor as well as up. On phones, many show only the level above.

- **Full path.** Use it when pages sit three or more levels deep, like folders or a shop’s departments.
- **With menus.** Use it when people often move between neighbors, like cities in one country.
- **Parent only.** Use it on phones, where a full trail would wrap onto several lines.

## Rules

Three rules keep breadcrumbs useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Skip them in flat structures

https://ryan-di.github.io/design-field-guide/#breadcrumbs-rule-1

With only one or two levels, the trail mostly repeats the page title: one more line to read that doesn’t take people anywhere new. A clear title says where people are, and a Back link covers the one way up.

### 2. Show location, not history

https://ryan-di.github.io/design-field-guide/#breadcrumbs-rule-2

A trail made of the pages people visited changes every time and says nothing about where the page belongs, so finding more things like it means starting again from the top. Leave the visited pages to the Back button, and make the trail show where the page sits in the structure, so its category is one click away however people got there.

### 3. Shorten long paths

https://ryan-di.github.io/design-field-guide/#breadcrumbs-rule-3

A deep path wraps onto a second line and pushes the page down, and people have to read every level to find the one they want. Keep the top level and the current one, and put the middle behind a “…” button, where the middle levels are still one click away.

## In real products

Notice that every level above the page is one click away, and that long paths get shortened in the middle.

- GitHub: above a file, the path names the repository and each folder down to the file. Every folder is a link and the file name is plain text, so you can jump up any number of levels in one click. `breadcrumbs-example-01`
- Notion: the top bar shows where a page lives. When the path gets deep, the middle levels fold into “…”, which lists them when clicked, so the first and last levels stay readable. `breadcrumbs-example-02`
- Windows File Explorer: each folder in the address bar is a button, and the arrow after it lists that folder’s subfolders. You can jump up, or up and across, in one move. `breadcrumbs-example-03`
- Amazon: a product page shows its category trail, like Electronics › Headphones. It shows where the product sits in the store, not how you got there, and each level opens a broader category. `breadcrumbs-example-04`
