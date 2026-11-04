# What design engineering is

Design Field Guide v35 (2026-11) · Start here · Two definitions
Live: https://ryan-di.github.io/design-field-guide/#design-engineering
Kind: principle
Cite as: Design Field Guide v35, #design-engineering

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A design engineer designs in the material the product is made of: code. Instead of handing over pictures, they build the thing, try it, and change it until it works.

The role exists because many design decisions only show up when something runs. How long should a spinner wait before it appears? What happens to a 40-character name? Where does focus go when a dialog closes? A mockup rarely answers these, but a prototype in code answers them in minutes.

- **Prototypes**: Quick working versions that answer a design question, so the team decides on evidence instead of opinions.
- **The details**: States, timing, motion, edge cases and the keyboard path. Mockups skip them, but people notice all of them.
- **What ships**: Keeping what was designed and what ships the same, through components, tokens and review of the built thing.

It sits between two roles that already exist. The three differ mostly in where each one starts and what each one is judged on.

|  | Designer | Design engineer | Frontend engineer |
|---|---|---|---|
| Starts from | A problem and the people who have it | A design question, or a design that has to work for real | A spec and a codebase |
| Produces | Flows, mockups, the design system | Working prototypes, interface details, components | Features that ship, are tested and can be maintained |
| Judged on | Whether it solves the right problem clearly | Whether the built thing feels as intended, in every state | Whether it works, is fast and lasts |

The rest of the book follows that work, from judging the problem to shipping the solution.
