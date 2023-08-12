from fastapi import APIRouter

router = APIRouter()


@router.get('/usuarios', 
    description='Retorna todos os cursos ou uma lista vazia.', 
    summary='Retorna todos os cursos.')
async def get_usuarios(): # Primeiro executa a dependencia para obter o seu retorno. 
    pass