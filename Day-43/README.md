# Day 43 — Algorithmic complexity and practical optimization

## Outcomes
Reason about time/space complexity and improve algorithms before micro-optimizing.

## Concepts
- Big-O describes growth as input size increases, not exact runtime.
- Identify nested loops, repeated scans, sorting, hashing and expensive I/O.
- Average dictionary/set lookup is commonly O(1), subject to hashing and collisions.
- Choose data structures based on access patterns and invariants.
- A faster algorithm may use more memory; evaluate the whole workload.
- Optimize the dominant cost and preserve readability.

## Lab
Run python examples/complexity_lab.py and compare repeated membership scans with a set-based approach.

## Exercises
1. Analyze time and space complexity of three implementations.
2. Replace O(n²) duplicate detection with a set-based approach.
3. Compare list, set and dictionary for a realistic lookup workload.
4. Test duplicates, empty input and large input.

## Senior perspective
Architecture and algorithm choices dominate most performance wins. Complexity analysis helps predict scaling before load testing.

## Acceptance criteria
Explain complexity, select appropriate structures and validate improvements with tests and measurements.

## References
https://docs.python.org/3/tutorial/datastructures.html
