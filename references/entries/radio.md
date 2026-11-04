# Radio group

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 20 · Inputs
Live: https://ryan-di.github.io/design-field-guide/#radio
Kind: component
Cite as: Design Field Guide v35, #radio

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A radio group is a short list of options where people pick exactly one. Every option is visible, so people can compare them before they choose, and picking one clears the one picked before.

Its round buttons say “pick one”, where [checkboxes](https://ryan-di.github.io/design-field-guide/#checkbox) allow any number.

## Forms

Most radio groups are a stacked list. Two or three short options can sit side by side on one line. When each option needs a price or a detail, the options become cards. Picking one option can also open a follow-up field, such as “Tell us more”.

- **List.** Use it for three to six options. One under the other, they’re the easiest to read, and the labels can be as long as they need.
- **Inline.** Use it for two or three short options that fit on one line. Keep each label to a word or two, or the row wraps and gets hard to read.
- **Cards.** Use it when each option needs a price or a short detail to choose well. The whole card responds to a click, not just the small circle.
- **With a follow-up.** Use it when one answer needs more detail. The extra field appears right under that option, and only once it’s picked.

## Rules

Four rules keep radio groups useful.

### 1. Keep it to a few options

https://ryan-di.github.io/design-field-guide/#radio-rule-1

Past about six options, the group becomes a long column: people read down it to find their country, and the Continue button ends up far below. A field that filters as people type, or a [select](https://ryan-di.github.io/design-field-guide/#combobox), keeps the form short, and a few typed letters bring up the right answer.

### 2. Preselect the safe choice

https://ryan-di.github.io/design-field-guide/#radio-rule-2

With nothing picked, people can’t tell if they have to answer. If they skip it, the app has to choose for them, and it may pick the least safe option, like sharing the file with anyone who has the link. Pick the safest common option up front, so skipping still gives a safe result, and if no option is safe, leave it empty and ask for an answer.

### 3. Make long options easy to compare

https://ryan-di.github.io/design-field-guide/#radio-rule-3

When each option is a long sentence, the price, the billing and the rules run together, and people have to read every word to see how two plans differ. Turn each option into a card, with the name and the one fact people compare first, and the details on a short line below.

### 4. Don’t use it to switch views

https://ryan-di.github.io/design-field-guide/#radio-rule-4

Radio buttons look like a form setting, so people expect to press Save before anything changes, and a calendar that jumps to Month the moment they click doesn’t match that. Stacked in a column, the buttons also push the calendar down. For a view that changes at once, use a [segmented control](https://ryan-di.github.io/design-field-guide/#segmented) in the toolbar, like other calendar apps.

## In real products

- Google Calendar: changing a repeating event asks how far the change should reach. This event, the safest choice, is preselected, so a quick OK can’t rewrite the whole series. `radio-example-01`
- Duolingo: the daily goal options are listed together, each with its minutes per day, so people can compare the effort. `radio-example-02`
- Uber: ride options are large rows with a car picture, seats, arrival time and price, and picking one deselects the others. `radio-example-03`

## Related entries

[checkbox](checkbox.md), [combobox](combobox.md), [segmented](segmented.md)
