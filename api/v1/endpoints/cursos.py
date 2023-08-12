from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel
from schemas.curso_schema import CursoSchema
from core.connection import get_session

router = APIRouter()


# GET Cursos
@router.get('/', 
    description='Retorna todos os cursos ou uma lista vazia.', 
    summary='Retorna todos os cursos.',
    response_model=List[CursoSchema],
    response_description='Cursos encontrados com sucesso.')
async def get_cursos(db: AsyncSession = Depends(get_session)): # Primeiro executa a dependencia para obter o seu retorno. 
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        return cursos


# GET Curso ID        
@router.get('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id) # criando a query
        result = await session.execute(query) # abrindo session passando uma query como parâmentro
        curso = result.scalar_one_or_none()

        if curso:
            return curso
        else:
            raise HTTPException(detail='Curso não encontrado.', 
                status_code=status.HTTP_404_NOT_FOUND)


# POST Curso
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_cursos(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        novo_curso = CursoModel(
            titulo = curso.titulo,
            aulas = curso.aulas,
            horas = curso.horas
        )
        session.add(novo_curso)
        await session.commit()
        await session.close()

        return novo_curso


# PUT Curso
@router.put('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_update = result.scalar_one_or_none()

        if curso_update:
            curso_update.titulo = curso.titulo
            curso_update.aulas = curso.aulas
            curso_update.horas = curso.horas

            await session.commit()
            await session.close()
            return curso_update

        else:
            raise HTTPException(detail='Curso não encontrado', status_code=status.HTTP_404_NOT_FOUND)


# DELETE Curso
@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def put_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_delete = result.scalar_one_or_none()

        if curso_delete:
            await session.delete(curso_delete)
            await session.commit()
            await session.close()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
            
        else:
            raise HTTPException(detail='Curso não encontrado', status_code=status.HTTP_404_NOT_FOUND)
