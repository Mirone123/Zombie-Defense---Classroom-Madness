# Zombie-Defense---Classroom-Madness


## Automatizované testy

Projekt obsahuje test runner `pytest` a testy ve složce `tests/`.

### Spuštění testů lokálně
1. (Doporučeno) vytvoř si virtuální prostředí:
   - `python -m venv .venv`
   - Linux/macOS: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
2. Nainstaluj závislosti pro testování:
   - `python -m pip install pytest pygame`
3. Spusť testy z kořene repozitáře:
   - `python -m pytest`

## Organizace práce v týmu

### Tabulka odpovědností členů týmu

> Aktualizace: doplňte datum poslední změny (např. `2026-02-05`) a při každé rotaci přepište tabulku.

| Člen týmu | Aktuální role | Hlavní odpovědnosti | Zástupná role při výpadku |
|---|---|---|---|
| Člen A | Vedoucí | plán sprintu, rozdělení úkolů, kontrola termínů, komunikace s vyučujícím | Produktový koordinátor |
| Člen B | Vývojář | implementace gameplay, opravy bugů, code review | Vedoucí |
| Člen C | Dokumentátor | README, zápisy, backlog, příprava prezentace | Tester |
| Člen D | Grafik | UI, assety, animace, vizuální konzistence | Vývojář |
| Člen E | Tester / DevOps | test scénáře, GitHub workflow, release buildy | Dokumentátor |

### Pravidla rotace rolí

1. **Rotace probíhá po každém kontrolním termínu** (K1, K2, K3).
2. Role **Vedoucí** se střídá povinně mezi všemi členy.
3. Nikdo nesmí mít stejnou hlavní roli více než **2 po sobě jdoucí termíny**.
4. Změna rolí musí být zaznamenána:
   - v tomto README (tabulka výše),
   - v GitHub Issues/Project boardu (přiřazení úkolů),
   - v commit zprávě označené `role-rotation`.
5. Při rotaci musí proběhnout **předávka**: otevřené úkoly, známé chyby, rozpracované větve.

---

## 1. ročník

### Role ve skupině
- Vedoucí: organizace prvního milníku a založení repozitáře/projektu.
- Vývojář: základní herní smyčka, pohyb, kolize.
- Dokumentátor: specifikace zadání, backlog, popis architektury.
- Grafik: první verze assetů (postavy, prostředí, UI prvky).

### Požadované artefakty
- Inicializovaný GitHub repozitář se strukturou projektu.
- Funkční prototyp (spuštění hry + základní interakce).
- `README.md` s cílem projektu, setupem a rozdělením rolí.
- Backlog (Issues/Project board) s prioritami.

### Kontrolní termíny a kritéria splnění
- **K1 (konec 1. měsíce):** repozitář, backlog, technické rozhodnutí.
- **K2 (polovina semestru):** hratelný prototyp s minimálně jednou herní smyčkou.
- **K3 (konec semestru):** stabilní verze prototypu + základní dokumentace.

#### Definition of Done (1. ročník)

**K1 – DoD**
- [ ] V GitHubu existuje `main` větev a minimálně 1 feature větev.
- [ ] Vytvořeno minimálně 10 backlog položek (Issues) s prioritou.
- [ ] README obsahuje popis projektu, role, setup a spuštění.
- [ ] Jsou založené štítky (`bug`, `feature`, `documentation`, `priority`).

**K2 – DoD**
- [ ] V repozitáři je kód, který po klonování spustí prototyp bez ručních zásahů.
- [ ] Minimálně 2 pull requesty prošly review (komentáře viditelné v GitHubu).
- [ ] Je doložen changelog/protokol změn od K1.
- [ ] Je přiložen krátký video/gif důkaz funkčnosti (v README nebo Releases).

**K3 – DoD**
- [ ] Uzavřené klíčové issues pro MVP 1. ročníku.
- [ ] Evidované známé chyby v samostatném seznamu.
- [ ] README obsahuje sekci „Jak hrát“ a „Známá omezení“.
- [ ] Vytvořen tag/release (např. `v0.1-school`).

---

## 2. ročník

### Role ve skupině
- Vedoucí: koordinace rozšíření funkcí a technického dluhu.
- Vývojář: AI nepřátel, ekonomika/score systém, ukládání stavu.
- Dokumentátor: aktualizace technické dokumentace, testovací plán.
- Grafik: sjednocení vizuálního stylu, nové efekty a HUD.

### Požadované artefakty
- Rozšířená hratelnost (nové mechaniky, minimálně 2 nové systémy).
- Testovací scénáře (manuální + případně automatizované).
- Aktualizovaná dokumentace architektury a modulů.
- Verze hry určená pro interní playtest.

### Kontrolní termíny a kritéria splnění
- **K1 (začátek semestru):** plán rozšíření + revize backlogu.
- **K2 (polovina semestru):** implementace hlavních nových mechanik.
- **K3 (konec semestru):** integrovaný build po playtestu a opravách.

