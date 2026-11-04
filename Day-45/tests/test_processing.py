from io import StringIO

from day45_profiler.processing import process_jsonl


def test_processes_valid_records_and_aggregates_categories():
    stream = StringIO(
        '{"id":"a","category":"books","value":10}\n'
        '{"id":"b","category":"books","value":2.5}\n'
        '{"id":"c","category":"games","value":4}\n'
    )

    result = process_jsonl(stream)

    assert result.total_lines == 3
    assert result.valid_records == 3
    assert result.invalid_records == 0
    assert result.counts_by_category == {"books": 2, "games": 1}
    assert result.totals_by_category == {"books": 12.5, "games": 4.0}


def test_invalid_records_are_counted_and_processing_continues():
    stream = StringIO(
        '{"id":"a","category":"books","value":10}\n'
        '{"id":"b","category":"books","value":true}\n'
        'not-json\n'
        '{"id":"c","category":"games","value":4}\n'
    )

    result = process_jsonl(stream)

    assert result.total_lines == 4
    assert result.valid_records == 2
    assert result.invalid_records == 2
    assert result.counts_by_category == {"books": 1, "games": 1}


def test_blank_lines_are_ignored():
    result = process_jsonl(StringIO("\n  \n"))
    assert result.total_lines == 0
    assert result.valid_records == 0
    assert result.invalid_records == 0


def test_non_finite_numbers_are_rejected():
    result = process_jsonl(StringIO('{"id":"a","category":"x","value":NaN}\n'))
    assert result.valid_records == 0
    assert result.invalid_records == 1
