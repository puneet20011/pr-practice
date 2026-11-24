"""Practice #27: digit sum and fast power (attempt 1)."""

def digit_sum(n):
    """Sum of digits, recursively."""
    return n if n < 10 else n % 10 + digit_sum(n // 10)


def fast_power(base, exp):
    """Exponentiation by squaring: O(log exp) multiplications."""
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    return half * half * (base if exp % 2 else 1)


if __name__ == "__main__":
    print(digit_sum(98048), fast_power(5, 12))
    assert digit_sum(98048) == sum(map(int, str(98048)))
    assert fast_power(5, 12) == 5 ** 12
