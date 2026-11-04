# Day 68 example

Run with Python 3.12:

```bash
python binary_search.py
```

Teaching example; extend it with tests and validation as described in the lesson.

```python
"""Lower/upper bounds and binary search on a monotonic predicate."""


def lower_bound(values: list[int], target: int) -> int:
    low, high = 0, len(values)
    while low < high:
        mid = (low + high) // 2
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def upper_bound(values: list[int], target: int) -> int:
    low, high = 0, len(values)
    while low < high:
        mid = (low + high) // 2
        if values[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


def min_capacity(weights: list[int], days: int) -> int:
    if not weights or days < 1 or any(weight <= 0 for weight in weights):
        raise ValueError("positive weights, non-empty input and days >= 1 required")

    def feasible(capacity: int) -> bool:
        used, total = 1, 0
        for weight in weights:
            if total + weight > capacity:
                used, total = used + 1, 0
            total += weight
        return used <= days

    low, high = max(weights), sum(weights)
    while low < high:
        mid = (low + high) // 2
        if feasible(mid):
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == "__main__":
    print(lower_bound([1, 2, 2, 2, 5], 2), upper_bound([1, 2, 2, 2, 5], 2))
    print(min_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
```
