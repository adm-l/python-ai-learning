"""Bounded producer-consumer pipeline with explicit shutdown."""
from queue import Queue
from threading import Thread

_STOP = object()


def worker(jobs: Queue) -> None:
    while True:
        item = jobs.get()
        try:
            if item is _STOP:
                return
            print(f"processed {item}")
        finally:
            jobs.task_done()


def main() -> None:
    jobs: Queue = Queue(maxsize=3)
    thread = Thread(target=worker, args=(jobs,))
    thread.start()
    for number in range(8):
        jobs.put(number)
    jobs.put(_STOP)
    jobs.join()
    thread.join()


if __name__ == "__main__":
    main()
