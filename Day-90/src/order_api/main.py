"""FastAPI transport layer. Run with: uvicorn order_api.main:app --reload."""
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel, Field

from .database import Database
from .service import IdempotencyConflict, create_order


class OrderCreate(BaseModel):
    customer_id: str = Field(min_length=1, max_length=100)
    total_cents: int = Field(gt=0, le=100_000_000)


def create_app(database_path: str | None = None) -> FastAPI:
    path = database_path or os.getenv("ORDER_API_DB", "var/orders.db")

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.database = Database(path)
        yield

    application = FastAPI(title="Day 90 Order API", version="1.0.0", lifespan=lifespan)

    @application.get("/health/live")
    def live() -> dict[str, str]:
        return {"status": "alive"}

    @application.get("/health/ready")
    def ready(request: Request) -> dict[str, str]:
        try:
            with request.app.state.database.connect() as connection:
                connection.execute("SELECT 1")
        except Exception as exc:
            raise HTTPException(status_code=503, detail="database unavailable") from exc
        return {"status": "ready"}

    @application.post("/orders", status_code=201)
    def post_order(
        payload: OrderCreate,
        request: Request,
        idempotency_key: str = Header(min_length=8, max_length=128, alias="Idempotency-Key"),
    ) -> dict:
        try:
            with request.app.state.database.connect() as connection:
                return create_order(connection, payload.customer_id, payload.total_cents, idempotency_key)
        except IdempotencyConflict as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc

    @application.get("/orders/{order_id}")
    def get_order(order_id: int, request: Request) -> dict:
        with request.app.state.database.connect() as connection:
            row = connection.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="order not found")
        return dict(row)

    return application


app = create_app()


def run() -> None:
    import uvicorn
    uvicorn.run("order_api.main:app", host="127.0.0.1", port=8000)
