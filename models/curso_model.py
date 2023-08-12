from core.settings import settings
from sqlalchemy import Column, Integer, String 
from pydantic import validator

class CursoModel(settings.DB_BASE_MODEL):
    __tablename__ = 'curso'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)


    @validator('titulo')
    def validar_titulo(cls, value):

        # Validação 1
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ter ao menos 3 palavras')

        # Validação 2
        if value.islower():
            raise ValueError('O título deve ser capitalizado')
        
        return value



