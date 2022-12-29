from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import CheckConstraint
import uuid

from app.api.stores.models import Store
from app.database import Base
from app.utils.validator import cellphone_number_regex, email_regex


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String)
    user = relationship("User")


class User(Base):
    __tablename__ = "users"

    __table_args__ = (
        CheckConstraint(
            f"cellphone_number ~* '{cellphone_number_regex}'", name="cellphone_number_check"
        ),
        CheckConstraint(
            f"email ~* '{email_regex}'", name="email_check"
        )
    )

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    address = Column(String)
    cellphone_number = Column(String)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)

    store = relationship(
        "Store",
        back_populates="seller",
        uselist=False,
        cascade="all, delete",
        passive_deletes=True
    )

    cart = relationship("Cart", backref="cart_user")
    orders = relationship("Order")
