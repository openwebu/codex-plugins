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
| `aws-openai-workflow` | Guides end-to-end AWS + OpenAI implementation choices and execution flow |

## MCP Servers

| Server | Description |
| --- | --- |
| `aws-mcp` | AWS CLI MCP proxy (`uvx mcp-proxy-for-aws@latest`) for AWS documentation and service workflows |

## Prerequisites

- AWS CLI configured for your target account
- Node.js and Python 3 available
- OpenAI API key available for local development or in AWS Secrets Manager

Validate your environment:

```bash
bash scripts/prereq-check.sh
```

## Example prompts

- "Design an AWS architecture for a chat API that uses OpenAI"
- "Securely store and rotate the OpenAI API key in AWS"
- "Reduce cost and latency for OpenAI calls from Lambda"
- "Set up observability and incident response for OpenAI traffic on AWS"

## Files

- `skills/aws-openai-workflow/SKILL.md` - Main orchestration workflow
- `skills/aws-openai-workflow/references/architecture.md` - Deployment and topology patterns
- `skills/aws-openai-workflow/references/security.md` - IAM, secrets, and data protection baseline
- `skills/aws-openai-workflow/references/operations.md` - Reliability and troubleshooting playbook
- `scripts/prereq-check.sh` - Local prerequisite validator
