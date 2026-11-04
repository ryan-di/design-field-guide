# Toolkit

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 31 · One problem, start to finish
Live: https://ryan-di.github.io/design-field-guide/#eff-toolkit
Kind: workflow
Cite as: Design Field Guide v35, #eff-toolkit

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Design work has separate jobs: frame the problem, gather context, explore, decide, build, check and share. Each job has a tool that fits it, and splitting the work by job keeps each step small enough to check, with a result the next step can use.

One long chat can do all of it, but then the decisions are buried and nobody can check them. Whatever the agents make, the brief, the decision and the pull request’s list of behaviors should read as yours, because you’re the one answering for them.

- **Frame the problem** (Linear, Claude Code): Write the brief in the Linear ticket: who, what they’re trying to do, what stops them. Claude Code can draft it from threads you paste in. For the tab-close problem: one paragraph naming people who tidy tabs and lose changes, with a “done when” line.
- **Gather context** (Claude Code, Figma connector, Linear): Send Claude Code subagents in parallel to read the repo and past tickets. Pull frames and tokens from Figma through its connector. For the tab-close problem: a one-page pack: how tabs close, how saving works, related tickets, the tab frames.
- **Explore directions** (Claude Code, Claude artifacts): Ask subagents for clearly different directions, one each, and put them side by side on one artifact page. For the tab-close problem: ask on close, close then Undo, and keep a draft.
- **Prototype** (Claude artifacts, Claude Code): Make a clickable page as an artifact and share the link. If it needs the real app, prototype in a git worktree instead. For the tab-close problem: a page where you close a tab and see each direction play out.
- **Decide** (Claude artifacts, Linear): Score the options against criteria from the brief on a shared page. Record the decision and why in the ticket. For the tab-close problem: C, with B’s Undo, once “never loses work” counted twice.
- **Build** (Claude Code): Start in plan mode and agree on the plan. Then build in a worktree, so several agents can work at once without clashing. For the tab-close problem: one worktree, draft on close, restore on reopen, Undo toast.
- **Check** (Vitest, Playwright, Claude Code): Vitest for the logic, Playwright for the flow people use, with screenshots. Claude Code can run both and report what failed. For the tab-close problem: three unit tests for the draft, two end-to-end specs for close and reopen.
- **Review** (GitHub PRs, Claude Code): Open a GitHub PR that leads with what changes for people, then the checks. Claude Code can read review comments and make the fixes. For the tab-close problem: reviewers checked the behavior list first, then the code.
- **Share** (Claude artifacts, Linear, GitHub PRs): Publish a short artifact page with before and after, and link it from the ticket and the PR. For the tab-close problem: a before and after page linked from the ticket, so support knows what changed.

## Rules

Four rules keep the tools working for you.

### 1. Split the work by job

https://ryan-di.github.io/design-field-guide/#eff-toolkit-rule-1

One chat asked to explore, decide and build does all three at once: it builds the first idea, and the choice between directions is never made in the open. Explore with parallel subagents, decide on a shared page, then build in a worktree with tests, so each step leaves something you can check.

### 2. Read the real design values

https://ryan-di.github.io/design-field-guide/#eff-toolkit-rule-2

A screenshot shows how a design looks, not the values behind it. An agent that rebuilds from one guesses the colors, spacing and corner radius, and each guess is a little off. Read the frames and tokens through the Figma connector instead, so the build uses the same values as the design.

### 3. Ask for a test that fails first

https://ryan-di.github.io/design-field-guide/#eff-toolkit-rule-3

An agent says “done” when the code runs, not when the behavior works, so if you take that on trust, the bug turns up when someone uses it. Ask for a test that fails before the change and passes after, then run the Playwright specs that touch the changed screens.

### 4. Share a link people can click

https://ryan-di.github.io/design-field-guide/#eff-toolkit-rule-4

A screen recording shows one path, at the pace of whoever made it. People can’t try the other buttons, so their questions stay open. Publish the prototype as an artifact link people can click through, and link it from the ticket so it’s still there next week.

## In real products

Notice that each tool does one job well and hands its result to the next, instead of one tool doing everything.

- Linear: the issue holds the problem and the plan. When a branch or pull request names the issue, Linear links them and moves the issue along as the PR opens and merges, so the plan follows the code without anyone updating it. `eff-toolkit-example-01`
- Figma: designers mark frames “Ready for dev”, and the build takes its exact spacing, colors and variables from Dev Mode instead of guessing them from a screenshot. `eff-toolkit-example-02`
- Vercel: a bot posts a preview link on every pull request, and each new push updates it, so the link people click always shows the latest build. `eff-toolkit-example-03`
- GitHub: a pull request gathers a separate tool for each check, like tests, lint, a preview and visual review, so each job reports its result in one place. `eff-toolkit-example-04`
