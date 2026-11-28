"""Practice #64: binary search (attempt 3)."""

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
    data = [9, 10, 11, 32, 37, 49, 56, 61, 84, 95]
    print("index of", 32, "=", binary_search(data, 32))
    assert binary_search(data, 32) == data.index(32)
    assert binary_search(data, 1000) == -1
