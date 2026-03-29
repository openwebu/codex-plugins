---
name: jam-bug-triage
description: Analyze Jam bug reports into reproducible steps, impact, suspected root cause, and an implementation-ready fix checklist
---

# Jam Bug Triage

Use this workflow when a Jam recording is shared and you need a crisp engineering handoff.

## 1. Extract Reproduction Steps

From the recording and report metadata, produce:
- environment/context assumptions
- exact user actions in order
- expected vs actual behavior

## 2. Define Impact Clearly

Summarize:
- who is affected
- how often it occurs
- severity (blocker/high/medium/low)

## 3. Build a Root-Cause Hypothesis

Use visible UI behavior and timing cues to propose likely failure points.
Include uncertainty explicitly when evidence is partial.

## 4. Produce an Implementation Checklist

Output an actionable checklist for engineers:
- code areas to inspect first
- logs/telemetry to verify
- minimal fix candidate
- regression checks

## Output Format

Return a concise triage packet with these headings:
1. Reproduction
2. Impact
3. Root-Cause Hypothesis
4. Fix Plan
5. Validation Steps
