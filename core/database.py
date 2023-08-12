from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession

from core.settings import settings

# Criando a engine de comunicação com o database configurado no settings
engine: AsyncEngine = create_async_engine(settings.DB_URL)

# Criando estrutura para sessão de acesso ao database
Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

