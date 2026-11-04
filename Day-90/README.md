# Day 90: Project — production-style order API

## What you are building
A small FastAPI order service with a clear transport/application/persistence split. It demonstrates request validation, health endpoints, SQL parameterization, database constraints, transactions, idempotency keys and a transactional outbox record.

## Architecture
- `main.py`: HTTP transport, validation, status codes and health endpoints.
- `service.py`: application use case and idempotency behavior.
- `database.py`: SQLite schema and connection factory.
- `tests/`: API, validation, replay and outbox tests.

The database adapter uses SQLite to keep the project easy to run locally. In a production deployment, replace it with PostgreSQL, add a bounded connection pool and schema migration tooling, and run the outbox publisher as a separately supervised worker. The outbox table is written transactionally here; publishing to Kafka is an extension exercise, not a feature claimed as complete.

## Run locally
Requires Python 3.12+.

```bash
cd Day-90
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
uvicorn order_api.main:app --reload
```

Try the API:

```bash
curl http://127.0.0.1:8000/health/ready
curl -X POST http://127.0.0.1:8000/orders \\
  -H 'Content-Type: application/json' \\
  -H 'Idempotency-Key: order-request-001' \\
  -d '{"customer_id":"customer-1","total_cents":2500}'
curl http://127.0.0.1:8000/orders/1
```

## Important design decisions
- The service uses parameterized SQL and database constraints.
- A single transaction writes the order, idempotency record and outbox event.
- Replaying the same idempotency key and same request returns the existing order.
- Reusing a key with a different request returns HTTP 409.
- Health readiness performs a database check; liveness does not depend on the database.
- SQLite is suitable for this learning project, not a substitute for PostgreSQL under production concurrency.

## Production extensions
1. PostgreSQL adapter, migrations and bounded connection pool.
2. Authentication, tenant authorization and audit trail.
3. Redis-backed distributed rate limiting and cache-aside behavior.
4. Outbox publisher with lease/claim semantics, retry budget and dead-letter handling.
5. Kafka producer/consumer with idempotent consumer inbox.
6. Structured logs, metrics, traces, request IDs and latency histograms.
7. Docker Compose for API + PostgreSQL + Redis + Kafka-compatible broker.
8. Load tests, fault injection and documented SLOs.

## Definition of done
- [ ] Tests pass in a clean Python 3.12 environment.
- [ ] Invalid input and idempotency conflicts have stable API responses.
- [ ] Transaction and outbox invariants are understood.
- [ ] Architecture and failure modes are documented.
