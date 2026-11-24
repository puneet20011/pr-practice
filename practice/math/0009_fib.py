"""Practice #9: Fibonacci with memoization (attempt 1)."""

from functools import lru_cache


@lru_cache(maxsize=None)
def fib_memo(n):
    """Recursive Fibonacci, made fast with memoization."""
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)


def fib_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    n = 17
    print(f"fib({n}) =", fib_loop(n))
    assert fib_memo(n) == fib_loop(n)
