import pytest
from bcrypt import gensalt, hashpw
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.database import SessionLocal, initialize_db

from app.api.store.models import Store
from app.api.user.models import User
from app.api.items.models import Item, ItemPhoto


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

    database.add(item)

    photo = ItemPhoto(
        id="002891b5-6019-4144-b174-9aaaf8095063",
        item_id="0df1dacb-67f6-495c-b993-49d06a293787"
    )

    database.add(photo)

    photo = ItemPhoto(
        id="f5832ea6-4c3c-48f0-8bd6-72ebd8754758",
        item_id="0df1dacb-67f6-495c-b993-49d06a293787"
    )

    database.add(photo)
    item = Item(
        id="16c9a2d0-2f3d-4730-8e30-d4232366d2c4",
        name="pain",
        description="so painful",
        price=690,
        store_id="49b2b69a-512c-4492-a5ea-50633893f8cc",
        inventory=50
    )

    database.add(item)

    photo = ItemPhoto(
        id="2a906e72-7604-11ed-a1eb-0242ac120002",
        item_id="16c9a2d0-2f3d-4730-8e30-d4232366d2c4"
    )

    database.add(photo)

    item = Item(
        id="16c9a2d0-2f3d-4730-8e30-d4232366d2c8",
        name="No Photo",
        description="there is no photo my friend",
        price=690,
        store_id="49b2b69a-512c-4492-a5ea-50633893f8cc",
        inventory=50
    )

    database.add(item)


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
        cellphone_number="0900000000",
        telephone_number="02-22222222"
    )

    db.add(store)

    initialize_user_test_data(db)

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
