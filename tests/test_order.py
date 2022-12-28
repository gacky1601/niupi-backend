from fastapi.testclient import TestClient


def test_get_order_by_order_id(client: TestClient):
    order_id = "20221212ED43w2"

    response = client.get(f"/api/orders/{order_id}")

    assert response.status_code == 200
    assert response.json() == {
        'address': None,
        'items': [
            {
                'name': 'pain_marker',
                'photo_id': 'a41439ee-d3fb-4f52-b86c-624b659eb092',
                'price': 690,
                'quantity': 10
            },
            {
                'name': 'marker',
                'photo_id': 'c7e7db3b-a097-4fac-81d0-5f999ad33d86',
                'price': 500,
                'quantity': 5
            }
        ],
        'recipient': 'liang',
        'recipient_telephone_number': None,
        'shipping_fee': 20,
        'store_id': '49b2b69a-512c-4492-a5ea-50633893f8cc',
        'store_name': 'test',
        'sub_total': 10000,
        'total_amount': 10020,
    }


def test_get_order_by_order_id_invalid_order_id_format(client: TestClient):
    order_id = "AAAAAAAAAA2222"

    response = client.get(f"/api/orders/{order_id}")

    assert response.status_code == 422
    print(response.json())
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "order_id"],
                "msg": "value is not a valid format",
                "type": "type_error.uuid"
            }
        ]
    }


def test_get_order_by_order_id_order_id_not_found(client: TestClient):
    order_id = "20221225ED43w2"

    response = client.get(f"/api/orders/{order_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Order not found"
    }


def test_get_order_by_order_id_order_id_is_empty(client: TestClient):
    order_id = ""
    response = client.get(f"/api/orders/{order_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }
