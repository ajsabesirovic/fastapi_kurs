# Čas 3 – CRUD i validacija

## Gradivo

- CRUD: Create (POST), Read (GET), Update (PUT), Delete (DELETE)
- `PUT /studenti/{student_id}` – izmjena studenta
- `DELETE /studenti/{student_id}` – brisanje, status 204 (bez tijela odgovora)
- Pomoćna funkcija `nadji_studenta` umjesto ponavljanja petlje i 404
- Validacija sa `Field`: `min_length`, `max_length`, `ge`, `le`
- Nasljeđivanje modela: `Student(NoviStudent)` dodaje `id`
- Tip povratne vrijednosti (`-> Student`, `-> list[Student]`) kao opis odgovora u `/docs`
- Zašto `len(studenti) + 1` nije dobar `id` nakon brisanja → brojač `sljedeci_id`

## Pokretanje

```bash
fastapi dev cas-03/main.py
```

Sve zahtjeve testirati kroz http://127.0.0.1:8000/docs.

## Probati

1. `POST /studenti` sa `{"ime": "Ana", "godina": 3}` → 201
2. `POST /studenti` sa `{"ime": "A", "godina": 9}` → 422, pročitati poruke greške
3. `PUT /studenti/1` sa `{"ime": "Amar H.", "godina": 2}` → 200
4. `DELETE /studenti/2` → 204
5. `GET /studenti/2` → 404
6. `POST /studenti` ponovo → novi `id` je 5, ne 4 ili 3

## Zadatak: API za knjige (nastavak)

Nastaviti na rješenju domaćeg iz časa 2.

1. Modeli `NovaKnjiga` i `Knjiga(NovaKnjiga)` sa `id`
2. Validacija: `naslov` i `autor` najmanje 1 znak, `godina` između 1450 i 2026
3. Pomoćna funkcija `nadji_knjigu` za 404
4. `PUT /knjige/{id}` i `DELETE /knjige/{id}` (204)
5. Brojač `sljedeci_id` umjesto `len(knjige) + 1`

## Domaći

Dodati polje `dostupna: bool = True` i endpoint `POST /knjige/{id}/posudi`:
- ako je knjiga dostupna → postaviti `dostupna = False` i vratiti knjigu
- ako nije → greška 400 sa porukom `"Knjiga je već posuđena"`

Bonus: `POST /knjige/{id}/vrati`.
