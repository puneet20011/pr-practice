"""Practice #19: quick sort (attempt 1)."""

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
    data = [3, -5, 37, 22, 10, 5, 42, 43, 3, 41]
    result = quick_sort(data)
    print(data, "->", result)
    assert result == sorted(data)
