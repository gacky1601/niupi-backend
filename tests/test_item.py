from fastapi.testclient import TestClient


def test_get_item_by_item_id(client: TestClient):
    item_id = "0df1dacb-67f6-495c-b993-49d06a293787"

    response = client.get(f"/api/items/{item_id}")

    assert response.status_code == 200
    assert response.json() == {
        "id": "0df1dacb-67f6-495c-b993-49d06a293787",
        "name": "marker",
        "description": "so many water",
        "price": 500,
        "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "inventory": 50,
        "photo_ids": [
            "c7e7db3b-a097-4fac-81d0-5f999ad33d86",
            "f5832ea6-4c3c-48f0-8bd6-72ebd8754758"
        ]
    }


def test_get_item_by_item_id_not_found(client: TestClient):
    item_id = "65761879-19ec-45ac-8d3d-41b477bf134b"

    response = client.get(f"/api/items/{item_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }


def test_get_item_by_item_id_item_id_is_empty_string(client: TestClient):
    item_id = ""

    response = client.get(f"/api/items/{item_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }


def test_get_item_by_item_id_invalid_item_id_format(client: TestClient):
    item_id = "asldijfas>asdfj"

    response = client.get(f"/api/items/{item_id}")

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

    response = client.get(f"/api/items/{item_id}")

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


def test_update_item(client: TestClient):
    item_id = "0df1dacb-67f6-495c-b993-49d06a293787"

    json = {
        "name": "newitem",
        "description": "no water",
        "price": 5000,
        "inventory": 10,
    }

    response = client.patch(f"/api/items/{item_id}", json=json)

    assert response.json() == {
        "id": "0df1dacb-67f6-495c-b993-49d06a293787",
        "name": "newitem",
        "description": "no water",
        "price": 5000,
        "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "inventory": 10,
        "photo_ids": [
            "c7e7db3b-a097-4fac-81d0-5f999ad33d86",
            "f5832ea6-4c3c-48f0-8bd6-72ebd8754758"
        ]
    }
    assert response.status_code == 200


def test_update_item_not_exist_item(client: TestClient):
    item_id = "65761879-19ec-45ac-8d3d-41b477bf134b"
    json = {
        "name": "newitem",
        "description": "no water",
        "price": 5000,
        "inventory": 10,
    }
    response = client.patch(f"/api/items/{item_id}", json=json)
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }


def test_update_item_id_is_empty_string(client: TestClient):
    item_id = ""

    response = client.patch(f"/api/items/{item_id}")
    assert response.status_code == 404
    assert response.json() == {
        'detail': "Not Found"
    }


def test_update_item_id_has_strip_whitespaces(client: TestClient):
    item_id = " 0df1dacb-67f6-495c-b993-49d06a293787 "

    json = {
        "name": "newitem",
        "description": "no water",
        "price": 5000,
        "inventory": 10,
    }
    response = client.patch(f"/api/items/{item_id}", json=json)
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'loc': [
                    'path',
                    'item_id'
                ],
                'msg': 'value is not a valid uuid',
                'type': 'type_error.uuid'
            }
        ]
    }


def test_update_item_invalid_item_id_format(client: TestClient):
    item_id = "asldijfas>asdfj"

    response = client.get(f"/api/items/{item_id}")

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


def test_update_item_not_update_every_column(client: TestClient):
    item_id = "0df1dacb-67f6-495c-b993-49d06a293787"

    json = {
        "name": "newitem",
        "description": "no water",
        "price": 5000,
    }

    response = client.patch(f"/api/items/{item_id}", json=json)

    assert response.json() == {
        "detail": [
            {
                'loc': [
                    'body',
                    'inventory'
                ],
                'msg': 'field required',
                'type': 'value_error.missing'
            }
        ]
    }
    assert response.status_code == 422


def test_delete_item_by_id(client: TestClient):
    item_id = "16c9a2d0-2f3d-4730-8e30-d4232366d2c4"

    response = client.delete(f"/api/items/{item_id}")

    assert response.status_code == 204
    response = client.get(f"/api/items/{item_id}")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }


def test_delete_item_by_empty_item_id_string(client: TestClient):
    item_id = ""

    response = client.delete(f"/api/items/{item_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }


def test_delete_item_by_id_invalid_item_id_format(client: TestClient):
    item_id = "asldijfas>asdfj"

    response = client.get(f"/api/items/{item_id}")

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


def test_delete_item_by_id_without_photo(client: TestClient):
    item_id = "16c9a2d0-2f3d-4730-8e30-d4232366d2c8"

    response = client.delete(f"/api/items/{item_id}")

    assert response.status_code == 204
    response = client.get(f"/api/items/{item_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }


def test_get_photos_after_delete_item(client: TestClient):
    item_id = "16c9a2d0-2f3d-4730-8e30-d4232366d2c4"

    response = client.delete(f"/api/items/{item_id}")

    assert response.status_code == 204

    response = client.get(f"/api/items/{item_id}/photos")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }


def test_create_new_item(client: TestClient):
    json = {
        "name": "marker",
        "description": "so many water",
        "price": 500,
        "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "inventory": 50,
        "photo_ids": [
            "56cef54e-78c1-4c4d-9f4f-44ebcad5bcfa",
            "da27353b-b024-4c1c-bf3a-91c48f0698f4"
        ]
    }
    response = client.post("/api/items", json=json)
    item_id = response.json()["id"]
    assert response.json() == {
        "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "name": "marker",
        "description": "so many water",
        "price": 500,
        "inventory": 50,
        "id": item_id,
        'photo_ids': [
            "56cef54e-78c1-4c4d-9f4f-44ebcad5bcfa",
            "da27353b-b024-4c1c-bf3a-91c48f0698f4"
        ]
    }
    assert response.status_code == 201


def test_create_new_item_without_photo(client: TestClient):
    json = {
        "name": "marker",
        "description": "so many water",
        "price": 500,
        "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "inventory": 50,
    }
    response = client.post("/api/items", json=json)
    item_id = response.json()["id"]
    assert response.json() == {
        "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "name": "marker",
        "description": "so many water",
        "price": 500,
        "inventory": 50,
        "id": item_id,
        'photo_ids': []
    }
    assert response.status_code == 201


def test_set_new_item_store_id_not_fuond(client: TestClient):

    json = {
        "name": "marker",
        "description": "so many water",
        "price": 500,
        "store_id": "98A7A34B-CBBD-4517-B514-0ACC2B631C22",
        "inventory": 50
    }
    response = client.post("/api/items", json=json)
    assert response.json() == {
        "detail": "Cannot add a new item to a store that does not exist"
    }
    assert response.status_code == 400
