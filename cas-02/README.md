# Čas 2 – API za studente

## Gradivo

- Podaci u listi (bez baze)
- `GET /studenti` i filtriranje: `/studenti?godina=1`
- `GET /studenti/{student_id}` i greška 404 (`HTTPException`)
- `POST /studenti` i Pydantic model (`BaseModel`)

## Pokretanje

```bash
fastapi dev cas-02/main.py
```

POST zahtjeve testirati kroz http://127.0.0.1:8000/docs.

## Zadatak: API za knjige

Svaka knjiga ima `id`, `naslov`, `autor`, `godina`. U listu unaprijed upisati 2–3 knjige.

1. `GET /knjige` – sve knjige
2. `GET /knjige/{id}` – jedna knjiga ili 404
3. `GET /knjige?autor=...` – filtriranje po autoru
4. Bonus: `POST /knjige` – dodavanje knjige
5. Bonus: `DELETE /knjige/{id}` – brisanje knjige

## Domaći

Završiti zadatak i dodati `PUT /knjige/{id}` za izmjenu knjige.
