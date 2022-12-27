from sqlalchemy import Column, DateTime, Integer, ForeignKey, String, TIMESTAMP, BOOLEAN
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base
from app.utils.validator import order_id_regex
from sqlalchemy.sql import func


class Orders(Base):
    __tablename__ = "orders"

    id = Column(
        String,
        nullable=False,
        primary_key=True,
        index=True
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    store_id = Column(
        UUID(as_uuid=True),
        ForeignKey("store.id", ondelete="CASCADE"),
        nullable=False
    )

    shipping_fee = Column(
        Integer,
        nullable=False
    )

    create_at = Column(TIMESTAMP, nullable=False)
    paid_at = Column(TIMESTAMP)
    shipped_at = Column(TIMESTAMP)
    received_at = Column(TIMESTAMP)
    reviewed_at = Column(TIMESTAMP)

    is_cancelled = Column(
        BOOLEAN,
        default=False,
        nullable=False
    )

    items = relationship("OrderItem", backref="Orders")


class OrderItem(Base):
    __tablename__ = "order_item"

    order_id = Column(
        String,
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True
    )

    item_id = Column(
        UUID(as_uuid=True),
        ForeignKey("item.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True
    )

    quantity = Column(
        Integer,
        nullable=False
    )
