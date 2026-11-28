"""Practice #52: exception handling (attempt 2)."""

def parse_number(text):
    """Convert text to float, returning None when it is not a number."""
    try:
        return float(text)
    except ValueError:
        return None
    finally:
        pass  # finally always runs; useful for cleanup


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float("inf")


if __name__ == "__main__":
    for raw in ['3.5', '', '1e3', 'seven']:
        print(repr(raw), "->", parse_number(raw))
    assert parse_number("abc") is None
    assert safe_divide(1, 0) == float("inf")
