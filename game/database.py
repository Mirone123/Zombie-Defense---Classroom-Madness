"""SQLite persistence layer used by game runtime and web integration."""

from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "game.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def get_connection(db_path: Path | None = None) -> sqlite3.Connection:
    """Create SQLite connection with row dict-like access enabled."""
    db_path = db_path or DB_PATH
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: Path | None = None, schema_path: Path = SCHEMA_PATH) -> None:
    """Initialize DB schema from file (or fallback schema)."""
    with get_connection(db_path or DB_PATH) as conn:
        if schema_path.exists():
            conn.executescript(schema_path.read_text(encoding="utf-8"))
        else:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS matches (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player_id INTEGER NOT NULL,
                    score INTEGER NOT NULL DEFAULT 0,
                    match_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    duration_seconds REAL NOT NULL DEFAULT 0,
                    FOREIGN KEY(player_id) REFERENCES players(id)
                );
                """
            )


def save_match_result(player_name: str, score: int, duration_seconds: float) -> None:
    """Insert player if needed and save one match row."""
    cleaned_name = player_name.strip() or "Hrac"
    match_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO players(name) VALUES (?) ON CONFLICT(name) DO NOTHING",
            (cleaned_name,),
        )
        player_id = conn.execute("SELECT id FROM players WHERE name = ?", (cleaned_name,)).fetchone()["id"]
        conn.execute(
            """
            INSERT INTO matches(player_id, score, match_date, duration_seconds)
            VALUES (?, ?, ?, ?)
            """,
            (player_id, int(score), match_date, float(duration_seconds)),
        )


def get_leaderboard(limit: int = 5) -> list[dict[str, str | int | float]]:
    """Return leaderboard rows sorted by score and date."""
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT p.name AS jmeno, m.score AS skore, m.match_date AS datum, m.duration_seconds AS doba
            FROM matches m
            JOIN players p ON p.id = m.player_id
            ORDER BY m.score DESC, m.match_date DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    return [dict(row) for row in rows]


def register_player(name: str, email: str | None = None) -> int:
    """Register player account (or update email) and return player id."""
    clean_name = name.strip()
    if not clean_name:
        raise ValueError("Jméno hráče nesmí být prázdné.")

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO players(name, email)
            VALUES (?, ?)
            ON CONFLICT(name) DO UPDATE SET email = COALESCE(excluded.email, players.email)
            """,
            (clean_name, email.strip() if email else None),
        )
        row = conn.execute("SELECT id FROM players WHERE name = ?", (clean_name,)).fetchone()
        return int(row["id"])
