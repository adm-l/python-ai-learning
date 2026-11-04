# Day 45 — Project: profile and optimize a Python application

## Goal
Build a data-processing service, establish a baseline, identify bottlenecks, optimize safely and publish evidence.

## Requirements
- Accept JSON records with identifier, category and numeric value.
- Validate input and report invalid records without crashing the batch.
- Provide summary counts and totals by category.
- Include a deliberately inefficient baseline and measured optimized implementation.
- Keep memory bounded for large files; stream where appropriate.
- Expose a CLI with clear exit codes and structured logging.

## Suggested structure
day45-profiler/
  pyproject.toml
  src/day45_profiler/
    __init__.py
    cli.py
    processing.py
    models.py
  tests/
    test_processing.py
    test_cli.py
  benchmarks/
    benchmark_processing.py
  README.md

## Engineering tasks
1. Write requirements and edge cases before implementation.
2. Implement a correct baseline and tests.
3. Generate representative small and large datasets.
4. Profile CPU and memory; record environment and commands.
5. Optimize the measured bottleneck without changing behavior.
6. Re-run all tests and benchmarks.
7. Document trade-offs, complexity and limitations.

## Acceptance criteria
- Reproducible setup and execution instructions.
- Unit tests for valid, invalid, empty and large inputs.
- At least one CLI integration test.
- Before/after profiling evidence with methodology.
- Bounded memory behavior for large inputs.
- No optimization without a correctness test.

## Review questions
What was the bottleneck? Why did it occur? What evidence justified the change? Which inputs could invalidate the benchmark? What is the memory/latency trade-off?
