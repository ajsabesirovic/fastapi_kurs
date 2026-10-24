from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class NoviStudent(BaseModel):
    ime: str = Field(min_length=2, max_length=50)
    godina: int = Field(ge=1, le=5)


class Student(NoviStudent):
    id: int


studenti = [
    Student(id=1, ime="Amar", godina=1),
    Student(id=2, ime="Lejla", godina=2),
    Student(id=3, ime="Kenan", godina=1),
]
sljedeci_id = 4


def nadji_studenta(student_id: int) -> Student:
    for s in studenti:
        if s.id == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student ne postoji")


@app.get("/studenti")
def svi_studenti(godina: int | None = None) -> list[Student]:
    if godina is None:
        return studenti
    return [s for s in studenti if s.godina == godina]


@app.get("/studenti/{student_id}")
def jedan_student(student_id: int) -> Student:
    return nadji_studenta(student_id)


@app.post("/studenti", status_code=201)
def dodaj_studenta(novi: NoviStudent) -> Student:
    global sljedeci_id
    student = Student(id=sljedeci_id, ime=novi.ime, godina=novi.godina)
    sljedeci_id += 1
    studenti.append(student)
    return student


@app.put("/studenti/{student_id}")
def izmijeni_studenta(student_id: int, izmjena: NoviStudent) -> Student:
    student = nadji_studenta(student_id)
    student.ime = izmjena.ime
    student.godina = izmjena.godina
    return student


@app.delete("/studenti/{student_id}", status_code=204)
def obrisi_studenta(student_id: int):
    student = nadji_studenta(student_id)
    studenti.remove(student)
