---
language: Language name (native name)
code: xx
patterns: XX1-XX0
---

# Language pack template

Copy this file to `languages/<code>.md`, where `<code>` matches the `code:` field. Then:

1. Add one row to the registry table in `SKILL.md`.
2. Add one row to the language table in `README.md` and a pattern table using the same `XX1`, `XX2` ids.
3. Run `python3 scripts/validate-package.py`. It checks the frontmatter range against the headings in this file, the registry row, and the README table.

Rules for a good pack:

- Write the rule text in English so the prompt reads consistently, but write every **before/after example in the target language**. Examples translated from English teach the model to translate, which is the failure this structure exists to prevent.
- Only include tells that are specific to this language. Anything already covered by patterns 1-33 belongs in `SKILL.md`, not here.
- Cover register and variety explicitly: which standard is the default, which regional forms exist, and the rule that the skill must never "upgrade" a colloquial or regional register into the standard one.
- Cover the language's own punctuation, quotation marks, numerals, and diacritics.
- List false positives: quoted scripture, poetry, proverbs, fixed formulas, and native rhythms that an English-trained ear misreads as AI.
- Keep the pack under 250 lines.

Delete everything above the first pattern heading when you fill this in, and replace the sections below.

## Register

What the default standard is, which varieties exist, and how to match rather than normalize them.

## What carries over from the core skill

Which of patterns 1-33 need extra force or a different reading in this language.

## Language-specific patterns

### XX1. Pattern name in the target language

**Watch for:** the words and constructions that signal it
**Problem:** why LLM output produces it and why a person usually would not
**Before:** an example in the target language
**After:** the rewrite

## False positives

- Things that look like AI tells in this language but are ordinary human writing.

## Signs of human writing

- What to preserve rather than smooth away.
