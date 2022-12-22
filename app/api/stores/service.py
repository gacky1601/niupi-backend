from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Session

from . import models
from .schemas import StoreUpdate


def get_store_by_store_id(database: Session, store_id: UUID):
    address_json_object = (
        """
        json_build_object(
            'county', county.name,
            'district', district.name,
            'detail', store.detail_address
        ) AS address
        """
    )

    statement = (
        f"""
        SELECT store.*, {address_json_object}
        FROM store
        LEFT JOIN county ON county.id=store.county_id
        LEFT JOIN district ON district.id=store.district_id
        WHERE store.id='{store_id}'
        """
    )

    return database.execute(statement).first()


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
