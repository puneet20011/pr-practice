"""Practice #20: GCD and LCM (attempt 1)."""

import math


def gcd(a, b):
    """Euclid's algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == "__main__":
    a, b = 358, 34
    print(f"gcd={gcd(a, b)} lcm={lcm(a, b)}")
    assert gcd(a, b) == math.gcd(a, b)
    assert lcm(a, b) % a == 0 and lcm(a, b) % b == 0
