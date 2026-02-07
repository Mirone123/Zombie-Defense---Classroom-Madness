"""File-based fallback storage for score records."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
SCORES_FILE = BASE_DIR / "game" / "scores.json"


def _read_raw_scores(file_path: Path = SCORES_FILE) -> list[dict[str, Any]]:
    """Read raw score list from JSON; return empty list when missing/corrupt."""
    if not file_path.exists():
        return []

    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    return []


def load_scores(file_path: Path = SCORES_FILE) -> list[dict[str, Any]]:
    """Load and sort scores descending by score value."""
    scores = _read_raw_scores(file_path)
    return sorted(scores, key=lambda row: int(row.get("skore", 0)), reverse=True)


def save_score(jmeno: str, skore: int, datum: str | None = None, file_path: Path = SCORES_FILE) -> dict[str, Any]:
    """Append one score record and persist JSON file."""
    datum = datum or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = {"jmeno": jmeno.strip() or "Hrac", "skore": int(skore), "datum": datum}

    scores = _read_raw_scores(file_path)
    scores.append(record)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(json.dumps(scores, ensure_ascii=False, indent=2), encoding="utf-8")

    return record


def format_score_line(score_row: dict[str, Any]) -> str:
    """Format record as 'name | score | date'."""
    return f"{score_row.get('jmeno', 'Hrac')} | {score_row.get('skore', 0)} | {score_row.get('datum', '-') }"


def get_leaderboard_lines(limit: int = 5, file_path: Path = SCORES_FILE) -> list[str]:
    """Return formatted leaderboard lines."""
    return [format_score_line(row) for row in load_scores(file_path)[:limit]]
