---
name: mapi-developer-assistant
description: Use for Google Merchant API documentation questions, Content API migration guidance, code generation, and API error troubleshooting.
---

# Merchant API Developer Assistant

Use this skill when the user is working on Google Merchant API (Shopping) integrations.

## Best for

- Merchant API resource/method/field questions
- Migration from Content API to Merchant API
- Language-specific snippets (Python, Java, PHP, etc.)
- Diagnosing 4xx/5xx Merchant API errors and validation failures

## Core workflow

1. Clarify target account, API resource, and operation.
2. Identify whether the request is greenfield integration or Content API migration.
3. Provide minimal, idiomatic code + request/response structure.
4. For errors, map error payload -> likely root cause -> concrete fix steps.
5. End with a short verification checklist.

## High-value prompts

```text
How do I insert a product using the Merchant API in Python?
```

```text
What is the difference between ProductInput and Product?
```

```text
I get 400 Bad Request with validation errors. Help me fix it.
```

## Installation notes (source skill)

Merchant API skill source repository:

```bash
git clone https://github.com/google/merchant-api-samples.git
```

Skill path in that repository:

```text
agent-skills/mapi-developer-assistant
```

### Gemini CLI setup

```bash
npm install -g @google/gemini-cli@latest
gemini config set experimental.skills true
```

Install skill locally from the source repo path:

```bash
cd merchant-api-samples/agent-skills/mapi-developer-assistant
gemini skills install .
gemini skills list
```

### Claude / other agents setup

Copy the skill directory into your agent skills folder and ensure `SKILL.md` plus references are readable.

Example for Claude Code:

```bash
mkdir -p .claude/skills/
cp -r merchant-api-samples/agent-skills/mapi-developer-assistant .claude/skills/
```

## MCP helper scripts in this plugin

This plugin also provides two shell helpers:

- `plugins/google/scripts/query_mapi_docs.sh`
- `plugins/google/scripts/find_mapi_code_sample.sh`

Examples:

```bash
plugins/google/scripts/query_mapi_docs.sh "How do I insert a product in Merchant API?"
```

```bash
plugins/google/scripts/find_mapi_code_sample.sh "insert product" python
```
