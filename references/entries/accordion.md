# Accordion

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 22 · Containers
Live: https://ryan-di.github.io/design-field-guide/#accordion
Kind: component
Cite as: Design Field Guide v35, #accordion

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

An accordion is a stack of headers. Each header opens to show the content under it and closes to hide it again, which keeps a long page short when most people need only part of it, like the answers on a help page or the filters in a shop.

Where [tabs](https://ryan-di.github.io/design-field-guide/#tabs) keep their names in a row and show one panel at a time, an accordion keeps its headers in a column, opens each section in place, and can show several at once.

## Forms

Accordions differ in how their sections open and in what a closed header shows. In the most common form, each section opens on its own. In another, opening one section closes the others. In a filter panel, each closed header also shows what’s chosen inside it.

- **Several open.** Use it for a list of separate topics, like the questions on a help page.
- **One at a time.** Use it when people need only one section at a time, as on a phone.
- **Filter panel.** Use it for groups of filters or settings in a narrow side panel.

## Rules

Four rules keep accordions useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Show what people come for

https://ryan-di.github.io/design-field-guide/#accordion-rule-1

Most people open an order page to see when it arrives, so if that sits behind a closed header, every visit costs the same extra click. Show the part people come for as soon as the page loads, either open or above the accordion, and leave behind headers only what few people need.

### 2. Don’t fold what people read in full

https://ryan-di.github.io/design-field-guide/#accordion-rule-2

Some pages are read from top to bottom, like the details of a home before booking it. In an accordion, people open the sections one by one, and a closed header doesn’t show what’s inside. Put it all on one page instead, with headings to guide the eye and a few links at the top that jump to each part.

### 3. Keep it one level deep

https://ryan-di.github.io/design-field-guide/#accordion-rule-3

Each level of nesting costs another click and pushes the content further in, so a setting three levels down is hard to find and people lose track of where they are. Open one level, and group what’s inside with small headings. If that is still too much, split it into separate pages.

### 4. Don’t hide what people must see

https://ryan-di.github.io/design-field-guide/#accordion-rule-4

People read what’s open and skip what’s closed. If a problem sits in a closed section, such as an expired card, the page looks fine and people leave, and they find out later, when something stops working. Show the problem where people look first, with the fix next to it, and keep the accordion for extra detail.

## In real products

Notice what stays open: the part people use most is shown, and the rest folds into headers that open in place.

- VS Code: the Explorer keeps the file tree open and folds Outline and Timeline into headers at the bottom. They open in place when you need them. `accordion-example-01`
- Lightroom Classic: the Develop panel stacks Basic, Tone Curve, Detail and more as sections. Solo mode keeps just one open, so the panel stays short. `accordion-example-02`
- Gmail: in a long thread, older messages shrink to one-line headers and the newest stays open. A count stands in for the ones in between, and any of them opens with a click. `accordion-example-03`
- Google Search: “People also ask” lists related questions. Each one opens in place to show a short answer, so the results page stays short. `accordion-example-04`

## Related entries

[tabs](tabs.md)
