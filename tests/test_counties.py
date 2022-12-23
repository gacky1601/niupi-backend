from fastapi.testclient import TestClient


def test_get_county_ids(client: TestClient):
    response = client.get("/api/counties/ids")

    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "臺北市",
            "id": 0
        },
        {
            "name": "新北市",
            "id": 1
        },
        {
            "name": "基隆市",
            "id": 2
        },
        {
            "name": "桃園市",
            "id": 3
        },
        {
            "name": "新竹縣",
            "id": 4
        },
        {
            "name": "新竹市",
            "id": 5
        },
        {
            "name": "苗栗縣",
            "id": 6
        },
        {
            "name": "臺中市",
            "id": 7
        },
        {
            "name": "南投縣",
            "id": 8
        },
        {
            "name": "彰化縣",
            "id": 9
        },
        {
            "name": "雲林縣",
            "id": 10
        },
        {
            "name": "嘉義縣",
            "id": 11
        },
        {
            "name": "嘉義市",
            "id": 12
        },
        {
            "name": "臺南市",
            "id": 13
        },
        {
            "name": "高雄市",
            "id": 14
        },
        {
            "name": "屏東縣",
            "id": 15
        },
        {
            "name": "宜蘭縣",
            "id": 16
        },
        {
            "name": "花蓮縣",
            "id": 17
        },
        {
            "name": "臺東縣",
            "id": 18
        },
        {
            "name": "澎湖縣",
            "id": 19
        },
        {
            "name": "金門縣",
            "id": 20
        },
        {
            "name": "連江縣",
            "id": 21
        }
    ]
