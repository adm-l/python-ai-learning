"""Bounded async job runner with retries and in-memory deduplication."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Job:
    job_id: str
    operation: str
    value: int


@dataclass(frozen=True)
class JobResult:
    job_id: str
    status: str
    result: int | None = None
    error: str | None = None


def parse_job(raw: dict[str, Any]) -> Job:
    job_id, operation, value = raw.get("job_id"), raw.get("operation"), raw.get("value")
    if not isinstance(job_id, str) or not job_id:
        raise ValueError("job_id must be a non-empty string")
    if operation != "double":
        raise ValueError("operation must be 'double'")
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("value must be an integer")
    return Job(job_id, operation, value)


async def execute(job: Job) -> int:
    await asyncio.sleep(0)
    if job.value < 0:
        raise ValueError("negative values are not accepted")
    return job.value * 2


async def run_jobs(jobs: list[Job], *, workers: int = 2, queue_size: int = 4,
                   retries: int = 1) -> list[JobResult]:
    if workers < 1 or queue_size < 1 or retries < 0:
        raise ValueError("workers and queue_size must be positive; retries cannot be negative")
    queue: asyncio.Queue[tuple[int, Job] | None] = asyncio.Queue(maxsize=queue_size)
    results: list[JobResult | None] = [None] * len(jobs)
    seen: set[str] = set()

    async def worker() -> None:
        while True:
            item = await queue.get()
            try:
                if item is None:
                    return
                index, job = item
                if job.job_id in seen:
                    results[index] = JobResult(job.job_id, "duplicate", error="duplicate job_id")
                    continue
                seen.add(job.job_id)
                for attempt in range(retries + 1):
                    try:
                        value = await execute(job)
                        results[index] = JobResult(job.job_id, "completed", result=value)
                        break
                    except ValueError as exc:
                        if attempt == retries:
                            results[index] = JobResult(job.job_id, "failed", error=str(exc))
            finally:
                queue.task_done()

    tasks = [asyncio.create_task(worker()) for _ in range(workers)]
    try:
        for index, job in enumerate(jobs):
            await queue.put((index, job))
        await queue.join()
    finally:
        for _ in tasks:
            await queue.put(None)
        await asyncio.gather(*tasks)
    return [result for result in results if result is not None]
