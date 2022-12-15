from fastapi import Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from .exceptions import StoreNotFound
from .models import Store
from .service import get_store_by_store_id


def validate_store_id(store_id: UUID4, database: Session = Depends(get_db)) -> Store:
    store = get_store_by_store_id(database, store_id)

    if store is None:
        raise StoreNotFound

    return store
