import uuid

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4,
        nullable=False
    )

    name = Column(String, index=True, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)

    store_id = Column(
        UUID(as_uuid=True),
        ForeignKey("store.id", ondelete="CASCADE"),
        nullable=False
    )

    inventory = Column(Integer, nullable=False)

    photos = relationship("ItemPhoto", backref="item")


class ItemPhoto(Base):
    __tablename__ = "item_photo"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, index=True)

    item_id = Column(
        UUID(as_uuid=True),
        ForeignKey("item.id", ondelete="CASCADE"),
        nullable=False,
    )
