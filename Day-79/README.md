# Day 79: FastAPI async behavior and lifecycle

## Learning outcomes
- Explain the concepts and their production implications.
- Implement the lab with explicit boundaries and type hints.
- Test success, validation failures and relevant failure modes.

## Core concepts
Understand async endpoints, sync blocking work, lifespan hooks, connection pools and cancellation.

## Hands-on lab
Add startup/shutdown lifecycle management and an async service dependency.

## Senior engineering perspective
An async def does not make blocking I/O non-blocking. Bound concurrency and close resources.

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
