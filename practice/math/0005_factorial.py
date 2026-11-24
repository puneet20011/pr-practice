"""Practice #5: factorial (iterative vs recursive) (attempt 1)."""

import math


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    return 1 if n <= 1 else n * factorial_recursive(n - 1)


if __name__ == "__main__":
    n = 8
    print(f"{n}! =", factorial_iterative(n))
    assert factorial_iterative(n) == factorial_recursive(n) == math.factorial(n)
