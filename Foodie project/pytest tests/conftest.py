import pytest
import requests
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from appmodules import storage

BASE = "http://127.0.0.1:2700"


@pytest.fixture(scope="function", autouse=True)
def reset_app_state():
    storage.reset_storage()


@pytest.fixture(scope="function")
def base_url():
    return BASE


@pytest.fixture(scope="function")
def created_restaurant(base_url):
    res = requests.post(f"{base_url}/api/v1/restaurants", json={
        "name": "Sattibabu Biryani",
        "category": "Veg/Non - Veg",
        "location": "Hyderabad",
        "contact": "11223344556"
    })
    assert res.status_code == 201
    return res.json()["id"]


@pytest.fixture(scope="function")
def created_dish(base_url, created_restaurant):
    res = requests.post(
        f"{base_url}/api/v1/restaurants/{created_restaurant}/dishes",
        json={
            "name": "Mutton Tikka",
            "price": 250
        }
    )
    assert res.status_code == 201
    return res.json()["id"]