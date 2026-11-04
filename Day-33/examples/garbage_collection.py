import gc
import weakref


class Node:
    def __init__(self, name):
        self.name = name
        self.peer = None


if __name__ == "__main__":
    node = Node("temporary")
    reference = weakref.ref(node)
    print("alive before delete:", reference() is not None)
    del node
    print("alive after delete:", reference() is not None)

    left = Node("left")
    right = Node("right")
    left.peer = right
    right.peer = left
    del left, right

    before = gc.get_count()
    collected = gc.collect()
    print("GC counts before explicit collection:", before)
    print("objects collected (runtime dependent):", collected)
    print("tracked list:", gc.is_tracked([]))
