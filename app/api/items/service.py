from pydantic import UUID4
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from .models import ItemPhoto


def get_item_by_item_id(db: Session, item_id: UUID4):
    statement = (
        f"""
        SELECT item.*, array_agg(item_photo.id) as photo_ids
        FROM item
        JOIN item_photo
        ON item.id=item_photo.item_id
        WHERE item.id='{item_id}'
        GROUP BY item.id
        """
    )

    return db.execute(statement).first()


def get_photo_by_item_id(db: Session, item_id: UUID4):
    photos_agg = func.array_agg(ItemPhoto.id, type_=ARRAY(UUID)).label("photo_ids")

    return db.query(photos_agg).filter(item_id == ItemPhoto.item_id).first()
