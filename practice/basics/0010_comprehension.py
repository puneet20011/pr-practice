"""Practice #10: list/dict/set comprehensions (attempt 1)."""

if __name__ == "__main__":
    data = [39, 27, 14, -3, 3, -20, 23, 44, 39, -10]

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
