"""Small, documented algorithm implementations."""
from collections import Counter, deque


def lower_bound(values: list[int], target: int) -> int:
    """Return first index whose value is >= target. O(log n), O(1) space."""
    low, high = 0, len(values)
    while low < high:
        middle = (low + high) // 2
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle
    return low


def top_k_frequent(values: list[int], k: int) -> list[tuple[int, int]]:
    """Return up to k (value, frequency) pairs. O(n + u log u) worst case."""
    if k < 0:
        raise ValueError("k cannot be negative")
    return Counter(values).most_common(k)


def bfs(graph: dict[str, list[str]], start: str) -> list[str]:
    """Return reachable nodes in BFS order. O(V + E) for adjacency lists."""
    visited = {start}
    queue = deque([start])
    order: list[str] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
