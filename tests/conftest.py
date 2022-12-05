import email
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.database import SessionLocal, initialize_db

from app.api.store.models import Store
from app.api.user.models import User
from app.api.item.models import Item, ItemPhoto

base_url = "http://127.0.0.1:8000"


@pytest.fixture
def client():
    return TestClient(app, base_url)


def initialize_item_test_data(database: Session):

    item = Item(
        id="0df1dacb-67f6-495c-b993-49d06a293787",
        name="marker",
        description="so many water",
        price=500,
        store_id="49b2b69a-512c-4492-a5ea-50633893f8cc",
        inventory=50
    )

    photo = ItemPhoto(
        id="002891b5-6019-4144-b174-9aaaf8095063",
        item_id="0df1dacb-67f6-495c-b993-49d06a293787"
    )
    photo1 = ItemPhoto(
        id="f5832ea6-4c3c-48f0-8bd6-72ebd8754758",
        item_id="0df1dacb-67f6-495c-b993-49d06a293787"
    )

    database.add(item)

    database.add(photo)

    database.add(photo1)


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

    user = User(
        id="0df1dacb-67f6-495c-b993-49d06a293765",
        username="test",
        hashed_password="a",
        email="test@gmail.com",
        role_id=0
    )

    db.add(user)

    user1 = User(
        id="66761879-19ec-45ac-8d3d-41b477bf134b",
        email="ahuhwr886128@gmail.com",
        username="liang",
        hashed_password="b",
        role_id=0
    )
    
    db.add(user1)

    initialize_item_test_data(db)

    db.commit()
    db.close()
