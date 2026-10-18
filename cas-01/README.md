# Čas 1 – Uvod u FastAPI

## Gradivo

- Šta je API, klijent i server, zahtjev i odgovor
- HTTP metode: GET, POST, PUT, DELETE
- JSON i status kodovi (200, 404, 422, 500)
- Prvi endpoint i automatska dokumentacija (`/docs`)
- Path parametri: `/pozdrav/{ime}`, `/kvadrat/{broj}`
- Query parametri: `/saberi?a=5&b=3`

## Pokretanje

```bash
fastapi dev cas-01/main.py
```

## Probati

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/pozdrav/Amar
- http://127.0.0.1:8000/kvadrat/7
- http://127.0.0.1:8000/kvadrat/abc (greška 422)
- http://127.0.0.1:8000/saberi?a=5&b=3
- http://127.0.0.1:8000/docs
