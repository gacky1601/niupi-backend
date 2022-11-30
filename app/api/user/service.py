from uuid import UUID
from sqlalchemy.orm import Session
from . import models
from . import schemas

def get_user_by_id(db: Session, user_id: UUID):
    return db.query(models.User).filter(models.User.id == user_id).first()


def delete_user_by_id(db: Session, user_id: UUID):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()


def update_user_by_id(db: Session, user_id: UUID, user_update: schemas.User):
    user_info = db.query(models.User).filter(models.User.id == user_id).first()
    if user_update.email:
        user_info.email = user_update.email
    if user_update.username:
        user_info.username = user_update.username
    if user_update.address:
        user_info.address = user_update.address
    if user_update.cellphone_number:
        user_info.cellphone_number = user_update.cellphone_number
    db.commit()
    return db.query(models.User).filter(models.User.id == user_id).first()
