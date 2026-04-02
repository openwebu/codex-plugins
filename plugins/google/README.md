# Google

## Top Skills

- `mapi-developer-assistant`

## What It Can Do

- Provides domain guidance for Google Merchant API integrations.
- Helps migrate Shopping integrations from Content API to Merchant API.
- Troubleshoots Merchant API errors and suggests concrete fixes.
- Includes ready-to-run shell scripts for Merchant API docs and code-sample MCP queries.

## Why Use It

- Reduces trial-and-error during Merchant API development.
- Speeds up migration planning with focused API-specific guidance.
- Gives a repeatable way to query docs and code samples from the terminal.

## How It Works

1. Activate `mapi-developer-assistant` for Merchant API questions.
2. Use provided shell scripts to query docs and code samples over Merchant API MCP endpoint.
3. Apply migration/troubleshooting guidance to your integration code.

## Quick Examples

```text
How do I insert a product using the Merchant API in Python?
```

```bash
plugins/google/scripts/query_mapi_docs.sh "What is the difference between ProductInput and Product?"
```

```bash
plugins/google/scripts/find_mapi_code_sample.sh "insert product" java
```

## Requirements

- Access to Google Merchant API documentation and credentials for your integration context.
- `bash` and `curl` available for running helper scripts.
- Merchant API MCP endpoint reachable at `https://merchantapi.googleapis.com/devdocs/mcp/`.
