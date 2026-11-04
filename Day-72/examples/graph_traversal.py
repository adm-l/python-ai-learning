# Day 72 example

Run with Python 3.12:

```bash
python graph_traversal.py
```

Teaching example; add tests and explore edge cases from the lesson.

```python
"""Breadth-first and depth-first graph traversal."""
from collections import deque

Graph = dict[str, list[str]]


def bfs(graph: Graph, start: str) -> list[str]:
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def dfs(graph: Graph, start: str) -> list[str]:
    visited: set[str] = set()
    order: list[str] = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph.get(node, [])))
    return order


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    print("BFS", bfs(graph, "A"))
    print("DFS", dfs(graph, "A"))
```
