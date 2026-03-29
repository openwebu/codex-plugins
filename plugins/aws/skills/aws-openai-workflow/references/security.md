# Security Baseline

## Credentials and secret handling

- Store `OPENAI_API_KEY` only in `AWS Secrets Manager`.
- Grant runtime IAM permission to read only the exact secret ARN required.
- Rotate secrets on a fixed cadence and on incident response events.

## IAM and access control

- Use least-privilege IAM roles per workload.
- Separate deploy role and runtime role.
- Avoid wildcard permissions for `secretsmanager:*`, `s3:*`, and `dynamodb:*`.

## Data protection

- Never log raw API keys or full sensitive prompts.
- Encrypt data at rest (`S3`, `DynamoDB`) and in transit (`TLS`).
- Apply tenant-scoped access controls when building multi-tenant APIs.

## Boundary controls

- Rate-limit and authenticate external endpoints with API Gateway authorizers or equivalent.
- Validate prompt input length and schema before calling model APIs.
- Add allowlists for internal tool execution paths if using function/tool calling.

## Incident readiness

- Keep CloudTrail and CloudWatch retention aligned to compliance needs.
- Alert on unusual secret access, high error spikes, and cost anomalies.
- Maintain a key rotation runbook and rollback procedure.
