def mutate(items):
    items.append("changed")


def rebind(items):
    items = ["new object"]
    return items


if __name__ == "__main__":
    original = ["initial"]
    alias = original
    print("same identity:", original is alias)
    mutate(alias)
    print("mutation visible:", original)

    replacement = rebind(original)
    print("caller unchanged by rebinding:", original)
    print("replacement:", replacement)

    equal_but_distinct = ["initial", "changed"]
    print("equal values:", original == equal_but_distinct)
    print("same object:", original is equal_but_distinct)
