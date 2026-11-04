# Stepper

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 23 · Navigation
Live: https://ryan-di.github.io/design-field-guide/#stepper
Kind: component
Cite as: Design Field Guide v35, #stepper

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A stepper, also called a wizard, splits a long task into a few steps in a fixed order, such as Delivery, Payment and Review. A row at the top names the steps, marks the current one and ticks off the ones that are done, so people answer a little at a time and can always see how much is left.

Where [tabs](https://ryan-di.github.io/design-field-guide/#tabs) open in any order and are never finished, a stepper has an order, and each step is done before the next one starts.

## Forms

Steppers come in three common forms. A horizontal stepper names each step in a row across the top. A vertical one stacks the steps and opens the current one in place. On phones, many show only a count and a progress bar.

- **Horizontal.** Use it for three to five steps on a wide screen, like a checkout.
- **Vertical.** Use it when steps need room to explain, or when the page is narrow.
- **Step count.** Use it on phones, or when the task is a run of short questions.

## Rules

Four rules keep steppers useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Let people jump back

https://ryan-di.github.io/design-field-guide/#stepper-rule-1

In a strict stepper, changing one answer means going back through every screen and forward again, which costs so many clicks that people stop checking their answers. Make finished steps clickable, and put an Edit link next to each answer on the review step. If people need to move around freely, use one page with sections instead.

### 2. Give regulars a shortcut

https://ryan-di.github.io/design-field-guide/#stepper-rule-2

A guided path helps the first time, but someone who sends the same invoice every month still has to sit through the welcome screen and every step. Offer [templates](https://ryan-di.github.io/design-field-guide/#pat-templates) or a one-page form next to the guided path, so newcomers keep the guide and regulars finish in a couple of clicks.

### 3. Keep answers on Back

https://ryan-di.github.io/design-field-guide/#stepper-rule-3

Losing answers on Back is the most common stepper bug. People have to choose everything again, and they may miss that a value was reset, like the number of copies going back to 1, and order the wrong number of prints. Hold on to every answer until people finish or cancel the whole task, so checking a step costs nothing and people check more.

### 4. Use as few steps as you can

https://ryan-di.github.io/design-field-guide/#stepper-rule-4

Past about five steps, people lose count of how much is left, and some give up before they pay. Most of the extra screens only confirm an answer that was already picked. Cut steps, merge them, or fill them with [smart defaults](https://ryan-di.github.io/design-field-guide/#pat-smart-defaults) that people can change in one place. Three named steps fit on one line, so the end is always in sight.

## In real products

Notice how each one shows how far along you are and asks for a little at a time.

- macOS Installer: a list on the left names every step from Introduction to Summary and marks the current one, so people always know how much is left. `stepper-example-01`
- Airbnb: listing a home is many short screens grouped into a few big steps, with a progress bar at the bottom. Save & exit keeps the answers so hosts can finish later. `stepper-example-02`
- Duolingo: setup asks one short question per screen, with a progress bar on top. Each screen takes seconds, so the whole thing feels light. `stepper-example-03`
- VS Code: the Get Started walkthrough lists its steps with checkmarks. You can open any step in any order, and finished ones stay ticked. `stepper-example-04`

## Related entries

[pat-smart-defaults](pat-smart-defaults.md), [pat-templates](pat-templates.md), [tabs](tabs.md)
