"""Practice #12: merge sort (attempt 1)."""

def merge_sort(items):
    """Divide in half, sort each half, merge. O(n log n)."""
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left, right = merge_sort(items[:mid]), merge_sort(items[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    return merged + left[i:] + right[j:]


if __name__ == "__main__":
    data = [37, 39, 37, 45, 4, 3, 45, 40, 3, -8]
    result = merge_sort(data)
    print(data, "->", result)
    assert result == sorted(data)
