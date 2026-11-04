# Select & combobox

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 20 · Inputs
Live: https://ryan-di.github.io/design-field-guide/#combobox
Kind: component
Cite as: Design Field Guide v35, #combobox

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A select shows the current choice in a closed field, and people open it to see the list and pick one option. A combobox adds a text field, so people can type to narrow a long list down.

Where a [radio group](https://ryan-di.github.io/design-field-guide/#radio) shows every option all the time, a select hides them until it’s opened, which saves space but costs a click and makes options hard to compare.

## Forms

There are four common forms. A plain select opens a short list. A combobox adds typing to filter a long list. A multi-select lets people pick several. An autocomplete suggests answers but also accepts text that isn’t in the list.

- **Select.** Use it for about six to fifteen known options, like a language. There’s no search box, so the list has to be short enough to scan.
- **Combobox.** Use it for a long list where people know the name they want, like an airport. Only an item from the list can be picked, so the answer is always valid.
- **Multi-select.** Use it when people pick several, like labels on an email. Each pick shows as a chip with its own remove button.
- **Autocomplete.** Use it when the list helps but can’t cover every answer, like a street address. People can pick a suggestion or keep their own text.

## Rules

Four rules keep selects and comboboxes useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Show short lists in full

https://ryan-di.github.io/design-field-guide/#combobox-rule-1

With only a few options, a dropdown hides them for no reason, and every change takes two clicks. Show them as a [segmented control](https://ryan-di.github.io/design-field-guide/#segmented) or a [radio group](https://ryan-di.github.io/design-field-guide/#radio), so they’re all in view and a change takes one click.

### 2. Make long lists searchable

https://ryan-di.github.io/design-field-guide/#combobox-rule-2

In a long list, people scroll through the whole alphabet to find one name, which is slow and makes it easy to scroll past the one they want. Let people type a few letters to filter. Put the items they use most at the top and group the rest, so common picks are one click away.

### 3. Show previews when looks matter

https://ryan-di.github.io/design-field-guide/#combobox-rule-3

Some options differ in how they look, like themes or photo filters. A name like Atlas or Juno says nothing about that, so people open the list again and again to try each one. Use a gallery or a panel that shows a small preview of each option, so people can compare them side by side and pick once.

### 4. Let people pick several when they need to

https://ryan-di.github.io/design-field-guide/#combobox-rule-4

A single-choice list replaces the old pick without saying so: someone adds a second person, the first one drops off, and they find out only when that person never gets the email. When people may pick several, use checkboxes, or a multi-select that keeps every pick in view.

## In real products

Notice how each product fits the control to the choice: a filter for long lists, previews when looks matter, chips for several picks, and an open list when people compare.

- Linear: fields like status and assignee open a short list with a filter on top. Type a few letters and press Enter, so a change never needs the mouse. `combobox-example-01`
- Google Docs: the font menu writes each font name in its own typeface and keeps recently used fonts at the top. `combobox-example-02`
- Gmail: each recipient in the To field becomes a chip with its own remove button, and typing suggests contacts. `combobox-example-03`
- Uber: ride types are an open list, not a dropdown, so every price and arrival time stays in view. `combobox-example-04`

## Related entries

[radio](radio.md), [segmented](segmented.md)
