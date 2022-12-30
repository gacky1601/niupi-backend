from fastapi.testclient import TestClient


def test_get_photos_by_item_id(client: TestClient):
    item_id = "0df1dacb-67f6-495c-b993-49d06a293787"

    response = client.get(f"/api/items/{item_id}/photos")

    assert response.status_code == 200
    assert response.json() == [
        "c7e7db3b-a097-4fac-81d0-5f999ad33d86",
        "f5832ea6-4c3c-48f0-8bd6-72ebd8754758"
    ]


def test_get_photo_by_item_id_not_found(client: TestClient):
    item_id = "65761879-19ec-45ac-8d3d-41b477bf134b"

    response = client.get(f"/api/items/{item_id}/photos")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }


def test_get_photo_by_item_id_photo_not_exist(client: TestClient):
    item_id = "0df1dacb-67f6-495c-b993-49d06a293789"

    response = client.get(f"/api/items/{item_id}/photos")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }


def test_add_photos_by_item_id(client: TestClient):
    item_id = "0df1dacb-67f6-495c-b993-49d06a293787"
    json = ["003791b5-6019-4144-b174-9aaaf8095063", "004591b5-6019-4144-b174-9aaaf8095063"]
    response = client.post(f"/api/items/{item_id}/photos", json=json)

    assert response.status_code == 200
    assert response.json() == [
        "c7e7db3b-a097-4fac-81d0-5f999ad33d86",
        "f5832ea6-4c3c-48f0-8bd6-72ebd8754758",
        "003791b5-6019-4144-b174-9aaaf8095063",
        "004591b5-6019-4144-b174-9aaaf8095063"
    ]


def test_add_photos_by_item_id_not_found(client: TestClient):
    item_id = "65761879-19ec-45ac-8d3d-41b477bf134b"
    json = ["003791b5-6019-4144-b174-9aaaf8095063"]
    response = client.post(f"/api/items/{item_id}/photos", json=json)

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }


def test_add_photos_by_item_id_request_body_is_empty(client: TestClient):
    item_id = "0df1dacb-67f6-495c-b993-49d06a293787"
    json = []
    response = client.post(f"/api/items/{item_id}/photos", json=json)

    assert response.status_code == 422
    assert response.json() == {
        "detail": [{'ctx': {'limit_value': 1},
                    'loc': ['body'],
                    'msg': 'ensure this value has at least 1 items',
                    'type': 'value_error.list.min_items'}]
    }


def test_delete_photos_by_photo_id(client: TestClient):
    item_id = "16c9a2d0-2f3d-4730-8e30-d4232366d2c9"

    json = ["2ae40a76-d6af-4a4f-9293-648f8ae74024"]

    response = client.delete(f"/api/items/{item_id}/photos", json=json)

    assert response.status_code == 200
    assert response.json() == ["3da32f9c-69b3-448d-b68c-658fc8db91fd"]

    response = client.get(f"/api/items/{item_id}/photos")

    assert response.status_code == 200
    assert response.json() == ["3da32f9c-69b3-448d-b68c-658fc8db91fd"]


def test_delete_photos_by_photo_id_item_not_exist(client: TestClient):
    item_id = "0df1dacb-67f6-495c-b993-49d06a293789"

    response = client.get(f"/api/items/{item_id}/photos")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }


def test_delete_photos_by_photo_id_invalid_item_id_format(client: TestClient):
    item_id = "16c9a2d0-2f3d-4730-8e30-d4232366d2c9"

    json = ["asldijfas>asdfj"]

    response = client.delete(f"/api/items/{item_id}/photos", json=json)

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ['body', 0],
                "msg": "value is not a valid uuid",
                "type": "type_error.uuid"
            }
        ]
    }


def test_delete_photos_by_photo_id_item_id_is_empty_string(client: TestClient):
    item_id = ""
    json = ["2ae40a76-d6af-4a4f-9293-648f8ae74024", "3da32f9c-69b3-448d-b68c-658fc8db91fd"]

    response = client.delete(f"/api/items/{item_id}/photos", json=json)
    assert response.status_code == 404
    assert response.json() == {
        'detail': "Not Found"
    }


def test_delete_photos_id_request_body_is_empty_array(client: TestClient):
    item_id = "16c9a2d0-2f3d-4730-8e30-d4232366d2c9"

    json = []

    response = client.delete(f"/api/items/{item_id}/photos", json=json)

    assert response.status_code == 422


def test_delete_photos_ids_delete_non_existing_photo_id(client: TestClient):
    item_id = "16c9a2d0-2f3d-4730-8e30-d4232366d2c9"

    json = ["baf8f19d-60cf-4089-b0c0-467b1d593a88", "0d46d352-a319-4864-9d84-875e0fea5a4d"]

    response = client.delete(f"/api/items/{item_id}/photos", json=json)

    assert response.status_code == 200
    assert response.json() == [
        "2ae40a76-d6af-4a4f-9293-648f8ae74024",
        "3da32f9c-69b3-448d-b68c-658fc8db91fd"
    ]


def test_get_item_after_delete_all_photos(client: TestClient):
    item_id = "16c9a2d0-2f3d-4730-8e30-d4232366d2c9"

    json = ["2ae40a76-d6af-4a4f-9293-648f8ae74024", "3da32f9c-69b3-448d-b68c-658fc8db91fd"]

    response = client.delete(f"/api/items/{item_id}/photos", json=json)

    assert response.status_code == 200
    assert response.json() == []

    response = client.get(f"/api/items/{item_id}")

    assert response.status_code == 200
    assert response.json() == {
        "id": "16c9a2d0-2f3d-4730-8e30-d4232366d2c9",
        "name": "one",
        "description": "photos",
        "price": 690,
        "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "inventory": 50,
        "photo_ids": []
    }
