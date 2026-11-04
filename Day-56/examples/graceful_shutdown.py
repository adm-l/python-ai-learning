"""Worker loop that responds to a cooperative stop event."""
import asyncio


async def run_worker(stop: asyncio.Event) -> None:
    while not stop.is_set():
        try:
            await asyncio.wait_for(stop.wait(), timeout=0.5)
        except TimeoutError:
            print("worker heartbeat")
    print("worker stopped")


async def main() -> None:
    stop = asyncio.Event()
    task = asyncio.create_task(run_worker(stop))
    await asyncio.sleep(1)
    stop.set()
    await asyncio.wait_for(task, timeout=2)


if __name__ == "__main__":
    asyncio.run(main())
