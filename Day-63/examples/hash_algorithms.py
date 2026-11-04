# Day 63 example

Run with Python 3.12:

```bash
python hash_algorithms.py
```

Teaching example; extend it with tests and validation as described in the lesson.

```python
"""Frequency and grouping algorithms using dictionaries."""
from collections import Counter, defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for word in words:
        groups[tuple(sorted(word))].append(word)
    return list(groups.values())


def first_unique(text: str) -> str | None:
    counts = Counter(text)
    return next((char for char in text if counts[char] == 1), None)


def top_k(values: list[int], k: int) -> list[tuple[int, int]]:
    if k < 0:
        raise ValueError("k cannot be negative")
    return Counter(values).most_common(k)


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(first_unique("swiss"))
    print(top_k([1, 1, 1, 2, 2, 3], 2))
```
