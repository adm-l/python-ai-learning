# Day 85: Rate limiting and distributed coordination

## Learning outcomes
- Explain the concepts and their production implications.
- Implement the lab with explicit boundaries and type hints.
- Test success, validation failures and relevant failure modes.

## Core concepts
Implement token bucket and fixed/sliding-window limits; understand atomicity and distributed counters.

## Hands-on lab
Design per-user and per-tenant limits with Redis Lua or atomic primitives; include Retry-After.

## Senior engineering perspective
A process-local limiter is not globally correct across replicas. Define identity, burst and fail-open/fail-closed policy.

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
