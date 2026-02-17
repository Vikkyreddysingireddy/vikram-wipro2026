import requests

def test_user_registration(base_url):
    res = requests.post(f"{base_url}/api/v1/users/register", json={
        "name": "Chintu",
        "email": "Chintu@gmail.com",
        "password": "121212121212"
    })
    assert res.status_code == 201


def test_search_restaurants(base_url):
    res = requests.get(f"{base_url}/api/v1/restaurants/search?name=Food")
    assert res.status_code == 200