from pydantic import constr
from uuid import UUID
import re

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils.validator import order_id_regex
from .dependencies import get_db
from .exceptions import OrderNotFound
from .service import get_order_by_order_id


router = APIRouter()


@router.get("/{order_id}")
def read_order(order_id: constr(regex=order_id_regex), db: Session = Depends(get_db)):
    order = get_order_by_order_id(db, order_id)

    if order is None:
        raise OrderNotFound

    return order
