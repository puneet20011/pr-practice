"""Practice #32: FizzBuzz with custom divisors (attempt 2)."""

def fizzbuzz(n, fizz=3, buzz=5):
    """FizzBuzz with configurable divisors."""
    out = []
    for i in range(1, n + 1):
        word = ""
        if i % fizz == 0:
            word += "Fizz"
        if i % buzz == 0:
            word += "Buzz"
        out.append(word or str(i))
    return out


if __name__ == "__main__":
    result = fizzbuzz(30)
    print(", ".join(result))
    assert result[3 - 1] == "Fizz"
    assert result[5 - 1] == "Buzz"
    assert len(result) == 30
