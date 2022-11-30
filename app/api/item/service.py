from uuid import UUID
from sqlalchemy.orm import Session

from . import models


def get_item_by_item_id(db: Session, item_id: UUID):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def delete_item_by_id(db: Session, item_id: UUID):
    db.query(models.Item).filter(models.Item.id == item_id).delete()
    db.commit()
