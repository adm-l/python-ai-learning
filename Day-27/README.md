# Day 27 — HTTP clients and resilient integrations

## Outcomes
Understand and apply http clients and resilient integrations in a small Python codebase.

## Study
- HTTP lifecycle
- status codes
- JSON
- connect/read timeouts
- retries
- backoff
- idempotency and pooling.

## Practical work
1. Build typed client for mock API
2. handle timeout/4xx/5xx/invalid JSON
3. retry only safe operations
4. test deterministically.

## Senior perspective
Retries multiply load and may duplicate side effects. Bound retries and define idempotency.

## Acceptance
- [ ] Explain the key concepts without reading the lesson.
- [ ] Implement the practical work.
- [ ] Add tests for success, edge and failure cases.
- [ ] Run from a clean virtual environment.
- [ ] Record one trade-off and one unresolved question.