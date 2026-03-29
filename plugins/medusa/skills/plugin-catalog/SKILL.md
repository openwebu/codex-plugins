---
name: plugin-catalog
description: Recommend and configure Medusa community plugins from local MEDUSA/PLUGINS catalog
argument-hint: "[goal-or-plugin]"
---

# Medusa Community Plugin Catalog

Use this skill to recommend plugins from the local catalog and generate installation guidance.

Primary data source:

- `assets/community-plugin-catalog.json`

## Behavior

1. Match the user's goal or plugin name to catalog entries.
2. Prefer entries with `compatibility: "v2"` unless user asks for legacy behavior.
3. If a matching entry is `legacy-v1`, clearly warn that it is legacy and suggest a v2 alternative when possible.
4. Never include `medusa-test-plugin` in recommendations.

## Output Format

For each recommended plugin, provide:

- Package name
- Compatibility (`v2` or `legacy-v1`)
- Short rationale
- Install command examples:
  - `npm install <package>`
  - `yarn add <package>`
  - `pnpm add <package>`
- A minimal `medusa-config` `plugins` snippet
- If relevant, a migration reminder (`npx medusa db:migrate`)

## Guardrails

- Do not claim runtime compatibility not reflected in the catalog.
- Do not auto-install packages; provide commands for the user to run.
- If no good match exists, return nearest matches by category and explain tradeoffs.
