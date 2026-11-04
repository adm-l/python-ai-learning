"""Stream records incrementally and allow early consumer exit."""
import asyncio
from collections.abc import AsyncIterator


async def records() -> AsyncIterator[int]:
    for value in range(10):
        await asyncio.sleep(0)
        yield value


async def main() -> None:
    async for value in records():
        print(value)
        if value == 4:
            break


if __name__ == "__main__":
    asyncio.run(main())
