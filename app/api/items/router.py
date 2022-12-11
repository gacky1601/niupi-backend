from uuid import UUID
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from pydantic import UUID4
from .schemas import Item, ItemUpdate
from . import service
from .dependencies import get_db, validate_item_id
from .exceptions import ItemNotFound


router = APIRouter()


@router.get("/{item_id}", response_model=Item)
def read_item(item: Item = Depends(validate_item_id)):
    return item


@router.patch("/{item_id}", response_model=Item)
def update_item(item_id: UUID4, payload: ItemUpdate, db: Session = Depends(get_db)):
    item = service.get_item_by_item_id(db, item_id)

    if item is None:
        raise ItemNotFound

    updated_item = service.update_item(db, item_id, payload)

    return updated_item
