"""Practice #42: merge sort (attempt 2)."""

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
    data = [28, 22, 9, 1, 29, 16, 50, 15, 29, -19]
    result = merge_sort(data)
    print(data, "->", result)
    assert result == sorted(data)
