# Day 46 example

Run with Python 3.12 unless the lesson states otherwise:

```bash
python execution_models.py
```

This is a focused teaching example, not a complete production service.

```python
"""Compare sequential, threaded and process execution for a CPU workload."""
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import perf_counter


def cpu_work(n: int) -> int:
    total = 0
    for value in range(n):
        total += value * value % 97
    return total


def measure(label: str, operation) -> None:
    started = perf_counter()
    results = operation()
    print(f"{label:12} {perf_counter() - started:.3f}s checksum={sum(results)}")


def main() -> None:
    inputs = [250_000] * 4
    measure("sequential", lambda: [cpu_work(n) for n in inputs])
    with ThreadPoolExecutor(max_workers=4) as pool:
        measure("threads", lambda: list(pool.map(cpu_work, inputs)))
    with ProcessPoolExecutor(max_workers=4) as pool:
        measure("processes", lambda: list(pool.map(cpu_work, inputs)))


if __name__ == "__main__":
    main()
```
