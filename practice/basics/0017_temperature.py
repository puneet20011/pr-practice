"""Practice #17: temperature conversion (attempt 1)."""

def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


if __name__ == "__main__":
    for c in [62, 90, 93, 42, 76]:
        f = c_to_f(c)
        print(f"{c}C = {f:.1f}F")
        assert abs(f_to_c(f) - c) < 1e-9
    assert c_to_f(100) == 212
