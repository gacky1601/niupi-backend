from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import models, schemas, service
from .dependencies import get_db, validate_seller_id

router = APIRouter()


@router.get("/{seller_id}", response_model=schemas.Store)
def read_store(store: models.Store = Depends(validate_seller_id)):
    return store


@router.patch("/{seller_id}", response_model=schemas.Store)
def update_store(
    payload: schemas.StoreUpdate,
    store: models.Store = Depends(validate_seller_id),
    database: Session = Depends(get_db)
):
    updated_store = service.update_store(database, store.seller_id, payload)

    return updated_store
