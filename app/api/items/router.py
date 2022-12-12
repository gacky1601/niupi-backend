from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4

from . import service
from .dependencies import get_db, validate_item_id
from .exceptions import ItemNotFound
from .schemas import Item, ItemUpdate


router = APIRouter()


@router.get("/{item_id}", response_model=Item)
def read_item(item: Item = Depends(validate_item_id)):
    return item


@router.patch("/{item_id}", response_model=Item)
def update_item(
    payload: ItemUpdate,
    item: Item = Depends(validate_item_id),
    db: Session = Depends(get_db)
):

    updated_item = service.update_item(db, item.id, payload)

    return updated_item