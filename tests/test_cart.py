from fastapi.testclient import TestClient
from sqlalchemy import DateTime


def test_get_cart(client: TestClient):
    user_id = "0df1dacb-67f6-495c-b993-49d06a293765"
    response = client.get(f"/api/carts/{user_id}")
    data = response.json()

    assert response.status_code == 200
    assert data[0]["id"] == '49b2b69a-512c-4492-a5ea-50633893f8cc'
    assert data[0]['name'] == 'test'
    assert data[0]['items'][1]['name'] == 'marker'
    assert data[0]['items'][1]['price'] == 500
    assert data[0]['items'][1]['photo_id'] == 'c7e7db3b-a097-4fac-81d0-5f999ad33d86'
    assert data[0]['items'][1]['quantity'] == 2
    assert data[0]['items'][1]['updated_at'] == '2022-12-28T20:02:10.054216'
    assert data[0]['items'][0]['name'] == 'one'
    assert data[0]['items'][0]['price'] == 690
    assert data[0]['items'][0]['photo_id'] == '2ae40a76-d6af-4a4f-9293-648f8ae74024'
    assert data[0]['items'][0]['quantity'] == 1
    assert data[0]['items'][0]['updated_at'] == '2022-12-28T20:01:16.844201'


def test_get_cart_not_exist_user(client: TestClient):
    user_id = "77f1dacb-67f6-495c-b993-49d06a293765"
    response = client.get(f"/api/carts/{user_id}")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "User not found"
    }


def test_get_cart_invalid_user_id_format(client: TestClient):
    user_id = "1212121212"
    response = client.get(f"/api/carts/{user_id}")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "user_id"],
                "msg": "value is not a valid uuid",
                "type": "type_error.uuid"
            }
        ]
    }


def test_get_cart_with_empty_id(client: TestClient):
    user_id = ""
    response = client.get(f"/api/carts/{user_id}")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }
