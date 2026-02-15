import pytest

def add(a, b):
    return a + b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0),
    ]
)
@pytest.mark.smoke
def test_addition(a, b, expected):
    assert add(a, b) == expected


def test_environment(env):
    assert env in ["dev", "qa", "prod"]


@pytest.mark.skip(reason="Feature not ready")
def test_payment():
    assert True


@pytest.mark.xfail(reason="Known bug")
def test_known_bug():
    assert 2 * 2 == 5
