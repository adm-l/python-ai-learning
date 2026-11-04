# Day 47: Threading, locks and shared state

## Outcomes
By the end of this lesson, you should be able to explain the concepts, implement the lab, and defend the engineering trade-offs.

## Core concepts
Understand thread lifecycle, race conditions, critical sections, locks, events, queues and deadlocks.

Study the relevant Python standard-library APIs and understand their lifecycle, failure behavior, resource costs, and version constraints. Do not treat a code sample as a production-ready abstraction without examining those concerns.

## Hands-on lab
Build a bounded producer-consumer pipeline with threading.Thread and queue.Queue. Add graceful shutdown and failure propagation.

## Senior engineering perspective
Prefer message passing and immutable work items over broad shared mutable state. Keep lock scope small.

## Exercises
1. Explain the model in your own words, including what it does not guarantee.
2. Add input validation and explicit failure handling.
3. Write automated tests for the important invariant and at least one failure path.
4. Measure behavior under a small workload and a larger workload; record environment and assumptions.
5. Review the implementation for unbounded queues, tasks, memory, retries, or resource lifetimes.

## Acceptance criteria
- Demonstrate correctness under repeated runs and document lock ownership.
- Code is typed where it improves clarity and follows PEP 8.
- Tests are deterministic and do not rely on arbitrary timing sleeps.
- README explains how to run the lab and its limitations.

## References
- [Python documentation](https://docs.python.org/3/)
- [Python threading](https://docs.python.org/3/library/threading.html)
- [Python concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)
