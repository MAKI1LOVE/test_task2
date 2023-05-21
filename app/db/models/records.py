from uuid import uuid4

from sqlalchemy import Column, UUID, ForeignKey, String

from db.base import Base


class Records(Base):
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    filepath = Column(String)
    user_uuid = Column(UUID(as_uuid=True), ForeignKey('users.uuid'))
