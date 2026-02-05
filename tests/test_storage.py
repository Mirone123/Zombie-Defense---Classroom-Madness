from pathlib import Path

from game import storage


def test_save_and_load_scores_sorted(tmp_path: Path):
    file_path = tmp_path / "scores.json"

    storage.save_score("Alice", 10, "2026-01-01 10:00:00", file_path=file_path)
    storage.save_score("Bob", 20, "2026-01-01 10:01:00", file_path=file_path)

    scores = storage.load_scores(file_path=file_path)
    assert scores[0]["jmeno"] == "Bob"
    assert scores[0]["skore"] == 20


def test_format_score_line_defaults():
    line = storage.format_score_line({})
    assert line == "Hrac | 0 | -"
