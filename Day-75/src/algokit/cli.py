"""Command-line demonstration for the algorithm toolkit."""
import argparse
import json

from .algorithms import bfs, lower_bound, top_k_frequent


def main() -> None:
    parser = argparse.ArgumentParser(description="Demonstrate algorithm toolkit functions")
    parser.add_argument("--target", type=int, default=4)
    args = parser.parse_args()
    values = [1, 2, 4, 4, 5, 7]
    graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    output = {
        "lower_bound_index": lower_bound(values, args.target),
        "top_frequent": top_k_frequent([1, 1, 2, 2, 2, 3], 2),
        "bfs": bfs(graph, "A"),
    }
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
