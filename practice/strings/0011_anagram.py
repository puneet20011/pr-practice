"""Practice #11: anagram check (attempt 1)."""

def is_anagram(a, b):
    """Two words are anagrams if they use the same letters the same number of times."""
    if len(a) != len(b):
        return False
    counts = {}
    for ch in a:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in b:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True


if __name__ == "__main__":
    for a, b in [('listen', 'silent'), ('state', 'taste'), ('cat', 'act')]:
        print(a, b, is_anagram(a, b))
        assert is_anagram(a, b)
    assert not is_anagram("hello", "world")
