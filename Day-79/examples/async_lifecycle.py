# Day 79 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python async_lifecycle.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""Use lifespan to own a shared async resource."""
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Replace this placeholder with an async DB/HTTP client in a real service.
    app.state.resource = {"closed": False}
    try:
        yield
    finally:
        app.state.resource["closed"] = True


app = FastAPI(lifespan=lifespan)


@app.get("/resource-state")
async def resource_state(request: Request) -> dict[str, bool]:
    return {"closed": request.app.state.resource["closed"]}
```
