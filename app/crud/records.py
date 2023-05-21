from uuid import UUID

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.records import Records


async def create_record(path: str, record_uuid: UUID, user_uuid: UUID,
                        session: AsyncSession):
    await session.execute(insert(Records).values((record_uuid, path, user_uuid)))


async def get_record_by_uuid(record_uuid: UUID, user_uuid: UUID, session: AsyncSession):
    return await session.execute(select(Records).where(Records.uuid == record_uuid,
                                                       Records.user_uuid == user_uuid))
