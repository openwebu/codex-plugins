# AGENTS Governance for `plugins/`

This file is the authoritative contributor/agent policy for this repository.

## Non-optional README Maintenance Rule

Every meaningful repository change must include a README quality check and, when needed, a README improvement pass.

Meaningful changes include:
- plugin additions, removals, renames, or capability shifts,
- new or removed skills,
- setup/install/update flow changes,
- roadmap-impacting platform coverage changes.

README quality means the root `README.md` remains:
- clear (easy to scan, no stale wording),
- complete (covers current capabilities and limits),
- current (matches actual plugin metadata and lineup).

## Plugin Metadata and README Sync Policy

Any plugin add/rename/remove/update must synchronize all impacted documentation surfaces before work is considered complete:
- plugin lineup and capability sections,
- `What Codex plugins can do today (planner style)` block,
- roadmap/TODO items affected by the change,
- setup/update instructions when behavior or prerequisites change,
- top-skills and hidden-skills presentation references.

If a plugin change ships without these synchronized updates, the change is incomplete.

## Done Criteria (Strict)

A task is **not done** until all of the following are true:
- code/doc/plugin metadata changes are committed and coherent,
- root `README.md` has been reviewed and updated where needed,
- affected plugin docs are aligned with root README language,
- setup and update instructions are accurate for the current state.

## Lightweight Maintenance Checklist

Use this checklist on each meaningful change:
- [ ] Plugin metadata updated.
- [ ] Root README sections synchronized (planner block, lineup, roadmap, setup/policy sections).
- [ ] Setup/update instructions validated against current behavior.
- [ ] Roadmap reviewed for newly unlocked capabilities and remaining gaps.

## Root Source Folder to README Link Rule

If a new root-level source folder is added to this repository (for example `desktopcommandermcp`), it must be reflected in `README.md` under `Skill Source Repositories` in the same change.

Requirements:
- Add a corresponding linked entry in `Skill Source Repositories`.
- Keep naming consistent between folder/repo identity and README label.
- Do not leave source folders undocumented in that section.

## Canonical Repository Link Rule

The canonical repository URL for this project is:

- `https://github.com/openwebu/codex-plugins`

Whenever this repository is referenced in README/docs/posts/templates, always use the canonical URL above.
Do not use alternate repository URLs for this project in maintained docs.

The baseline source repository set that must remain represented in README:
- `agent-plugins`
- `aws-cli`
- `claude-codex-settings`
- `cli`
- `medusa-agent-skills`
- `openai/plugins` (official upstream plugin repository)
- `plugins`
- `resend-cli`
- `resend-mcp`
- `saleor-paper-storefront` (base reference for the Saleor storefront skill pack)
- `superpowers`
