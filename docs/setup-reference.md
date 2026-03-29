# Setup Reference

Advanced and manual setup for `CODEX PLUGINS`.

## Manual setup (no installer scripts)

```bash
REPO_DIR="${REPO_DIR:-$HOME/Documents/OPENAI/plugins}"
cd "$REPO_DIR"

ln -sfn "$REPO_DIR/plugins" "$HOME/plugins"
mkdir -p "$HOME/.agents/plugins"
ln -sfn "$REPO_DIR/.agents/plugins/marketplace.json" "$HOME/.agents/plugins/marketplace.json"

git config core.hooksPath .githooks
scripts/sync_plugins_to_marketplace.py
```

## Plugin scaffold flow

```bash
bash scripts/new-plugin.sh my-plugin
git add plugins/my-plugin .agents/plugins/marketplace.json
git commit -m "Add my-plugin"
git push
```

## Advanced scaffold options

`scripts/new-plugin.sh` forwards extra options to the canonical Python scaffolder:

```bash
bash scripts/new-plugin.sh my-plugin \
  --with-skills --with-hooks --with-scripts --with-assets --with-mcp --with-apps \
  --install-policy AVAILABLE --auth-policy ON_INSTALL --category Productivity
```

## Repo structure

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

## Troubleshooting

### `ln: failed to create symbolic link` (Linux)

A non-symlink already exists at the target path. Move/remove it, then rerun install.

### Symlink errors on Windows

Use Git Bash, enable Windows Developer Mode, or run Git Bash as Administrator.

### `git push` blocked by pre-push hook

The sync script updated `.agents/plugins/marketplace.json` (or it was already dirty). Commit the file and push again:

```bash
git add .agents/plugins/marketplace.json
git commit -m "Sync marketplace"
git push
```
