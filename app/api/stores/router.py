from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from . import service
from .dependencies import get_db
from .exceptions import SellerNotFound
from .schemas import Store, StoreUpdate

router = APIRouter()


@router.get("/{seller_id}", response_model=Store)
def read_store(seller_id: UUID4, database: Session = Depends(get_db)):
    store = service.get_store_by_user_id(database, seller_id)

    if store is None:
        raise SellerNotFound

    return store


@router.patch("/{seller_id}", response_model=Store)
def update_store(seller_id: UUID4, store: StoreUpdate, database: Session = Depends(get_db)):
    seller = service.get_store_by_user_id(database, seller_id)

    if seller is None:
        raise SellerNotFound

    updated_store = service.update_store(database, seller_id, store)

    return updated_store
