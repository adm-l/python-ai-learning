import platform
import sys


def sample(value):
    return value * 2


if __name__ == "__main__":
    print("implementation:", platform.python_implementation())
    print("version:", sys.version)
    print("implementation details:", sys.implementation)
    print("code object:", sample.__code__)
    print("constants:", sample.__code__.co_consts)
    print("names:", sample.__code__.co_names)
