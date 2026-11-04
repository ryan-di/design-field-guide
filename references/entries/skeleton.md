# Skeleton

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 17 · Loading & progress
Live: https://ryan-di.github.io/design-field-guide/#skeleton
Kind: component
Cite as: Design Field Guide v35, #skeleton

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A skeleton is a gray outline of content that is still loading, with the same boxes and lines as the content that will replace it: a box for each photo, a bar for each line of text. When the content arrives, it drops into place and nothing moves. Unlike a [spinner](https://ryan-di.github.io/design-field-guide/#spinner), which only says “wait”, it shows what is coming and where it will go.

## Forms

Skeletons take the shape of what they stand in for. The common forms are a grid of tiles, a list of rows and a block of text. A fourth, smaller form holds the place of one value on a page that has already loaded.

- **Grid.** Use it for photos, products or videos, with one box for each tile.
- **List.** Use it for rows like messages, songs or orders.
- **Text.** Use it for an article, a description or a review.
- **One value.** Use it when the page is ready but one number or name is still on its way.

## Rules

Four rules keep skeletons useful.

### 1. Match the real layout

https://ryan-di.github.io/design-field-guide/#skeleton-rule-1

A skeleton is there to [hold the space of content that loads late](https://ryan-di.github.io/design-field-guide/#good-edge-cases), so if its shape is wrong, the page still jumps when the content arrives. Give each placeholder the size and place of what will fill it, and if you can’t know the shape in advance, use a spinner instead.

### 2. Skip it when loading is quick

https://ryan-di.github.io/design-field-guide/#skeleton-rule-2

When content arrives almost at once, a skeleton shows for only a split second, too short to read as loading, so people see a flicker and the app feels jumpy instead of fast. As with a [spinner](https://ryan-di.github.io/design-field-guide/#spinner), wait about 400 ms before showing it, so fast content just appears.

### 3. Replace it if loading fails

https://ryan-di.github.io/design-field-guide/#skeleton-rule-3

A skeleton tells people that content is on its way, so if loading fails and it stays, they keep waiting for something that will never come, then reload or give up without knowing why. As soon as loading fails, replace it with what went wrong and a way to try again.

### 4. Keep the motion calm

https://ryan-di.github.io/design-field-guide/#skeleton-rule-4

Fast shimmer on every part of the screen is tiring to look at, and it covers parts that are already known, like the account name, so nothing can be read until everything arrives. Show what you have at once and load the most important part next. Give only the parts still loading a slow, soft pulse, and stop it for people who turn off motion.

## In real products

- YouTube: the home page first shows gray boxes where thumbnails go and bars where titles go, so the videos drop in without moving anything. `skeleton-example-01`
- Facebook: the feed shows gray posts before the real ones arrive, with a circle for the profile photo and bars for the name and text. `skeleton-example-02`
- Google Photos: when you scroll fast, each photo’s spot is held by a plain tile of the right size and shape. Photos fill in where they belong, so the grid doesn’t reflow. `skeleton-example-03`

## Related entries

[good-edge-cases](good-edge-cases.md), [spinner](spinner.md)
