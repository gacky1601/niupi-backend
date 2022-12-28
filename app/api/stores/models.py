import uuid

from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.api.counties.models import County
from app.api.districts.models import District
from app.api.items.models import Item
from app.database import Base
from app.utils.validator import cellphone_number_regex, email_regex, telephone_number_regex


class Store(Base):
    __tablename__ = "store"

    __table_args__ = (
        CheckConstraint(
            f"cellphone_number ~* '{cellphone_number_regex}'", name="cellphone_number_check"
        ),
        CheckConstraint(
            f"email ~* '{email_regex}'", name="email_check"
        ),
        CheckConstraint(
            f"telephone_number ~* '{telephone_number_regex}'", name="telephone_number_check"
        )
    )

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)

    seller_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    name = Column(String, unique=True, index=True)
    county_id = Column(Integer, ForeignKey("county.id"))
    district_id = Column(Integer, ForeignKey("district.id"))
    detail_address = Column(String)
    email = Column(String)
    cellphone_number = Column(String)
    telephone_number = Column(String)

    seller = relationship("User", back_populates="store", cascade_backrefs=True)

    items = relationship("Item")

    orders = relationship("Orders")
