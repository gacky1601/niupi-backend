from fastapi.testclient import TestClient


def test_get_user_by_id(client: TestClient):
    user_id = "0df1dacb-67f6-495c-b993-49d06a293765"

    response = client.get(f"/api/user/{user_id}")

    assert response.status_code == 200
    assert response.json() == {
        "id": "0df1dacb-67f6-495c-b993-49d06a293765",
        "email": "test@gmail.com",
        "username": "test",
        "address": None,
        "cellphone_number": None,
        "role_id": 0,
    }


def test_get_user_by_id_user_not_found(client: TestClient):
    user_id = "65761879-19ec-45ac-8d3d-41b477bf134b"

    response = client.get(f"/api/user/{user_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "User not found"
    }


def test_get_user_by_id_empty_user_id_string(client: TestClient):
    user_id = ""

    response = client.get(f"/api/user/{user_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }


def test_get_user_by_id_invalid_user_id_format(client: TestClient):
    user_id = "asldijfas>asdfj"

    response = client.get(f"/api/user/{user_id}")

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


def test_get_user_by_id_id_has_strip_whitespaces(client: TestClient):
    user_id = " 0df1dacb-67f6-495c-b993-49d06a293765 "

    response = client.get(f"/api/user/{user_id}")

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
