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
