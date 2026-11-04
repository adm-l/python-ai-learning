import pytest

from algokit.algorithms import bfs, lower_bound, top_k_frequent


def test_lower_bound_boundaries() -> None:
    assert lower_bound([], 2) == 0
    assert lower_bound([1, 2, 2, 4], 2) == 1
    assert lower_bound([1, 2, 2, 4], 3) == 3
    assert lower_bound([1, 2], 9) == 2


def test_top_k_frequent() -> None:
    assert top_k_frequent([1, 1, 2, 2, 2, 3], 2) == [(2, 3), (1, 2)]
    assert top_k_frequent([], 3) == []
    with pytest.raises(ValueError):
        top_k_frequent([1], -1)


def test_bfs_handles_cycles_and_disconnected_nodes() -> None:
    graph = {"a": ["b"], "b": ["a", "c"], "x": []}
    assert bfs(graph, "a") == ["a", "b", "c"]
    assert bfs(graph, "missing") == ["missing"]
