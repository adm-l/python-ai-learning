from time import perf_counter


def duplicates_slow(values):
    result = []
    for value in values:
        if value in result:
            continue
        result.append(value)
    return result


def duplicates_fast(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def measure(function, values):
    started = perf_counter()
    result = function(values)
    return len(result), perf_counter() - started


if __name__ == "__main__":
    data = [number % 5_000 for number in range(20_000)]
    print("quadratic baseline:", measure(duplicates_slow, data))
    print("set-based:", measure(duplicates_fast, data))
