---
name: docker-build-local-images
description: Build local Docker images with explicit context/Dockerfile/tag inputs, smoke-test validation, and a concise build report
---

# Docker Build Local Images

Use this skill when the user asks to build or rebuild a local image from a repository Dockerfile.

## 1. Confirm Build Inputs

Collect and confirm:
- build context path,
- Dockerfile path,
- target image name and tag,
- optional target stage, build args, and platform.

If inputs are missing, infer safe defaults:
- context: `.`
- Dockerfile: `./Dockerfile`
- tag: `local` or `dev`.

## 2. Run the Build

Use the standard command shape:

```sh
docker build -f <dockerfile> -t <image>:<tag> <context>
```

Add optional flags only when needed:
- `--target <stage>`
- `--build-arg KEY=VALUE`
- `--platform <os/arch>`

Do not claim success without a successful build exit.

## 3. Validate Built Artifact

Check resulting metadata:

```sh
docker image inspect <image>:<tag> --format 'ID={{.Id}} SIZE={{.Size}}'
```

Optionally verify layer history:

```sh
docker history <image>:<tag>
```

## 4. Run a Smoke Test

Run a minimal container validation when possible:

```sh
docker run --rm <image>:<tag> <cmd>
```

Use project-appropriate smoke commands (`--help`, version output, health endpoint check) instead of interactive flows.

## 5. Report Output

Return a short summary table in a fenced markdown block:
- image tag,
- build status,
- smoke test status,
- notes.

If build fails, include the failing command and the first actionable fix path.

