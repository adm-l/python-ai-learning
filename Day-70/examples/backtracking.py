# Day 70 example

Run with Python 3.12:

```bash
python backtracking.py
```

Teaching example; add tests and explore edge cases from the lesson.

```python
"""Generate subsets and permutations with backtracking."""


def subsets(values: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def visit(index: int) -> None:
        if index == len(values):
            result.append(path.copy())
            return
        visit(index + 1)
        path.append(values[index])
        visit(index + 1)
        path.pop()

    visit(0)
    return result


def permutations(values: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []
    used = [False] * len(values)

    def visit() -> None:
        if len(path) == len(values):
            result.append(path.copy())
            return
        for index, value in enumerate(values):
            if used[index]:
                continue
            used[index] = True
            path.append(value)
            visit()
            path.pop()
            used[index] = False

    visit()
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    print(permutations([1, 2, 3]))
```
