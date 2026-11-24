"""Practice #2: FizzBuzz with custom divisors (attempt 1)."""

def fizzbuzz(n, fizz=2, buzz=7):
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
    result = fizzbuzz(33)
    print(", ".join(result))
    assert result[2 - 1] == "Fizz"
    assert result[7 - 1] == "Buzz"
    assert len(result) == 33
