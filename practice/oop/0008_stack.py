"""Practice #8: Stack class + bracket matching (attempt 1)."""

class Stack:
    """Last-in, first-out container built on a Python list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def is_empty(self):
        return not self._items


def balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    for ch in text:
        if ch in "([{":
            stack.push(ch)
        elif ch in pairs:
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    expr = '((x)'
    print(expr, "balanced?", balanced(expr))
    assert balanced(expr) is False
