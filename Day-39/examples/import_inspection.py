import importlib
import json
import sys


if __name__ == "__main__":
    print("module name:", __name__)
    print("python executable:", sys.executable)
    print("first import paths:", sys.path[:3])
    print("json module:", json.__file__)
    print("cached in sys.modules:", "json" in sys.modules)

    module = importlib.import_module("math")
    print("dynamic import:", module.sqrt(81))
    print("cached math module:", sys.modules["math"] is module)
