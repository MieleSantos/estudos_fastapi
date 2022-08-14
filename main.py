from fastapi import HTTPException
from fastapi import status
from fastapi import FastAPI
from typing import Optional, List
from models import Curso

app = FastAPI()

cursos = {
    1: {"titulo": "Programação para Leigos", "aulas": 112, "horas": 58},
    2: {"titulo": "Algoritmos e Logica de Programação", "aulas": 87, "horas": 67},
}


@app.get("/cursos")
async def get_cursos():
    """
    Retorna todos os cursos
    """
    return cursos


@app.get("/cursos/{curso_id}")
async def get_cursos_id(curso_id: int):
    """
    Retorna um unico curso
    """
    try:

        curso = cursos[curso_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )
    return curso


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):

    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id

    return curso


@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não exite um curso com id {curso_id}",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
