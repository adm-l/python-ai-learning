# Day 73 example

Run with Python 3.12:

```bash
python graph_algorithms.py
```

Teaching example; add tests and explore edge cases from the lesson.

```python
"""Kahn topological sorting and Dijkstra shortest paths."""
import heapq
from collections import defaultdict, deque


def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    indegree = {node: 0 for node in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree.setdefault(neighbor, 0)
            indegree[neighbor] += 1
    queue = deque(node for node, degree in indegree.items() if degree == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != len(indegree):
        raise ValueError("graph contains a cycle")
    return order


def dijkstra(graph: dict[str, list[tuple[str, int]]], start: str) -> dict[str, int]:
    distances = {start: 0}
    heap = [(0, start)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance != distances[node]:
            continue
        for neighbor, weight in graph.get(node, []):
            if weight < 0:
                raise ValueError("Dijkstra requires non-negative weights")
            candidate = distance + weight
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))
    return distances


if __name__ == "__main__":
    print(topological_sort({"compile": ["test"], "test": ["deploy"], "deploy": []}))
    weighted = {"A": [("B", 4), ("C", 1)], "C": [("B", 2)], "B": []}
    print(dijkstra(weighted, "A"))
```
