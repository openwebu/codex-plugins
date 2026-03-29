#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: bash scripts/new-plugin.sh <plugin-name> [scaffold-options...]

Rules:
- plugin name is normalized by the Python scaffolder (example: `My Plugin` -> `my-plugin`)
- plugin name must include at least one letter or digit
Notes:
- This wrapper calls the canonical Python scaffolder.
- Additional flags are forwarded to the Python scaffolder.
USAGE
}

title_case() {
  echo "$1" | tr '-' ' ' | awk '{for (i = 1; i <= NF; i++) $i = toupper(substr($i,1,1)) substr($i,2); print}'
}

run_python_script() {
  local script_path="$1"
  shift
  if command -v python3 >/dev/null 2>&1; then
    python3 "$script_path" "$@"
  elif command -v python >/dev/null 2>&1; then
    python "$script_path" "$@"
  elif [[ -x "$script_path" ]]; then
    "$script_path" "$@"
  else
    echo "[new-plugin] ERROR: no usable Python runtime found for $script_path" >&2
    exit 1
  fi
}

if [[ $# -lt 1 ]]; then
  usage
  exit 1
fi

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
  usage
  exit 0
fi

plugin_name="$1"
shift
if [[ -z "$plugin_name" ]]; then
  echo "[new-plugin] ERROR: invalid plugin name '$plugin_name'" >&2
  usage
  exit 1
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
sync_script="$repo_root/scripts/sync_plugins_to_marketplace.py"
scaffold_script="$repo_root/.agents/skills/plugin-creator/scripts/create_basic_plugin.py"

display_name="$(title_case "$plugin_name")"

if [[ ! -f "$scaffold_script" ]]; then
  echo "[new-plugin] ERROR: missing scaffold script at $scaffold_script" >&2
  exit 1
fi

echo "[new-plugin] Creating plugin: $plugin_name"
run_python_script "$scaffold_script" "$plugin_name" --with-marketplace "$@"

echo "[new-plugin] Syncing marketplace..."
run_python_script "$sync_script"

echo "[new-plugin] Done. Next commands:"
echo "  git add plugins/$plugin_name .agents/plugins/marketplace.json"
echo "  git commit -m \"Add $display_name plugin\""
echo "  git push"
