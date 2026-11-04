# Day 42 — CPU and memory profiling

## Outcomes
Find bottlenecks with profiling tools and distinguish CPU time, wall time and memory allocation.

## Concepts
- Profile before optimizing; use representative workloads.
- time.perf_counter() measures elapsed wall time.
- cProfile provides deterministic call statistics; sampling profilers help with production-like workloads.
- tracemalloc tracks Python memory allocations, not every native allocation.
- Benchmark warm-up, input size, variance and environment.
- Avoid publishing benchmark numbers without methodology.

## Lab
Run python examples/profiling_lab.py. Generate a profile and inspect it with python -m pstats.

## Exercises
1. Profile a deliberately inefficient function.
2. Optimize it and show before/after results with identical input.
3. Use tracemalloc snapshots to locate retained allocations.
4. Explain what your profiler cannot observe.

## Senior perspective
Optimization is hypothesis-driven. Preserve correctness with tests and keep benchmarks reproducible.

## Acceptance criteria
Produce a report with bottleneck, evidence, change, correctness tests and measured result.

## References
https://docs.python.org/3/library/profile.html
