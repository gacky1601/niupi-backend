from fastapi.testclient import TestClient


def test_get_store_by_user_id(client: TestClient):
    user_id = "0df1dacb-67f6-495c-b993-49d06a293765"

    response = client.get(f"/api/store/{user_id}")

    assert response.status_code == 200
    assert response.json() == {
        "id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "user_id": "0df1dacb-67f6-495c-b993-49d06a293765",
        "name": "test",
        "address": "test",
        "email": "test@gmail.com",
        "cellphone_number": "0000000000",
        "telephone_number": "0000000000"
    }


def test_get_store_by_user_id_store_not_found(client: TestClient):
    user_id = "65761879-19ec-45ac-8d3d-41b477bf134b"

    response = client.get(f"/api/store/{user_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "There is no store owned by this user"
    }


def test_get_store_by_user_id_user_id_empty(client: TestClient):
    user_id = ""

    response = client.get(f"/api/store/{user_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }


def test_get_store_by_user_id_invalid_user_id_format(client: TestClient):
    user_id = "asldijfas>asdfj"

    response = client.get(f"/api/store/{user_id}")

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


def test_get_store_by_user_id_user_id_has_strip_whitespaces(client: TestClient):
    user_id = " 0df1dacb-67f6-495c-b993-49d06a293765 "

    response = client.get(f"/api/store/{user_id}")

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
