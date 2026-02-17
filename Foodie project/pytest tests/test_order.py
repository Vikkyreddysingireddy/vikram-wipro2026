import requests

def test_place_order(base_url):
    res = requests.post(f"{base_url}/api/v1/orders", json={
        "user_id": 1,
        "restaurant_id": 1,
        "dish": "Mutton Tikka"
    })
    assert res.status_code == 201


def test_give_rating(base_url):
    res = requests.post(f"{base_url}/api/v1/ratings", json={
        "order_id": 1,
        "rating": 5,
        "comment": "Excellent Taste!"
    })
    assert res.status_code == 201


def test_view_orders_by_restaurant(base_url):
    res = requests.get(f"{base_url}/api/v1/restaurants/1/orders")
    assert res.status_code == 200


def test_view_orders_by_user(base_url):
    res = requests.get(f"{base_url}/api/v1/users/1/orders")
    assert res.status_code == 200