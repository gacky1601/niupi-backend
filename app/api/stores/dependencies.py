from fastapi import Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from .exceptions import SellerNotFound
from .models import Store
from .service import get_store_by_user_id


def validate_seller_id(seller_id: UUID4, database: Session = Depends(get_db)) -> Store:
    store = get_store_by_user_id(database, seller_id)

    if store is None:
        raise SellerNotFound

    return store
