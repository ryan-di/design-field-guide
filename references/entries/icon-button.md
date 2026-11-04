# Icon button

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 21 · Actions
Live: https://ryan-di.github.io/design-field-guide/#icon-button
Kind: component
Cite as: Design Field Guide v35, #icon-button

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

An icon button is a button that shows a small picture instead of a word: a magnifier for search, an × to close, a heart to like. It fits in tight spaces like toolbars and photo overlays, and suits actions people use again and again.

That is what separates it from a button with a label. A word can be read the first time, but an icon has to be recognized, so it only works for actions people already know or quickly learn.

## Forms

Icon buttons come in four common forms. Plain ones sit in a toolbar and do one thing each. Toggles stay on or off, like bold or mute. A floating button holds the main action on a phone screen, and a More button opens a list of the actions that don’t fit.

- **Plain.** Use it in a toolbar for actions people repeat, like zoom in and out.
- **Toggle.** Use it for something that’s on or off, like bold text.
- **Floating.** Use it for the one main action on a phone screen, like writing a new email.
- **More.** Use it to hold actions people need now and then, like Download or Move to trash.

## Rules

Three rules keep icon buttons useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Label icons people don’t know

https://ryan-di.github.io/design-field-guide/#icon-button-rule-1

Only a few icons mean the same thing to everyone, like search, close, settings and home. Most others, like crop, could mean several things, so people click around to find out, and some never find the right one. Give those buttons a word, and keep bare icons for the few that everyone knows.

### 2. Keep the row short

https://ryan-di.github.io/design-field-guide/#icon-button-rule-2

In a row of ten look-alike icons, every action gets the same weight, so people hover them one by one to find the one they want. Group related icons, give the main action a word, and move rare actions into a More menu, so there is less to scan.

### 3. Make them big enough to hit

https://ryan-di.github.io/design-field-guide/#icon-button-rule-3

A 16 px button is smaller than a fingertip, and with no gap between buttons, one tap covers all three, so people hit Close when they meant Add. Make each button at least 24 px (the WCAG 2.2 minimum), ideally 40 to 44 px, with space between, and keep Close a little apart from the rest.

## In real products

Notice which icons stand alone and which get help: a label, a tooltip with the shortcut, or a menu with words.

- Instagram: like, comment, share and save sit under every post as bare icons. People see them on every post, so they learn them fast and labels would only add clutter. `icon-button-example-01`
- Spotify: each tab at the bottom of the app has a short label under its icon, because a library icon alone could mean many things. `icon-button-example-02`
- VS Code: the activity bar down the side is icons only, but hovering one shows its name and keyboard shortcut. People learn the icon and the faster way at the same time. `icon-button-example-03`
- Gmail: the message toolbar groups its icons into small clusters, and less common actions sit in a More menu with text labels. The row stays short and easy to scan. `icon-button-example-04`
