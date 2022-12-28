from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4
from .schemas import Cart
from . import service
from .dependencies import get_db
from .exceptions import UserNotFound


router = APIRouter()


@router.get("/{user_id}")
def read_cart(user_id: UUID4, db: Session = Depends(get_db)):
    carts = service.get_cart_by_id(db, user_id)

    if carts == []:
        raise UserNotFound
    return carts
