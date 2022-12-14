from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from . import service
from .dependencies import get_db
from .exceptions import InitializeNonExistingStore, StoreNotFound
from .schemas import Store, StoreInitialize

router = APIRouter()


@router.get("/{user_id}", response_model=Store)
def read_store(user_id: UUID4, db: Session = Depends(get_db)):
    store = service.get_store_by_user_id(db, user_id)

    if store is None:
        raise StoreNotFound

    return store


@router.put("/{owner_id}", response_model=Store)
def initialize_store(owner_id: UUID4, store: StoreInitialize, db: Session = Depends(get_db)):
    seller = service.get_store_by_user_id(db, owner_id)

    if seller is None:
        raise InitializeNonExistingStore

    initialized_store = service.initialize_store(db, owner_id, store)

    return initialized_store
