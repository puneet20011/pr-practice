"""Practice #67: insertion sort (attempt 3)."""

def insertion_sort(items):
    """Grow a sorted prefix, inserting each new item into place. O(n^2)."""
    items = list(items)
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
    return items


if __name__ == "__main__":
    data = [-11, 19, 35, 11, 37, 17, 12, -8]
    result = insertion_sort(data)
    print(data, "->", result)
    assert result == sorted(data)
