# Day 25 — Clean architecture and dependency inversion

## Outcomes
Understand and apply clean architecture and dependency inversion in a small Python codebase.

## Study
- Domain/application/infrastructure/presentation
- ports/adapters
- SOLID and composition root.

## Practical work
1. Refactor document processor so domain does not import FastAPI, database or model SDK
2. draw dependency graph.

## Senior perspective
Architecture controls change and dependency direction; it is not maximizing folder count.

## Acceptance
- [ ] Explain the key concepts without reading the lesson.
- [ ] Implement the practical work.
- [ ] Add tests for success, edge and failure cases.
- [ ] Run from a clean virtual environment.
- [ ] Record one trade-off and one unresolved question.