# Day 62 example

Run with Python 3.12:

```bash
python two_pointers.py
```

Teaching example; extend it with tests and validation as described in the lesson.

```python
"""Sorted pair sum and longest unique substring."""


def pair_sum_sorted(values: list[int], target: int) -> tuple[int, int] | None:
    left, right = 0, len(values) - 1
    while left < right:
        total = values[left] + values[right]
        if total == target:
            return left, right
        if total < target:
            left += 1
        else:
            right -= 1
    return None


def longest_unique_substring(text: str) -> int:
    last_seen: dict[str, int] = {}
    start = best = 0
    for index, char in enumerate(text):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = index
        best = max(best, index - start + 1)
    return best


if __name__ == "__main__":
    print(pair_sum_sorted([1, 2, 4, 7, 11], 9))
    print(longest_unique_substring("abcabcbb"))
```
