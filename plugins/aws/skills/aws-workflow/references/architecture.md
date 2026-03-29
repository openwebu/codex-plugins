# AWS + OpenAI Architecture

## Pattern selection

- Use `API Gateway + Lambda` for low-to-medium traffic, bursty workloads, and simple ops.
- Use `ALB + ECS/Fargate` for stable throughput, long-running requests, or custom networking.
- Use async pipelines (`SQS`, `EventBridge`, `Step Functions`) for non-interactive generation jobs.

## Baseline components

- Compute:
- `Lambda` for sync request/response APIs
- `ECS/Fargate` for sustained high throughput
- Integration:
- OpenAI API over outbound HTTPS
- `Secrets Manager` for API keys
- Data:
- `DynamoDB` for request metadata and idempotency keys
- `S3` for input/output artifacts
- Networking:
- `VPC` only if needed for private dependencies; avoid unnecessary NAT costs

## Request path guidance

1. Validate input early and enforce token budget limits.
2. Attach a correlation ID to every request.
3. Use bounded retries with exponential backoff on transient OpenAI failures.
4. Persist request metadata and model usage for auditing and cost controls.
5. Return graceful fallbacks when upstream model calls fail.

## Cost controls

- Define per-route model defaults and max token caps.
- Apply caching for deterministic prompts and retrieval outputs.
- Prefer async processing for heavy generation workloads.
- Emit usage metrics by route, model, and tenant.
