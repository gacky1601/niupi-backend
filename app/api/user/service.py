from uuid import UUID
from sqlalchemy.orm import Session
from .models import User
from .schemas import UserUpdate


def get_user_by_id(db: Session, user_id: UUID):
    return db.query(User).filter(User.id == user_id).first()


def delete_user_by_id(db: Session, user_id: UUID):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()


def update_user(db: Session, user_id: UUID, payload: UserUpdate):
    db.query(User).filter(User.id == user_id).update(payload.dict(), synchronize_session="fetch")
    db.commit()
    return db.query(User).filter(User.id == user_id).first()
