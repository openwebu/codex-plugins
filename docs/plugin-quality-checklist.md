# Plugin Quality Checklist

Use this checklist before adding or updating any plugin in `plugins/*`.

## Required assets

- Plugin folder exists in `plugins/<plugin-name>`.
- `.codex-plugin/plugin.json` exists and is valid JSON.
- `README.md` exists.
- `skills/` contains at least one skill with `SKILL.md`.

## README section contract

Each plugin README should include:

- `## Top Skills`
- `## What It Can Do`
- `## Why Use It`
- `## How It Works`
- `## Quick Examples`
- `## Requirements`

## Quick Examples UX

- Use fenced code blocks for copy-friendly examples.
- Avoid inline bullet-code prompts in `Quick Examples`.
- Keep examples actionable and runnable where possible.

## Skill discoverability

- Skills listed in `Top Skills` must exist in `skills/*/SKILL.md`.
- Skill names in docs should match folder names exactly.
- Include at least one starter prompt in `Quick Examples` tied to real skills.

## Marketplace consistency

- Every plugin folder should be present in `.agents/plugins/marketplace.json`.
- No stale marketplace entries pointing to missing folders.

## Validation command

Run this before committing:

```bash
python3 scripts/generate_readme_catalog.py
python3 scripts/validate_plugin_quality.py
```
