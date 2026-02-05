# Zombie-Defense---Classroom-Madness

Top-down (bird-view) zombie defense hra + webová prezentace + databáze.

## Rychlé spuštění

### Hra (Python + Pygame)
```bash
python game/main.py
```

### Web (Flask: registrace/login hráče + žebříček)
```bash
python web/backend_app.py
```
Poté otevři `http://127.0.0.1:5000`.

### Testy
```bash
pytest -q
```

---

## Splnění školních požadavků (souhrn)

## 1. ročník – webová prezentace
- `web/index.html` (hlavní stránka)
- `web/diagramy.html` (vývojové diagramy)
- `web/o-hre.html` (pravidla + technické požadavky)
- `web/o-nas.html` (členové + role + kontakt)
- Všechny stránky sdílí jeden styl: `web/styles.css`
- Navigace má min. 4 odkazy (4 HTML soubory)

## 2. ročník – hra v Pythonu
- Herní smyčka (update + render): `game/main.py`
- Menu + start/konec + ovládání klávesnice/myši
- Pohyb hráče, střelba, zombie, kolize, game over
- Ukládání výsledků do souboru: `game/storage.py` (`game/scores.json`)
- Třídy a funkce jsou komentované (docstringy)

## 3. ročník – uzavření + databáze + propojení
- SQLite vrstva: `game/database.py`
- SQL skripty: `database/schema.sql`, `database/seed.sql`, `database/queries.sql`
- ER diagram: `database/ER_DIAGRAM.md`
- Vztahy 1:N i M:N + JOIN dotazy
- Web rozhraní komunikuje s DB (`web/backend_app.py`):
  - registrace/login hráče (jméno/email)
  - zobrazení výsledků (leaderboard)
- Hra ukládá výsledek jako jméno | skóre | datum

## Samostatný projekt
- Přidány automatizované testy:
  - `tests/test_storage.py`
  - `tests/test_database.py`

---

## Role a termíny (doplnitelné třídou)

### Role
- Vedoucí projektu
- Vývojář
- Dokumentátor
- Grafik/UI
- (ve 3. ročníku navíc) Správce dat

Při 3 členech se role spojují podle zadání.

### Kontrolní termíny
- 1. termín: začátek února
- 2. termín: prostředek března
- 3. termín: konec dubna
- 4. termín: začátek června

---

## Poznámky k repozitáři
- Projekt je navržen tak, aby byl snadno rozšiřitelný (moduly `player`, `enemy`, `projectile`, `ui`, `storage`, `database`).
- DB vrstva je sdílená mezi hrou a webovou částí.
