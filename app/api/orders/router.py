from uuid import UUID
import re

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils.validator import order_id_regex
from .dependencies import get_db
from .exceptions import OrderNotFound, OrderIdInvalidFormat
from .service import get_order_by_order_id


router = APIRouter()


@router.get("/{order_id}")
def read_order(order_id: str, db: Session = Depends(get_db)):
    if not re.match(order_id_regex, order_id):
        raise OrderIdInvalidFormat

    order = get_order_by_order_id(db, order_id)

    if order is None:
        raise OrderNotFound

    return order
