from uuid import UUID
from sqlalchemy.orm import Session
from pydantic import UUID4
from .schemas import update_Store
from . import models


def get_store_by_user_id(db: Session, user_id: UUID):
    return db.query(models.Store).filter(models.Store.user_id == user_id).first()


def initialize_store_by_owner_id(db: Session, owner_id: UUID4, store: update_Store):
    update = db.query(models.Store).filter(
        models.Store.user_id == owner_id).first()
    update.name = store.name
    if store.email:
        update.email = store.email
    if store.address:
        update.address = store.address
    if store.cellphone_number:
        update.cellphone_number = store.cellphone_number
    if store.telephone_number:
        update.telephone_number = store.telephone_number
    db.commit()
    return db.query(models.Store).filter(models.Store.user_id == owner_id).first()
