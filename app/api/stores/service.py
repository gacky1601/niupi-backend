from uuid import UUID

from sqlalchemy.orm import Session

from . import models
from .schemas import StoreUpdate


def get_store_by_store_id(database: Session, store_id: UUID):
    return database.query(models.Store).get(store_id)


def update_store(database: Session, store_id: UUID, payload: StoreUpdate):
    database.query(models.Store) \
            .filter(models.Store.id == store_id) \
            .update(payload.dict(exclude_none=True), synchronize_session="fetch")

    updated_store = get_store_by_store_id(database, store_id)

    return updated_store
