from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()


class Student(BaseModel):
    id: int
    ime: str = Field(min_length=2, max_length=50)
    godina: int = Field(ge=1, le=5)


studenti = [
    Student(id=1, ime="Amar", godina=1),
    Student(id=2, ime="Lejla", godina=2),
    Student(id=3, ime="Kenan", godina=1),
    Student(id=4, ime="Ana", godina=3),
    Student(id=5, ime="Haris", godina=2),
    Student(id=6, ime="Selma", godina=4),
    Student(id=7, ime="Tarik", godina=1),
    Student(id=8, ime="Amila", godina=3),
]


@app.get("/studenti")
def svi_studenti(
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=20)] = 5,
    godina: Annotated[int | None, Query(ge=1, le=5)] = None,
    ime: Annotated[str | None, Query(min_length=2, max_length=50)] = None,
) -> list[Student]:
    rezultat = studenti
    if godina is not None:
        rezultat = [s for s in rezultat if s.godina == godina]
    if ime is not None:
        rezultat = [s for s in rezultat if ime.lower() in s.ime.lower()]
    return rezultat[skip : skip + limit]


@app.get("/studenti/{student_id}")
def jedan_student(student_id: Annotated[int, Path(ge=1)]) -> Student:
    for s in studenti:
        if s.id == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student ne postoji")
