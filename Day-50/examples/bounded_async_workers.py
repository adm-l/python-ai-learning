"""Bounded asyncio queue and worker pool (Python 3.11+)."""
import asyncio


async def worker(name: str, queue: asyncio.Queue[int | None]) -> None:
    while True:
        item = await queue.get()
        try:
            if item is None:
                return
            await asyncio.sleep(0.05)
            print(f"{name} processed {item}")
        finally:
            queue.task_done()


async def main() -> None:
    queue: asyncio.Queue[int | None] = asyncio.Queue(maxsize=4)
    workers = [asyncio.create_task(worker(f"worker-{i}", queue)) for i in range(2)]
    for item in range(10):
        await queue.put(item)
    await queue.join()
    for _ in workers:
        await queue.put(None)
    await asyncio.gather(*workers)


if __name__ == "__main__":
    asyncio.run(main())
