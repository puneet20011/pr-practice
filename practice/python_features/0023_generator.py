"""Practice #23: generators (attempt 1)."""

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
    print(list(countdown(7)))
    gen = evens_forever()
    first = [next(gen) for _ in range(7)]
    print(first)
    assert list(countdown(7)) == list(range(7, 0, -1))
    assert first == list(range(0, 2 * 7, 2))
