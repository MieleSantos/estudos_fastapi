from re import A
from fastapi import APIRouter

router = APIRouter()


@router.get("/api/v1/usuarios")
async def get_cursos():
    return {"info": "Tudos os usuarios"}
