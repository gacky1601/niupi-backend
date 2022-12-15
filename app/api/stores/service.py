from uuid import UUID

from sqlalchemy.orm import Session

from . import models
from .schemas import StoreInitialize


def get_store_by_user_id(database: Session, seller_id: UUID):
    return database.query(models.Store).filter(models.Store.seller_id == seller_id).first()


def update_store(database: Session, seller_id: UUID, payload: StoreInitialize):
    database.query(models.Store) \
            .filter(models.Store.seller_id == seller_id) \
            .update(payload.dict(exclude_none=True), synchronize_session="fetch")

    initialized_store = get_store_by_user_id(database, seller_id)

    return initialized_store
