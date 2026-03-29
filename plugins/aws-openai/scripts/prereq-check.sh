#!/usr/bin/env bash
set -euo pipefail

echo "[aws-openai] Running prerequisite checks..."

missing=0

check_cmd() {
  local cmd="$1"
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "  [ok] $cmd"
  else
    echo "  [missing] $cmd"
    missing=1
  fi
}

check_cmd aws
check_cmd node
check_cmd python3

if command -v aws >/dev/null 2>&1; then
  if aws sts get-caller-identity >/dev/null 2>&1; then
    echo "  [ok] AWS credentials are configured"
  else
    echo "  [warn] AWS CLI is installed but credentials are not configured"
    echo "         Run: aws configure"
  fi
fi

if [[ -n "${OPENAI_API_KEY:-}" ]]; then
  echo "  [ok] OPENAI_API_KEY is set in current shell"
else
  echo "  [warn] OPENAI_API_KEY is not set in current shell"
  echo "         For production on AWS, store it in Secrets Manager."
fi

if [[ "$missing" -eq 1 ]]; then
  echo "[aws-openai] Prerequisite check failed."
  exit 1
fi

echo "[aws-openai] Prerequisite check passed."
