---
name: aws-openai-workflow
description: Use when planning, implementing, or operating AWS workloads that call OpenAI APIs, including architecture, security, deployment, and troubleshooting.
---

Use this workflow whenever the user is building with OpenAI on AWS.

Before implementation, run the prerequisite check:

```bash
bash scripts/prereq-check.sh
```

## Execution order

1. Clarify runtime and scale assumptions:
- Expected request volume and latency targets
- Deployment target (`Lambda`, `ECS/Fargate`, `EC2`, or mixed)
- Data residency and compliance constraints

2. Pick a deployment pattern:
- `Lambda + API Gateway` for bursty traffic and quick iteration
- `ECS/Fargate` for steady throughput or longer-running tasks
- Queue-based async processing (`SQS`, `EventBridge`) for long operations
- See `references/architecture.md`

3. Enforce security baseline:
- Store OpenAI credentials in `AWS Secrets Manager`
- Use least-privilege IAM for runtime and CI/CD roles
- Avoid logging sensitive prompt or credential data
- See `references/security.md`

4. Add reliability and operations:
- Exponential backoff and idempotency around OpenAI requests
- Structured logs and metrics (`CloudWatch`) with request correlation IDs
- Alerting on error rate, p95 latency, and token/cost anomalies
- See `references/operations.md`

5. Optimize cost and latency:
- Cache deterministic outputs where appropriate
- Batch or async non-interactive jobs
- Set explicit model and token budgets per route
- See `references/architecture.md`

## Deliverable format

When proposing implementation:
- Provide target AWS architecture
- List required AWS resources
- Provide deployment and secrets steps
- Include observability and rollback strategy

## Output contract

For requests that ask for implementation guidance, provide:

1. A recommended AWS topology diagram in words
2. An IAM and secrets plan
3. A deployment checklist
4. An observability and incident response checklist
