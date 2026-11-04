# Forgiving input

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 13 · Prevent, explain, recover
Live: https://ryan-di.github.io/design-field-guide/#pat-forgiving-input
Kind: pattern
Cite as: Design Field Guide v35, #pat-forgiving-input

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Forgiving input accepts a value in the ways people actually write it. “1024 x 768”, “1024×768” and “1024 by 768” all mean the same size, so the field reads all of them. It cleans up spaces, symbols and units on its own, and it shows how it read the input.

Where a [constraint](https://ryan-di.github.io/design-field-guide/#pat-constraints) limits what people can enter, forgiving input lets them enter a value their way and does the translating. Both prevent the same thing: an error about formatting that any person would have understood.

## Ways to do it

A field can forgive in a few ways. It can accept several formats for the same value. It can clean up formatting, such as spaces and dashes. It can notice a likely typo and offer the fix. It can read plain words, like “tomorrow 9am”. Each way shows the result, so people can check it.

- **Many formats.** Use it for values people write in different ways, like amounts.
- **Clean-up.** Use it for values full of spaces, dashes and brackets, like phone numbers.
- **Typo fix.** Use it when a small slip is likely and costly, like a mistyped email domain.
- **Plain words.** Use it for dates and times, where people think in words.

## Rules

Four rules keep forgiving input useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Show how you read it

https://ryan-di.github.io/design-field-guide/#pat-forgiving-input-rule-1

A field that guesses can guess wrong, and if it says nothing, people find out later, when the parcel costs seven times as much or the wrong thing arrives. Show the reading next to the field, in words, before the value is used, so a wrong guess is caught on sight.

### 2. Ask only when it could mean two things

https://ryan-di.github.io/design-field-guide/#pat-forgiving-input-rule-2

Most input has one obvious reading, and asking about it only slows people down. Some input really could mean two things, like “7” for a time, and a field that quietly picks one is sometimes wrong without anyone noticing. Take the obvious reading when there is one, and ask only in the real two-way cases, with each answer one click away.

### 3. Forgive the same way everywhere

https://ryan-di.github.io/design-field-guide/#pat-forgiving-input-rule-3

When one field accepts “12m 30s” and the next one rejects it, people can’t learn what works, so they fall back to the strictest format everywhere or give up on the shortcuts. Put the reading of times, sizes and amounts in one shared function and use it in every field, so a format that works once works everywhere.

### 4. Say when the value itself changes

https://ryan-di.github.io/design-field-guide/#pat-forgiving-input-rule-4

Cleaning up spaces or a “cm” is harmless, so do it without comment. Changing the number is different, because people get something they didn’t ask for. When you round to the nearest valid value, say so, and when the value is far outside what’s possible, refuse it and give the limit instead of picking one.

## In real products

- Google Search: a misspelled search still gets results, with a line saying what it searched for instead and a link to search exactly what you typed. `pat-forgiving-input-example-01`
- Figma: size and position fields accept math, so typing “120*2” sets the width to 240 without leaving the field to work it out. `pat-forgiving-input-example-02`
- Todoist: as you type a task like “Call Sam tomorrow at 3pm”, the date words are highlighted and turned into a due date, so you see what it understood before you save. `pat-forgiving-input-example-03`
- Gmail: paste a list of addresses separated by commas or semicolons into the To field, and each one becomes its own recipient. `pat-forgiving-input-example-04`

## Related entries

[pat-constraints](pat-constraints.md)
