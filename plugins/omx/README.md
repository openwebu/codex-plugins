# OMX

## Top Skills

- `setup`

## What It Can Do

- Detects whether `codex` and `omx` are available in your shell.
- Installs `@openai/codex` and `oh-my-codex` when missing.
- Runs `omx setup` and `omx doctor` to validate the OMX workflow layer.

## Why Use It

- Standardizes first-time OMX onboarding in one repeatable flow.
- Reduces setup drift across machines and contributors.
- Produces clear verification evidence before you begin workflow execution.

## How It Works

1. Checks Node/npm and current `codex`/`omx` availability.
2. Installs missing binaries with global npm install.
3. Executes `omx setup`, then `omx doctor`.
4. Reports status and any concrete remediation commands.

## Quick Examples

```text
Run /omx:setup and install Codex + OMX if either binary is missing.
```

```text
Validate my OMX environment, run omx doctor, and tell me any blocker to running omx --madmax --high.
```

## Requirements

- Node.js 20+ and npm.
- Permission to run global npm installs.
- Network access to npm registry.
