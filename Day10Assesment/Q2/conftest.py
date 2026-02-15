import pytest

@pytest.fixture(scope="function")
def numbers():
    return 2, 3

@pytest.fixture(scope="module")
def calculator_resource():
    print("[SETUP] Calculator Resource Created")
    yield
    print("[SETUP] Calculator Resource Closed")
