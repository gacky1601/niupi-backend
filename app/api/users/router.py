from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .service import get_all_user
from .dependencies import get_db
from app.api.user.schemas import User

router = APIRouter()


@router.get("",response_model=List[User])
def read_users(db: Session = Depends(get_db)):
    users = get_all_user(db)
    
    return users
