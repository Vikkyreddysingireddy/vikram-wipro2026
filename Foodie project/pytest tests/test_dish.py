import requests


def test_add_dish(base_url, created_restaurant):
    res = requests.post(
        f"{base_url}/api/v1/restaurants/{created_restaurant}/dishes",
        json={
            "name": "Mutton Tikka",
            "price": 250
        }
    )
    assert res.status_code == 201


def test_update_dish(base_url, created_restaurant, created_dish):
    res = requests.put(
        f"{base_url}/api/v1/restaurants/{created_restaurant}/dishes/{created_dish}",
        json={"price": 300}
    )
    assert res.status_code == 200


def test_enable_disable_dish(base_url, created_restaurant, created_dish):
    res = requests.put(
        f"{base_url}/api/v1/restaurants/{created_restaurant}/dishes/{created_dish}/status",
        json={"enabled": False}
    )
    assert res.status_code == 200


def test_delete_dish(base_url, created_restaurant, created_dish):
    res = requests.delete(
        f"{base_url}/api/v1/restaurants/{created_restaurant}/dishes/{created_dish}"
    )
    assert res.status_code == 200