import pytest
from calculator import divide
def test_division(sample_number, calculator_resource):
    a,b = sample_number
    assert divide(a,b) == 2

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(2,0)