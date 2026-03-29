# CODEX PLUGINS

The plugin workspace for Codex.

Built for humans, AI agents, and CI/CD pipelines.

```text
 ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗    ██████╗ ██╗     ██╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝    ██╔══██╗██║     ██║   ██║██╔════╝ ██║████╗  ██║██╔════╝
██║     ██║   ██║██║  ██║█████╗   ╚███╔╝     ██████╔╝██║     ██║   ██║██║  ███╗██║██╔██╗ ██║███████╗
██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗     ██╔═══╝ ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██████╔╝███████╗██╔╝ ██╗    ██║     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
```

## 2-minute setup

Clone and open the repo (any location is fine):

```bash
git clone https://github.com/openwebu/codex-plugins.git
cd codex-plugins
```

### Linux

```bash
bash scripts/install_linux.sh
```

### Windows (Git Bash)

```bash
bash scripts/install_windows.sh
```

## Check it worked

```bash
ls -l "$HOME/plugins"
ls -l "$HOME/.agents/plugins/marketplace.json"
scripts/sync_plugins_to_marketplace.py --dry-run
```

Expected:

- `~/plugins` points to this repo `plugins/`
- `~/.agents/plugins/marketplace.json` points to this repo marketplace

## Add your first plugin

```bash
bash scripts/new-plugin.sh my-plugin
```

This creates the plugin scaffold, syncs marketplace, and prints the exact `git add`, `git commit`, and `git push` commands.

## Need advanced options?

See [docs/setup-reference.md](docs/setup-reference.md) for:

- manual setup commands
- manual plugin creation flow
- repo structure and optional plugin surfaces
- troubleshooting notes

## License

MIT
