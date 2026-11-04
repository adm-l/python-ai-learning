# Day 75: Project — algorithmic toolkit and benchmark suite

## Goal
Build an installable package that exposes binary search, frequency analysis and graph traversal utilities. Practice API design, complexity analysis, tests and repeatable experiments.

## Structure
- `src/algokit/algorithms.py`: focused implementations with complexity notes.
- `src/algokit/cli.py`: command-line demonstration.
- `tests/`: boundary, duplicate and graph-cycle tests.
- `pyproject.toml`: package and development dependency metadata.

## Setup
Requires Python 3.12 or newer.

```bash
cd Day-75
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
algokit --target 4
```

## Complexity notes
- `lower_bound`: O(log n) time and O(1) auxiliary space on sorted input.
- `top_k_frequent`: Counter frequency construction is O(n) average; selecting with most_common is bounded by work over the distinct values and may sort them in the worst case.
- `bfs`: O(V + E) time and O(V) auxiliary space for adjacency-list representation.

## Exercises
1. Add merge sort and stable-sort tests.
2. Add Dijkstra with non-negative edge validation.
3. Add a benchmark script that varies input size and distribution.
4. Record Python version, machine, warm-up, repeated-run median and input generation method.
5. Compare built-in sorting with your educational implementation; explain why production code normally uses built-ins.

## Definition of done
- Package installs in a clean virtual environment.
- CLI produces valid JSON output.
- Tests cover normal, boundary and invalid cases.
- Complexity assumptions and benchmark limitations are documented.
