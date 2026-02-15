import pytest

BASE_URL = "http://127.0.0.1:5001"

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def patient_data():
    return {
        "name": "Ram",
        "age": 30,
        "gender": "Male"
    }
