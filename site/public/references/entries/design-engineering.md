# Design when agents build

Design Field Guide v35 (2026-11) · Start here · Two ideas
Live: https://ryan-di.github.io/design-field-guide/#design-engineering
Kind: principle
Cite as: Design Field Guide v35, #design-engineering

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Agents can turn a clear description into working code in minutes. Building used to be the slow, costly part of making a product. Now the slow part is knowing what to ask for, and seeing what’s wrong with what comes back.

The details matter as much as ever. How long should a spinner wait before it appears? What happens to a 40-character name? Where does focus go when a dialog closes? An agent answers each of these with a guess, most often the common choice, and the guess usually looks fine in a demo. Whether it fits your product is a design call, and you can only make it if you know what good looks like.

- **What to build**: A problem and a behavior clear enough that an agent builds the right thing, not only a working one.
- **What good looks like**: States, timing, motion, edge cases and the keyboard path. Agents skip them unless asked, and people notice all of them.
- **Whether it’s right**: Checking the built thing in every state, because a build can pass every test and still feel wrong.

The work splits by what each side is good at. The agent is fast at what can be written down, and you own what needs judgment.

|  | You | The agent |
|---|---|---|
| Starts from | A problem and the people who have it | Your brief and the codebase |
| Produces | The brief, the decisions and the review | Plans, prototypes and code |
| Judged on | Whether the right problem is solved, in every state | Whether the result does what the brief asks |

Parts 1 to 3 train that judgment: what makes a product and its interactions good, and why. Part 4 puts it to work with agents, from framing the problem to shipping the solution.
