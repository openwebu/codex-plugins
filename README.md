# CODEX PLUGINS

A plugin workspace for Codex.

Built for humans, AI agents, and CI/CD pipelines.

```text
 ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗    ██████╗ ██╗     ██╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝    ██╔══██╗██║     ██║   ██║██╔════╝ ██║████╗  ██║██╔════╝
██║     ██║   ██║██║  ██║█████╗   ╚███╔╝     ██████╔╝██║     ██║   ██║██║  ███╗██║██╔██╗ ██║███████╗
██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗     ██╔═══╝ ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██████╔╝███████╗██╔╝ ██╗    ██║     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
```

## Quick install

Run from this repo root (`$HOME/Documents/OPENAI/plugins` by default):

### Linux

```bash
bash scripts/install_linux.sh
```

### Windows (Git Bash)

```bash
bash scripts/install_windows.sh
```

## Success check

```bash
ls -l "$HOME/plugins"
ls -l "$HOME/.agents/plugins/marketplace.json"
git config --get core.hooksPath
scripts/sync_plugins_to_marketplace.py --dry-run
```

Expected:

- `~/plugins` points to this repo's `plugins/`
- `~/.agents/plugins/marketplace.json` points to this repo marketplace
- `core.hooksPath` is `.githooks`

---

## Add a new plugin (fast path)

```bash
bash scripts/new-plugin.sh my-plugin
```

This command will:

- validate the plugin name (`lowercase-hyphen`)
- create `plugins/<name>/.codex-plugin/plugin.json`
- run marketplace sync automatically
- print exact `git add`, `git commit`, and `git push` commands

### Manual fallback

```bash
mkdir -p plugins/my-plugin/.codex-plugin
cat > plugins/my-plugin/.codex-plugin/plugin.json <<'JSON'
{
  "name": "my-plugin",
  "interface": {
    "displayName": "My Plugin"
  }
}
JSON

scripts/sync_plugins_to_marketplace.py
git add plugins/my-plugin .agents/plugins/marketplace.json
git commit -m "Add my-plugin"
git push
```

---

## Automatic sync on push

This repo uses `.githooks/pre-push`.

On every `git push`, it runs:

```bash
scripts/sync_plugins_to_marketplace.py
```

If marketplace changes are detected and not committed, push is blocked so you can commit first.

---

## Advanced / manual setup

Use this if you want full manual control instead of installer scripts.

```bash
REPO_DIR="${REPO_DIR:-$HOME/Documents/OPENAI/plugins}"
cd "$REPO_DIR"

ln -sfn "$REPO_DIR/plugins" "$HOME/plugins"
mkdir -p "$HOME/.agents/plugins"
ln -sfn "$REPO_DIR/.agents/plugins/marketplace.json" "$HOME/.agents/plugins/marketplace.json"

git config core.hooksPath .githooks
scripts/sync_plugins_to_marketplace.py
```

---

## What this repo contains

Each plugin lives under `plugins/<name>/` and must include:

- `.codex-plugin/plugin.json`

Optional plugin surfaces:

- `skills/`
- `.app.json`
- `.mcp.json`
- plugin-level `agents/`
- `commands/`
- `hooks.json`
- `assets/`

## License

MIT
