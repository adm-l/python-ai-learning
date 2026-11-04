# Day 72: Graphs, BFS and DFS

## Learning outcomes
- Explain the data structure or algorithm and its invariants.
- Analyze time and space complexity, including practical Python costs.
- Implement the lab and test edge cases.

## Core concepts
Represent graphs with adjacency lists; understand directed/undirected edges, visited state, components and cycles.

## Hands-on lab
Implement BFS shortest path in an unweighted graph, DFS traversal and connected components.

## Senior engineering perspective
Mark nodes at the correct time to avoid duplicate work. Consider memory costs of frontier queues.

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
