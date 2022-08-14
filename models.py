from lib2to3.pytree import Base
from typing import Optional
from pydantic import BaseModel


class Curso(BaseModel):

    id: Optional[int] = None
    tituto = str
    aulas: int
    horas: int
