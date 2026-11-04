# Day 23 — Logging, debugging and exception design

## Outcomes
Understand and apply logging, debugging and exception design in a small Python codebase.

## Study
- Logging levels
- logger hierarchy
- structured context
- traceback
- pdb
- correlation IDs and redaction.

## Practical work
1. Add structured logs
2. include request IDs
3. verify secrets are not logged
4. debug a deliberately failing function.

## Senior perspective
Logs are operational data. Avoid secrets/PII and duplicate exception logging.

## Acceptance
- [ ] Explain the key concepts without reading the lesson.
- [ ] Implement the practical work.
- [ ] Add tests for success, edge and failure cases.
- [ ] Run from a clean virtual environment.
- [ ] Record one trade-off and one unresolved question.