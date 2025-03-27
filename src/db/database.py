from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.core.config import settings
from sqlalchemy.pool import NullPool
from typing import AsyncGenerator


DATABASE_URL = settings.get_db_url()

engine = create_async_engine(
    DATABASE_URL,
    poolclass=NullPool if settings.TESTING else None,
    echo=settings.DEBUG,
    future=True
)


AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
