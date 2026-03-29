# Operations and Troubleshooting

## Observability minimums

- Emit structured logs with:
- `request_id`
- `tenant_id` (if applicable)
- `model`
- `latency_ms`
- `prompt_tokens`
- `completion_tokens`
- Create CloudWatch dashboards for:
- p50/p95 latency
- error rate by route
- token usage and estimated cost

## Reliability patterns

- Use timeouts shorter than upstream timeout ceilings.
- Retry only transient errors (`429`, selected `5xx`) with bounded backoff.
- Use idempotency keys for retried requests.
- Add circuit breaker behavior for sustained upstream failure windows.

## Common failure modes

- `401` / auth errors:
- Verify secret value, IAM access, and deployment environment wiring.
- `429` / rate limits:
- Implement queueing, jittered retries, and request shedding.
- timeout spikes:
- Lower prompt size, tune max tokens, and move heavy tasks async.
- sudden cost increase:
- Inspect model changes, prompt expansion, and retry storms.

## Runbook checklist

1. Confirm impact scope and affected routes.
2. Check recent deploys and secret rotations.
3. Validate upstream OpenAI health and local error class mix.
4. Apply rollback or traffic shaping if needed.
5. Capture post-incident fixes (alerts, limits, and tests).
