"""Practice #1: bubble sort (attempt 1)."""

def bubble_sort(items):
    """Repeatedly swap adjacent out-of-order items. O(n^2)."""
    items = list(items)
    for end in range(len(items) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:  # already sorted, stop early
            break
    return items


if __name__ == "__main__":
    data = [29, 33, -15, 13, 45, 42, 31, 18]
    result = bubble_sort(data)
    print(data, "->", result)
    assert result == sorted(data)
