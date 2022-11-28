from uuid import UUID
from sqlalchemy.orm import Session

from . import models


def get_store_by_user_id(db: Session, user_id: UUID):
    return db.query(models.Store).filter(models.Store.user_id == user_id).first()
