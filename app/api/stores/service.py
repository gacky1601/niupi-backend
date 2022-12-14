from uuid import UUID

from pydantic import UUID4
from sqlalchemy.orm import Session

from . import models
from .schemas import StoreInitialize


def get_store_by_user_id(db: Session, user_id: UUID):
    return db.query(models.Store).filter(models.Store.user_id == user_id).first()


def initialize_store(db: Session, owner_id: UUID4, payload: StoreInitialize):
    db.query(models.Store) \
      .filter(models.Store.user_id == owner_id) \
      .update(payload.dict(exclude_none=True), synchronize_session="fetch")

    initialized_store = get_store_by_user_id(db, owner_id)

    return initialized_store
