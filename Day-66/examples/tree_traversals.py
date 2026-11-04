# Day 66 example

Run with Python 3.12:

```bash
python tree_traversals.py
```

Teaching example; extend it with tests and validation as described in the lesson.

```python
"""Binary tree traversals and breadth-first levels."""
from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: "Node | None" = None
    right: "Node | None" = None


def preorder(root: Node | None) -> list[int]:
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root: Node | None) -> list[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def level_order(root: Node | None) -> list[int]:
    if root is None:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == "__main__":
    root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    print(preorder(root), inorder(root), level_order(root))
```
