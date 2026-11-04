# Day 45 — Project: profile and optimize a Python application

## Goal
Build a streaming JSON Lines processor, establish a baseline, profile it, optimize safely and publish evidence.

## Included implementation
This folder contains a working starter application:
- JSONL input is processed one line at a time.
- Each record must contain a non-empty string id, non-empty string category and finite numeric value.
- Invalid lines are counted and skipped; processing continues.
- Counts and numeric totals are aggregated by category.
- Memory use grows with the number of categories rather than the number of input records.

## Setup
From the repository root:

```bash
cd Day-45
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

## Run
Create a file named sample.jsonl:

```json
{"id":"order-1","category":"books","value":12.5}
{"id":"order-2","category":"games","value":30}
{"id":"order-3","category":"books","value":7}
```

Then run:

```bash
day45-profiler sample.jsonl
# or
python -m day45_profiler.cli sample.jsonl
```

Exit code is 0 when all non-empty lines are valid, 1 when invalid records were found, and 2 when the input file cannot be read.

## Your engineering tasks
1. Write tests for duplicate IDs and decide whether duplicates should be rejected or aggregated.
2. Add a configurable maximum line size to protect against unexpectedly large records.
3. Add a baseline implementation that loads all records into memory, then compare it with the streaming implementation.
4. Generate representative data at multiple sizes.
5. Profile CPU and memory; record Python version, machine, commands and input size.
6. Optimize only a measured bottleneck and rerun all tests.
7. Document complexity, limitations and trade-offs.

## Required acceptance criteria
- Reproducible setup and execution instructions.
- Unit tests for valid, invalid, empty and non-finite inputs.
- At least one CLI integration test.
- Before/after profiling evidence with methodology.
- Bounded memory behavior for large input.
- No optimization without a correctness test.

## Review questions
What was the bottleneck? Why did it occur? What evidence justified the change? Which inputs could invalidate the benchmark? What is the memory/latency trade-off?
