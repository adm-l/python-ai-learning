# Day 10 — Modules, imports and package structure

## Outcomes
Understand and apply modules, imports and package structure in a small Python codebase.

## Study
- Import execution/caching
- absolute/relative imports
- __main__
- packages
- __init__
- circular imports and side effects.

## Practical work
1. Split config/validation/main modules
2. run package with python -m
3. draw import graph
4. reproduce and remove circular import
5. avoid startup work during import.

## Senior perspective
Imports are architecture boundaries. Keep startup side effects explicit and dependency direction intentional.

## Acceptance
- [ ] Explain the key concepts without reading the lesson.
- [ ] Implement the practical work.
- [ ] Add tests for success, edge and failure cases.
- [ ] Run from a clean virtual environment.
- [ ] Record one trade-off and one unresolved question.