import pytest

from task_runner.runner import Job, parse_job, run_jobs


def test_parse_job_validates_types() -> None:
    assert parse_job({"job_id": "a", "operation": "double", "value": 4}) == Job("a", "double", 4)
    with pytest.raises(ValueError):
        parse_job({"job_id": "", "operation": "double", "value": 4})
    with pytest.raises(ValueError):
        parse_job({"job_id": "a", "operation": "double", "value": True})


@pytest.mark.asyncio
async def test_run_jobs_preserves_order_and_completes() -> None:
    results = await run_jobs([Job("a", "double", 3), Job("b", "double", 8)], workers=2, queue_size=1)
    assert [(item.job_id, item.status, item.result) for item in results] == [
        ("a", "completed", 6), ("b", "completed", 16)
    ]


@pytest.mark.asyncio
async def test_duplicate_id_is_not_executed_twice() -> None:
    results = await run_jobs([Job("same", "double", 2), Job("same", "double", 9)])
    assert [item.status for item in results] == ["completed", "duplicate"]


@pytest.mark.asyncio
async def test_invalid_job_fails_without_crashing_pool() -> None:
    results = await run_jobs([Job("bad", "double", -1), Job("good", "double", 5)])
    assert results[0].status == "failed"
    assert results[1].result == 10


@pytest.mark.asyncio
async def test_invalid_limits_are_rejected() -> None:
    with pytest.raises(ValueError):
        await run_jobs([], workers=0)
