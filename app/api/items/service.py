from pydantic import UUID4, conlist
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Session

from .models import Item, ItemPhoto
from .schemas import ItemUpdate


def get_item_by_item_id(database: Session, item_id: UUID4):
    statement = (
        f"""
        SELECT item.*, array_agg(item_photo.id) as photo_ids
        FROM item
        LEFT JOIN item_photo
        ON item.id=item_photo.item_id
        WHERE item.id='{item_id}'
        GROUP BY item.id
        """
    )
    return database.execute(statement).first()


def get_photos_by_item_id(database: Session, item_id: UUID4):
    statement = (
        f"""
        SELECT array_agg(id)
        FROM item_photo
        WHERE item_id='{item_id}'
        """
    )

    photos = database.execute(statement).scalar()

    return photos


def delete_item_by_item_id(db: Session, item_id: UUID4):
    db.query(Item).filter(Item.id == item_id).delete()
    db.commit()


def update_item(db: Session, item_id: UUID4, payload: ItemUpdate):
    db.query(Item) \
      .filter(Item.id == item_id) \
      .update(payload.dict(exclude_none=True), synchronize_session="fetch")
    db.commit()

    updated_item = get_item_by_item_id(db, item_id)
    return updated_item


def add_photos(db: Session, item_id: UUID4, photos: conlist(UUID4, min_items=1)):
    db.query(Item).filter(Item.id == item_id).first()

    new_item_photo = [ItemPhoto(id=photo, item_id=item_id) for photo in photos]
    db.bulk_save_objects(new_item_photo)
    db.commit()

    photos = get_photos_by_item_id(db, item_id)
    return photos
