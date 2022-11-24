from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class Store(Base):
    __tablename__ = "store"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True)
    name = Column(String, unique=True, index=True, nullable=False)
    address = Column(String)
    email = Column(String)
    cellphone_number = Column(String)
    telephone_number = Column(String)
    
    user = relationship("User", back_populates="store")
