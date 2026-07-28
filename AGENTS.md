# AGENTS.md

Guidance for AI coding agents (Claude Code, Codex, Warp, etc.) working in this repository.

## What this repo is

A portable agent skill implemented entirely as Markdown. The runtime artifact is `SKILL.md`: the agent reads its YAML frontmatter and editor prompt. There is no build step, and the repo should avoid wording that limits support to one or two harnesses.

## Key files

- `SKILL.md` — the skill itself. Portable YAML frontmatter (`name`, `description`, `license`, `metadata.version`) followed by the canonical, numbered pattern list (words to watch, one-line problem, and compact inline examples for the highest-value patterns). **This is the source of truth.**
- `references/examples.md` — the full before/after example for every one of the 33 patterns, under `## N. <name>` headings matching `SKILL.md`'s numbering exactly. Loaded on demand, not part of the always-resident skill body.
- `README.md` — for humans: installation, usage, a summary table of the patterns, and a version history.
- `.claude-plugin/plugin.json` — optional Claude Code plugin manifest.
- `.claude-plugin/marketplace.json` — optional single-repo marketplace entry so `/plugin marketplace add blader/humanizer` works.
- `scripts/validate-package.py` — dependency-free package and synchronization checks used locally and in CI.

## The maintenance contract

`SKILL.md`, `references/examples.md`, and `README.md` must stay in sync. When you change behavior or content:

- **Patterns:** the skill currently defines **33 numbered patterns**. If you add, remove, or renumber any, update the README pattern table, its "N Patterns Detected" heading, `references/examples.md`'s matching `## N.` heading, and every cross-reference in the same change. Keep numbering stable unless you are deliberately renumbering.
- **Context budget:** `SKILL.md` is loaded in full on every invocation, so it must stay self-sufficient for detection (words to watch + problem statement) for all 33 patterns, but does not need a worked example for every one. Only add a full before/after pair inline in `SKILL.md` for a pattern that's genuinely ambiguous without one (currently §1, §3, §7, §14, §21, §26); every pattern's full example, including those, belongs in `references/examples.md`. Don't let `SKILL.md` regrow past its trimmed size without a specific reason.
- **Description:** the frontmatter `description` is the only thing agents see before deciding whether to load the skill (progressive disclosure). Keep it imperative ("Use when...", not "This skill does..."), focused on user intent and non-obvious trigger contexts, and under the Agent Skills spec's 1024-character hard limit. See [agentskills.io's description-optimization guide](https://agentskills.io/skill-creation/optimizing-descriptions) before rewording it, and prefer testing changes with an eval-query set (should-trigger / should-not-trigger) over intuition alone.
- **Version:** `SKILL.md` frontmatter stores the version under `metadata.version`, `README.md` has a "Version History" section, and `.claude-plugin/plugin.json` has a `version` field. Bump them together so package metadata matches the skill. Keep the skill version under `metadata`; a top-level `version` key is not portable across Agent Skills hosts. (`marketplace.json` intentionally omits a version so `plugin.json` stays the package source of truth.)
- **Compatibility:** keep install and usage language harness-neutral. The skill should work in any agent harness that can load Markdown skill instructions; Claude Code, OpenCode, Codex, and other harnesses are examples, not limits. Note that a harness which only reads `SKILL.md` (not the `references/` directory) still gets full detection coverage for all 33 patterns, just fewer worked examples.
- **Validation:** run `python3 scripts/validate-package.py`, `npx skills add . --list`, and `claude plugin validate .` before publishing.
- **Non-obvious fixes:** if you change the prompt to handle a tricky failure mode (a repeated mis-edit, an unexpected tone shift), add a short note to the README version history explaining what was fixed and why.

## Editing SKILL.md

- Preserve valid YAML frontmatter (formatting and indentation).
- The prompt below the frontmatter is the product. Edit it like a careful instruction document, not code.
- Keep pattern detection cues (words to watch, problem) in `SKILL.md`; keep worked examples in `references/examples.md` unless the pattern is on the curated inline list above.
