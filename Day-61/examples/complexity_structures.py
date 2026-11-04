# Day 61 example

Run with Python 3.12:

```bash
python complexity_structures.py
```

Teaching example; extend it with tests and validation as described in the lesson.

```python
"""Compare common container operations; timings are illustrative, not universal."""
from collections import deque
from time import perf_counter


def timed(label: str, action) -> None:
    start = perf_counter()
    action()
    print(f"{label:20} {perf_counter() - start:.6f}s")


def main() -> None:
    size = 100_000
    values = list(range(size))
    lookup = set(values)
    queue = deque(values)
    timed("list membership", lambda: size - 1 in values)
    timed("set membership", lambda: size - 1 in lookup)
    timed("deque append/pop", lambda: (queue.append(-1), queue.pop()))


if __name__ == "__main__":
    main()
```
