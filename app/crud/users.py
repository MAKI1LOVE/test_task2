from sqlalchemy import select, insert, Result
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.users import Users
from schemas.user import UserCreate


async def get_user_by_username(username: str, session: AsyncSession) -> Result:
    return await session.execute(select(Users).where(Users.username == username))


async def create_user(user: UserCreate, session: AsyncSession):
    await session.execute(insert(Users).values(dict(user)))
