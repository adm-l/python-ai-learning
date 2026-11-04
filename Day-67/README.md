# Day 67: Heaps and priority queues

## Learning outcomes
- Explain the data structure or algorithm and its invariants.
- Analyze time and space complexity, including practical Python costs.
- Implement the lab and test edge cases.

## Core concepts
Use heapq for top-k, scheduling and merging sorted streams. Understand min-heap semantics.

## Hands-on lab
Implement top-k frequent values, merge k sorted iterables and a priority-based task scheduler.

## Senior engineering perspective
Heap operations are O(log n); heap entries need stable tie-breaking when payloads are not comparable.

## Exercises
1. Write the invariant or state definition before implementation.
2. Implement a straightforward solution, then improve it if justified.
3. State time and space complexity for best, average and worst cases where meaningful.
4. Add tests for empty, singleton, duplicate, boundary and invalid inputs as relevant.
5. Benchmark representative input sizes and distributions; do not infer performance from Big-O alone.

## Definition of done
- Runnable implementation with type hints and clear documentation.
- Deterministic pytest tests for normal and edge cases.
- Complexity analysis and trade-offs documented.
- No unnecessary third-party dependency.

## References
- [Python data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python heapq](https://docs.python.org/3/library/heapq.html)
- [Python collections](https://docs.python.org/3/library/collections.html)
- [Python sorting techniques](https://docs.python.org/3/howto/sorting.html)
