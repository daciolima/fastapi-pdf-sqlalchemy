from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base # função para declara a base da comunicação pelo sqlalchemy

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR = '/api/v1'

    # Configuração do String adequanda para comunicação assíncrona no banco.
    DB_URL: str = "postgresql+asyncpg://postgres:d080406@localhost:5432/cursinho" 
    DB_BASE_MODEL = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()
