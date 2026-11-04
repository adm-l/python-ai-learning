from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import perf_counter, sleep


def cpu_work(limit):
    total = 0
    for number in range(limit):
        total += number * number
    return total


def io_work(_):
    sleep(0.05)
    return "done"


def measure(label, function):
    started = perf_counter()
    result = function()
    print(f"{label}: {perf_counter() - started:.3f}s")
    return result


if __name__ == "__main__":
    count = 250_000
    jobs = 8

    measure("CPU sequential", lambda: [cpu_work(count) for _ in range(jobs)])
    measure("CPU threads", lambda: list(ThreadPoolExecutor(4).map(cpu_work, [count] * jobs)))
    measure("CPU processes", lambda: list(ProcessPoolExecutor(2).map(cpu_work, [count] * jobs)))

    measure("I/O sequential", lambda: [io_work(i) for i in range(jobs)])
    measure("I/O threads", lambda: list(ThreadPoolExecutor(4).map(io_work, range(jobs))))
