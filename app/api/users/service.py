from sqlalchemy.orm import Session

import app.api.user.models as models


def get_all_user(db: Session):
    return db.query(models.User).all()
