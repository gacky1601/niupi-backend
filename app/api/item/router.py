from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4
from .schemas import Item
from .service import get_item_by_item_id, delete_item_by_id
from .dependencies import get_db
from .exceptions import ItemNotExist

router = APIRouter()


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: UUID4, db: Session = Depends(get_db)):
    item = get_item_by_item_id(db, item_id)

    if item is None:
        raise ItemNotExist

    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: UUID4, db: Session = Depends(get_db)):
    delete_item_by_id(db, item_id)
