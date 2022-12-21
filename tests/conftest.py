import pytest
from bcrypt import gensalt, hashpw
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.database import SessionLocal, initialize_database

from app.api.stores.models import Store
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
        id="c7e7db3b-a097-4fac-81d0-5f999ad33d86",
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
        name="pain_marker",
        description="so painful",
        price=690,
        store_id="49b2b69a-512c-4492-a5ea-50633893f8cc",
        inventory=50
    )

    database.add(item)

    photo = ItemPhoto(
        id="a41439ee-d3fb-4f52-b86c-624b659eb092",
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

    item = Item(
        id="16c9a2d0-2f3d-4730-8e30-d4232366d2c9",
        name="one",
        description="photos",
        price=690,
        store_id="49b2b69a-512c-4492-a5ea-50633893f8cc",
        inventory=50
    )

    database.add(item)

    photo = ItemPhoto(
        id="2ae40a76-d6af-4a4f-9293-648f8ae74024",
        item_id="16c9a2d0-2f3d-4730-8e30-d4232366d2c9"
    )

    database.add(photo)

    photo = ItemPhoto(
        id="3da32f9c-69b3-448d-b68c-658fc8db91fd",
        item_id="16c9a2d0-2f3d-4730-8e30-d4232366d2c9"
    )

    database.add(photo)


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


def initialize_store_test_data(database: Session):
    store = Store(
        id="49b2b69a-512c-4492-a5ea-50633893f8cc",
        seller_id="0df1dacb-67f6-495c-b993-49d06a293765",
        name="test",
        county_id=0,
        district_id=2,
        detail_address="民權東路二段 41 號",
        email="test@gmail.com",
        cellphone_number="0900000000",
        telephone_number="02-22222222"
    )

    database.add(store)


@pytest.fixture(autouse=True)
def reset_db():
    initialize_database()

    db = SessionLocal()

    initialize_user_test_data(db)
    initialize_store_test_data(db)

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
