from fastapi.testclient import TestClient


def test_sign_up_invalid_email_format(client: TestClient):
    json = {
        "email": "hidasfk",
        "username": "yu",
        "password": "test",
    }

    response = client.post("/api/auth/signup", json=json)

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


def test_sign_up_empty_username_string(client: TestClient):
    json = {
        "email": "test@gamil.com",
        "username": "",
        "password": "test",
    }

    response = client.post("/api/auth/signup", json=json)

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "ctx": {
                    "limit_value": 1
                },
                "loc": ["body", "username"],
                "msg": "ensure this value has at least 1 characters",
                "type": "value_error.any_str.min_length"
            }
        ]
    }


def test_sign_up_empty_password_string(client: TestClient):
    json = {
        "email": "test@gamil.com",
        "username": "yu",
        "password": "",
    }

    response = client.post("/api/auth/signup", json=json)

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "ctx": {
                    "limit_value": 1
                },
                "loc": ["body", "password"],
                "msg": "ensure this value has at least 1 characters",
                "type": "value_error.any_str.min_length"
            }
        ]
    }


def test_sign_up_email_has_strip_whitespaces(client: TestClient):
    json = {
        "email": " yu2001@gamil.com ",
        "username": "yu",
        "password": "test",
    }

    response = client.post("/api/auth/signup", json=json)

    assert response.status_code == 200

    data = response.json()
    assert data["email"] == "yu2001@gamil.com"
    assert data["username"] == "yu"
    assert data["address"] is None
    assert data["cellphone_number"] is None
    assert data["role_id"] == 0
    assert "hashed_password" not in data
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/api/user/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "yu2001@gamil.com"
    assert data["username"] == "yu"
    assert data["address"] is None
    assert data["cellphone_number"] is None
    assert data["role_id"] == 0
    assert "hashed_password" not in data
    assert data["id"] == user_id


def test_sign_up_username_has_strip_whitespaces(client: TestClient):
    json = {
        "email": "yu@gamil.com",
        "username": " yu ",
        "password": "test",
    }

    response = client.post("/api/auth/signup", json=json)

    assert response.status_code == 200

    data = response.json()
    assert data["email"] == "yu@gamil.com"
    assert data["username"] == "yu"
    assert data["address"] is None
    assert data["cellphone_number"] is None
    assert data["role_id"] == 0
    assert "hashed_password" not in data
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/api/user/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "yu@gamil.com"
    assert data["username"] == "yu"
    assert data["address"] is None
    assert data["cellphone_number"] is None
    assert data["role_id"] == 0
    assert "hashed_password" not in data
    assert data["id"] == user_id


def test_sign_up(client: TestClient):
    json = {
        "email": "justYu@gamil.com",
        "username": "yu",
        "password": "test",
    }

    response = client.post("/api/auth/signup", json=json)

    assert response.status_code == 200

    data = response.json()
    assert data["email"] == "justYu@gamil.com"
    assert data["username"] == "yu"
    assert data["address"] is None
    assert data["cellphone_number"] is None
    assert data["role_id"] == 0
    assert "hashed_password" not in data
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/api/user/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "justYu@gamil.com"
    assert data["username"] == "yu"
    assert data["address"] is None
    assert data["cellphone_number"] is None
    assert data["role_id"] == 0
    assert "hashed_password" not in data
    assert data["id"] == user_id

    response = client.get(f"/api/stores/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["seller_id"] == user_id
    assert data["name"] is None
    assert data["email"] is None
    assert data["address"] is None
    assert data["cellphone_number"] is None
    assert data["telephone_number"] is None


def test_sign_up_email_already_in_use(client: TestClient):
    json = {
        "email": "test@gmail.com",
        "username": "yu",
        "password": "test",
    }

    response = client.post("/api/auth/signup", json=json)

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Email already in use"
    }


def test_login_invalid_email_format(client: TestClient):
    json = {
        "email": "hidasfk",
        "password": "test",
    }

    response = client.get("/api/auth/login", json=json)

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


def test_login_empty_password_string(client: TestClient):
    json = {
        "email": "test@gamil.com",
        "password": "",
    }

    response = client.get("/api/auth/login", json=json)

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "ctx": {
                    "limit_value": 1
                },
                "loc": ["body", "password"],
                "msg": "ensure this value has at least 1 characters",
                "type": "value_error.any_str.min_length"
            }
        ]
    }


def test_login(client: TestClient):
    json = {
        "email": "test@gmail.com",
        "password": "a",
    }

    response = client.get("/api/auth/login", json=json)

    assert response.status_code == 200

    data = response.json()
    assert data["email"] == "test@gmail.com"
    assert data["username"] == "test"
    assert data["address"] is None
    assert data["cellphone_number"] is None
    assert data["role_id"] == 0
    assert "hashed_password" not in data
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/api/user/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@gmail.com"
    assert data["username"] == "test"
    assert data["address"] is None
    assert data["cellphone_number"] is None
    assert data["role_id"] == 0
    assert "hashed_password" not in data
    assert data["id"] == user_id


def test_login_invalid_email(client: TestClient):
    json = {
        "email": "y@gamil.com",
        "password": "test",
    }

    response = client.get("/api/auth/login", json=json)

    assert response.status_code == 400

    assert response.json() == {
        "detail": "Invalid email or password."
    }


def test_login_invalid_password(client: TestClient):
    json = {
        "email": "yu2001@gamil.com",
        "password": "t",
    }

    response = client.get("/api/auth/login", json=json)

    assert response.status_code == 400

    assert response.json() == {
        "detail": "Invalid email or password."
    }
