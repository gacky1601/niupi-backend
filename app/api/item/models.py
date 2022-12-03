import uuid
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4, nullable=False)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    store_id = Column(
        UUID(as_uuid=True),
        ForeignKey("store.id", ondelete="CASCADE"),
        nullable=False
    )
    inventory = Column(Integer)
    photos_id = Column(String,ForeignKey("item_photo.id"))
    photo = relationship("ItemPhoto")

class ItemPhoto(Base):
    __tablename__ = "item_photo"

    id = Column(String, primary_key=True, index=True, nullable=False)
    item = relationship(
        "Item",
        back_populates="item_photo",
        uselist=False,
        cascade="all, delete",
        passive_deletes=True
    )