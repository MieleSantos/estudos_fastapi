from typing import Dict, List
from fastapi import HTTPException
from fastapi import status
from fastapi import FastAPI
from models.models import Curso, cursos

from fastapi import Response

from fastapi import Path

app = FastAPI(
    title="Api de Cursos da Geek University",
    version="0.0.1",
    description="Uma Api para estudos do FastApi",
)


@app.get(
    "/cursos",
    description="Retorna todos os cursos ou uma lista vazia",
    summary="Retorna todos os cursos",
    response_model=List[Curso],
    response_description="Cursos encontrados com sucesso",
)
async def get_cursos():
    """
    Retorna todos os cursos
    """
    return cursos


@app.get(
    "/cursos/{curso_id}",
    description="Retorna um unico curso do ID especificado",
    summary="Retorna curso",
    response_model=Curso,
)
async def get_cursos_id(
    curso_id: int = Path(
        default=None,
        title="ID do cursp",
        description="deve ser entre 1 e 2",
        gt=0,
        lt=3,
    )
):
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


@app.post(
    "/cursos",
    status_code=status.HTTP_201_CREATED,
    description="Fazendo a criação de um curso",
    summary="Criando curso",
    response_model=Curso,
)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos.append(
        Curso(id=next_id, titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)
    )

    del curso.id

    return curso


@app.put(
    "/cursos/{curso_id}",
    description="Fazendo a atualização de um curso especifico",
    summary="Atualizando curso",
)
async def put_curso(curso_id: int, curso: Curso):
    for i in cursos:
        if curso_id == i.id:
            cursos[curso_id] = curso
            del curso.id
            return curso
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Não exite um curso com id {curso_id}",
            )


@app.delete(
    "/cursos/{curso_id}",
    description="Fazendo a remoção de um curso",
    summary="Removendo curso",
)
async def delete_curso(curso_id: int):

    for i in cursos:
        print(i)
        if curso_id == i.id:
            del cursos[curso_id]
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Não exite um curso com id {curso_id}",
            )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
