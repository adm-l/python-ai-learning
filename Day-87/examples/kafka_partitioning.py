# Day 87 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python kafka_partitioning.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""Illustrate deterministic key partitioning (not Kafka's exact partitioner)."""
import hashlib


def partition_for(key: str, partition_count: int) -> int:
    if partition_count < 1:
        raise ValueError("partition_count must be positive")
    digest = hashlib.sha256(key.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") % partition_count


if __name__ == "__main__":
    for order_id in ("order-1", "order-2", "order-3", "order-1"):
        print(order_id, partition_for(order_id, 6))
```
