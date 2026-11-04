import cProfile
import pstats
import tracemalloc


def inefficient_lookup(records, targets):
    matches = []
    for target in targets:
        for record in records:
            if record == target:
                matches.append(record)
                break
    return matches


if __name__ == "__main__":
    records = list(range(20_000))
    targets = list(range(0, 20_000, 3))

    profiler = cProfile.Profile()
    profiler.enable()
    result = inefficient_lookup(records, targets)
    profiler.disable()
    print("matches:", len(result))
    pstats.Stats(profiler).sort_stats("cumtime").print_stats(10)

    tracemalloc.start()
    data = [str(number) for number in range(10_000)]
    current, peak = tracemalloc.get_traced_memory()
    print("current bytes:", current, "peak bytes:", peak)
    del data
    tracemalloc.stop()
