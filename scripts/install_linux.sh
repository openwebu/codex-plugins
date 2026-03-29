#!/usr/bin/env bash
set -euo pipefail

step() {
  printf '\n[install-linux] %s\n' "$1"
}

fail() {
  printf '[install-linux] ERROR: %s\n' "$1" >&2
  exit 1
}

link_checked() {
  local source="$1"
  local target="$2"
  if [[ -e "$target" && ! -L "$target" ]]; then
    fail "Target exists and is not a symlink: $target (move/remove it, then rerun)"
  fi
  ln -sfn "$source" "$target"
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
sync_script="$repo_root/scripts/sync_plugins_to_marketplace.py"

step "Step 1/4: Detect repository root"
echo "[install-linux] Repo root: $repo_root"

step "Step 2/4: Link global plugin paths"
link_checked "$repo_root/plugins" "$HOME/plugins"
mkdir -p "$HOME/.agents/plugins"
link_checked "$repo_root/.agents/plugins/marketplace.json" "$HOME/.agents/plugins/marketplace.json"

step "Step 3/4: Enable pre-push hook path"
git -C "$repo_root" config core.hooksPath .githooks

step "Step 4/4: Run initial marketplace sync"
if [[ -x "$sync_script" ]]; then
  "$sync_script"
elif command -v python3 >/dev/null 2>&1; then
  python3 "$sync_script"
else
  fail "sync script is not executable and python3 is not available"
fi

printf '\n[install-linux] Install complete.\n'
echo "[install-linux] Linked:"
echo "  $HOME/plugins -> $repo_root/plugins"
echo "  $HOME/.agents/plugins/marketplace.json -> $repo_root/.agents/plugins/marketplace.json"
echo "[install-linux] Next: bash scripts/new-plugin.sh my-plugin"
