"""Practice #53: generators (attempt 2)."""

def countdown(n):
    """A generator yields values lazily, one at a time."""
    while n > 0:
        yield n
        n -= 1


def evens_forever():
    n = 0
    while True:
        yield n
        n += 2


if __name__ == "__main__":
    print(list(countdown(9)))
    gen = evens_forever()
    first = [next(gen) for _ in range(9)]
    print(first)
    assert list(countdown(9)) == list(range(9, 0, -1))
    assert first == list(range(0, 2 * 9, 2))