#### Definition of Done (2. ročník)

**K1 – DoD**
- [ ] V GitHub Projectu jsou přeplánované priority pro 2. ročník.
- [ ] U každého epiku je uveden vlastník (role/člen týmu).
- [ ] V README je aktualizovaný roadmap blok pro daný semestr.
- [ ] Evidovány minimálně 3 technické dluhy a plán jejich řešení.

**K2 – DoD**
- [ ] Nové mechaniky jsou zdokumentované a mají přiřazené issues/PR.
- [ ] Minimálně 1 testovací checklist je uložen v repozitáři.
- [ ] Proběhl alespoň 1 týmový playtest se zápisem výsledků.
- [ ] Závažné chyby mají ticket, prioritu a přiřazeného řešitele.

**K3 – DoD**
- [ ] Build je reprodukovatelný dle návodu v README.
- [ ] Uzavřeny blokující bugy z playtestu.
- [ ] Vydaná release verze (např. `v0.2-school`) s poznámkami.
- [ ] Dokumentace odpovídá aktuální struktuře kódu a modulů.

---

## 3. ročník

### Role ve skupině
- Vedoucí: příprava finálního harmonogramu a rizik.
- Vývojář: optimalizace výkonu, polishing, stabilita.
- Dokumentátor: finální technická a uživatelská dokumentace.
- Grafik: finální vizuální pass, UX konzistence, prezentovatelnost.

### Požadované artefakty
- Finální, stabilní build hry připravený na obhajobu.
- Kompletní dokumentace (technická + uživatelská).
- Prezentace projektu (slide deck + demo scénář).
- Seznam dosažených cílů vs. původní plán.

### Kontrolní termíny a kritéria splnění
- **K1 (začátek semestru):** finální plán dokončení + analýza rizik.
- **K2 (polovina semestru):** feature-freeze a důraz na kvalitu.
- **K3 (před obhajobou):** release kandidát + prezentace.

#### Definition of Done (3. ročník)

**K1 – DoD**
- [ ] V repozitáři je finální plán (milníky, odpovědnosti, rizika).
- [ ] Každé riziko má mitigaci a odpovědnou osobu.
- [ ] Všechny otevřené epiky mají cílové datum dokončení.
- [ ] Schválená rotace rolí pro závěrečnou fázi.

**K2 – DoD**
- [ ] Aktivní feature-freeze (nové feature jen po schválení Vedoucím).
- [ ] Checklist regresního testování je vyplněn a uložen v repozitáři.
- [ ] Výkonové metriky (FPS, load time) jsou zaznamenány.
- [ ] Otevřené bugy mají klasifikaci (blokující/neblokující).

**K3 – DoD**
- [ ] Final release candidate je označen tagem (např. `v1.0-rc`).
- [ ] V GitHub Releases jsou release notes a známé problémy.
- [ ] Prezentace a demo scénář jsou dostupné v repozitáři.
- [ ] README obsahuje finální instrukce k instalaci, spuštění a ovládání.

---

## Samostatný projekt

### Role ve skupině
- Pokud projekt řeší 1 student, role se sloučí:
  - Vedoucí + Vývojář + Dokumentátor + Tester (+ Grafik dle potřeby).
- Doporučení: plánovat práci po blocích podle rolí (např. pondělí vývoj, pátek dokumentace/testy).

### Požadované artefakty
- Individuální plán práce s týdenními cíli.
- Funkční build + průběžná dokumentace rozhodnutí.
- Evidence testování a prioritizace chyb.
- Závěrečná reflexe (co se podařilo / co zlepšit).

### Kontrolní termíny a kritéria splnění
- **K1:** scope projektu, architektura, minimální prototyp.
- **K2:** implementace hlavních funkcí + první testování.
- **K3:** stabilizace, dokumentace, finální odevzdání.

#### Definition of Done (Samostatný projekt)

**K1 – DoD**
- [ ] README obsahuje cíl, rozsah, tech stack a plán práce.
- [ ] V GitHub Issues je backlog minimálně na 4 týdny dopředu.
- [ ] Prototyp je spustitelný podle návodu.
- [ ] První technická rozhodnutí jsou zaznamenána (ADR/zápis).

**K2 – DoD**
- [ ] Hlavní funkce jsou implementovány a přiřazeny k issue/commitům.
- [ ] Existuje testovací checklist s výsledky.
- [ ] Nevyřešené chyby mají prioritu a termín řešení.
- [ ] Dokumentace je aktualizována po každém větším PR.

**K3 – DoD**
- [ ] Finální verze je otagovaná a publikovaná jako release.
- [ ] Kompletní dokumentace je v repozitáři a je konzistentní s kódem.
- [ ] Je přiložen krátký report/reflexe postupu a výsledků.
- [ ] Všechny povinné artefakty jsou dohledatelné přímo v GitHubu.
