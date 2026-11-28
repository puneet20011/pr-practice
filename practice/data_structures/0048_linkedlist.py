"""Practice #48: linked list reversal (attempt 2)."""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


def reverse(head):
    """Reverse a singly linked list in place."""
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


if __name__ == "__main__":
    values = [12, 3, 14, 18, 15, 19]
    print(to_list(reverse(build(values))))
    assert to_list(reverse(build(values))) == values[::-1]
