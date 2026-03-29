# docker

Docker brings container-first workflows into Codex sessions, from local image builds to registry publishing and production-style debugging.

## Top Skills
- `docker-build-local-images`
- `docker-compose-dev-loop`
- `docker-publish-images`
- `docker-debug-containers`

## Secondary Skills
- `audit-go-dependencies`
- `triage-go-vulnerabilities`
- `plan-go-major-upgrades`
- `bump-go-dependencies`

## What It Can Do
- Build local images with explicit Dockerfile/context/tag control.
- Run efficient Docker Compose development loops with service-focused rebuilds.
- Publish images with a registry-agnostic flow (Docker Hub, GHCR, or private registries).
- Debug unhealthy or failing containers with logs, inspect output, exec checks, and resource signals.
- Support Go maintenance workflows as secondary capabilities when dependency health work is needed.

## Why Use It
- Standardizes local container workflows across teams and projects.
- Reduces release friction by using repeatable image tagging and publish patterns.
- Speeds up issue triage by structuring debug steps instead of ad-hoc command chains.
- Keeps Go dependency maintenance available without making it the default plugin path.

## How It Works
1. Build and validate local images.
2. Run compose stacks for iterative development.
3. Push tested image tags to the target registry.
4. Debug runtime issues with container-first diagnostics.
5. Use Go-maintenance skills only when dependency/security work is explicitly requested.

## Quick Examples

```text
Use docker:docker-build-local-images to build an image from ./Dockerfile and run a smoke test
Use docker:docker-compose-dev-loop to boot docker compose services and focus logs on the api service
Use docker:docker-publish-images to push ghcr.io/org/app:1.4.0 and ghcr.io/org/app:latest
Use docker:docker-debug-containers to investigate a restarting container with inspect, logs, and exec checks
Use docker:audit-go-dependencies to generate a prioritized Go dependency health report (secondary capability)
```

## Requirements
- Docker Engine with `docker` CLI and Compose plugin (`docker compose`).
- Registry credentials for publish operations (`docker login` to Docker Hub, GHCR, or private registry).
- Go toolchain only when using secondary Go maintenance skills.
