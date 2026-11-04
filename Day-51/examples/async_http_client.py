"""HTTP client with explicit timeout and bounded retries. Install httpx first."""
import asyncio
import sys
import httpx


async def get_with_retry(url: str, attempts: int = 3) -> int:
    timeout = httpx.Timeout(5.0, connect=2.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(attempts):
            try:
                response = await client.get(url)
                response.raise_for_status()
                return response.status_code
            except (httpx.TimeoutException, httpx.TransportError):
                if attempt == attempts - 1:
                    raise
                await asyncio.sleep(0.2 * (2**attempt))
    raise RuntimeError("unreachable")


async def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python async_http_client.py URL")
    print(await get_with_retry(sys.argv[1]))


if __name__ == "__main__":
    asyncio.run(main())
