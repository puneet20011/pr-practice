"""Practice #15: two-sum with a hash map (attempt 1)."""

def two_sum(numbers, target):
    """Return indices of two numbers that add to target, using a hash map. O(n)."""
    seen = {}  # value -> index
    for i, value in enumerate(numbers):
        need = target - value
        if need in seen:
            return seen[need], i
        seen[value] = i
    return None


if __name__ == "__main__":
    numbers = [7, 40, 45, 49, 42, 34, 16, 18]
    pair = two_sum(numbers, 87)
    print("indices:", pair)
    assert pair is not None
    assert numbers[pair[0]] + numbers[pair[1]] == 87
