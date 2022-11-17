import email
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database import engine, Base, SessionLocal

from app.api.user.models import User

base_url = "http://127.0.0.1:8000"


@pytest.fixture
def client():
    return TestClient(app, base_url)


@pytest.fixture(scope="session", autouse=True)
def clear_db():
    db = SessionLocal()

    user = User(
        id="0df1dacb-67f6-495c-b993-49d06a293765",
        email="test@gmail.com",
        username="test",
        hashed_password="a",
        role_id=0
    )

    db.add(user)

    db.commit()
    db.close()

    yield
    Base.metadata.drop_all(engine)
