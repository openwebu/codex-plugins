# desktop-commander

```
██████╗ ███████╗███████╗██╗  ██╗████████╗ ██████╗ ██████╗
██╔══██╗██╔════╝██╔════╝██║ ██╔╝╚══██╔══╝██╔═══██╗██╔══██╗
██║  ██║█████╗  ███████╗█████╔╝    ██║   ██║   ██║██████╔╝
██║  ██║██╔══╝  ╚════██║██╔═██╗    ██║   ██║   ██║██╔═══╝
██████╔╝███████╗███████║██║  ██╗   ██║   ╚██████╔╝██║
╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝
```

Run local filesystem and terminal workflows in Codex through Desktop Commander MCP.

## Top Skills
- `desktop-commander-ops`

## What It Can Do
- Connects Codex to the official Desktop Commander MCP server.
- Reads, writes, and edits local files with path-safe operations.
- Runs terminal commands and interactive processes with controlled output.
- Supports local data workflows for CSV/JSON/Excel/PDF/DOCX using MCP tools.

## Why Use It
- Gives Codex reliable local-machine execution and file tooling in one plugin.
- Keeps repeatable operational patterns in a reusable skill.
- Reduces friction for project inspection, edits, and process-driven analysis.

## How It Works
1. Install the plugin in Codex.
2. Load the `desktop-commander-ops` skill for local operations.
3. Execute Desktop Commander MCP tools by task type (read/search/edit/process).

## Quick Examples

```text
Use /desktop-commander:desktop-commander-ops and read /home/deadpool/Documents/OPENAI/plugins/README.md
```

```text
Use desktop-commander to list /home/deadpool/Documents/OPENAI/plugins/plugins with depth 2 and summarize the plugin structure
```

```text
Use desktop-commander process tools to open python3 -i and inspect a local CSV at /absolute/path/data.csv
```

## Requirements
- `npx` available in the runtime environment.
- Access to install/run `@wonderwhy-er/desktop-commander`.
- Local filesystem permissions for the paths being accessed.

