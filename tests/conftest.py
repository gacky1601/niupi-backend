import email
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database import engine, Base, SessionLocal

from app.api.store.models import Store

base_url = "http://127.0.0.1:8000"


@pytest.fixture
def client():
    return TestClient(app, base_url)


@pytest.fixture(scope="session", autouse=True)
def clear_db():
    db = SessionLocal()

    store = Store(
        id = "0df1dacb-67f6-495c-b993-49d06a293765",
        user_id = "0df1dacb-67f6-495c-b993-49d06a293766",
        name = "test",
        address = "test",
        email = "test@gmail.com",
        cellphone_number = "0000000000",
        telephone_number = "0000000000",
    )

    db.add(store)

    db.commit()
    db.close()

    yield
    Base.metadata.drop_all(engine)
