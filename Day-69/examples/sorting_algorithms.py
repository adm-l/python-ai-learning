# Day 69 example

Run with Python 3.12:

```bash
python sorting_algorithms.py
```

Teaching example; add tests and explore edge cases from the lesson.

```python
"""Merge sort for study; use Python's built-in sort in production."""


def merge_sort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return values.copy()
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    merged: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    return merged + left[i:] + right[j:]


if __name__ == "__main__":
    sample = [8, 3, 5, 1, 9, 3]
    print(merge_sort(sample), sorted(sample), sample)
```
