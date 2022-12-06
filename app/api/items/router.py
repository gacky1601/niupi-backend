from fastapi import APIRouter, Depends

from .dependencies import validate_item_id
from .schemas import Item

router = APIRouter()


@router.get("/{item_id}", response_model=Item)
def read_item(item: Item = Depends(validate_item_id)):
    return item
