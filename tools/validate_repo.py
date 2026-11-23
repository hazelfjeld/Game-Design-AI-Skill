#!/usr/bin/env python3
"""Check this skill's distribution invariants; no network or third-party packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


REFERENCE_NAMES = {
    "design-foundations.md", "systems-and-balance.md",
    "playtesting-and-evidence.md", "game-feel-and-accessibility.md",
    "production-and-collaboration.md", "audience-and-positioning.md",
    "learning-path.md", "sources.md",
}
TEMPLATE_NAMES = {
    "design-brief.md", "mechanic-spec.md", "experiment-card.md",
    "playtest-plan.md", "playtest-observation.md", "decision-record.md",
    "slice-plan.md", "project-board.md", "run-handoff.md",
}
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)")


def heading_ids(text: str) -> set[str]:
    seen: dict[str, int] = {}
    result = set()
    for title in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(f"{slug}-{count}" if count else slug)
    return result


def validate(root: Path) -> tuple[list[str], dict[str, str]]:
    errors: list[str] = []
    manifest: dict[str, str] = {}
    required = {"SKILL.md", "agents/openai.yaml"}
    required |= {f"references/{n}" for n in REFERENCE_NAMES}
    required |= {f"assets/templates/{n}" for n in TEMPLATE_NAMES}
    for name in sorted(required):
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")

    texts: dict[Path, str] = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            errors.append(f"Symlink is not supported in this package: {path.relative_to(root)}")
            continue
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        if path.suffix not in {".md", ".yaml"}:
            errors.append(f"Unexpected package file type: {relative}")
        data = path.read_bytes()
        manifest[relative] = hashlib.sha256(data).hexdigest()
        try:
            value = data.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"Non-UTF-8 content: {relative}")
            continue
        texts[path.resolve()] = value
        if not value.endswith("\n"):
            errors.append(f"Missing terminal newline: {relative}")
        if re.search(r"\b(?:TODO|FIXME|TBD)\b", value):
            errors.append(f"Unfinished placeholder: {relative}")

    skill_path = (root / "SKILL.md").resolve()
    skill = texts.get(skill_path, "")
    match = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
    if not match:
        errors.append("SKILL.md lacks the expected YAML frontmatter")
    else:
        fields = {}
        for line in match.group(1).splitlines():
            if ":" not in line:
                errors.append("Frontmatter must use simple name/description fields")
                continue
            key, value = line.split(":", 1)
            if key in fields:
                errors.append(f"Duplicate frontmatter field: {key}")
            fields[key] = value.strip()
        if set(fields) != {"name", "description"}:
            errors.append("Frontmatter fields must be exactly name and description")
        if fields.get("name") != "game-designer":
            errors.append("Skill name must be game-designer")
        if not fields.get("description"):
            errors.append("Skill description is empty")
    if len(skill.splitlines()) >= 500:
        errors.append("Main skill must stay below 500 lines")

    metadata = texts.get((root / "agents/openai.yaml").resolve(), "")
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf'^  {key}: "[^"\n]+"$', metadata, re.MULTILINE):
            errors.append(f"Missing or unquoted interface field: {key}")
    blurb = re.search(r'^  short_description: "([^"\n]+)"$', metadata, re.MULTILINE)
    if blurb and not 25 <= len(blurb.group(1)) <= 64:
        errors.append("Interface short_description must be 25–64 characters")
    if "$game-designer" not in metadata:
        errors.append("Default prompt must reference $game-designer")

    for path, value in texts.items():
        if path.suffix != ".md":
            continue
        for target in LINK.findall(value):
            parsed = urlparse(target)
            if parsed.scheme in {"https", "http", "mailto"}:
                continue
            if parsed.scheme:
                errors.append(f"Unexpected link scheme in {path.name}: {target}")
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not resolved.is_relative_to(root.resolve()):
                errors.append(f"Package link escapes its directory: {path.name}: {target}")
            elif not resolved.exists():
                errors.append(f"Broken local link in {path.name}: {target}")
            elif parsed.fragment and resolved.suffix == ".md":
                target_text = texts.get(resolved, "")
                if unquote(parsed.fragment) not in heading_ids(target_text):
                    errors.append(f"Missing heading in {path.name}: {target}")

    for name in REFERENCE_NAMES:
        if f"references/{name}" not in skill:
            errors.append(f"Reference not routed directly from SKILL.md: {name}")
    for name in TEMPLATE_NAMES:
        if f"assets/templates/{name}" not in skill:
            errors.append(f"Template not linked directly from SKILL.md: {name}")
    sources = texts.get((root / "references/sources.md").resolve(), "")
    for source_id in [f"B{i}" for i in range(1, 8)] + [f"W{i}" for i in range(1, 6)]:
        if f"| {source_id} |" not in sources:
            errors.append(f"Missing source entry: {source_id}")
    for forbidden in ("README.md", "INSTALLATION_GUIDE.md", "CHANGELOG.md"):
        if (root / forbidden).exists():
            errors.append(f"Keep repository documentation outside the skill: {forbidden}")
    return errors, manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1] / "game-designer")
    parser.add_argument("--manifest", type=Path, help="Optionally write SHA-256 manifest after validation")
    args = parser.parse_args()
    root = args.skill_root.resolve()
    if not root.is_dir():
        print(f"FAIL: skill directory does not exist: {root}", file=sys.stderr)
        return 1
    errors, manifest = validate(root)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    if args.manifest:
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS: {len(manifest)} package files; frontmatter, metadata, links, routing, and source coverage")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
