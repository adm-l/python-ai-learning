"""Application service: transactionally writes order, idempotency key and outbox event."""
import hashlib
import json
import sqlite3


class IdempotencyConflict(Exception):
    pass


def create_order(connection: sqlite3.Connection, customer_id: str, total_cents: int, key: str) -> dict:
    canonical = json.dumps({"customer_id": customer_id, "total_cents": total_cents}, sort_keys=True)
    fingerprint = hashlib.sha256(canonical.encode()).hexdigest()
    existing = connection.execute(
        "SELECT request_fingerprint, order_id FROM idempotency_keys WHERE key = ?", (key,)
    ).fetchone()
    if existing:
        if existing["request_fingerprint"] != fingerprint:
            raise IdempotencyConflict("idempotency key was already used for a different request")
        row = connection.execute("SELECT * FROM orders WHERE id = ?", (existing["order_id"],)).fetchone()
        return dict(row)

    with connection:
        cursor = connection.execute(
            "INSERT INTO orders(customer_id, total_cents) VALUES (?, ?)",
            (customer_id, total_cents),
        )
        order_id = int(cursor.lastrowid)
        connection.execute(
            "INSERT INTO idempotency_keys(key, request_fingerprint, order_id) VALUES (?, ?, ?)",
            (key, fingerprint, order_id),
        )
        event_id = f"order:{order_id}:created"
        payload = json.dumps({"order_id": order_id, "customer_id": customer_id, "total_cents": total_cents})
        connection.execute(
            "INSERT INTO outbox(event_id, aggregate_id, event_type, payload) VALUES (?, ?, ?, ?)",
            (event_id, order_id, "OrderCreated", payload),
        )
    row = connection.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
    return dict(row)
