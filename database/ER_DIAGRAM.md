# ER diagram

```mermaid
erDiagram
    PLAYERS ||--o{ MATCHES : "1:N"
    MATCHES ||--o{ MATCH_WEAPONS : "1:N"
    WEAPONS ||--o{ MATCH_WEAPONS : "1:N"

    PLAYERS {
        int id PK
        string name UNIQUE
        string email UNIQUE
        datetime registered_at
    }

    MATCHES {
        int id PK
        int player_id FK
        int score
        float duration_seconds
        datetime match_date
    }

    WEAPONS {
        int id PK
        string name UNIQUE
        int damage
        string rarity
    }

    MATCH_WEAPONS {
        int match_id PK, FK
        int weapon_id PK, FK
        int kills_with_weapon
    }
```
