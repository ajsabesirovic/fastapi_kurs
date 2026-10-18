from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

studenti = [
    {"id": 1, "ime": "Amar", "godina": 1},
    {"id": 2, "ime": "Lejla", "godina": 2},
    {"id": 3, "ime": "Kenan", "godina": 1},
]


class NoviStudent(BaseModel):
    ime: str
    godina: int


@app.get("/studenti")
def svi_studenti(godina: int | None = None):
    if godina is None:
        return studenti
    return [s for s in studenti if s["godina"] == godina]


@app.get("/studenti/{student_id}")
def jedan_student(student_id: int):
    for s in studenti:
        if s["id"] == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student ne postoji")


@app.post("/studenti", status_code=201)
def dodaj_studenta(novi: NoviStudent):
    student = {"id": len(studenti) + 1, "ime": novi.ime, "godina": novi.godina}
    studenti.append(student)
    return student
