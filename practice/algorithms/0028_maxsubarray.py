"""Practice #28: Kadane's max subarray (attempt 1)."""

def max_subarray(numbers):
    """Kadane's algorithm: largest sum of a contiguous slice. O(n)."""
    best = current = numbers[0]
    for x in numbers[1:]:
        current = max(x, current + x)
        best = max(best, current)
    return best


def brute_force(numbers):
    return max(sum(numbers[i:j]) for i in range(len(numbers)) for j in range(i + 1, len(numbers) + 1))


if __name__ == "__main__":
    data = [5, 0, 7, -7, 15, -6, -9, -13, -13, -7]
    print("max subarray sum:", max_subarray(data))
    assert max_subarray(data) == brute_force(data)
