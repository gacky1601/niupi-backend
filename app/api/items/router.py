from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session
from .dependencies import get_db, validate_item_id
from .schemas import Item
from .service import get_photos_by_item_id

router = APIRouter()


@router.get("/{item_id}", response_model=Item)
def read_item(item: Item = Depends(validate_item_id)):
    return item


@router.get("/{item_id}/photos", response_model=list[UUID4])
def read_photos(item: Item = Depends(validate_item_id), db: Session = Depends(get_db)):
    photo_ids = get_photos_by_item_id(db, item.id)
    return photo_ids
