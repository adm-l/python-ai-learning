# Day 89: API security and production hardening

## Learning outcomes
- Explain the concepts and their production implications.
- Implement the lab with explicit boundaries and type hints.
- Test success, validation failures and relevant failure modes.

## Core concepts
Cover authentication vs authorization, JWT validation, secrets, CORS, input limits, SQL injection, SSRF and audit logs.

## Hands-on lab
Add auth dependency, role/tenant checks, request size limits and security-focused tests.

## Senior engineering perspective
Trust boundaries must be explicit. Never log credentials or trust tenant IDs from arbitrary payload fields.

## Exercises
1. Draw the request/data flow and identify trust and failure boundaries.
2. Implement the smallest working version before adding abstractions.
3. Add deterministic tests for normal, boundary and failure cases.
4. Record latency, resource use and operational assumptions where relevant.
5. Explain one alternative design and why you did not choose it.

## Definition of done
- Runnable implementation with clear configuration and type hints.
- Tests cover behavior and important failure paths.
- No secrets or credentials committed.
- README explains setup, architecture, trade-offs and limitations.

## References
- [Python documentation](https://docs.python.org/3/)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
- [Redis documentation](https://redis.io/docs/)
- [Kafka documentation](https://kafka.apache.org/documentation/)
