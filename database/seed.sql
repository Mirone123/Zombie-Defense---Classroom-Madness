INSERT INTO players (name, email) VALUES
('Alice', 'alice@school.local'),
('Bob', 'bob@school.local'),
('Cyril', 'cyril@school.local')
ON CONFLICT(name) DO NOTHING;

INSERT INTO weapons (name, damage, rarity) VALUES
('Pistol', 12, 'common'),
('Shotgun', 25, 'rare'),
('Laser', 35, 'epic')
ON CONFLICT(name) DO NOTHING;

INSERT INTO matches (player_id, score, duration_seconds, match_date) VALUES
(1, 15, 102.5, '2026-01-10 14:00:00'),
(2, 22, 140.0, '2026-01-11 14:00:00'),
(1, 30, 180.3, '2026-01-12 14:00:00');

INSERT INTO match_weapons (match_id, weapon_id, kills_with_weapon) VALUES
(1, 1, 8),
(1, 2, 7),
(2, 2, 12),
(2, 3, 10),
(3, 3, 30);
