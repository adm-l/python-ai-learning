"""CLI for JSONL job input."""
import argparse
import asyncio
import json
from pathlib import Path

from .runner import parse_job, run_jobs


def main() -> None:
    parser = argparse.ArgumentParser(description="Run bounded asynchronous JSONL jobs")
    parser.add_argument("input", type=Path)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--queue-size", type=int, default=4)
    parser.add_argument("--retries", type=int, default=1)
    args = parser.parse_args()
    try:
        jobs = [parse_job(json.loads(line)) for line in args.input.read_text().splitlines() if line.strip()]
        results = asyncio.run(run_jobs(jobs, workers=args.workers, queue_size=args.queue_size, retries=args.retries))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.exit(2, f"error: {exc}\\n")
    for result in results:
        print(json.dumps(result.__dict__, sort_keys=True))
    if any(result.status == "failed" for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
