from fastapi.testclient import TestClient

from order_api.main import create_app


def test_create_order_and_idempotent_replay(tmp_path) -> None:
    client = TestClient(create_app(str(tmp_path / "test.db")))
    payload = {"customer_id": "customer-1", "total_cents": 2500}
    first = client.post("/orders", json=payload, headers={"Idempotency-Key": "request-0001"})
    replay = client.post("/orders", json=payload, headers={"Idempotency-Key": "request-0001"})
    assert first.status_code == 201
    assert replay.status_code == 201
    assert first.json()["id"] == replay.json()["id"]


def test_idempotency_key_cannot_change_payload(tmp_path) -> None:
    client = TestClient(create_app(str(tmp_path / "test.db")))
    headers = {"Idempotency-Key": "request-0002"}
    assert client.post("/orders", json={"customer_id": "c1", "total_cents": 100}, headers=headers).status_code == 201
    response = client.post("/orders", json={"customer_id": "c1", "total_cents": 200}, headers=headers)
    assert response.status_code == 409


def test_validation_and_not_found(tmp_path) -> None:
    client = TestClient(create_app(str(tmp_path / "test.db")))
    invalid = client.post("/orders", json={"customer_id": "", "total_cents": 0}, headers={"Idempotency-Key": "request-0003"})
    assert invalid.status_code == 422
    assert client.get("/orders/999").status_code == 404
    assert client.get("/health/live").json() == {"status": "alive"}
    assert client.get("/health/ready").json() == {"status": "ready"}


def test_outbox_written_atomically(tmp_path) -> None:
    from order_api.database import Database
    from order_api.service import create_order

    database = Database(str(tmp_path / "outbox.db"))
    with database.connect() as connection:
        order = create_order(connection, "customer-x", 999, "request-0004")
        rows = connection.execute("SELECT event_type, aggregate_id FROM outbox").fetchall()
    assert len(rows) == 1
    assert rows[0]["event_type"] == "OrderCreated"
    assert rows[0]["aggregate_id"] == order["id"]
