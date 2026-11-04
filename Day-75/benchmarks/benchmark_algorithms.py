"""Repeatable sorting benchmark; reports median runtime across rounds."""
import statistics
import time
import random


def merge_sort(values: list[int]) -> list[int]:
    if len(values) < 2:
        return values.copy()
    middle = len(values) // 2
    left, right = merge_sort(values[:middle]), merge_sort(values[middle:])
    output: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            output.append(left[i]); i += 1
        else:
            output.append(right[j]); j += 1
    return output + left[i:] + right[j:]


def median_seconds(operation, values: list[int], rounds: int = 5) -> float:
    measurements = []
    for _ in range(rounds):
        sample = values.copy()
        started = time.perf_counter()
        operation(sample)
        measurements.append(time.perf_counter() - started)
    return statistics.median(measurements)


def main() -> None:
    random.seed(7)
    for size in (100, 1_000, 5_000):
        data = [random.randrange(size * 10) for _ in range(size)]
        builtin = median_seconds(list.sort, data)
        custom = median_seconds(merge_sort, data)
        print(f"n={size:5} builtin_median={builtin:.6f}s merge_sort_median={custom:.6f}s")


if __name__ == "__main__":
    main()
