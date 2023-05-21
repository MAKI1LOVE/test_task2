from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings
from db.base import Base

async_engine = create_async_engine(settings.DB_URL, echo=True)
async_session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)


async def init_db():
    async with async_engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print('connected')


async def close_db_connection():
    await async_engine.dispose()
    print('disconnected')


async def get_sesssion():
    async with async_session.begin() as session:
        yield session
