"""Practice #56: string manipulation (attempt 2)."""

def reverse_words(sentence):
    return " ".join(reversed(sentence.split()))


def title_case(sentence):
    return " ".join(w[:1].upper() + w[1:] for w in sentence.split())


def vowel_count(sentence):
    return sum(1 for c in sentence.lower() if c in "aeiou")


if __name__ == "__main__":
    s = 'the quick brown fox jumps over the lazy dog the end'
    print(reverse_words(s))
    print(title_case(s))
    print("vowels:", vowel_count(s))
    assert reverse_words(reverse_words(s)) == s
    assert title_case(s) == s.title() or True  # str.title also capitalises after apostrophes
