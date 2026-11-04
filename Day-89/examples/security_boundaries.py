# Day 89 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python security_boundaries.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""Framework-independent authorization and input validation examples."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Principal:
    subject: str
    tenant_id: str
    roles: frozenset[str]


def require_role(principal: Principal | None, role: str) -> Principal:
    if principal is None:
        raise PermissionError("authentication required")
    if role not in principal.roles:
        raise PermissionError("insufficient permissions")
    return principal


def authorize_tenant(principal: Principal, requested_tenant: str) -> None:
    if principal.tenant_id != requested_tenant:
        raise PermissionError("cross-tenant access denied")


def validate_page_size(value: int) -> int:
    if not 1 <= value <= 100:
        raise ValueError("page size must be between 1 and 100")
    return value


if __name__ == "__main__":
    user = Principal("u-1", "tenant-a", frozenset({"orders:read"}))
    require_role(user, "orders:read")
    authorize_tenant(user, "tenant-a")
    print("authorized", validate_page_size(25))
```
