# Day 47 example

Run with Python 3.12 unless the lesson states otherwise:

```bash
python thread_pipeline.py
```

This is a focused teaching example, not a complete production service.

```python
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
        jobs.put(number)  # blocks when the queue is full: backpressure
    jobs.put(_STOP)
    jobs.join()
    thread.join()


if __name__ == "__main__":
    main()
```
