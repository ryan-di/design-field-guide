# Error messages

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 4 · Treat the words as the interface
Live: https://ryan-di.github.io/design-field-guide/#good-error-copy
Kind: principle
Cite as: Design Field Guide v35, #good-error-copy

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A good error message says what happened, why if you know, and what to do next, in plain words that don’t blame anyone. People read it at a bad moment, when something they wanted didn’t work, and the message decides whether they fix it in a few seconds or give up.

This entry is about the words. Where the message goes, next to a field or across the page, is covered in [Inline message](https://ryan-di.github.io/design-field-guide/#inline-message) and [Error state](https://ryan-di.github.io/design-field-guide/#error-state).

## Rules

Four rules keep error messages helpful.

### 1. Describe the problem, not the person

https://ryan-di.github.io/design-field-guide/#good-error-copy-rule-1

“You entered an invalid value” tells people they did something wrong, but not what, so they feel blamed and still have to guess the rule. Describe the thing in neutral words and include the rule, like “Quantity needs a number from 1 to 99”, so people can fix it in one try.

### 2. Lead with plain words

https://ryan-di.github.io/design-field-guide/#good-error-copy-rule-2

A code like “Error 0x80070002” means nothing to most people, who can’t tell whether the problem is theirs, the app’s or the network’s, and screen readers read it out one character at a time. Say what happened in plain words first. Keep the code small, or behind “Show details”, for support and developers.

### 3. Offer the next step

https://ryan-di.github.io/design-field-guide/#good-error-copy-rule-3

A message that explains the problem and offers only “OK” leaves people where they started: once it closes, they have to find the fix on their own. Put the action that fixes it on the message, on a button that names it, like “Give Sam access” or “Try again”.

### 4. Match the tone to the stakes

https://ryan-di.github.io/design-field-guide/#good-error-copy-rule-4

Red capitals and words like “fatal” make people think their work is lost. Most errors aren’t like that: the problem can be fixed, or the app will try again on its own. Use calm words that fit what happened, and say what still works: “Your changes are saved on this device.”

## In real products

- VS Code: if a file changed on disk after you opened it, saving stops and says why. The message offers Compare and Overwrite, so both ways forward are right there. `good-error-copy-example-01`
- GitHub: a pull request that can’t merge says the branch has conflicts, lists the files, and puts a Resolve conflicts button right there. No error code, no blame. `good-error-copy-example-02`
- Gmail: a bounced email leads with “Address not found” and one plain sentence about which address failed. The server’s code comes last, in small print, for whoever needs it. `good-error-copy-example-03`
- Google sign-in: a wrong password gets a short, neutral message right under the field, with both ways forward: try again, or reset the password. `good-error-copy-example-04`

## Related entries

[error-state](error-state.md), [inline-message](inline-message.md)
