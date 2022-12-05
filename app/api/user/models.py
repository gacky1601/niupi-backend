from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import CheckConstraint
import uuid

from app.database import Base
from app.api.store.models import Store


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String)
    user = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    address = Column(String)
    cellphone_number = Column(String)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)

    store = relationship(
        "Store",
        back_populates="user",
        uselist=False,
        cascade="all, delete",
        passive_deletes=True
    )


CheckConstraint(
    "REGEXP_LIKE(email,'^[a-zA-Z0-9]+@+[a-zA-Z0-9-]+.+([a-zA-Z]{2,4})$')",
    name='emailcheck')
CheckConstraint(
    "REGEXP_LIKE(cellphone_number,'^09+([0-9]{8})$')",
    name='cellphone_numbercheck')
