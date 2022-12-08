from sqlalchemy.orm import Session
from pydantic import UUID4

from .models import Item, ItemPhoto

def get_item_by_item_id(db: Session, item_id: UUID4):
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

    return db.execute(statement).first()


