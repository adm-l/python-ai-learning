# Day 67 example

Run with Python 3.12:

```bash
python heap_priority_queue.py
```

Teaching example; extend it with tests and validation as described in the lesson.

```python
"""Top-k and merging sorted streams with heapq."""
import heapq
from collections import Counter
from itertools import count


def top_k(values: list[int], k: int) -> list[tuple[int, int]]:
    if k < 0:
        raise ValueError("k cannot be negative")
    return heapq.nlargest(k, Counter(values).items(), key=lambda pair: pair[1])


def merge_streams(streams: list[list[int]]) -> list[int]:
    return list(heapq.merge(*streams))


def main() -> None:
    sequence = count()
    tasks = [(2, next(sequence), "send email"), (1, next(sequence), "charge card")]
    heapq.heapify(tasks)
    while tasks:
        print(heapq.heappop(tasks))
    print(top_k([1, 1, 1, 2, 2, 3], 2))
    print(merge_streams([[1, 4, 7], [2, 3, 8]]))


if __name__ == "__main__":
    main()
```
