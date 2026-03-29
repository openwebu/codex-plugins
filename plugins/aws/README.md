# aws Plugin

Build and operate AWS workloads, including OpenAI-integrated systems.

## Overview

This plugin provides AWS-focused guidance for OpenAI-powered systems:

1. Architecture and service selection
2. Secure API key and secret handling
3. Deployment patterns for serverless and containerized workloads
4. Operational troubleshooting for latency, reliability, and cost
5. Cost controls and reliability guardrails

## Skills

| Skill | Description |
| --- | --- |
| `aws-workflow` | Primary end-to-end AWS + OpenAI implementation workflow |
| `aws-openai-workflow` | Backward-compatible alias for legacy references |

## Quick Start (Core MCP Default)

1. Run prerequisite checks:

```bash
bash scripts/prereq-check.sh
```

2. Set up core AWS MCP integration for Codex:

```bash
bash scripts/install-mcp.sh
```

3. Verify MCP setup:

```bash
codex mcp list
```

## Optional: Full AWS MCP Suite (Opt-in)

To generate a full MCP configuration snippet (pricing, IaC, serverless, DSQL):

```bash
bash scripts/install-mcp-full.sh
```

By default, write-capable/advanced servers are printed with `disabled: true`.
Enable only what you need.

## MCP Servers

| Server | Description |
| --- | --- |
| `aws-mcp` | Core AWS CLI MCP proxy (`uvx mcp-proxy-for-aws@latest`) |
| `awsknowledge` | AWS knowledge endpoint (optional full-suite) |
| `awsiac` | AWS IaC MCP server (optional full-suite, disabled by default) |
| `awspricing` | AWS pricing MCP server (optional full-suite, disabled by default) |
| `aws-serverless-mcp` | AWS serverless MCP server (optional full-suite, disabled by default) |
| `aurora-dsql` | Aurora DSQL MCP server (optional full-suite, disabled by default) |

## Prerequisites

- AWS CLI configured for your target account
- `uvx` available locally
- Node.js and Python 3 available
- OpenAI API key available for local development or in AWS Secrets Manager

## Example prompts

- "Design an AWS architecture for a chat API that uses OpenAI"
- "Securely store and rotate the OpenAI API key in AWS"
- "Reduce cost and latency for OpenAI calls from Lambda"
- "Set up observability and incident response for OpenAI traffic on AWS"

## Files

- `skills/aws-workflow/SKILL.md` - Primary orchestration workflow
- `skills/aws-openai-workflow/SKILL.md` - Backward-compat alias
- `scripts/prereq-check.sh` - Local prerequisite validator
- `scripts/install-mcp.sh` - Core MCP setup helper
- `scripts/install-mcp-full.sh` - Full-suite MCP config helper
