from fastapi import APIRouter

from api.v1.endpoints import cursos

api_router = APIRouter()

 # Carregando a rota para cursos  # /api/v1/cursos. tags: Documenta o grupo lá no /docs
api_router.include_router(cursos.router, prefix='/cursos', tags=["cursos"])
