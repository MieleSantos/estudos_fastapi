from re import A
from fastapi import APIRouter
from models.models import Curso, cursos
from typing import Dict, List
from fastapi import HTTPException
from fastapi import status

from fastapi import Response

from fastapi import Path

router = APIRouter()


@router.get(
    "/api/v1/cursos",
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


@router.get(
    "/api/v1/cursos/{curso_id}",
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


@router.post(
    "/api/v1/cursos",
    status_code=status.HTTP_201_CREATED,
    description="Fazendo a criação de um curso",
    summary="Criando curso",
    response_model=Curso,
)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)

    return curso


@router.put(
    "/api/v1/cursos/{curso_id}",
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


@router.delete(
    "/api/v1/cursos/{curso_id}",
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
