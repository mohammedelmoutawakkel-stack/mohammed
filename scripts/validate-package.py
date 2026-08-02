#!/usr/bin/env python3
"""Validate Humanizer's portable package surfaces without external dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = (ROOT / "SKILL.md").read_text()
README = (ROOT / "README.md").read_text()
PLUGIN = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())


def require(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


frontmatter = require(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "SKILL.md must start with YAML frontmatter",
).group(1)

for nonportable_key in ("compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(nonportable_key)}", frontmatter):
        raise SystemExit(f"Remove nonportable frontmatter key: {nonportable_key[:-1]}")

skill_version = require(
    re.search(r'(?m)^\s+version:\s*["\']([^"\']+)["\']\s*$', frontmatter),
    "SKILL.md metadata.version is missing",
).group(1)
readme_version = require(
    re.search(r"(?m)^- \*\*([0-9]+\.[0-9]+\.[0-9]+)\*\*", README),
    "README version history is missing",
).group(1)

versions = {skill_version, readme_version, str(PLUGIN.get("version", ""))}
if len(versions) != 1:
    raise SystemExit(f"Version mismatch: {sorted(versions)}")

pattern_numbers = [
    int(number)
    for number in re.findall(r"(?m)^### ([0-9]+)\. ", SKILL)
]
if pattern_numbers != list(range(1, 34)):
    raise SystemExit(f"Expected patterns 1-33, found {pattern_numbers}")

readme_numbers = {
    int(number) for number in re.findall(r"(?m)^\| ([0-9]+) \|", README)
}
if readme_numbers != set(range(1, 34)):
    raise SystemExit("README pattern table must contain patterns 1-33")

# Language packs: each languages/<code>.md is self-describing, and the registry
packs = sorted(
    path
    for path in (ROOT / "languages").glob("*.md")
    if not path.name.startswith("_") and path.name != "TEMPLATE.md"
)
if not packs:
    raise SystemExit("No language packs found under languages/")

for pack in packs:
    text = pack.read_text()
    header = require(
        re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL),
        f"{pack.name} must start with YAML frontmatter",
    ).group(1)
    code = require(
        re.search(r"(?m)^code:\s*(\S+)\s*$", header), f"{pack.name} is missing code:"
    ).group(1)
    prefix, first, last = require(
        re.search(r"(?m)^patterns:\s*([A-Z]+)([0-9]+)-[A-Z]+([0-9]+)\s*$", header),
        f"{pack.name} is missing a patterns: range like AR1-AR14",
    ).groups()
    expected = list(range(int(first), int(last) + 1))

    if code != pack.stem:
        raise SystemExit(f"{pack.name}: code '{code}' does not match the filename")

    found = [
        int(number)
        for number in re.findall(rf"(?m)^### {prefix}([0-9]+)\. ", text)
    ]
    if found != expected:
        raise SystemExit(f"{pack.name}: expected {prefix}{first}-{prefix}{last}, found {found}")

    if not re.search(rf"(?m)^\| {re.escape(code)} \|.*`languages/{pack.name}`", SKILL):
        raise SystemExit(f"SKILL.md language registry is missing a row for {pack.name}")

    in_readme = {
        int(number) for number in re.findall(rf"(?m)^\| {prefix}([0-9]+) \|", README)
    }
    if in_readme != set(expected):
        raise SystemExit(
            f"README pattern table must contain {prefix}{first}-{prefix}{last} for {pack.name}"
        )

    if len(text.splitlines()) > 250:
        raise SystemExit(f"{pack.name} exceeds the 250-line language pack budget")

registry_rows = set(re.findall(r"(?m)^\| ([a-z]{2,3}) \| .* \| `languages/", SKILL))
if registry_rows != {pack.stem for pack in packs}:
    raise SystemExit(
        f"SKILL.md registry {sorted(registry_rows)} does not match packs "
        f"{sorted(pack.stem for pack in packs)}"
    )

if len(SKILL.splitlines()) > 500:
    raise SystemExit("SKILL.md exceeds the 500-line portability budget")

print(f"Humanizer package v{skill_version} is valid")
