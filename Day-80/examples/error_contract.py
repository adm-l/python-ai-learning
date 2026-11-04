# Day 80 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python error_contract.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""Framework-independent validation and error response shape."""
from dataclasses import dataclass


@dataclass(frozen=True)
class ApiError:
    code: str
    message: str
    request_id: str

    def as_dict(self) -> dict[str, str]:
        return {"code": self.code, "message": self.message, "request_id": self.request_id}


def validate_page(limit: int, offset: int) -> tuple[int, int]:
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    if offset < 0:
        raise ValueError("offset cannot be negative")
    return limit, offset


if __name__ == "__main__":
    print(ApiError("not_found", "Order not found", "req-123").as_dict())
    print(validate_page(20, 0))
```
