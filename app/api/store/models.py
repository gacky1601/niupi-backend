from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String)
    store = relationship("store")


class Store(Base):
    __tablename__ = "stores"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True),  index=True, default=uuid.uuid4, nullable=False)
    name = Column(String, unique=True, index=True, nullable=False)
    address = Column(String)
    email = Column(String)
    cellphone_number = Column(String)
    telephone_number = Column(String)
