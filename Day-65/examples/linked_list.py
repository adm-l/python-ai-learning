# Day 65 example

Run with Python 3.12:

```bash
python linked_list.py
```

Teaching example; extend it with tests and validation as described in the lesson.

```python
"""Singly linked list reversal and Floyd cycle detection."""
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: "Node | None" = None


def reverse(head: Node | None) -> Node | None:
    previous = None
    current = head
    while current is not None:
        following = current.next
        current.next = previous
        previous, current = current, following
    return previous


def has_cycle(head: Node | None) -> bool:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def values(head: Node | None) -> list[int]:
    result = []
    while head is not None:
        result.append(head.value)
        head = head.next
    return result


if __name__ == "__main__":
    first = Node(1, Node(2, Node(3)))
    reversed_head = reverse(first)
    print(values(reversed_head), has_cycle(reversed_head))
```
