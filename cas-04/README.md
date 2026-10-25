# Čas 4 – Validacija parametara

## Gradivo

- `Annotated` – tip parametra + dodatna pravila na jednom mjestu
- `Path(ge=1)` – path parametar mora biti 1 ili veći
- `Query(ge=..., le=...)` – granice za brojeve u query parametrima
- `Query(min_length=..., max_length=...)` – dužina teksta
- Paginacija: `skip` i `limit` (`/studenti?skip=0&limit=5`)
- Pretraga po dijelu imena: `/studenti?ime=am`
- Kombinovanje filtera: `/studenti?godina=1&ime=a`

## Pokretanje

```bash
fastapi dev cas-04/main.py
```

## Probati

1. `GET /studenti` → 200, prvih 5 studenata
2. `GET /studenti?skip=5&limit=5` → 200, ostala 3 studenta
3. `GET /studenti?limit=50` → 422 (najviše 20)
4. `GET /studenti?ime=am` → 200, Amar i Amila
5. `GET /studenti?ime=a` → 422 (najmanje 2 znaka)
6. `GET /studenti?godina=1` → 200, Amar, Kenan, Tarik
7. `GET /studenti?godina=7` → 422
8. `GET /studenti/0` → 422 (`id` mora biti ≥ 1)
9. `GET /studenti/99` → 404

## Zadatak: API za knjige

U listu upisati najmanje 8 knjiga (`id`, `naslov`, `autor`, `godina`).

1. `GET /knjige/{id}` – `id` mora biti ≥ 1
2. `GET /knjige` sa paginacijom `skip` (≥ 0) i `limit` (1–20, podrazumijevano 5)
3. Pretraga `?naslov=...` po dijelu naslova, 2–100 znakova, bez obzira na velika/mala slova
4. Filter `?od_godine=...&do_godine=...`, obje vrijednosti između 1450 i 2026
5. Svi filteri moraju raditi zajedno

## Domaći

Dodati `GET /knjige/autor/{autor}` gdje `autor` ima 2–50 znakova i vraća sve knjige tog autora.
Bonus: query parametar `sortiraj` koji može biti `naslov` ili `godina` (`Query(pattern="^(naslov|godina)$")`).
