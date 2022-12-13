from pydantic import UUID4
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Session
from .models import ItemPhoto

from .models import Item
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
    result = database.query(ItemPhoto.id).filter(ItemPhoto.item_id == item_id).all()
    # 回傳list(UUID(UUID數值),), (UUID(UUID數值),)))
    photo_ids = []
    for photo_id in result:
        photo_ids.append(photo_id[0])
        # photo_id 是 sql.alchemy.row.row 型態, photo_id[0]是UUID型態
    print(photo_ids)
    return photo_ids


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
