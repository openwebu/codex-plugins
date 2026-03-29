---
name: docker-compose-dev-loop
description: Run a Docker Compose development loop with config validation, service-focused rebuilds, logs, and clean shutdown guidance
---

# Docker Compose Dev Loop

Use this skill for `docker compose` local development workflows.

## 1. Validate Compose Config

Before starting services, validate the effective config:

```sh
docker compose config
```

If config resolution fails, stop and report the concrete error.

## 2. Start the Stack

Use one of:

```sh
docker compose up --build
```

or detached mode:

```sh
docker compose up --build -d
```

Pick detached mode when the user wants background services and separate log commands.

## 3. Focus the Edit-Run Loop

Use service-level commands for fast iteration:

```sh
docker compose logs -f <service>
docker compose up -d --build <service>
docker compose exec <service> <command>
```

Avoid full-stack rebuilds unless needed.

## 4. Inspect Runtime State

Check service status:

```sh
docker compose ps
```

If failures occur, capture:
- failing service name,
- exit/restart behavior,
- key error lines from logs.

## 5. Stop and Clean Up

Default cleanup:

```sh
docker compose down
```

Use volume removal only when explicitly requested:

```sh
docker compose down -v
```

## 6. Return Dev-Loop Summary

Return a concise status report:
- started services,
- rebuilt services,
- failing services (if any),
- cleanup action taken.

