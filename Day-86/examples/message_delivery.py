# Day 86 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python message_delivery.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""At-least-once delivery simulation and idempotent consumer."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    event_id: str
    payload: str


class IdempotentConsumer:
    def __init__(self) -> None:
        self.processed: set[str] = set()
        self.values: list[str] = []

    def handle(self, event: Event) -> bool:
        if event.event_id in self.processed:
            return False
        # In production, persist the dedupe marker and business change atomically.
        self.values.append(event.payload)
        self.processed.add(event.event_id)
        return True


if __name__ == "__main__":
    consumer = IdempotentConsumer()
    event = Event("evt-1", "order-created")
    print(consumer.handle(event), consumer.handle(event), consumer.values)
```
