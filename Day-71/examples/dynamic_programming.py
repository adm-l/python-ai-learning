# Day 71 example

Run with Python 3.12:

```bash
python dynamic_programming.py
```

Teaching example; add tests and explore edge cases from the lesson.

```python
"""Memoized and bottom-up dynamic programming examples."""
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def coin_change(coins: list[int], amount: int) -> int:
    if amount < 0 or any(coin <= 0 for coin in coins):
        raise ValueError("amount must be non-negative and coins positive")
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for current in range(1, amount + 1):
        for coin in coins:
            if coin <= current:
                dp[current] = min(dp[current], dp[current - coin] + 1)
    return -1 if dp[amount] > amount else dp[amount]


def lcs_length(first: str, second: str) -> int:
    previous = [0] * (len(second) + 1)
    for left in first:
        current = [0]
        for index, right in enumerate(second, start=1):
            current.append(previous[index - 1] + 1 if left == right else max(previous[index], current[-1]))
        previous = current
    return previous[-1]


if __name__ == "__main__":
    print(fibonacci(10), coin_change([1, 3, 4], 6), lcs_length("stone", "longest"))
```
