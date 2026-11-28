"""Practice #63: palindrome check (attempt 3)."""

def is_palindrome(text):
    """Two-pointer check, ignoring case and non-letters."""
    chars = [c.lower() for c in text if c.isalnum()]
    left, right = 0, len(chars) - 1
    while left < right:
        if chars[left] != chars[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    for word in ['civic', 'python', 'madam', 'stack', 'kayak']:
        print(word, is_palindrome(word))
        assert is_palindrome(word) == (word == word[::-1])
    assert is_palindrome("A man, a plan, a canal: Panama")
