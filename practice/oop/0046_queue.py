"""Practice #46: Queue class (attempt 2)."""

from collections import deque


class Queue:
    """First-in, first-out queue backed by deque (O(1) at both ends)."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.popleft()

    def __len__(self):
        return len(self._items)


if __name__ == "__main__":
    q = Queue()
    for x in [5, 7, 8, 5, 2, 5]:
        q.enqueue(x)
    order = [q.dequeue() for _ in range(len(q))]
    print("served in order:", order)
    assert order == [5, 7, 8, 5, 2, 5]
