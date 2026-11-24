"""Practice #4: binary search (attempt 1)."""

def binary_search(sorted_items, target):
    """Return index of target in sorted_items, or -1. O(log n)."""
    lo, hi = 0, len(sorted_items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_items[mid] == target:
            return mid
        if sorted_items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    data = [1, 8, 16, 30, 47, 60, 69, 74, 75, 77, 80]
    print("index of", 74, "=", binary_search(data, 74))
    assert binary_search(data, 74) == data.index(74)
    assert binary_search(data, 1000) == -1
