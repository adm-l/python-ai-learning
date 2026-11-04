"""Token bucket rate limiter using monotonic time."""
from time import monotonic, sleep


class TokenBucket:
    def __init__(self, capacity: int, refill_per_second: float) -> None:
        if capacity <= 0 or refill_per_second <= 0:
            raise ValueError("capacity and refill rate must be positive")
        self.capacity = capacity
        self.tokens = float(capacity)
        self.refill_rate = refill_per_second
        self.updated_at = monotonic()

    def allow(self, cost: float = 1.0) -> bool:
        now = monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.updated_at) * self.refill_rate)
        self.updated_at = now
        if cost <= 0 or cost > self.capacity:
            raise ValueError("cost must be within (0, capacity]")
        if self.tokens < cost:
            return False
        self.tokens -= cost
        return True


def main() -> None:
    limiter = TokenBucket(3, 1)
    for _ in range(5):
        print("allowed" if limiter.allow() else "limited")
        sleep(0.1)


if __name__ == "__main__":
    main()
