"""Composition and dependency injection without a framework."""
from collections.abc import Iterable
from typing import Protocol


class DataSource(Protocol):
    def load(self) -> Iterable[int]: ...


class MemorySource:
    def __init__(self, values: list[int]) -> None:
        self.values = values

    def load(self) -> Iterable[int]:
        return self.values


class Report:
    def __init__(self, source: DataSource) -> None:
        self.source = source

    def render(self) -> str:
        values = list(self.source.load())
        return f"count={len(values)}, total={sum(values)}"


if __name__ == "__main__":
    report = Report(MemorySource([10, 20, 30]))
    print(report.render())
