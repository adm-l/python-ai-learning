"""Summarize latency samples and expose tail behavior."""
import random


def percentile(values: list[float], p: float) -> float:
    if not values or not 0 <= p <= 100:
        raise ValueError("provide values and percentile in [0, 100]")
    ordered = sorted(values)
    index = round((len(ordered) - 1) * p / 100)
    return ordered[index]


def main() -> None:
    samples = [random.lognormvariate(-2, 0.8) for _ in range(1000)]
    for p in (50, 95, 99):
        print(f"p{p}={percentile(samples, p):.4f}s")


if __name__ == "__main__":
    main()
