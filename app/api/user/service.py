from uuid import UUID
from sqlalchemy.orm import Session

from . import models


def get_user_by_id(db: Session, user_id: UUID):
    return db.query(models.User).filter(models.User.id == user_id).first()
