from copy import copy, deepcopy


if __name__ == "__main__":
    original = {"users": [{"name": "Ada"}]}
    shallow = copy(original)
    deep = deepcopy(original)

    shallow["users"][0]["name"] = "Grace"
    print("original after shallow nested mutation:", original["users"][0]["name"])
    deep["users"][0]["name"] = "Lin"
    print("original after deep nested mutation:", original["users"][0]["name"])
    print("deep copy:", deep)

    immutable_container = ("settings", ["dark"])
    immutable_container[1].append("high-contrast")
    print("tuple containing mutable list:", immutable_container)

    try:
        {["not", "hashable"]: "value"}
    except TypeError as exc:
        print("unhashable key:", type(exc).__name__)
