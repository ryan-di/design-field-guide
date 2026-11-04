# Progressive disclosure

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 8 · Too much at once
Live: https://ryan-di.github.io/design-field-guide/#pat-progressive-disclosure
Kind: pattern
Cite as: Design Field Guide v35, #pat-progressive-disclosure

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Progressive disclosure shows the settings most people need first and keeps the rest one step away, so people can start without judging every option on the screen. Nothing is removed: the rest is there for the people who look for it.

It works together with [smart defaults](https://ryan-di.github.io/design-field-guide/#pat-smart-defaults), but where a default fills in a value for people, progressive disclosure decides what they see at all. Hidden settings should start on good defaults, so most people never need to open them.

## Ways to do it

There are four common ways to keep the rest one step away. They differ in where the hidden part waits.

- **Show more.** Use it when a few extra fields belong with the basics in one form. The button names what’s behind it.
- **Sections.** Use it when there are many settings in a few clear groups. Closed sections still show their names, so people can scan for the one they need.
- **Separate page.** Use it for settings few people change, which need room of their own. It costs a page change, so make the way back obvious.
- **When relevant.** Use it when some options only matter after an earlier choice. Pick “Choose days” and the days appear.

## Rules

Four rules keep progressive disclosure useful.

### 1. Say what’s hidden

https://ryan-di.github.io/design-field-guide/#pat-progressive-disclosure-rule-1

A button that says only “More options” gives no hint of what’s behind it, so people who need one of those settings don’t know it exists, and they give up or ask someone. Name what’s inside on the button and say how many, so people can tell whether it’s worth opening before they open it.

### 2. Let experts skip the extra click

https://ryan-di.github.io/design-field-guide/#pat-progressive-disclosure-rule-2

People who use the hidden settings every time pay for the split every time, and if the section closes again after each use, they open it over and over. Remember whether each person left it open, and give frequent users a keyboard shortcut or a setting to always show everything.

### 3. Split by what people change

https://ryan-di.github.io/design-field-guide/#pat-progressive-disclosure-rule-3

The line between basic and advanced is often a guess made before launch. If most people open the hidden part every time, the guess was wrong, and the split only adds a click. Look at what people actually change, and move anything most people need up into the basics.

### 4. Show what the hidden settings changed

https://ryan-di.github.io/design-field-guide/#pat-progressive-disclosure-rule-4

A hidden setting can still change the result, and people can’t fix a cause they can’t see. While the section is closed, show a short summary of every value that isn’t the default, and let people clear it from there. The most common case, a filter left on from an earlier visit, is covered in [search with filters](https://ryan-di.github.io/design-field-guide/#pat-search-filters).

## In real products

- Gmail: the search box is a single field. An icon in it opens fields for sender, subject and date, for the few searches that need them. `pat-progressive-disclosure-example-01`
- Lightroom: sliders are grouped into sections like Light and Color that open and close. Closed sections still show their names, so people know what’s inside. `pat-progressive-disclosure-example-02`
- VS Code: the settings editor opens on a short Commonly Used list. Every other setting is a search away, and experts can edit the settings file directly. `pat-progressive-disclosure-example-03`
- Google Maps: directions show the fastest route at once. Choices like avoiding tolls or highways wait in route options, for the trips that need them. `pat-progressive-disclosure-example-04`

## Related entries

[pat-search-filters](pat-search-filters.md), [pat-smart-defaults](pat-smart-defaults.md)
