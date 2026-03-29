---
description: Create a Medusa admin user with canonical CLI flags or create a user invite.
---

# Create Medusa Admin User

Use `/medusa:new-user` to create a user directly or create an invite.

## Usage

- Direct user creation:
`/medusa:new-user admin@example.com supersecret`
- Invite flow (no password argument):
`/medusa:new-user admin@example.com`

## Command Mapping

Run one of the following:

```bash
npx medusa user --email <email> --password <password>
```

Or, when password is omitted:

```bash
npx medusa user --email <email> --invite
```

Equivalent form:

```bash
yarn medusa user --email <email> [--password <password> | --invite]
```

## Output to Report

- Whether user creation or invite creation succeeded.
- Email address used.
- Invite token (if invite flow was used).
- Errors and next step (admin login or invite acceptance).
