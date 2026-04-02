#!/usr/bin/env python3
"""Sync OMX skills from local oh-my-codex repo into plugins/omx/skills.

Rules:
- Source skills live under <repo>/oh-my-codex/skills
- Destination skills live under <repo>/plugins/omx/skills
- Preserve local compatibility alias `setup/` in destination
- Copy/replace all source skill directories deterministically
- Optionally remove destination skill directories missing in source (`--clean`)
"""

from __future__ import annotations

import argparse
import shutil
from dataclasses import dataclass
from pathlib import Path


PRESERVED_DEST_SKILLS = {"setup"}


@dataclass
class SyncReport:
    copied: list[str]
    removed: list[str]
    preserved: list[str]


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent

    parser = argparse.ArgumentParser(description="Sync OMX skills into plugins/omx/skills")
    parser.add_argument(
        "--source",
        type=Path,
        default=repo_root / "oh-my-codex" / "skills",
        help="Source skills directory (default: <repo>/oh-my-codex/skills)",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=repo_root / "plugins" / "omx" / "skills",
        help="Destination skills directory (default: <repo>/plugins/omx/skills)",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove destination skill dirs that are not present in source (except preserved)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned changes without writing files",
    )
    return parser.parse_args()


def list_skill_dirs(path: Path) -> list[Path]:
    if not path.exists():
        return []
    return sorted([p for p in path.iterdir() if p.is_dir()], key=lambda p: p.name.lower())


def ensure_skill_dir_valid(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"{label} not found: {path}")
    if not path.is_dir():
        raise NotADirectoryError(f"{label} must be a directory: {path}")


def copy_skill_dir(src: Path, dst: Path, dry_run: bool) -> None:
    if dry_run:
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def remove_dir(path: Path, dry_run: bool) -> None:
    if dry_run:
        return
    if path.exists():
        shutil.rmtree(path)


def sync(source: Path, dest: Path, clean: bool, dry_run: bool) -> SyncReport:
    ensure_skill_dir_valid(source, "source skills directory")
    dest.mkdir(parents=True, exist_ok=True)

    source_skills = list_skill_dirs(source)
    dest_skills = list_skill_dirs(dest)

    source_names = {p.name for p in source_skills}
    dest_names = {p.name for p in dest_skills}

    copied: list[str] = []
    removed: list[str] = []
    preserved: list[str] = []

    for skill_dir in source_skills:
        src_skill = skill_dir / "SKILL.md"
        if not src_skill.is_file():
            raise FileNotFoundError(f"Missing SKILL.md in source skill: {skill_dir}")
        dst_skill = dest / skill_dir.name
        copy_skill_dir(skill_dir, dst_skill, dry_run=dry_run)
        copied.append(skill_dir.name)

    if clean:
        stale = sorted(dest_names - source_names)
        for skill_name in stale:
            if skill_name in PRESERVED_DEST_SKILLS:
                preserved.append(skill_name)
                continue
            remove_dir(dest / skill_name, dry_run=dry_run)
            removed.append(skill_name)
    else:
        preserved = sorted([name for name in dest_names if name in PRESERVED_DEST_SKILLS])

    return SyncReport(copied=copied, removed=removed, preserved=preserved)


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    dest = args.dest.resolve()

    report = sync(source=source, dest=dest, clean=args.clean, dry_run=args.dry_run)
    print(
        "source_skills={} copied={} removed={} preserved={} dry_run={} clean={}".format(
            len(report.copied),
            len(report.copied),
            len(report.removed),
            ",".join(report.preserved) if report.preserved else "-",
            args.dry_run,
            args.clean,
        )
    )
    if report.removed:
        print("removed_skills=" + ",".join(report.removed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

