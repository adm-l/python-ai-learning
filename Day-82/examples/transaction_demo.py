# Day 82 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python transaction_demo.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""SQLite transaction demo using only the standard library."""
import sqlite3


def transfer(connection: sqlite3.Connection, source: int, target: int, amount: int) -> None:
    if amount <= 0:
        raise ValueError("amount must be positive")
    with connection:
        debit = connection.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ? AND balance >= ?",
            (amount, source, amount),
        )
        if debit.rowcount != 1:
            raise ValueError("source account missing or insufficient funds")
        credit = connection.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, target)
        )
        if credit.rowcount != 1:
            raise ValueError("target account does not exist")


if __name__ == "__main__":
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE accounts(id INTEGER PRIMARY KEY, balance INTEGER NOT NULL CHECK(balance >= 0))")
    db.executemany("INSERT INTO accounts VALUES (?, ?)", [(1, 1000), (2, 200)])
    transfer(db, 1, 2, 300)
    print(db.execute("SELECT * FROM accounts ORDER BY id").fetchall())
```
