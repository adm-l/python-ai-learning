# Day 49 example

Run with Python 3.12 unless the lesson states otherwise:

```bash
python async_tasks.py
```

This is a focused teaching example, not a complete production service.

```python
"""Concurrent I/O-shaped tasks; no real network access required."""
import asyncio


async def fetch_simulated(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name}: complete"


async def main() -> None:
    results = await asyncio.gather(
        fetch_simulated("catalog", 0.3),
        fetch_simulated("inventory", 0.2),
        fetch_simulated("pricing", 0.1),
    )
    print("\\n".join(results))


if __name__ == "__main__":
    asyncio.run(main())
```
