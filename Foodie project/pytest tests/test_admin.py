import requests

def test_approve_restaurant(base_url, created_restaurant):
    res = requests.put(
        f"{base_url}/api/v1/admin/restaurants/{created_restaurant}/approve"
    )
    assert res.status_code == 200


def test_admin_disable_restaurant(base_url, created_restaurant):
    res = requests.put(f"{base_url}/api/v1/admin/restaurants/{created_restaurant}/disable")
    assert res.status_code == 200


def test_view_feedback(base_url):
    res = requests.get(f"{base_url}/api/v1/admin/feedback")
    assert res.status_code == 200


def test_view_orders_status(base_url):
    res = requests.get(f"{base_url}/api/v1/admin/orders")
    assert res.status_code == 200