# Day 81 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python relational_model.sql
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
-- Relational model with explicit constraints and useful indexes.
CREATE TABLE customers (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE orders (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id BIGINT NOT NULL REFERENCES customers(id),
    status TEXT NOT NULL CHECK (status IN ('pending', 'paid', 'cancelled')),
    total_cents BIGINT NOT NULL CHECK (total_cents > 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE order_items (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id BIGINT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    sku TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price_cents BIGINT NOT NULL CHECK (unit_price_cents >= 0)
);

CREATE INDEX orders_customer_created_idx ON orders(customer_id, created_at DESC);
CREATE INDEX order_items_order_idx ON order_items(order_id);
```
