from fastapi import Depends
from sqlalchemy.orm import Session
from pydantic import UUID4

from .exceptions import ItemNotFound
from .service import get_item_by_item_id
from app.api.dependencies import get_db


def validate_item_id(item_id: UUID4, database: Session = Depends(get_db)):
    item = get_item_by_item_id(database, item_id)
    print(item)
    if item is None:
        raise ItemNotFound

    return item
