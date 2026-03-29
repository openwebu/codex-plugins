#!/usr/bin/env python3
"""Generate bounded README catalog sections from plugin metadata."""

from __future__ import annotations

import argparse
import difflib
import json
import re
from collections import OrderedDict
from pathlib import Path
from typing import Any


VALID_MATURITY = {"alpha", "beta", "stable"}
BLOCK_PLUGIN_LINEUP = "PLUGIN_LINEUP"
BLOCK_CAPABILITY_MATRIX = "CAPABILITY_MATRIX"
BLOCK_MATURITY_BADGES = "MATURITY_BADGES"


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    parser = argparse.ArgumentParser(
        description="Generate bounded README catalog sections from marketplace and plugin metadata."
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=repo_root / "README.md",
        help="Path to root README.md",
    )
    parser.add_argument(
        "--plugins-dir",
        type=Path,
        default=repo_root / "plugins",
        help="Directory containing plugin folders",
    )
    parser.add_argument(
        "--marketplace",
        type=Path,
        default=repo_root / ".agents" / "plugins" / "marketplace.json",
        help="Path to marketplace.json",
    )
    parser.add_argument(
        "--top-skills-limit",
        type=int,
        default=4,
        help="Top skills to show inline before collapsing extras",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if README would change.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain a JSON object.")
    return payload


def list_skill_names(plugin_dir: Path) -> list[str]:
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return []

    names: list[str] = []
    for child in sorted(skills_dir.iterdir(), key=lambda p: p.name.lower()):
        if child.is_dir() and (child / "SKILL.md").exists():
            names.append(child.name)
    return names


def load_manifest(plugin_dir: Path) -> dict[str, Any]:
    manifest_path = plugin_dir / ".codex-plugin" / "plugin.json"
    if not manifest_path.exists():
        return {}
    payload = load_json(manifest_path)
    return payload


def normalize_maturity(value: Any) -> str:
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in VALID_MATURITY:
            return lowered
    return "unspecified"


def normalize_top_skills(
    requested: Any, discovered: list[str], top_limit: int
) -> tuple[list[str], list[str]]:
    discovered_set = set(discovered)

    if isinstance(requested, list):
        chosen: list[str] = []
        for item in requested:
            if isinstance(item, str):
                skill = item.strip()
                if skill and skill in discovered_set and skill not in chosen:
                    chosen.append(skill)
        if chosen:
            remainder = [skill for skill in discovered if skill not in chosen]
            combined = chosen + remainder
            return combined[:top_limit], combined[top_limit:]

    return discovered[:top_limit], discovered[top_limit:]


def plugin_summary(plugin_name: str, manifest: dict[str, Any]) -> str:
    interface = manifest.get("interface")
    if isinstance(interface, dict):
        short_desc = interface.get("shortDescription")
        if isinstance(short_desc, str):
            short_desc = short_desc.strip()
            if short_desc and not short_desc.startswith("[TODO:"):
                return short_desc

    description = manifest.get("description")
    if isinstance(description, str):
        description = description.strip()
        if description and not description.startswith("[TODO:"):
            return description

    return f"Plugin workflows for `{plugin_name}`."


def collect_plugins(
    marketplace_plugins: list[dict[str, Any]], plugins_dir: Path, top_limit: int
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for entry in marketplace_plugins:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not name.strip():
            continue
        name = name.strip()
        category = entry.get("category")
        if not isinstance(category, str) or not category.strip():
            category = "Uncategorized"
        maturity = normalize_maturity(entry.get("maturity"))

        plugin_dir = plugins_dir / name
        discovered_skills = list_skill_names(plugin_dir) if plugin_dir.exists() else []
        top_skills, remaining_skills = normalize_top_skills(
            entry.get("topSkills"), discovered_skills, top_limit
        )
        manifest = load_manifest(plugin_dir) if plugin_dir.exists() else {}

        rows.append(
            {
                "name": name,
                "category": category.strip(),
                "maturity": maturity,
                "skill_count": len(discovered_skills),
                "top_skills": top_skills,
                "remaining_skills": remaining_skills,
                "summary": plugin_summary(name, manifest),
                "exists": plugin_dir.exists(),
            }
        )
    return rows


def render_lineup(rows: list[dict[str, Any]]) -> str:
    grouped: OrderedDict[str, list[dict[str, Any]]] = OrderedDict()
    for row in rows:
        grouped.setdefault(row["category"], []).append(row)

    lines: list[str] = []
    for category, entries in grouped.items():
        lines.append(f"### {category}")
        lines.append("")
        for row in entries:
            plugin_name = row["name"]
            lines.append(f"#### [`{plugin_name}`](./plugins/{plugin_name})")
            lines.append("")
            lines.append(row["summary"])
            lines.append("")
            if row["top_skills"]:
                top = ", ".join(f"`{skill}`" for skill in row["top_skills"])
            else:
                top = "_none_"
            lines.append(f"- Top skills: {top}")
            if row["remaining_skills"]:
                remaining = ", ".join(f"`{skill}`" for skill in row["remaining_skills"])
                lines.append(f"- Additional skills: {remaining}")
            lines.append(f"- Skill count: `{row['skill_count']}`")
            lines.append(f"- Maturity: `{row['maturity']}`")
            if not row["exists"]:
                lines.append("- Status: `missing-on-disk`")
            lines.append("")
    return "\n".join(lines).rstrip()


def render_capability_matrix(rows: list[dict[str, Any]]) -> str:
    lines = [
        "| Plugin | Category | Skills | Top Skills | Maturity |",
        "|---|---|---:|---|---|",
    ]
    for row in rows:
        top = ", ".join(row["top_skills"]) if row["top_skills"] else "n/a"
        lines.append(
            f"| `{row['name']}` | `{row['category']}` | {row['skill_count']} | {top} | `{row['maturity']}` |"
        )
    return "\n".join(lines)


def render_maturity(rows: list[dict[str, Any]]) -> str:
    counts = {"stable": 0, "beta": 0, "alpha": 0, "unspecified": 0}
    for row in rows:
        counts[row["maturity"]] += 1

    lines = [
        "- `stable`: " + str(counts["stable"]),
        "- `beta`: " + str(counts["beta"]),
        "- `alpha`: " + str(counts["alpha"]),
        "- `unspecified`: " + str(counts["unspecified"]),
    ]
    return "\n".join(lines)


def replace_block(readme_text: str, marker: str, body: str) -> tuple[str, bool]:
    begin = f"<!-- BEGIN AUTO:{marker} -->"
    end = f"<!-- END AUTO:{marker} -->"
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), flags=re.S)
    replacement = f"{begin}\n{body}\n{end}"

    if not pattern.search(readme_text):
        raise ValueError(f"Missing README marker block: {begin} ... {end}")

    updated = pattern.sub(replacement, readme_text, count=1)
    return updated, updated != readme_text


