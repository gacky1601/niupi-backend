from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .dependencies import validate_item_id, get_db
from .schemas import Item, ItemPhoto
from .service import get_photo_by_item_id
from .exceptions import PhotoNotFound

router = APIRouter()


@router.get("/{item_id}", response_model=Item)
def read_item(item: Item = Depends(validate_item_id)):
    return item


@router.get("/{item_id}/photos", response_model=ItemPhoto)
def read_photos(item: Item = Depends(validate_item_id), db: Session = Depends(get_db)):
    photos_id = get_photo_by_item_id(db, item.id)

    return photos_id
