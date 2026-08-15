# Language files

`SKILL.md`'s patterns are documented with English trigger phrases. Those are illustrations of an underlying rhetorical move (inflated significance, hedging, filler, mismatched formality, and so on), not a literal vocabulary list — most of them don't translate word-for-word into another language's actual AI tells.

Each file here covers one language or dialect and lists that language's own version of the moves in `SKILL.md`, plus that language's register/shorthand conventions. `SKILL.md`'s Voice Calibration section points here for non-English input.

## Adding a language

1. Name the file by BCP-47-style code: language, plus region when the dialect matters (`pt-br.md`, not a generic `pt.md`, since Brazilian and European Portuguese don't share the same stock AI phrasing or the same shorthand). Use a plain language code (`es.md`) only when the pattern genuinely doesn't vary by region.
2. Cover two things, using `SKILL.md`'s own Words/Phrases-to-watch → Problem → Before → After format:
   - **AI-flavored vocabulary and phrasing** in that language — the actual stock phrases, not translations of the English list. Note which `SKILL.md` section(s) each parallels.
   - **Register: shorthand vs. spelled-out formality** — how real speakers of that language abbreviate in casual chat contexts, and where AI defaults to full formal spelling instead.
3. Keep it descriptive, not prescriptive: a user-provided writing sample always outranks this file (see `SKILL.md`'s Voice Calibration).
4. No changes to `SKILL.md`'s pattern numbering or `scripts/validate-package.py` are needed — that script only reads `SKILL.md`, `README.md`, and `.claude-plugin/plugin.json`. A new file here is picked up automatically once `SKILL.md`'s Voice Calibration pointer is in place.

See `pt-br.md` for a worked example.
