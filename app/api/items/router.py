from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .dependencies import get_db, validate_item_id
from .schemas import Item
from .service import delete_item_by_item_id

router = APIRouter()


@router.get("/{item_id}", response_model=Item)
def read_item(item: Item = Depends(validate_item_id)):
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item: Item = Depends(validate_item_id), db: Session = Depends(get_db)):
    delete_item_by_item_id(db, item.id)
