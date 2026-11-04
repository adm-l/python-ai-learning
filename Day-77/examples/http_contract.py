# Day 77 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python http_contract.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""Illustrate HTTP status and idempotency semantics at the application boundary."""
from dataclasses import dataclass


@dataclass(frozen=True)
class HttpResult:
    status: int
    body: dict[str, object]
    headers: dict[str, str]


def create_order(order_id: str, total: int) -> HttpResult:
    if not order_id or total <= 0:
        return HttpResult(422, {"error": "invalid_order"}, {})
    return HttpResult(201, {"id": order_id, "total": total}, {"Location": f"/orders/{order_id}"})


def get_missing_order(order_id: str) -> HttpResult:
    return HttpResult(404, {"error": "not_found", "resource": order_id}, {})


if __name__ == "__main__":
    print(create_order("o-123", 500))
    print(get_missing_order("o-404"))
```
