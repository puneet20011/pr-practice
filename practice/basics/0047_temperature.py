"""Practice #47: temperature conversion (attempt 2)."""

def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


if __name__ == "__main__":
    for c in [-11, 72, -20, 28, 102]:
        f = c_to_f(c)
        print(f"{c}C = {f:.1f}F")
        assert abs(f_to_c(f) - c) < 1e-9
    assert c_to_f(100) == 212
