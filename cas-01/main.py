from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def pocetna():
    return {"poruka": "Zdravo, svijete!"}


@app.get("/pozdrav/{ime}")
def pozdrav(ime: str):
    return {"poruka": f"Zdravo, {ime}!"}


@app.get("/kvadrat/{broj}")
def kvadrat(broj: int):
    return {"broj": broj, "kvadrat": broj * broj}


@app.get("/saberi")
def saberi(a: int, b: int = 0):
    return {"rezultat": a + b}
