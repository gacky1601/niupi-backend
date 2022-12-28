from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import CheckConstraint
import uuid

from app.database import Base
from sqlalchemy.sql import func
# from app.api.store.models import Store


class Cart(Base):
    __tablename__ = "cart"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True
    )

    item_id = Column(
        UUID(as_uuid=True),
        ForeignKey("item.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True
    )
    updated_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    quantity = Column(Integer, nullable=False)
