"""Practice #24: matrix multiply (attempt 1)."""

def transpose(m):
    return [list(row) for row in zip(*m)]


def multiply(a, b):
    """Matrix product using list comprehensions."""
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


if __name__ == "__main__":
    a = [[9, 8, -4], [-5, 4, -1], [1, 1, 3]]
    for row in multiply(a, a):
        print(row)
    assert multiply(a, identity(len(a))) == a
    assert transpose(transpose(a)) == a
