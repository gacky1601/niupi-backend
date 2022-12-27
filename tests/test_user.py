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


def test_get_users(client: TestClient):
    response = client.get("/api/users")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "0df1dacb-67f6-495c-b993-49d06a293765",
            "email": "test@gmail.com",
            "username": "test",
            "address": None,
            "cellphone_number": None,
            "role_id": 0,
        },
        {
            "id": "66761879-19ec-45ac-8d3d-41b477bf134b",
            "email": "ahuhwr886128@gmail.com",
            "username": "liang",
            "address": None,
            "cellphone_number": None,
            "role_id": 0
        }
    ]


def test_delete_user_by_id_invalid_user_id_format(client: TestClient):
    user_id = "asldijfas>asdfj"

    response = client.delete(f"/api/user/{user_id}")

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


def test_delete_user_by_id_id_has_strip_whitespaces(client: TestClient):
    user_id = " 0df1dacb-67f6-495c-b993-49d06a293765 "

    response = client.delete(f"/api/user/{user_id}")

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


def test_delete_not_exist_user(client: TestClient):
    user_id = "65761879-19ec-45ac-8d3d-41b477bf134b"
    response = client.delete(f"/api/user/{user_id}")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Cannot delete an account that does not exist"
    }


def test_delete_user_with_empty_name(client: TestClient):
    user_id = ""
    response = client.delete(f"/api/user/{user_id}")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }


def test_delete_user_by_id(client: TestClient):
    user_id = "0df1dacb-67f6-495c-b993-49d06a293765"

    response = client.delete(f"/api/user/{user_id}")

    assert response.status_code == 204
    response = client.get(f"/api/user/{user_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "User not found"
    }


def test_update_user_by_id(client: TestClient):
    user_id = "0df1dacb-67f6-495c-b993-49d06a293765"

    json = {
        "email": "update@gmail.com",
        "username": "update",
    }

    response = client.patch(f"/api/user/{user_id}", json=json)

    assert response.json() == {
        "id": "0df1dacb-67f6-495c-b993-49d06a293765",
        "email": "update@gmail.com",
        "username": "update",
        "address": None,
        "cellphone_number": None,
        "role_id": 0,
    }
    assert response.status_code == 200


def test_update_user_not_exist_user(client: TestClient):
    user_id = "65761879-19ec-45ac-8d3d-41b477bf134b"
    json = {
        "email": "update@gmail.com",
        "username": "update",
    }
    response = client.patch(f"/api/user/{user_id}", json=json)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Non-existent users cannot be updated"
    }


def test_update_user_invalid_email(client: TestClient):
    user_id = "0df1dacb-67f6-495c-b993-49d06a293765"

    json = {
        "email": "nnnnn",
    }
    response = client.patch(f"/api/user/{user_id}", json=json)
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "email"
                ],
                "msg": "value is not a valid email address",
                "type": "value_error.email"
            }
        ]
    }


def test_update_user_address_is_empty_string(client: TestClient):
    user_id = "0df1dacb-67f6-495c-b993-49d06a293765"

    json = {
        "address": "",
    }
    response = client.patch(f"/api/user/{user_id}", json=json)
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'loc': [
                    'body',
                    'address'
                ],
                'msg': 'ensure this value has at least 1 characters',
                'type': 'value_error.any_str.min_length',
                'ctx': {'limit_value': 1}
            }
        ]
    }


def test_update_user_cellphone_number_is_empty_string(client: TestClient):
    user_id = "0df1dacb-67f6-495c-b993-49d06a293765"

    json = {
        "cellphone_number": "",
    }
    response = client.patch(f"/api/user/{user_id}", json=json)
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'loc': [
                    'body',
                    'cellphone_number'
                ],
                'msg': 'ensure this value has at least 1 characters',
                'type': 'value_error.any_str.min_length',
                'ctx': {'limit_value': 1}
            }
        ]
    }


def test_update_user_invalid_user_id(client: TestClient):
    user_id = "000000"

    json = {
        "email": "update@gmail.com",
        "username": "update",
    }
    response = client.patch(f"/api/user/{user_id}", json=json)
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


def test_update_user_invalid_cellphone_number(client: TestClient):
    user_id = "0df1dacb-67f6-495c-b993-49d06a293765"

    json = {
        "cellphone_number": "012345678",
    }
    response = client.patch(f"/api/user/{user_id}", json=json)
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "cellphone_number"
                ],
                "msg": 'string does not match regex "^09+([0-9]{8})$"',
                "type": "value_error.str.regex",
                'ctx': {'pattern': '^09+([0-9]{8})$'}
            }
        ]
    }
