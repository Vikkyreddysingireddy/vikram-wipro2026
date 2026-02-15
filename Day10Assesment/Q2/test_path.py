from calculator import add, sub

def setup_module(module):
    print("\n[SETUP MODULE] test_math_operations")

def teardown_module(module):
    print("\n[TEARDOWN MODULE] test_math_operations")

def setup_function(function):
    print("\n[SETUP FUNCTION]")

def teardown_function(function):
    print("\n[TEARDOWN FUNCTION]")

def test_addition(sample_numbers, calculator_resource):
    a, b = sample_numbers
    assert add(a, b) == 15

def test_subtraction(sample_numbers):
    a, b = sample_numbers
    assert sub(a, b) == 5
