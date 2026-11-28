"""Practice #66: word frequency count (attempt 3)."""

from collections import Counter


def word_frequencies(sentence):
    """Count words with a plain dict."""
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    sentence = 'data structures and algorithms are the building blocks of code'
    freq = word_frequencies(sentence)
    top = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:3]
    print("top words:", top)
    assert freq == dict(Counter(sentence.split()))
