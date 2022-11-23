from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4
from .schemas import User
from .service import get_store_by_user_id
from .dependencies import get_db
from .exceptions import StoreNotFound
from .exceptions import UserIdEmpty
router = APIRouter()


@router.get("/{user_id}", response_model=User)
def read_store(user_id: UUID4, db: Session = Depends(get_db)):
    
    store = get_store_by_user_id(db, user_id)
    if store is None:
        raise StoreNotFound
    if user_id is None:
        raise UserIdEmpty
    return store
