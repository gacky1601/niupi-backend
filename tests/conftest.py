import pytest
from bcrypt import gensalt, hashpw
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.api.store.models import Store
from app.api.user.models import User
from app.database import SessionLocal, initialize_db
from app.main import app

base_url = "http://127.0.0.1:8000"


@pytest.fixture
def client():
    return TestClient(app, base_url)


def initialize_user_test_data(database: Session):
    password = "a".encode("utf-8")
    hashed_password = hashpw(password, gensalt()).decode("utf-8")

    user = User(
        id="0df1dacb-67f6-495c-b993-49d06a293765",
        username="test",
        hashed_password=hashed_password,
        email="test@gmail.com",
        role_id=0
    )

    database.add(user)


@pytest.fixture(autouse=True)
def reset_db():
    initialize_db()

    db = SessionLocal()

    store = Store(
        id="49b2b69a-512c-4492-a5ea-50633893f8cc",
        user_id="0df1dacb-67f6-495c-b993-49d06a293765",
        name="test",
        address="test",
        email="test@gmail.com",
        cellphone_number="0000000000",
        telephone_number="0000000000"
    )

    db.add(store)

    initialize_user_test_data(db)

    db.commit()
    db.close()
