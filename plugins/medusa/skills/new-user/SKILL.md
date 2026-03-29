---
name: new-user
description: Create an admin user in Medusa
argument-hint: <email> [password]
allowed-tools: Bash(npx medusa user:*)
---

# Create Admin User

Create a new admin user in Medusa using docs-canonical flags.

The user provides:
- First argument: email address (required)
- Second argument: password (optional)

For example:
- `/medusa:new-user admin@test.com supersecret`
- `/medusa:new-user admin@test.com` (creates an invite)

Use the Bash tool:
- If password is provided: `npx medusa user --email <email> --password <password>`
- If password is omitted: `npx medusa user --email <email> --invite`

Equivalent package manager form: `yarn medusa user --email <email> [--password <password> | --invite]`.

Report the results to the user, including:

- Confirmation that the admin user or invite was created successfully
- The email address of the created user
- Invite token output (if `--invite` was used)
- Any errors that occurred
- Next steps (e.g., accepting invite or logging in to the admin dashboard)