def main() -> int:
    args = parse_args()
    readme_path = args.readme.resolve()
    plugins_dir = args.plugins_dir.resolve()
    marketplace_path = args.marketplace.resolve()

    marketplace = load_json(marketplace_path)
    marketplace_plugins = marketplace.get("plugins", [])
    if not isinstance(marketplace_plugins, list):
        raise ValueError(f"{marketplace_path} field 'plugins' must be an array.")

    rows = collect_plugins(marketplace_plugins, plugins_dir, args.top_skills_limit)
    readme_text = readme_path.read_text(encoding="utf-8")

    updated = readme_text
    changed_any = False

    for marker, body in (
        (BLOCK_PLUGIN_LINEUP, render_lineup(rows)),
        (BLOCK_CAPABILITY_MATRIX, render_capability_matrix(rows)),
        (BLOCK_MATURITY_BADGES, render_maturity(rows)),
    ):
        updated, changed = replace_block(updated, marker, body)
        changed_any = changed_any or changed

    if args.check:
        if changed_any:
            diff = difflib.unified_diff(
                readme_text.splitlines(),
                updated.splitlines(),
                fromfile="README.md",
                tofile="README.md (generated)",
                lineterm="",
            )
            print("\n".join(diff))
            return 1
        print("OK: README generated sections are up to date")
        return 0

    if changed_any:
        readme_path.write_text(updated, encoding="utf-8")
        print(f"Updated README generated sections: {readme_path}")
        return 0

    print("No README catalog changes needed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
