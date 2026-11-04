# Day 17 — Runtime validation and schema design

## Outcomes
Understand and apply runtime validation and schema design in a small Python codebase.

## Study
- Validation boundaries
- Pydantic concepts
- field constraints
- nested models
- serialization and schema evolution.

## Practical work
1. Define ingestion request/response models
2. reject malformed values
3. separate domain invariants from transport schemas.

## Senior perspective
Validate at boundaries; keep core domain rules independent of web framework models.

## Acceptance
- [ ] Explain the key concepts without reading the lesson.
- [ ] Implement the practical work.
- [ ] Add tests for success, edge and failure cases.
- [ ] Run from a clean virtual environment.
- [ ] Record one trade-off and one unresolved question.