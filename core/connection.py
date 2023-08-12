from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

# Abrindo instância de sessão como o banco para ser usado com injeção de dependência a quem chamar o banco
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session # Devolve essa sessão... Isso não é um return. Apenas fica a disposição
    finally:
        await session.close() # Aguarda o processamento e depois fecha.
