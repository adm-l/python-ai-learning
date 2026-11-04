from __future__ import annotations

import json
import math
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import TextIO


@dataclass(frozen=True)
class ProcessingResult:
    total_lines: int
    valid_records: int
    invalid_records: int
    counts_by_category: dict[str, int]
    totals_by_category: dict[str, float]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def _validate_record(value: object) -> tuple[str, str, float]:
    if not isinstance(value, dict):
        raise ValueError("record must be a JSON object")

    identifier = value.get("id")
    category = value.get("category")
    amount = value.get("value")

    if not isinstance(identifier, str) or not identifier.strip():
        raise ValueError("id must be a non-empty string")
    if not isinstance(category, str) or not category.strip():
        raise ValueError("category must be a non-empty string")
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("value must be a number")
    numeric_value = float(amount)
    if not math.isfinite(numeric_value):
        raise ValueError("value must be finite")

    return identifier, category, numeric_value


def process_jsonl(stream: TextIO) -> ProcessingResult:
    """Process newline-delimited JSON with memory bounded by category count."""
    counts: Counter[str] = Counter()
    totals: Counter[str] = Counter()
    total_lines = valid_records = invalid_records = 0

    for line_number, line in enumerate(stream, start=1):
        if not line.strip():
            continue
        total_lines += 1
        try:
            record = json.loads(line)
            _, category, amount = _validate_record(record)
        except (json.JSONDecodeError, ValueError) as exc:
            invalid_records += 1
            continue

        valid_records += 1
        counts[category] += 1
        totals[category] += amount

    return ProcessingResult(
        total_lines=total_lines,
        valid_records=valid_records,
        invalid_records=invalid_records,
        counts_by_category=dict(sorted(counts.items())),
        totals_by_category=dict(sorted(totals.items())),
    )


def process_file(path: str | Path) -> ProcessingResult:
    with Path(path).open("r", encoding="utf-8") as stream:
        return process_jsonl(stream)
