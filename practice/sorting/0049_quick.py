"""Practice #49: quick sort (attempt 2)."""

def quick_sort(items):
    """Pick a pivot, partition into smaller/equal/larger, recurse."""
    if len(items) <= 1:
        return list(items)
    pivot = items[len(items) // 2]
    smaller = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    larger = [x for x in items if x > pivot]
    return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == "__main__":
    data = [50, 20, -4, 48, 18, 44, 4, 35, 1, -1]
    result = quick_sort(data)
    print(data, "->", result)
    assert result == sorted(data)
