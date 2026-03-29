#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

bash "$ROOT_DIR/scripts/prereq-check.sh"

echo
echo "[aws] Full-suite MCP config (opt-in)"
echo "Write-capable servers are disabled by default."
echo
cat <<'JSON'
{
  "mcpServers": {
    "aws-mcp": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://aws-mcp.us-east-1.api.aws/mcp"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "timeout": 120000
    },
    "awsknowledge": {
      "type": "http",
      "url": "https://knowledge-mcp.global.api.aws"
    },
    "awsiac": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "awslabs.aws-iac-mcp-server@latest"
      ],
      "disabled": true
    },
    "awspricing": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "awslabs.aws-pricing-mcp-server@latest"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "timeout": 120000,
      "disabled": true
    },
    "aws-serverless-mcp": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "awslabs.aws-serverless-mcp-server@latest",
        "--allow-write"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "timeout": 120000,
      "disabled": true
    },
    "aurora-dsql": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "awslabs.aurora-dsql-mcp-server@latest"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": true
    }
  }
}
JSON

echo
echo "Copy this into your Codex MCP config, then enable only the servers you need."
echo "Recommended first enable: aws-mcp"
