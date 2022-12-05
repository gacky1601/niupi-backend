from sqlalchemy import Column, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base
from app.utils.validator import cellphone_number_regex, telephone_number_regex, email_regex


class Store(Base):
    __tablename__ = "store"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    name = Column(String, unique=True, index=True)
    address = Column(String)
    email = Column(String)
    cellphone_number = Column(String)
    telephone_number = Column(String)

    user = relationship("User", back_populates="store", cascade_backrefs=True)


CheckConstraint(
    "REGEXP_LIKE(Store.email," + email_regex,
    name='emailcheck')

CheckConstraint(
    "REGEXP_LIKE(Store.cellphone_number," + cellphone_number_regex,
    name='cellphone_numbercheck')

CheckConstraint(
    "REGEXP_LIKE(Store.telephone_number," + telephone_number_regex,
    name='cellphone_numbercheck')
