from typing import Optional
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


def search_items_by_keyword(database: Session, store_id: UUID, keyword: Optional[str]):
    statement = (
        f"""
        SELECT item.*, (array_agg(item_photo.id))[1] AS photo, item.id AS item_id
        FROM item
        LEFT JOIN item_photo
        ON item.id=item_photo.item_id
        WHERE item.store_id='{store_id}' AND item.name LIKE '%{keyword}%'
        GROUP BY item.id
        """
    )

    items = database.execute(statement).all()

    return items
