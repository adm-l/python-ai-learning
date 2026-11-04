"""Compare sequential, threaded and process execution for CPU work."""
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import perf_counter


def cpu_work(n: int) -> int:
    total = 0
    for value in range(n):
        total += value * value % 97
    return total


def measure(label: str, operation) -> None:
    start = perf_counter()
    result = operation()
    print(f"{label:12} {perf_counter() - start:.3f}s checksum={sum(result)}")


def main() -> None:
    inputs = [250_000] * 4
    measure("sequential", lambda: [cpu_work(n) for n in inputs])
    with ThreadPoolExecutor(max_workers=4) as pool:
        measure("threads", lambda: list(pool.map(cpu_work, inputs)))
    with ProcessPoolExecutor(max_workers=4) as pool:
        measure("processes", lambda: list(pool.map(cpu_work, inputs)))


if __name__ == "__main__":
    main()
