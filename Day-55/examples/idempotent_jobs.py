"""Duplicate job delivery and an in-memory idempotency guard."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Job:
    idempotency_key: str
    amount: int


class Worker:
    def __init__(self) -> None:
        self.completed: set[str] = set()
        self.total = 0

    def handle(self, job: Job) -> bool:
        if job.idempotency_key in self.completed:
            return False
        # Production systems must persist the key and side effect atomically.
        self.total += job.amount
        self.completed.add(job.idempotency_key)
        return True


def main() -> None:
    worker = Worker()
    job = Job("payment-123", 500)
    print(worker.handle(job), worker.handle(job), worker.total)


if __name__ == "__main__":
    main()
