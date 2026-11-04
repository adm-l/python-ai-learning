# Day 78 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python fastapi_app.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""Minimal FastAPI CRUD-shaped example. Install fastapi and uvicorn first."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Orders API", version="1.0.0")


class OrderIn(BaseModel):
    customer_id: str = Field(min_length=1)
    total_cents: int = Field(gt=0)


class OrderOut(OrderIn):
    order_id: int


orders: dict[int, OrderOut] = {}
next_id = 1


@app.post("/orders", response_model=OrderOut, status_code=201)
def create_order(payload: OrderIn) -> OrderOut:
    global next_id
    order = OrderOut(order_id=next_id, **payload.model_dump())
    orders[next_id] = order
    next_id += 1
    return order


@app.get("/orders/{order_id}", response_model=OrderOut)
def get_order(order_id: int) -> OrderOut:
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders[order_id]
```
