---
name: docker-debug-containers
description: Debug Docker container failures using inspect, logs, exec, resource checks, and targeted remediation steps
---

# Docker Debug Containers

Use this skill when containers fail to start, restart repeatedly, or behave unexpectedly.

## 1. Capture Container State

Start with high-signal status output:

```sh
docker ps -a --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
```

Then inspect the target container:

```sh
docker inspect <container>
```

Extract:
- exit code,
- restart count/policy,
- health status,
- mounted volumes,
- network attachment.

## 2. Read Logs with Scope

Get recent logs:

```sh
docker logs --tail 200 <container>
```

If the issue is timing-sensitive, follow logs:

```sh
docker logs -f <container>
```

Capture the first actionable error lines instead of dumping unfiltered output.

## 3. Run In-Container Checks

Use `exec` for runtime validation:

```sh
docker exec -it <container> sh
```

Check process health, config files, env values, connectivity, and required binaries.

## 4. Check Host and Resource Signals

Use non-streaming stats for quick pressure checks:

```sh
docker stats --no-stream
```

Investigate network/volume dependencies as needed:

```sh
docker network inspect <network>
docker volume inspect <volume>
```

## 5. Provide Remediation Path

Offer targeted next actions based on observed evidence:
- config/env fixes,
- image rebuilds,
- dependency service startup ordering,
- restart policy adjustments,
- container recreate (`docker rm` + `docker run`/`docker compose up`) when safe and requested.

## 6. Return a Debug Report

Return:
- symptom summary,
- root-cause hypothesis,
- evidence (commands + key outputs),
- specific remediation steps,
- validation command to confirm fix.

