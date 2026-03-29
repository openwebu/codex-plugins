#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: bash scripts/new-plugin.sh <plugin-name>

Rules:
- plugin name must be lowercase-hyphen (example: my-plugin)
- allowed chars: a-z, 0-9, -
- cannot start/end with '-'
USAGE
}

title_case() {
  echo "$1" | tr '-' ' ' | awk '{for (i = 1; i <= NF; i++) $i = toupper(substr($i,1,1)) substr($i,2); print}'
}

run_sync() {
  local sync_script="$1"
  if [[ -x "$sync_script" ]]; then
    "$sync_script"
  elif command -v python3 >/dev/null 2>&1; then
    python3 "$sync_script"
  elif command -v python >/dev/null 2>&1; then
    python "$sync_script"
  else
    echo "[new-plugin] ERROR: sync script is not executable and no Python runtime was found." >&2
    exit 1
  fi
}

if [[ $# -ne 1 ]]; then
  usage
  exit 1
fi

plugin_name="$1"
if [[ ! "$plugin_name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "[new-plugin] ERROR: invalid plugin name '$plugin_name'" >&2
  usage
  exit 1
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
plugin_dir="$repo_root/plugins/$plugin_name"
manifest_dir="$plugin_dir/.codex-plugin"
manifest_path="$manifest_dir/plugin.json"
sync_script="$repo_root/scripts/sync_plugins_to_marketplace.py"

display_name="$(title_case "$plugin_name")"

if [[ -e "$plugin_dir" ]]; then
  echo "[new-plugin] ERROR: plugin already exists at $plugin_dir" >&2
  exit 1
fi

echo "[new-plugin] Creating plugin: $plugin_name"
mkdir -p "$manifest_dir"

cat > "$manifest_path" <<JSON
{
  "name": "$plugin_name",
  "interface": {
    "displayName": "$display_name"
  }
}
JSON

echo "[new-plugin] Syncing marketplace..."
run_sync "$sync_script"

echo "[new-plugin] Done. Next commands:"
echo "  git add plugins/$plugin_name .agents/plugins/marketplace.json"
echo "  git commit -m \"Add $plugin_name plugin\""
echo "  git push"
