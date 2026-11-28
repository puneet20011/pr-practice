"""Practice #62: FizzBuzz with custom divisors (attempt 3)."""

def fizzbuzz(n, fizz=3, buzz=7):
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
    result = fizzbuzz(20)
    print(", ".join(result))
    assert result[3 - 1] == "Fizz"
    assert result[7 - 1] == "Buzz"
    assert len(result) == 20
