"""Practice #34: binary search (attempt 2)."""

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
    data = [21, 23, 29, 35, 61, 67, 68, 73, 78, 80, 83]
    print("index of", 78, "=", binary_search(data, 78))
    assert binary_search(data, 78) == data.index(78)
    assert binary_search(data, 1000) == -1
