#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

bash "$ROOT_DIR/scripts/prereq-check.sh"

echo
echo "[aws] Core MCP setup (default): aws-mcp"
echo

echo "Add this server to Codex:"
echo '  codex mcp add aws-mcp -- uvx "mcp-proxy-for-aws@latest" "https://aws-mcp.us-east-1.api.aws/mcp"'
echo
echo "Or use plugin-local config already provided at:"
echo "  $ROOT_DIR/.mcp.json"
echo

echo "Verify:"
echo "  codex mcp list"
echo "  /mcp"
