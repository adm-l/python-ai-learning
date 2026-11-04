"""Stack and queue operations with list and deque."""
from collections import deque


def brackets_are_balanced(source: str) -> bool:
    matching = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in source:
        if char in "([{":
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
    return len(stack) == 0


def next_larger(values: list[int]) -> list[int]:
    answer = [-1] * len(values)
    pending: list[int] = []
    for position, number in enumerate(values):
        while pending and values[pending[-1]] < number:
            answer[pending.pop()] = number
        pending.append(position)
    return answer


if __name__ == "__main__":
    queue = deque([10, 20, 30])
    print(queue.popleft())
    print(brackets_are_balanced("{[()]}"))
    print(next_larger([2, 1, 2, 4, 3]))
