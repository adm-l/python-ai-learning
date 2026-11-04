# Day 20 — Context managers and resource lifecycle

## Outcomes
Understand and apply context managers and resource lifecycle in a small Python codebase.

## Study
- with
- __enter__/__exit__
- contextlib
- cleanup and exception propagation.

## Practical work
1. Create temporary-resource context manager
2. prove cleanup after exception
3. inspect contextlib
4. model transaction-like lifecycle.

## Senior perspective
Files, DB connections, locks and tracing spans need deterministic ownership and cleanup.

## Acceptance
- [ ] Explain the key concepts without reading the lesson.
- [ ] Implement the practical work.
- [ ] Add tests for success, edge and failure cases.
- [ ] Run from a clean virtual environment.
- [ ] Record one trade-off and one unresolved question.