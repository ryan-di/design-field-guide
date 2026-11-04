# When you hear this, try that

Design Field Guide v35 (2026-11) · Part 2 · Patterns
Live: https://ryan-di.github.io/design-field-guide/#ch-patterns-cheat
Cite as: Design Field Guide v35, #ch-patterns-cheat

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Start from what people say or do, pick the pattern, then check its trade-off before you build. Each pattern links to its entry.

| If people say… | Try | Watch for |
|---|---|---|
| “There’s too much here.” | [Progressive disclosure](https://ryan-di.github.io/design-field-guide/#pat-progressive-disclosure) | Hidden settings get forgotten |
| “I don’t know what to pick.” | [Smart defaults](https://ryan-di.github.io/design-field-guide/#pat-smart-defaults) | Defaults that are wrong for many |
| “I just want it fast. Or good.” | [Presets](https://ryan-di.github.io/design-field-guide/#pat-presets) | Presets that hide what they change |
| “I’m scared to delete this.” | [Undo](https://ryan-di.github.io/design-field-guide/#pat-undo) | Needs real history in the data model |
| “What will this do?” | [Preview](https://ryan-di.github.io/design-field-guide/#pat-preview) | A preview that differs from the result |
| “I broke it. How do I go back?” | [Version history](https://ryan-di.github.io/design-field-guide/#pat-version-history) | History nobody can read |
| “Did that click work?” | [Instant feedback](https://ryan-di.github.io/design-field-guide/#pat-instant-feedback) | Feedback too fast to notice |
| “Why is this so slow?” | [Optimistic UI](https://ryan-di.github.io/design-field-guide/#pat-optimistic-ui) | Failures that roll back silently |
| “Can I do something else meanwhile?” | [Background work](https://ryan-di.github.io/design-field-guide/#pat-background-work) | People forgetting it’s still running |
| “Where’s that command again?” | [Command palette](https://ryan-di.github.io/design-field-guide/#pat-command-palette) | Invisible to newcomers |
| “I know it’s in here somewhere.” | [Search with filters](https://ryan-di.github.io/design-field-guide/#pat-search-filters) | Filters hiding results |
| “I looked there and didn’t see it.” | [Labels in people’s words](https://ryan-di.github.io/design-field-guide/#pat-information-scent) | Internal names leaking into the UI |
| “Where do I even start?” | [Templates](https://ryan-di.github.io/design-field-guide/#pat-templates) | Anchoring everyone to one way of working |
| “How does this part work?” | [Contextual hints](https://ryan-di.github.io/design-field-guide/#pat-contextual-hints) | Hints piling up |
| “Why won’t it accept that?” | [Constraints](https://ryan-di.github.io/design-field-guide/#pat-constraints) or [forgiving input](https://ryan-di.github.io/design-field-guide/#pat-forgiving-input) | Blocking valid edge cases, or guessing wrong |
| “I lost my work.” | [Autosave](https://ryan-di.github.io/design-field-guide/#pat-autosave) | People not trusting it |
| “This is overwhelming.” / “This is too slow for me.” | [Layered interface](https://ryan-di.github.io/design-field-guide/#pat-layered-ui) | Two layers drifting apart |
| “I do this a hundred times a day.” | [Keyboard shortcuts](https://ryan-di.github.io/design-field-guide/#pat-shortcuts) or [customization](https://ryan-di.github.io/design-field-guide/#pat-customization) | Undiscoverable shortcuts |

Next · Part 3

Patterns describe what should happen, and the next part is about the pieces you build them from. The wrong piece can undo a good pattern: an error in a toast is gone before anyone reads it.
