from fastapi import FastAPI
from routes import curso_router
from routes import usuario_router


app = FastAPI(
    title="Api de Cursos da Geek University",
    version="0.0.1",
    description="Uma Api para estudos do FastApi",
)

app.include_router(curso_router.router, tags=["cursos"])
app.include_router(usuario_router.router, tags=["usuarios"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
