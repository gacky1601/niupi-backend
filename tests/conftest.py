import email
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database import engine, Base, SessionLocal

from app.api.store.models import Store
from app.api.user.models import User
base_url = "http://127.0.0.1:8000"


@pytest.fixture
def client():
    return TestClient(app, base_url)


@pytest.fixture(scope="session", autouse=True)
def clear_db():
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
    user = User(
        id="0df1dacb-67f6-495c-b993-49d06a293765",
        store_id="49b2b69a-512c-4492-a5ea-50633893f8cc",
        username="test",
        hashed_password="test",
        address="test",
        email="test@gmail.com",
        cellphone_number="0000000000",
        role_id=0
    )
    db.add(store)
    db.add(user)
    db.commit()
    db.close()

    yield
    Base.metadata.drop_all(engine)
