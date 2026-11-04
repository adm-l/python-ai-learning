# Day 49: Asyncio event loop fundamentals

## Outcomes
By the end of this lesson, you should be able to explain the concepts, implement the lab, and defend the engineering trade-offs.

## Core concepts
Understand coroutines, await, tasks, cooperative scheduling, event-loop blocking and cancellation.

Study the relevant Python standard-library APIs and understand their lifecycle, failure behavior, resource costs, and version constraints. Do not treat a code sample as a production-ready abstraction without examining those concerns.

## Hands-on lab
Write concurrent simulated I/O using asyncio.sleep, asyncio.gather and TaskGroup (Python 3.11+). Compare with sequential awaits.

## Senior engineering perspective
Async is concurrency for waiting-heavy workloads, not automatic CPU parallelism. One blocking call can stall the loop.

## Exercises
1. Explain the model in your own words, including what it does not guarantee.
2. Add input validation and explicit failure handling.
3. Write automated tests for the important invariant and at least one failure path.
4. Measure behavior under a small workload and a larger workload; record environment and assumptions.
5. Review the implementation for unbounded queues, tasks, memory, retries, or resource lifetimes.

## Acceptance criteria
- No un-awaited coroutines; tasks are awaited or cancelled; cancellation is handled.
- Code is typed where it improves clarity and follows PEP 8.
- Tests are deterministic and do not rely on arbitrary timing sleeps.
- README explains how to run the lab and its limitations.

## References
- [Python documentation](https://docs.python.org/3/)
- [Python threading](https://docs.python.org/3/library/threading.html)
- [Python concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)
