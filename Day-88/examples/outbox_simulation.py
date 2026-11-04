# Day 88 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python outbox_simulation.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""Transactional outbox concept using one SQLite database."""
import json
import sqlite3


def initialize(db: sqlite3.Connection) -> None:
    db.executescript("""
    CREATE TABLE orders(id TEXT PRIMARY KEY, status TEXT NOT NULL);
    CREATE TABLE outbox(event_id TEXT PRIMARY KEY, aggregate_id TEXT NOT NULL,
                        event_type TEXT NOT NULL, payload TEXT NOT NULL,
                        published INTEGER NOT NULL DEFAULT 0);
    """)


def create_order(db: sqlite3.Connection, order_id: str) -> None:
    with db:
        db.execute("INSERT INTO orders VALUES (?, 'created')", (order_id,))
        db.execute(
            "INSERT INTO outbox(event_id, aggregate_id, event_type, payload) VALUES (?, ?, ?, ?)",
            (f"{order_id}:created", order_id, "OrderCreated", json.dumps({"order_id": order_id})),
        )


def pending_events(db: sqlite3.Connection) -> list[tuple[str, str]]:
    return db.execute(
        "SELECT event_id, payload FROM outbox WHERE published = 0 ORDER BY rowid"
    ).fetchall()


if __name__ == "__main__":
    db = sqlite3.connect(":memory:")
    initialize(db)
    create_order(db, "order-1")
    print(pending_events(db))
```
