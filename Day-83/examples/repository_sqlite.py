# Day 83 practical example

Run using Python 3.12 unless the lesson says otherwise:

```bash
python repository_sqlite.py
```

Some examples are framework-free simulations. Read the comments and lesson before treating them as production implementations.

```python
"""Parameterized SQL and a small repository boundary."""
import sqlite3


class UserRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def create(self, email: str) -> int:
        cursor = self.connection.execute("INSERT INTO users(email) VALUES (?)", (email,))
        self.connection.commit()
        return int(cursor.lastrowid)

    def find_by_email(self, email: str) -> tuple[int, str] | None:
        row = self.connection.execute(
            "SELECT id, email FROM users WHERE email = ?", (email,)
        ).fetchone()
        return (int(row[0]), str(row[1])) if row else None


if __name__ == "__main__":
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT UNIQUE NOT NULL)")
    repository = UserRepository(db)
    repository.create("dev@example.com")
    print(repository.find_by_email("dev@example.com"))
```
