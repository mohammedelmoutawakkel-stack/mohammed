# Baseline prompts

Three fixed prompts for reviewing this guide against a new model. See
"Reviewing this guide against a new model" in `SKILL.md` for what to do with the
output.

They cover the three length modes the guide calibrates to, because the tells
differ by length. One is Swedish, so patterns 37 to 41 get exercised too.

Keep the wording frozen. The point is to compare models, not prompts. If a
prompt has to change, note it in the log below and treat everything before the
change as a separate baseline.

## How to run them

**Run each one in a clean context.** No CLAUDE.md, no skills loaded, no prior
turns, no system prompt of your own. A fresh chat on claude.ai, or a directory
with no CLAUDE.md in it.

This matters more than it sounds. Stefan's global CLAUDE.md says "answer in
Swedish" and "keep answers concise", and both instructions change the output
enough to invalidate the comparison. You are measuring what the model does when
nobody has told it anything.

**Do not mention this skill, humanizing, AI writing patterns, or "write
naturally".** Any of those turn the test into a test of instruction following.

Paste the prompt, take the first response, change nothing. A second attempt is a
different measurement.

---

## 1. Long, English, personal

> Write a 900 word blog post, first person, about a side project I paused after
> three weeks. It was a price index for the Swedish second hand board game
> market, built to find out whether there was money in buying and selling used
> games. The answer turned out to be no: the median sale was 130 kronor, only
> about half of everything listed sells at all, and almost nothing published
> after 2020 changes hands in any volume. Cover what I built, what the data
> said, and what I would do differently.

Exercises: significance inflation, manufactured suspense, generic positive
conclusions, rule of three, em dashes, corporate compounds, whether it can hold
a first person voice without narrating its own structure.

## 2. Short, Swedish, social

> Någon har kommenterat mitt LinkedIn-inlägg om att jag lämnat anställningen för
> att bygga eget: "Vad kul Stefan! Vi hörs snart, jag är nyfiken på vad du
> bygger." Skriv mitt svar.

Exercises: Swedish LinkedIn voice, over-formal register, translated English
idiom, connector stacking, imported dash typography. Also the length
calibration: a good answer is one or two lines, and producing a paragraph is
itself the finding.

## 3. Functional, English, documentation

> Write the "Getting started" section of a README for a small command line tool
> that reads a CSV of expenses and prints a monthly summary. It runs on Node,
> installs with one command, and has a handful of subcommands.

Exercises: signposting, fragmented headers, boldface overuse, inline-header
vertical lists, title case in headings, decorative emojis, filler around code
blocks.

---

## Log

Record every review here. Model, date, and what changed in the guide as a
result. A pattern retired in one generation can return in the next, and knowing
when it was last seen is the difference between a judgement and a guess.

| Model | Date | Patterns that fired | Patterns that stayed quiet | Changes made |
|---|---|---|---|---|
| Fable 5.1 | 2026-08-26 | **P1:** #10 structural (four times: title, "three numbers", "three lessons", closing list), #9 (five instances), #25 (redemptive close), #28 narrative form and #31 paragraph form, both clear. **P2:** #20 hard (a full paragraph offering variants and a style-learning service), length mode failed (40 words for an 11-word comment), #41 mild ("ett samtal"). **P3:** nothing from the list. | #7, #14 (zero dashes in 900 words), #15, #17, #26, #37 (one 40-word Swedish sample, thin). | Status lines on the six quiet patterns. Structural paragraph added to #10. Narrative form and deletion test added to #28. Paragraph-level form added to #31. New #36 invented particulars. |

Pattern numbers in this row follow the guide as of v2.12.0, after the rebase
onto upstream v2.11.2. The review was originally written against the local
numbering where these were #30, #36 and #37.

**Caveat on run 1.** All three prompts were pasted into one chat, in order. P3
therefore saw the Swedish P2 before it ran, which is the only explanation for
`Bokföringsdag` and `kr` appearing in a README the prompt never localised. P1
was first and is clean. P2 saw P1. Treat P3's clean result as suggestive, not
established, and rerun it alone before retiring anything on its account.

**Reviewer note, and its resolution.** The review was done by Fable 5.1 reading
Fable 5.1, so the three patterns it found were flagged as unconfirmed. They are
now confirmed. Between the local review and the rebase, upstream independently
added "forced punchlines and dramatic fragments", "formulaic sayings", a
casual-register extension of "announcing the next point", and a no-fabrication
rule, from other people reading other text. Three of the same findings, the same
week, from writers who had not seen ours. That is the confirmation the note
asked for.

**Next run:** each prompt in its own fresh chat. No exceptions.
