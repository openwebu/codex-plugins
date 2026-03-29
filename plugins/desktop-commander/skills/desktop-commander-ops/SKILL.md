---
name: desktop-commander-ops
description: Use when the user wants Codex to run Desktop Commander MCP tools for local file, process, or terminal workflows.
---

# Desktop Commander Operations

Use Desktop Commander MCP tools for local machine operations in Codex sessions.

## Use This Skill When

- User wants `desktop-commander.read_file`, `list_directory`, `edit_block`, or similar file operations.
- User needs local process workflows (`start_process`, `interact_with_process`) for CSV/JSON/data analysis.
- User asks for command execution with streamed output and process control.

## Preferred Workflow

1. Confirm target path and task scope.
2. Use the safest Desktop Commander tool first:
   - read-only: `read_file`, `list_directory`, `get_file_info`
   - search: `start_search` + `get_more_search_results`
   - edits: `edit_block` or `write_file`
   - process execution: `start_process` + `interact_with_process`
3. Summarize the command/tool result with:
   - what was executed
   - key output lines
   - success/failure status
   - next action

## Data Analysis Rule

For local data analysis, prefer:

1. `start_process` with `python3 -i`
2. `interact_with_process` for imports + file reads
3. `interact_with_process` for analysis steps

Do not rely on external analysis tools when the data is local and Desktop Commander can access it directly.

## Safety Requirements

- Ask for explicit confirmation before destructive actions (delete/reset/overwrites with data-loss risk).
- Use absolute paths when practical.
- Avoid dangerous shell commands unless the user explicitly requests them.

