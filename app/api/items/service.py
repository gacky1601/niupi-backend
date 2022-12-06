from sqlalchemy.orm import Session
from pydantic import UUID4

from .models import Item, ItemPhoto


def get_item_by_item_id(db: Session, item_id: UUID4):
    return db.query(Item).get(item_id)
