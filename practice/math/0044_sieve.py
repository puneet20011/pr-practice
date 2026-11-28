"""Practice #44: Sieve of Eratosthenes (attempt 2)."""

def sieve(limit):
    """Sieve of Eratosthenes: all primes <= limit."""
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return [i for i, ok in enumerate(is_prime) if ok]


def is_prime_slow(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


if __name__ == "__main__":
    primes = sieve(39)
    print(primes)
    assert primes == [i for i in range(39 + 1) if is_prime_slow(i)]
