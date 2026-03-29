---
name: docker-publish-images
description: Publish Docker images with registry-agnostic tagging and push workflows for Docker Hub, GHCR, and private registries
---

# Docker Publish Images

Use this skill when the user asks to publish images to any container registry.

## 1. Define Registry-Agnostic Coordinates

Normalize every target image as:

```text
<registry>/<namespace>/<repo>:<tag>
```

Examples:
- `docker.io/acme/api:1.2.0`
- `ghcr.io/acme/api:1.2.0`
- `registry.example.com/team/api:1.2.0`

Do not assume Docker Hub defaults when the registry is provided explicitly.

## 2. Authenticate to Target Registry

Authenticate first:

```sh
docker login <registry>
```

Never print secrets or tokens in output.

## 3. Tag and Push

Tag local image(s):

```sh
docker tag <local-image>:<local-tag> <registry>/<namespace>/<repo>:<tag>
```

Push each required tag:

```sh
docker push <registry>/<namespace>/<repo>:<tag>
```

If multi-arch output is explicitly requested, prefer buildx:

```sh
docker buildx build --platform linux/amd64,linux/arm64 -t <registry>/<namespace>/<repo>:<tag> --push <context>
```

## 4. Verify Published References

Verify the pushed manifest:

```sh
docker manifest inspect <registry>/<namespace>/<repo>:<tag>
```

If inspect fails, report publish as incomplete and include next checks.

## 5. Return Publish Summary

Return a copy-pastable markdown table in a fenced code block:
- registry,
- repository,
- tags,
- push result,
- verification result.

