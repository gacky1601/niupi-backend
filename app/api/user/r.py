import requests

user_id = "0df1dacb-67f6-495c-b993-49d06a293765"
json = {
        "email": "test@gmail.com",
        "username": "test",
        "address": None,
        "cellphone_number": None,
    }
a = requests.patch(f"http://127.0.0.1:8000/api/user/{user_id}", json=json)
print( a.status_code )
print()
print(a.json())