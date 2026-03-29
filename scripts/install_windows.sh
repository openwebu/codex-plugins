#!/usr/bin/env bash
set -euo pipefail

step() {
  printf '\n[install-windows] %s\n' "$1"
}

fail() {
  printf '[install-windows] ERROR: %s\n' "$1" >&2
  exit 1
}

link_checked() {
  local source="$1"
  local target="$2"
  if [[ -e "$target" && ! -L "$target" ]]; then
    fail "Target exists and is not a symlink: $target (move/remove it, then rerun)"
  fi
  if ! ln -sfn "$source" "$target"; then
    fail "Could not create symlink for $target. Enable Windows Developer Mode or run Git Bash as Administrator."
  fi
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
sync_script="$repo_root/scripts/sync_plugins_to_marketplace.py"

step "Step 1/4: Validate shell"
echo "[install-windows] Repo root: $repo_root"
if [[ "${OSTYPE:-}" != msys* && "${OSTYPE:-}" != cygwin* && "${OSTYPE:-}" != win32* ]]; then
  echo "[install-windows] Warning: non-Windows shell detected; continuing anyway."
fi

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
elif command -v python >/dev/null 2>&1; then
  python "$sync_script"
else
  fail "sync script is not executable and no Python runtime was found"
fi

printf '\n[install-windows] Install complete.\n'
echo "[install-windows] Linked:"
echo "  $HOME/plugins -> $repo_root/plugins"
echo "  $HOME/.agents/plugins/marketplace.json -> $repo_root/.agents/plugins/marketplace.json"
echo "[install-windows] Next: bash scripts/new-plugin.sh my-plugin"
echo "[install-windows] If symlink errors persist: enable Developer Mode or run Git Bash as Administrator."
