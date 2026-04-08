from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlmodel import SQLModel
from src.books.models import Book

from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator

engine = AsyncEngine(create_engine(
    url=Config.DATABASE_URL,
    echo=True
))

async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# async def initdb():
#     """create a connection to our db"""

#     async with engine.begin() as conn:
#         statement = text("select 'Hello World'")

#         result = await conn.execute(statement)

#         print(result)

async def initdb():
    """create our database models in the database"""

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to provide the session object"""
    async with async_session() as session:
        yield session