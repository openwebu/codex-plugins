---
name: setup
description: Use when the user wants to install or verify the OMX (oh-my-codex) workflow layer and ensure Codex CLI + OMX are ready.
---

# OMX Setup

Compatibility alias for OMX setup flows.

Prefer `omx-setup` when available; `setup` is retained for users that expect a short setup entrypoint.

## What this setup guarantees

- `@openai/codex` and `oh-my-codex` are installed globally if they were missing.
- `omx setup` has been executed.
- `omx doctor` has been executed and reviewed.

## Canonical commands

### 1) Detect current environment

```bash
node --version
npm --version
command -v codex || true
command -v omx || true
```

### 2) Install Codex + OMX when missing

```bash
npm install -g @openai/codex oh-my-codex
```

Run this only when `codex` or `omx` is missing.

### 3) Initialize OMX

```bash
omx setup
```

### 4) Verify installation health

```bash
omx doctor
```

## Recommended first session

```bash
omx --madmax --high
```

Then use the canonical workflow:

```text
$deep-interview "clarify the task"
$ralplan "approve plan and tradeoffs"
$ralph "carry approved plan to completion"
$team 3:executor "execute approved plan in parallel"
```

## Platform notes (team mode)

- macOS/Linux team runtime requires `tmux`.
- Native Windows team runtime uses `psmux`.
- WSL2 team runtime can use `tmux`.

## Output contract

After running setup, report:
- which binaries were missing and what was installed,
- `omx setup` result,
- `omx doctor` result,
- any remaining blockers with exact remediation commands.
