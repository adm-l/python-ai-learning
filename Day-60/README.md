# Day 60: Project: resilient concurrent task runner

## Outcomes
By the end of this lesson, you should be able to explain the concepts, implement the lab, and defend the engineering trade-offs.

## Core concepts
Combine bounded execution, retries, deadlines, cancellation, idempotency, observability and tests.

Study the relevant Python standard-library APIs and understand their lifecycle, failure behavior, resource costs, and version constraints. Do not treat a code sample as a production-ready abstraction without examining those concerns.

## Hands-on lab
Build a package + CLI that runs JSON job definitions using an async worker pool, bounded queue, retry policy and structured result report.

## Senior engineering perspective
Define guarantees and non-guarantees. In-memory jobs are not durable; do not market this as a broker.

## Exercises
1. Explain the model in your own words, including what it does not guarantee.
2. Add input validation and explicit failure handling.
3. Write automated tests for the important invariant and at least one failure path.
4. Measure behavior under a small workload and a larger workload; record environment and assumptions.
5. Review the implementation for unbounded queues, tasks, memory, retries, or resource lifetimes.

## Acceptance criteria
- Installable package, tests, CLI docs, bounded resource behavior and graceful shutdown.
- Code is typed where it improves clarity and follows PEP 8.
- Tests are deterministic and do not rely on arbitrary timing sleeps.
- README explains how to run the lab and its limitations.

## References
- [Python documentation](https://docs.python.org/3/)
- [Python threading](https://docs.python.org/3/library/threading.html)
- [Python concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)
