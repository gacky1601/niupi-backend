from pydantic import UUID4
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from .models import Item, ItemPhoto


def get_item_by_item_id(db: Session, item_id: UUID4):
    photos_agg = func.array_agg(ItemPhoto.id, type_=ARRAY(UUID)).label("photos")
    item = db.query(Item.id, Item.name, Item.description, Item.inventory, Item.price,
                    Item.store_id, photos_agg) \
             .join(ItemPhoto) \
             .filter(item_id == ItemPhoto.item_id) \
             .group_by(Item.id) \
             .first()
    return item
