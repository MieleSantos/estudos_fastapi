from lib2to3.pytree import Base
from typing import Optional
from pydantic import BaseModel


class Curso(BaseModel):

    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=122, horas=58),
    Curso(id=2, titulo="Algoritmos e Logica de Programação", aulas=57, horas=67),
]