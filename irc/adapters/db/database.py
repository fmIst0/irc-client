from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

DATABASE_URL = (
    "postgresql+asyncpg://user:password@db_platform:5432/db_platform"
)


class Database:
    _instance = None

    def __new__(cls, database_url: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.engine = create_async_engine(database_url)
            cls._instance.session_maker = async_sessionmaker(
                cls._instance.engine, expire_on_commit=False
            )
        return cls._instance


db = Database(DATABASE_URL)
async_session_maker = db.session_maker


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
