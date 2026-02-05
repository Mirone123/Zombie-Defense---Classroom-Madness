from pathlib import Path

from game.storage import get_leaderboard_lines, load_scores, save_score


def test_save_score_and_load_sorted(tmp_path: Path):
    scores_file = tmp_path / "scores.json"

    save_score("Alice", 12, datum="2026-01-01 10:00:00", file_path=scores_file)
    save_score("Bob", 35, datum="2026-01-01 10:01:00", file_path=scores_file)
    save_score("Cara", 20, datum="2026-01-01 10:02:00", file_path=scores_file)

    loaded = load_scores(scores_file)

    assert [row["jmeno"] for row in loaded] == ["Bob", "Cara", "Alice"]
    assert [row["skore"] for row in loaded] == [35, 20, 12]

    leaderboard = get_leaderboard_lines(limit=2, file_path=scores_file)
    assert leaderboard == [
        "Bob | 35 | 2026-01-01 10:01:00",
        "Cara | 20 | 2026-01-01 10:02:00",
    ]
