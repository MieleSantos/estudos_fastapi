from fastapi import HTTPException
from fastapi import status
from fastapi import FastAPI


app = FastAPI()

cursos = {
    1: {"titulo": "Programação para Leigos", "aulas": 112, "horas": 58},
    2: {"titulo": "Algoritmos e Logica de Programação", "aulas": 87, "horas": 67},
}


@app.get("/cursos")
async def get_cursos():
    return cursos


@app.get("/cursos/{curso_id}")
async def get_cursos_id(curso_id: int):
    try:

        curso = cursos[curso_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )
    return curso


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
