# docker-agent

```
██████╗  ██████╗  ██████╗██╗  ██╗███████╗██████╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║  ██║██║   ██║██║     █████╔╝ █████╗  ██████╔╝
██║  ██║██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

 █████╗  ██████╗ ███████╗███╗   ██╗████████╗
██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝
███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║
██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║
██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝
```

Docker Agent brings practical, safe automation workflows into Codex sessions.

## Top Skills
- `bump-go-dependencies`

## What It Can Do
- Automates direct Go dependency bumping with one-dependency-at-a-time safety.
- Validates each bump with lint/tests before commit.
- Produces PR-ready markdown summaries of bumped vs skipped modules.

## Why Use It
- Reduces risky bulk upgrades that break builds.
- Makes dependency maintenance repeatable and auditable.
- Preserves engineering velocity with explicit pass/fail gating.

## How It Works
1. Enumerate outdated direct dependencies.
2. Upgrade, tidy, lint, and test each dependency independently.
3. Commit passing bumps and skip failing ones with reasons.

## Quick Examples

```
Use docker-agent:bump-go-dependencies to safely update direct Go dependencies and summarize results
```

## Requirements
- Go toolchain available in the target repository.
- `task lint` and `task test` commands available (or equivalent validation commands).
