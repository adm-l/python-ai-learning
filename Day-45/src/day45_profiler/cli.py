from __future__ import annotations

import argparse
import json
import logging
import sys

from day45_profiler.processing import process_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Stream a JSON Lines file and summarize numeric values by category."
    )
    parser.add_argument("input", help="Path to a UTF-8 JSONL input file")
    parser.add_argument(
        "--log-level",
        choices=("DEBUG", "INFO", "WARNING", "ERROR"),
        default="WARNING",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    try:
        result = process_file(args.input)
    except OSError as exc:
        logging.error("cannot read input file: %s", exc)
        return 2

    print(json.dumps(result.to_dict(), indent=2, sort_keys=True))
    return 0 if result.invalid_records == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
