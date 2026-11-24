"""Practice #40: list/dict/set comprehensions (attempt 2)."""

if __name__ == "__main__":
    data = [6, 13, 29, -17, 4, 8, 30, -20, 12, 25]

    # list comprehension with a filter
    evens = [x for x in data if x % 2 == 0]
    # dict comprehension: value -> its square
    squares = {x: x * x for x in data}
    # set comprehension removes duplicates
    signs = {"neg" if x < 0 else "non-neg" for x in data}
    # generator expression: no intermediate list
    total = sum(x for x in data if x > 0)

    print("evens:", evens)
    print("squares:", squares)
    print("signs:", signs)
    print("sum of positives:", total)
    assert all(x % 2 == 0 for x in evens)
    assert total == sum(filter(lambda x: x > 0, data))
