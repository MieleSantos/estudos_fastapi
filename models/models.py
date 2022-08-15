from lib2to3.pytree import Base
from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):

    id: Optional[int] = None
    titulo: str
    aulas: int  # mais de 12 aulas
    horas: int  # de 10 horas

    @validator("titulo")
    def validar_titulo(cls, value):
        palavras = value.split(" ")
        # Validação 1
        if len(palavras) < 3:
            raise ValueError("O titulo deve ter pelo menos 3 palavras")

        return value

    @validator("aulas")
    def validar_aulas(cls, value):
        if value < 12:
            raise ValueError("O número de aulas deve ser pelo menos 12 aulas")

        return value

    @validator("horas")
    def validar_horas(cls, value):
        if value < 10:
            raise ValueError("O número de horas deve ser pelo menos 10 horas")
        return value


cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=122, horas=58),
    Curso(id=2, titulo="Algoritmos e Logica de Programação", aulas=57, horas=67),
]
