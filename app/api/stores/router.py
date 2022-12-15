from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import models, schemas, service
from .dependencies import get_db, validate_store_id

router = APIRouter()


@router.get("/{store_id}", response_model=schemas.Store)
def read_store(store: models.Store = Depends(validate_store_id)):
    return store


@router.patch("/{store_id}", response_model=schemas.Store)
def update_store(
    payload: schemas.StoreUpdate,
    store: models.Store = Depends(validate_store_id),
    database: Session = Depends(get_db)
):
    updated_store = service.update_store(database, store.id, payload)

    return updated_store
