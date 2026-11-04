# Day 33 — Memory management and garbage collection

## Outcomes
Explain object reachability, reference counting, cycles, cyclic garbage collection and explicit resource cleanup.

## Concepts
- Names and containers hold references to objects.
- In CPython, reference counting commonly reclaims acyclic objects promptly.
- Reference cycles can keep reference counts above zero; cyclic GC detects unreachable cycles.
- The gc module exposes diagnostics and controls. Do not disable GC as a casual optimization.
- Collection timing is implementation-dependent. Never rely on __del__ for deterministic cleanup.
- Use with or explicit close() for files, sockets, database connections and locks.

## Lab
Run python examples/garbage_collection.py. Inspect gc.is_tracked, create a cycle and observe collection counts. Results vary by build/version.

## Exercises
1. Create a reference cycle and explain why reference counting alone is insufficient.
2. Use weakref to avoid an unnecessary strong-reference cycle.
3. Refactor file handling to use a context manager.
4. Measure memory before and after processing a large iterable.

## Senior perspective
A memory leak is often unintended reachability: unbounded caches, retained request objects, globals, callbacks or unclosed resources. Measure before changing GC settings.

## Acceptance criteria
Explain refcounting vs cyclic GC, demonstrate a cycle, and implement deterministic cleanup.

## References
https://docs.python.org/3/library/gc.html
