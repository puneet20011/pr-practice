"""Practice #45: two-sum with a hash map (attempt 2)."""

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
    numbers = [27, 34, 35, 45, 8, 12, 25, 15]
    pair = two_sum(numbers, 35)
    print("indices:", pair)
    assert pair is not None
    assert numbers[pair[0]] + numbers[pair[1]] == 35
