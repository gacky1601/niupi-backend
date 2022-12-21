from fastapi.testclient import TestClient


def test_get_store_by_store_id(client: TestClient):
    store_id = "49b2b69a-512c-4492-a5ea-50633893f8cc"

    response = client.get(f"/api/stores/{store_id}")

    assert response.status_code == 200
    assert response.json() == {
        "id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "seller_id": "0df1dacb-67f6-495c-b993-49d06a293765",
        "name": "test",
        "address": {
            "county": "臺北市",
            "district": "中山區",
            "detail": "民權東路二段 41 號",
        },
        "email": "test@gmail.com",
        "cellphone_number": "0900000000",
        "telephone_number": "02-22222222"
    }


def test_get_store_by_store_id_store_not_found(client: TestClient):
    store_id = "65761879-19ec-45ac-8d3d-41b477bf134b"

    response = client.get(f"/api/stores/{store_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Store not found"
    }


def test_get_store_by_store_id_store_id_empty(client: TestClient):
    store_id = ""

    response = client.get(f"/api/stores/{store_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }


def test_get_store_by_store_id_invalid_store_id_format(client: TestClient):
    store_id = "asldijfas>asdfj"

    response = client.get(f"/api/stores/{store_id}")

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "store_id"],
                "msg": "value is not a valid uuid",
                "type": "type_error.uuid"
            }
        ]
    }


def test_get_store_by_store_id_store_id_has_strip_whitespaces(client: TestClient):
    store_id = " 0df1dacb-67f6-495c-b993-49d06a293765 "

    response = client.get(f"/api/stores/{store_id}")

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "store_id"],
                "msg": "value is not a valid uuid",
                "type": "type_error.uuid"
            }
        ]
    }


def test_update_store(client: TestClient):
    store_id = "49b2b69a-512c-4492-a5ea-50633893f8cc"
    json = {
        "name": "NoNutNovember",
        "email": "NNN@gmail.com",
        "county_id": "0",
        "district_id": "2",
        "detail_address": "民權東路二段 41 號",
        "cellphone_number": "0987654321",
        "telephone_number": "02-22542120"
    }
    response = client.patch(f"/api/stores/{store_id}", json=json)

    assert response.status_code == 200
    assert response.json() == {
        "id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "seller_id": "0df1dacb-67f6-495c-b993-49d06a293765",
        "name": "NoNutNovember",
        "email": "NNN@gmail.com",
        "address": {
            "county": "臺北市",
            "district": "中山區",
            "detail": "民權東路二段 41 號",
        },
        "cellphone_number": "0987654321",
        "telephone_number": "02-22542120",
    }


def test_update_store_without_cellphone_number(client: TestClient):
    store_id = "49b2b69a-512c-4492-a5ea-50633893f8cc"
    json = {
        "name": "NoNutNovember",
        "email": "NNN@gmail.com",
        "address": {
            "county": "臺北市",
            "district": "中山區",
            "detail": "民權東路二段 41 號",
        },
        "telephone_number": "02-22542120",
    }
    response = client.patch(f"/api/stores/{store_id}", json=json)

    assert response.status_code == 200
    assert response.json() == {
        "id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
        "seller_id": "0df1dacb-67f6-495c-b993-49d06a293765",
        "name": "NoNutNovember",
        "address": {
            "county": "臺北市",
            "district": "中山區",
            "detail": "民權東路二段 41 號",
        },
        "email": "NNN@gmail.com",
        "cellphone_number": "0900000000",
        "telephone_number": "02-22542120",
    }


def test_update_store_with_empty_name(client: TestClient):
    store_id = "49b2b69a-512c-4492-a5ea-50633893f8cc"
    json = {
        "name": "",
    }
    response = client.patch(f"/api/stores/{store_id}", json=json)

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "ctx": {
                    "limit_value": 1
                },
                "loc": [
                    "body",
                    "name"
                ],
                "msg": "ensure this value has at least 1 characters",
                "type": "value_error.any_str.min_length"
            }
        ]
    }


def test_update_store_with_invalid_email(client: TestClient):
    store_id = "49b2b69a-512c-4492-a5ea-50633893f8cc"
    json = {
        "email": "NNNgmail.com",
    }
    response = client.patch(f"/api/stores/{store_id}", json=json)

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


def test_update_store_with_invalid_cellphone_number(client: TestClient):
    store_id = "49b2b69a-512c-4492-a5ea-50633893f8cc"
    json = {
        "cellphone_number": "8888",
    }
    response = client.patch(f"/api/stores/{store_id}", json=json)

    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'ctx': {'pattern': '^09+([0-9]{8})$'},
                'loc': ['body', 'cellphone_number'],
                'msg': 'string does not match regex "^09+([0-9]{8})$"',
                'type': 'value_error.str.regex'
            }
        ]
    }


