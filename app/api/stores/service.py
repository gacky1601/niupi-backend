from uuid import UUID

from pydantic import UUID4
from sqlalchemy.orm import Session

from . import models
from .schemas import StoreInitialize


def get_store_by_user_id(db: Session, seller_id: UUID):
    return db.query(models.Store).filter(models.Store.seller_id == seller_id).first()


def initialize_store(db: Session, seller_id: UUID4, payload: StoreInitialize):
    db.query(models.Store) \
      .filter(models.Store.seller_id == seller_id) \
      .update(payload.dict(exclude_none=True), synchronize_session="fetch")

    initialized_store = get_store_by_user_id(db, seller_id)

    return initialized_store
