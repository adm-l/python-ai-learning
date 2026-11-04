import json

from day45_profiler import cli


def test_cli_prints_summary_and_returns_success(tmp_path, monkeypatch, capsys):
    source = tmp_path / "records.jsonl"
    source.write_text(
        '{"id":"a","category":"books","value":5}\n',
        encoding="utf-8",
    )
    monkeypatch.setattr("sys.argv", ["day45-profiler", str(source)])

    assert cli.main() == 0
    output = json.loads(capsys.readouterr().out)
    assert output["valid_records"] == 1
    assert output["totals_by_category"] == {"books": 5.0}


def test_cli_returns_one_when_invalid_records_exist(tmp_path, monkeypatch):
    source = tmp_path / "records.jsonl"
    source.write_text("not-json\n", encoding="utf-8")
    monkeypatch.setattr("sys.argv", ["day45-profiler", str(source)])

    assert cli.main() == 1


def test_cli_returns_two_when_file_is_missing(tmp_path, monkeypatch):
    source = tmp_path / "missing.jsonl"
    monkeypatch.setattr("sys.argv", ["day45-profiler", str(source)])

    assert cli.main() == 2