def test_update_store_with_invalid_telephone_number(client: TestClient):
    store_id = "49b2b69a-512c-4492-a5ea-50633893f8cc"
    json = {
        "telephone_number": "4444",
    }
    response = client.patch(f"/api/stores/{store_id}", json=json)

    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'ctx': {'pattern': '^(?=([0-9]{2,4}\\-[0-9]{6,8})).{10,11}$'},
                'loc': ['body', 'telephone_number'],
                'msg': 'string does not match regex "^(?=([0-9]{2,4}\\-[0-9]{6,8})).{10,11}$"',
                'type': 'value_error.str.regex'
            }
        ]
    }


def test_update_store_with_invalid_store_id(client: TestClient):
    store_id = "qwerasdf"
    json = {
        "name": "NoNutNovember",
    }
    response = client.patch(f"/api/stores/{store_id}", json=json)

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "store_id"],
                "msg": "value is not a valid uuid",
                "type": "type_error.uuid"
            }
        ]
    }


def test_update_store_non_existing_store(client: TestClient):
    store_id = "65761879-19ec-45ac-8d3d-41b477bf134b"
    json = {
        "name": "NoNutNovember",
    }
    response = client.patch(f"/api/stores/{store_id}", json=json)

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Store not found"
    }


def test_search_item_by_keyword(client: TestClient):
    store_id = "49b2b69a-512c-4492-a5ea-50633893f8cc"
    keyword = "mark"

    response = client.get(f"/api/stores/{store_id}/items?keyword={keyword}")

    assert response.status_code == 200
    assert response.json() == [
        {
            "item_id": "0df1dacb-67f6-495c-b993-49d06a293787",
            "name": "marker",
            "price": 500,
            "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
            "inventory": 50,
            "photo": "c7e7db3b-a097-4fac-81d0-5f999ad33d86"
        },
        {
            "item_id": "16c9a2d0-2f3d-4730-8e30-d4232366d2c4",
            "name": "pain_marker",
            "price": 690,
            "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
            "inventory": 50,
            "photo": "a41439ee-d3fb-4f52-b86c-624b659eb092"
        }
    ]


def test_search_item_without_keyword(client: TestClient):
    store_id = "49b2b69a-512c-4492-a5ea-50633893f8cc"

    response = client.get(f"/api/stores/{store_id}/items")

    assert response.status_code == 200
    assert response.json() == [
        {
            "item_id": "0df1dacb-67f6-495c-b993-49d06a293787",
            "name": "marker",
            "price": 500,
            "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
            "inventory": 50,
            "photo": "c7e7db3b-a097-4fac-81d0-5f999ad33d86"
        },
        {
            "item_id": "16c9a2d0-2f3d-4730-8e30-d4232366d2c4",
            "name": "pain_marker",
            "price": 690,
            "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
            "inventory": 50,
            "photo": "a41439ee-d3fb-4f52-b86c-624b659eb092"
        },
        {
            "item_id": "16c9a2d0-2f3d-4730-8e30-d4232366d2c8",
            "name": "No Photo",
            "price": 690,
            "store_id": "49b2b69a-512c-4492-a5ea-50633893f8cc",
            "inventory": 50,
            "photo": None
        },
        {
            'inventory': 50,
            'item_id': '16c9a2d0-2f3d-4730-8e30-d4232366d2c9',
            'name': 'one',
            'photo': '2ae40a76-d6af-4a4f-9293-648f8ae74024',
            'price': 690,
            'store_id': '49b2b69a-512c-4492-a5ea-50633893f8cc'
        }
    ]


def test_search_item_keyword_is_empty_string(client: TestClient):
    store_id = "49b2b69a-512c-4492-a5ea-50633893f8cc"

    response = client.get(f"/api/stores/{store_id}/items?keyword=")

    assert response.status_code == 200
    assert response.json() == []


def test_search_item_store_not_exist(client: TestClient):
    store_id = "65761879-19ec-45ac-8d3d-41b477bf134b"

    response = client.get(f"/api/stores/{store_id}/items?keyword=")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Store not found"
    }


def test_search_item_store_invalid_store_id_format(client: TestClient):
    store_id = "asldijfas>asdfj"

    response = client.get(f"/api/stores/{store_id}/items?keyword=")

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "store_id"],
                "msg": "value is not a valid uuid",
                "type": "type_error.uuid"
            }
        ]
    }


def test_search_item_store_id_empty(client: TestClient):
    store_id = ""

    response = client.get(f"/api/stores/{store_id}/items?keyword=")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }
