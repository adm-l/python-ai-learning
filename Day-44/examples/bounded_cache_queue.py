from functools import lru_cache
from queue import Full, Queue


@lru_cache(maxsize=128)
def expensive_lookup(key):
    return key.upper()


if __name__ == "__main__":
    print("cache values:", expensive_lookup("customer-1"), expensive_lookup("customer-1"))
    print("cache stats:", expensive_lookup.cache_info())

    work_queue = Queue(maxsize=2)
    for task in ("task-a", "task-b", "task-c"):
        try:
            work_queue.put_nowait(task)
            print("accepted:", task)
        except Full:
            print("rejected due to backpressure:", task)

    while not work_queue.empty():
        print("consumed:", work_queue.get_nowait())
        work_queue.task_done()
