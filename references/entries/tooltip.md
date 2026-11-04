# Tooltip

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 18 · Overlays
Live: https://ryan-di.github.io/design-field-guide/#tooltip
Kind: component
Cite as: Design Field Guide v35, #tooltip

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A tooltip is a small label that appears when people point at something or move to it with the keyboard. It answers a quick question, like what an icon button does. It goes away as soon as the pointer or focus moves on.

Where a tooltip only adds a name or a short note, with nothing in it to click, a popover opens on a click, stays open and can hold buttons and links.

## Forms

Most tooltips name an icon button, and some also show its keyboard shortcut. Others explain a word in one short sentence, or show the full text of a name that is cut off. All of them hold a few words of plain text and nothing else.

- **Name.** Use it for icon buttons that have no text.
- **With shortcut.** Use it when the button also has a keyboard shortcut.
- **Explanation.** Use it to explain a word some people won’t know, in one short sentence.
- **Full text.** Use it when a long name is cut off to fit.

## Rules

Four rules keep tooltips useful.

### 1. Don’t rely on hover

https://ryan-di.github.io/design-field-guide/#tooltip-rule-1

Phones and tablets have no hover, so a tooltip there never appears, and people decide without the information, such as what an extra fee pays for. Put the text on the page where people can see it. If there isn’t room, add an info button that opens a popover when tapped, which works the same with a finger, a mouse or a keyboard.

### 2. Don’t hide what people must know

https://ryan-di.github.io/design-field-guide/#tooltip-rule-2

Most people never point at a small info icon, so if a warning hides there, they find out what the setting does only when their old messages are already gone. Put anything people need for a decision on the page, as helper text right under the choice.

### 3. Don’t put links or buttons in it

https://ryan-di.github.io/design-field-guide/#tooltip-rule-3

A tooltip closes as soon as the pointer moves off the icon, and the keyboard can’t move into it, so a link inside can be seen but not used. When the note needs a link, use a popover instead. It stays open until people close it, so they can reach the link with a mouse, a finger or the Tab key.

### 4. Don’t repeat the label

https://ryan-di.github.io/design-field-guide/#tooltip-rule-4

A tooltip that repeats a visible label tells people nothing new, but it still pops up over nearby content, such as the price next to the button, and screen readers read the same words twice. If the label already says it, leave the tooltip out.

## In real products

Notice that tooltips only add a name or a detail, and that on touch screens the name has to be visible instead.

- Figma: hovering a tool shows its name and its key, like Rectangle R. The toolbar stays compact, and the key teaches a faster way for next time. `tooltip-example-01`
- GitHub: relative times like “3 days ago” show the exact date and time on hover. Most people only need the rough age, and the precise one is there for those who wonder. `tooltip-example-02`
- Spotify: the phone app has no hover, so its tab bar puts a word under each icon instead of hiding the names in tooltips. `tooltip-example-03`
