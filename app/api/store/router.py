from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4
from .schemas import Store, update_Store
from .service import get_store_by_user_id, initialize_store_by_owner_id
from .dependencies import get_db
from .exceptions import StoreNotFound, SellerNotFound

router = APIRouter()


@router.get("/{user_id}", response_model=Store)
def read_store(user_id: UUID4, db: Session = Depends(get_db)):
    store = get_store_by_user_id(db, user_id)

    if store is None:
        raise StoreNotFound

    return store


@router.put("/{owner_id}")
def initialize_store(owner_id: UUID4, store: update_Store, db: Session = Depends((get_db))):
    seller = get_store_by_user_id(db, owner_id)
    if seller is None:
        raise SellerNotFound
    return initialize_store_by_owner_id(db, owner_id, store)
