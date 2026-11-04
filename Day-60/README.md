# Day 60: Project — resilient concurrent task runner

## Goal
Build a small installable Python CLI that reads JSONL jobs, validates input, executes work through a bounded asyncio queue, limits worker concurrency, handles duplicate IDs, and reports structured results.

## Architecture
- `cli.py`: argument parsing, JSONL loading and output.
- `runner.py`: typed job/result models, validation, bounded queue and worker lifecycle.
- `tests/`: input validation, ordering, duplicate handling, worker isolation and configuration checks.
- `sample.jsonl`: sample input.

## Setup
Requires Python 3.12 or newer.

```bash
cd Day-60
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

## Run

```bash
task-runner sample.jsonl --workers 2 --queue-size 4 --retries 1
# Or without installing the console script:
PYTHONPATH=src python -m task_runner.cli sample.jsonl
```

Each non-empty input line is a JSON object with `job_id`, `operation` (currently `double`) and integer `value`. Results are emitted as JSON lines. A failed job produces exit code 1; invalid input or unreadable files produce exit code 2.

## Engineering constraints and limitations
- The queue is bounded; producers wait when it is full.
- Worker count bounds active jobs. Results preserve input order.
- Duplicate IDs in a single run are marked `duplicate` and are not executed twice.
- This sample uses in-memory state only. It is not durable across process crashes and does not provide distributed idempotency.
- The `retries` option is reserved for the next exercise: add a distinct transient exception and retry only that exception. The current operation raises validation failures, which should not be retried.
- Add total deadlines, cancellation tests, structured logging and metrics as extension exercises before treating this as production software.

## Exercises
1. Introduce a `TransientJobError` and retry only that exception with bounded exponential backoff and jitter.
2. Add per-job deadlines and cancellation behavior.
3. Add a dead-letter JSONL output for permanent failures.
4. Add structured logs with job ID and queue wait/processing duration.
5. Persist idempotency keys and side effects transactionally using a database.
6. Add load tests and report p50/p95/p99 latency and throughput.

## Definition of done
- Tests pass locally and the CLI runs using the commands above.
- Queue capacity and worker count are configurable and bounded.
- Duplicate delivery behavior and crash limitations are documented.
- Failure behavior and exit codes are explicit.
