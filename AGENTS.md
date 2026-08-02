# AGENTS.md

Guidance for AI coding agents (Claude Code, Codex, Warp, etc.) working in this repository.

## What this repo is

A portable agent skill implemented entirely as Markdown. The runtime artifact is `SKILL.md`: the agent reads its YAML frontmatter and editor prompt. There is no build step, and the repo should avoid wording that limits support to one or two harnesses.

## Key files

- `SKILL.md` — the skill itself. Portable YAML frontmatter (`name`, `description`, `license`, `metadata.version`) followed by the canonical, numbered pattern list with before/after examples. **This is the source of truth.**
- `languages/<code>.md` — optional language packs (`ar.md` today) holding the AI tells specific to one language. `SKILL.md` registers them and loads one only when the text is in that language, so the runtime prompt stays small. `languages/TEMPLATE.md` is the starting point for a new language.
- `README.md` — for humans: installation, usage, a summary table of the patterns, and a version history.
- `.claude-plugin/plugin.json` — optional Claude Code plugin manifest.
- `.claude-plugin/marketplace.json` — optional single-repo marketplace entry so `/plugin marketplace add blader/humanizer` works.
- `scripts/validate-package.py` — dependency-free package and synchronization checks used locally and in CI.

## The maintenance contract

`SKILL.md` and `README.md` must stay in sync. When you change behavior or content:

- **Patterns:** the skill currently defines **33 numbered patterns** in `SKILL.md`. If you add, remove, or renumber any, update the README pattern table, its "N Patterns Detected" heading, the range in `scripts/validate-package.py`, and every cross-reference in the same change. Keep numbering stable unless you are deliberately renumbering.
- **Language packs:** language-specific tells live in `languages/<code>.md`, never in `SKILL.md`. Each pack is self-describing (`language`, `code`, `patterns: XX1-XXn` frontmatter) and needs three things in sync: the pack file, one registry row in `SKILL.md`, and one pattern table in `README.md`. Pack ids are prefixed (`AR1`) so core numbering never shifts. `scripts/validate-package.py` discovers packs by globbing `languages/*.md`, so a new language needs no validator change. `languages/TEMPLATE.md` documents the pack rules and is skipped by validation.
- **Language behavior is not translation.** Pack rule text stays in English so the prompt reads consistently; every example stays in the target language, because round-tripping through English is the exact failure the packs exist to prevent. Register matching (including dialects and regional varieties) and the pack's false-positive guards are part of the contract, not decoration.
- **Budgets:** `SKILL.md` stays under 500 lines, each pack under 250. Packs load on demand, so growth belongs there rather than in the runtime prompt.
- **Version:** `SKILL.md` frontmatter stores the version under `metadata.version`, `README.md` has a "Version History" section, and `.claude-plugin/plugin.json` has a `version` field. Bump them together so package metadata matches the skill. Keep the skill version under `metadata`; a top-level `version` key is not portable across Agent Skills hosts. (`marketplace.json` intentionally omits a version so `plugin.json` stays the package source of truth.)
- **Compatibility:** keep install and usage language harness-neutral. The skill should work in any agent harness that can load Markdown skill instructions; Claude Code, OpenCode, Codex, and other harnesses are examples, not limits.
- **Validation:** run `python3 scripts/validate-package.py`, `npx skills add . --list`, and `claude plugin validate .` before publishing.
- **Non-obvious fixes:** if you change the prompt to handle a tricky failure mode (a repeated mis-edit, an unexpected tone shift), add a short note to the README version history explaining what was fixed and why.

## Editing SKILL.md

- Preserve valid YAML frontmatter (formatting and indentation).
- The prompt below the frontmatter is the product. Edit it like a careful instruction document, not code.
