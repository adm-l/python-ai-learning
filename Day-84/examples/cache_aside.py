# Day 84 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python cache_aside.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""A bounded TTL cache-aside example using the standard library."""
from collections import OrderedDict
from time import monotonic
from typing import Callable, TypeVar

T = TypeVar("T")


class TTLCache:
    def __init__(self, max_entries: int = 100) -> None:
        if max_entries < 1:
            raise ValueError("max_entries must be positive")
        self.max_entries = max_entries
        self._items: OrderedDict[str, tuple[float, object]] = OrderedDict()

    def get_or_load(self, key: str, ttl: float, loader: Callable[[], T]) -> T:
        now = monotonic()
        item = self._items.get(key)
        if item and item[0] > now:
            self._items.move_to_end(key)
            return item[1]  # type: ignore[return-value]
        value = loader()
        self._items[key] = (now + ttl, value)
        self._items.move_to_end(key)
        while len(self._items) > self.max_entries:
            self._items.popitem(last=False)
        return value


if __name__ == "__main__":
    cache = TTLCache(2)
    print(cache.get_or_load("customer:1", 30, lambda: {"id": 1}))
```
