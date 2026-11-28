"""Practice #55: decorators (attempt 2)."""

import functools


def count_calls(func):
    """Decorator that counts how often a function is called."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


@count_calls
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    for i in range(4):
        greet(f"user{i}")
    print("greet was called", greet.calls, "times")
    assert greet.calls == 4
    assert greet.__name__ == "greet"  # thanks to functools.wraps
