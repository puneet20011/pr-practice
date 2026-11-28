"""Practice #50: GCD and LCM (attempt 2)."""

import math


def gcd(a, b):
    """Euclid's algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == "__main__":
    a, b = 46, 188
    print(f"gcd={gcd(a, b)} lcm={lcm(a, b)}")
    assert gcd(a, b) == math.gcd(a, b)
    assert lcm(a, b) % a == 0 and lcm(a, b) % b == 0
