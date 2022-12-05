from fastapi.testclient import TestClient


def test_get_item_by_item_id(client: TestClient):
    item_id = "0df1dacb-67f6-495c-b993-49d06a293787"

    response = client.get(f"/api/item/{item_id}")

    assert response.status_code == 200
    assert response.json() == {
        "id": "0df1dacb-67f6-495c-b993-49d06a293787",
        "name": "marker",
        "description": "so many water",
        "price": 500,
        "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "inventory": 50,
        "photos": ["002891b5-6019-4144-b174-9aaaf8095063", "f5832ea6-4c3c-48f0-8bd6-72ebd8754758"]
    }


def test_get_item_by_item_id_not_found(client: TestClient):
    item_id = "65761879-19ec-45ac-8d3d-41b477bf134b"

    response = client.get(f"/api/item/{item_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }


def test_get_item_by_item_id_item_id_is_empty_string(client: TestClient):
    item_id = ""

    response = client.get(f"/api/item/{item_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }


def test_get_item_by_item_id_invalid_item_id_format(client: TestClient):
    item_id = "asldijfas>asdfj"

    response = client.get(f"/api/item/{item_id}")

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "item_id"],
                "msg": "value is not a valid uuid",
                "type": "type_error.uuid"
            }
        ]
    }


def test_get_item_by_item_id_item_id_has_strip_whitespaces(client: TestClient):
    item_id = " 0df1dacb-67f6-495c-b993-49d06a293765 "

    response = client.get(f"/api/item/{item_id}")

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "item_id"],
                "msg": "value is not a valid uuid",
                "type": "type_error.uuid"
            }
        ]
    }
