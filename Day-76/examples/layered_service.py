# Day 76 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python layered_service.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""A tiny domain/service/repository split without a web framework."""
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Order:
    order_id: str
    total_cents: int


class OrderRepository(Protocol):
    def save(self, order: Order) -> None: ...


class MemoryOrderRepository:
    def __init__(self) -> None:
        self.orders: dict[str, Order] = {}

    def save(self, order: Order) -> None:
        self.orders[order.order_id] = order


class OrderService:
    def __init__(self, repository: OrderRepository) -> None:
        self.repository = repository

    def create(self, order_id: str, total_cents: int) -> Order:
        if not order_id or total_cents <= 0:
            raise ValueError("order id and positive total are required")
        order = Order(order_id, total_cents)
        self.repository.save(order)
        return order


if __name__ == "__main__":
    repo = MemoryOrderRepository()
    print(OrderService(repo).create("ord-1", 1250))
```
