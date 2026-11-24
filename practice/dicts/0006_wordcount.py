"""Practice #6: word frequency count (attempt 1)."""

from collections import Counter


def word_frequencies(sentence):
    """Count words with a plain dict."""
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    sentence = 'a stack is last in first out and a queue is first in first out'
    freq = word_frequencies(sentence)
    top = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:3]
    print("top words:", top)
    assert freq == dict(Counter(sentence.split()))
