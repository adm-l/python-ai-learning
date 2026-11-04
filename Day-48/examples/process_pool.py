# Day 48 example

Run with Python 3.12 unless the lesson states otherwise:

```bash
python process_pool.py
```

This is a focused teaching example, not a complete production service.

```python
"""CPU work in separate processes; keep process entry guarded."""
from concurrent.futures import ProcessPoolExecutor


def count_primes(limit: int) -> int:
    count = 0
    for candidate in range(2, limit):
        if all(candidate % divisor for divisor in range(2, int(candidate**0.5) + 1)):
            count += 1
    return count


def main() -> None:
    limits = [20_000, 21_000, 22_000, 23_000]
    with ProcessPoolExecutor() as pool:
        print(list(pool.map(count_primes, limits)))


if __name__ == "__main__":
    main()
```
