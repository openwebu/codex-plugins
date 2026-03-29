# ssh-skill

```
███████╗███████╗██╗  ██╗      ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗
██╔════╝██╔════╝██║  ██║      ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
███████╗███████╗███████║█████╗███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
╚════██║╚════██║██╔══██║╚════╝╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
███████║███████║██║  ██║      ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝      ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
```

Secure, reusable SSH access for Codex sessions, plus remote Supabase CLI execution.

## Top Skills
- `remote-supabase-ops`
- `setup-profile`

## What It Can Do
- Sets up reusable host aliases in `~/.ssh/config`.
- Connects safely with SSH key-based authentication.
- Runs Supabase CLI commands remotely through SSH wrappers.
- Enforces confirmation gates for destructive database operations.

## Why Use It
- Standardizes remote access across environments and teammates.
- Keeps credentials out of repo files by default.
- Makes sensitive remote operations safer and easier to audit.

## How It Works
1. Configure SSH profile aliases for each target environment.
2. Validate connectivity with non-destructive commands.
3. Execute operational commands through approved SSH workflows.

## Quick Examples

```
ssh prod-eu 'supabase --version'
```

```
ssh prod-eu 'supabase status'
```

## Requirements
- SSH key-based access to target hosts.
- Supabase CLI installed on the remote host.
- Explicit user confirmation before destructive database commands.
