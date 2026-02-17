import requests

def test_register_restaurant(base_url):
    res = requests.post(f"{base_url}/api/v1/restaurants", json={
        "name": "Sattibabu Biryani",
        "category": "Veg/Non - Veg",
        "location": "Hyderabad",
        "contact": "11223344556"
    })
    assert res.status_code == 201


def test_update_restaurant(base_url):
    res = requests.put(f"{base_url}/api/v1/restaurants/1", json={
        "location": "Bangalore"
    })
    assert res.status_code == 200


def test_disable_restaurant(base_url):
    res = requests.put(f"{base_url}/api/v1/restaurants/1/disable")
    assert res.status_code == 200


def test_view_restaurant_profile(base_url):
    res = requests.get(f"{base_url}/api/v1/restaurants/1")
    assert res.status_code == 200