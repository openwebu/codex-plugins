---
description: Discover curated Medusa community plugins and get install plus medusa-config snippets.
---

# Medusa Plugin Catalog

Use `/medusa:plugin-catalog` to browse curated plugins sourced from local `MEDUSA/PLUGINS`.

## Usage

- List all catalog entries:
`/medusa:plugin-catalog`
- Filter by goal or plugin:
`/medusa:plugin-catalog payments`
`/medusa:plugin-catalog wishlist`

## Expected Response

- Recommended package names
- Compatibility status (`v2` or `legacy-v1`)
- Install command snippets (`npm`, `yarn`, `pnpm`)
- Minimal `medusa-config` plugin snippet
- Migration reminder if needed (`npx medusa db:migrate`)

## Notes

- `medusa-test-plugin` is intentionally excluded.
- Legacy entries are shown with warning labels.
