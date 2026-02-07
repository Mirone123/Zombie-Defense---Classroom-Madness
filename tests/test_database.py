from pathlib import Path

from game import database


def test_register_and_save_result(tmp_path: Path):
    db_path = tmp_path / "game.db"
    schema_path = Path("database/schema.sql")

    database.init_db(db_path=db_path, schema_path=schema_path)

    # Monkey-patch module global used by helper methods.
    original = database.DB_PATH
    database.DB_PATH = db_path
    try:
        player_id = database.register_player("TestPlayer", "test@example.com")
        assert player_id > 0

        database.save_match_result("TestPlayer", 42, 12.3)
        leaderboard = database.get_leaderboard(5)
        assert leaderboard
        assert leaderboard[0]["jmeno"] == "TestPlayer"
        assert leaderboard[0]["skore"] == 42
    finally:
        database.DB_PATH = original
