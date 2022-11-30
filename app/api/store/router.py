from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4

from .schemas import Store, StoreInitialize
from . import service
from .dependencies import get_db
from .exceptions import StoreNotFound, SellerNotFound

router = APIRouter()


@router.get("/{user_id}", response_model=Store)
def read_store(user_id: UUID4, db: Session = Depends(get_db)):
    store = service.get_store_by_user_id(db, user_id)

    if store is None:
        raise StoreNotFound

    return store


@router.put("/{owner_id}")
def initialize_store(owner_id: UUID4, store: StoreInitialize, db: Session = Depends((get_db))):
    seller = service.get_store_by_user_id(db, owner_id)
    if seller is None:
        raise SellerNotFound
    initialized_store = service.initialize_store(db, owner_id, store)
    return initialized_store
