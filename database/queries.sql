-- SELECT: jednoduchy zebricek
SELECT p.name AS jmeno, m.score AS skore, m.match_date AS datum
FROM matches m
JOIN players p ON p.id = m.player_id
ORDER BY m.score DESC;

-- JOIN + agregace (M:N pres match_weapons)
SELECT p.name AS jmeno, w.name AS zbran, SUM(mw.kills_with_weapon) AS zabiti
FROM match_weapons mw
JOIN matches m ON m.id = mw.match_id
JOIN players p ON p.id = m.player_id
JOIN weapons w ON w.id = mw.weapon_id
GROUP BY p.name, w.name
ORDER BY zabiti DESC;

-- UPDATE: uprava score
UPDATE matches
SET score = score + 5
WHERE id = 1;

-- DELETE: smazani testovaciho zapasu
DELETE FROM matches
WHERE id = 999;
