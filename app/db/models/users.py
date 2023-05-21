from uuid import uuid4

from sqlalchemy import Column, UUID, String

from db.base import Base


class Users(Base):
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String, unique=True)
    access_token = Column(String)
