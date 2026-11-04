"""CPU work in separate processes; guard the process entry point."""
from concurrent.futures import ProcessPoolExecutor


def count_primes(limit: int) -> int:
    count = 0
    for candidate in range(2, limit):
        if all(candidate % divisor for divisor in range(2, int(candidate**0.5) + 1)):
            count += 1
    return count


def main() -> None:
    with ProcessPoolExecutor() as pool:
        print(list(pool.map(count_primes, [20_000, 21_000, 22_000, 23_000])))


if __name__ == "__main__":
    main()
