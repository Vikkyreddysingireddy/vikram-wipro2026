import time
from functools import wraps

def repeat(n):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                fn(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def greet():
    print("Hi")
greet()

def measure_and_print_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "_in_call"):
            wrapper._in_call = True
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"Function '{func.__name__}' executed in {end - start:.6f} seconds")
            del wrapper._in_call
            return result
        else:
            return func(*args, **kwargs)
    return wrapper


@measure_and_print_time
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)