#!/usr/bin/env python3
"""Validate plugin package quality baseline for plugins/."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REQUIRED_README_SECTIONS = [
    "## Top Skills",
    "## What It Can Do",
    "## Why Use It",
    "## How It Works",
    "## Quick Examples",
    "## Requirements",
]
VALID_MATURITY = {"alpha", "beta", "stable"}


def list_plugin_dirs(root: Path) -> list[Path]:
    return sorted([p for p in root.iterdir() if p.is_dir()])


def list_skill_names(plugin_dir: Path) -> list[str]:
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return []
    names = []
    for child in sorted(skills_dir.iterdir()):
        if child.is_dir() and (child / "SKILL.md").exists():
            names.append(child.name)
    return names


def extract_top_skills(readme_text: str) -> list[str]:
    m = re.search(r"## Top Skills\n(.*?)(?:\n##\s+|\Z)", readme_text, flags=re.S)
    if not m:
        return []
    block = m.group(1)
    return re.findall(r"`([^`]+)`", block)


def quick_examples_has_code_block(readme_text: str) -> bool:
    m = re.search(r"## Quick Examples\n(.*?)(?:\n##\s+|\Z)", readme_text, flags=re.S)
    if not m:
        return False
    block = m.group(1)
    has_fence = "```" in block
    has_inline_bullet_code = re.search(r"^\s*-\s+`", block, flags=re.M) is not None
    return has_fence and not has_inline_bullet_code


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    plugins_root = repo_root / "plugins"
    marketplace_file = repo_root / ".agents" / "plugins" / "marketplace.json"
    readme_generator = repo_root / "scripts" / "generate_readme_catalog.py"

    errors: list[str] = []

    if not marketplace_file.exists():
        errors.append(f"Missing marketplace file: {marketplace_file}")
        print("\n".join(f"ERROR: {e}" for e in errors))
        return 1

    market = json.loads(marketplace_file.read_text())
    marketplace_plugins = market.get("plugins", [])
    if not isinstance(marketplace_plugins, list):
        errors.append("marketplace.json field 'plugins' must be an array")
        print("\n".join(f"ERROR: {e}" for e in errors))
        return 1

    listed_plugins: list[str] = []
    for entry in marketplace_plugins:
        if not isinstance(entry, dict):
            errors.append("marketplace.json contains a non-object plugin entry")
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not name.strip():
            errors.append("marketplace.json plugin entry missing string 'name'")
            continue
        name = name.strip()
        listed_plugins.append(name)

        maturity = entry.get("maturity")
        if maturity is not None:
            if not isinstance(maturity, str) or maturity.lower() not in VALID_MATURITY:
                errors.append(
                    f"{name}: marketplace maturity must be one of {sorted(VALID_MATURITY)}"
                )

        top_skills = entry.get("topSkills")
        if top_skills is not None:
            if not isinstance(top_skills, list) or not all(
                isinstance(item, str) and item.strip() for item in top_skills
            ):
                errors.append(f"{name}: marketplace topSkills must be a string array")

    listed_plugins = sorted(listed_plugins)
    actual_plugins = sorted([p.name for p in list_plugin_dirs(plugins_root)])

    missing_in_market = [p for p in actual_plugins if p not in listed_plugins]
    missing_in_fs = [p for p in listed_plugins if p not in actual_plugins]

    if missing_in_market:
        errors.append(f"Plugins missing from marketplace.json: {', '.join(missing_in_market)}")
    if missing_in_fs:
        errors.append(f"Marketplace entries missing on disk: {', '.join(missing_in_fs)}")

    skill_names_by_plugin: dict[str, list[str]] = {}

    for plugin_dir in list_plugin_dirs(plugins_root):
        name = plugin_dir.name
        plugin_json = plugin_dir / ".codex-plugin" / "plugin.json"
        readme = plugin_dir / "README.md"

        if not plugin_json.exists():
            errors.append(f"{name}: missing .codex-plugin/plugin.json")
        if not readme.exists():
            errors.append(f"{name}: missing README.md")
            continue

        readme_text = readme.read_text()
        for section in REQUIRED_README_SECTIONS:
            if section not in readme_text:
                errors.append(f"{name}: missing README section '{section}'")

        skill_names = list_skill_names(plugin_dir)
        skill_names_by_plugin[name] = skill_names
        if not skill_names:
            errors.append(f"{name}: no skills found (expected skills/*/SKILL.md)")

        top_skills = extract_top_skills(readme_text)
        if not top_skills:
            errors.append(f"{name}: Top Skills section has no backticked skill entries")
        else:
            unknown = [s for s in top_skills if s not in skill_names and s not in {"skills/", "coming soon"}]
            if unknown:
                errors.append(f"{name}: Top Skills references missing skills: {', '.join(unknown)}")

        if not quick_examples_has_code_block(readme_text):
            errors.append(f"{name}: Quick Examples must use fenced code blocks (no inline bullet code)")

    for entry in marketplace_plugins:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        if not isinstance(name, str):
            continue
        top_skills = entry.get("topSkills")
        if top_skills is None:
            continue
        known = set(skill_names_by_plugin.get(name, []))
        if not known:
            continue
        unknown = sorted({skill for skill in top_skills if isinstance(skill, str) and skill not in known})
        if unknown:
            errors.append(
                f"{name}: marketplace topSkills references missing skills: {', '.join(unknown)}"
            )

    if not readme_generator.exists():
        errors.append(f"Missing README generator script: {readme_generator}")
    else:
        result = subprocess.run(
            [sys.executable, str(readme_generator), "--check"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            details = (result.stdout + "\n" + result.stderr).strip()
            errors.append(
                "Root README generated sections are out of date. "
                "Run: python3 scripts/generate_readme_catalog.py\n"
                + details
            )

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        print(f"\nValidation failed: {len(errors)} issue(s)")
        return 1

    print("OK: plugin quality baseline checks passed")
    print(f"Plugins checked: {len(actual_plugins)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
