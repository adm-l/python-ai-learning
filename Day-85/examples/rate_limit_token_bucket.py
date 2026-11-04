# Day 85 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python rate_limit_token_bucket.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""Single-process token bucket; distributed services need shared atomic state."""
from time import monotonic


class TokenBucket:
    def __init__(self, capacity: int, refill_per_second: float) -> None:
        if capacity < 1 or refill_per_second <= 0:
            raise ValueError("capacity and refill rate must be positive")
        self.capacity = float(capacity)
        self.tokens = float(capacity)
        self.refill_rate = refill_per_second
        self.updated_at = monotonic()

    def allow(self, cost: float = 1) -> bool:
        if cost <= 0 or cost > self.capacity:
            return False
        now = monotonic()
        elapsed = now - self.updated_at
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.updated_at = now
        if self.tokens < cost:
            return False
        self.tokens -= cost
        return True


if __name__ == "__main__":
    limiter = TokenBucket(3, 0.5)
    print([limiter.allow() for _ in range(5)])
```
