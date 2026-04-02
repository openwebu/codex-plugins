# OMX

## Top Skills

- `deep-interview`
- `ralplan`
- `ralph`
- `team`
<details>
<summary>Show all skills (37)</summary>

- `ai-slop-cleaner`
- `analyze`
- `ask-claude`
- `ask-gemini`
- `autopilot`
- `build-fix`
- `cancel`
- `code-review`
- `configure-notifications`
- `deep-interview`
- `deepsearch`
- `doctor`
- `ecomode`
- `frontend-ui-ux`
- `git-master`
- `help`
- `hud`
- `note`
- `omx-setup`
- `pipeline`
- `plan`
- `ralph`
- `ralph-init`
- `ralplan`
- `review`
- `security-review`
- `setup` _(compat alias)_
- `skill`
- `swarm`
- `tdd`
- `team`
- `trace`
- `ultraqa`
- `ultrawork`
- `visual-verdict`
- `web-clone`
- `worker`
</details>

## What It Can Do

- Mirrors the oh-my-codex workflow skill stack inside this plugin.
- Supports the canonical flow: `$deep-interview` → `$ralplan` → `$ralph`/`$team`.
- Includes setup/bootstrap coverage via `omx-setup` and local `setup` compatibility alias.

## Why Use It

- Gives you the same OMX-style orchestration surface directly from this plugin repository.
- Keeps planning/execution/verification workflows consistent across sessions.
- Makes OMX skill updates repeatable via one sync script.

## How It Works

1. Use `scripts/sync_omx_skills.py` to sync skills from `oh-my-codex/skills` into `plugins/omx/skills`.
2. Run `setup`/`omx-setup` when environment bootstrap is needed.
3. Use primary orchestration skills (`deep-interview`, `ralplan`, `ralph`, `team`) for delivery.

## Quick Examples

```text
$deep-interview "clarify scope and constraints"
$ralplan "approve architecture and tests"
$ralph "deliver the approved plan with verification"
```

```bash
python3 scripts/sync_omx_skills.py --clean
```

## Requirements

- Local `oh-my-codex/skills` source directory present for sync operations.
- Node.js 20+ and npm when using setup/install workflows.
- Codex CLI environment where OMX workflow skills are meaningful.
