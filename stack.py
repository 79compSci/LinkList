"""Reusable last-in, first-out stack abstract data type."""


class Stack:
    """A LIFO collection backed by a private Python list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item; raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("cannot pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it; raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("cannot peek at an empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack has no items."""
        return not self._items

    def size(self):
        """Return the number of items."""
        return len(self._items)


if __name__ == "__main__":
    stack = Stack()
    assert stack.is_empty()
    for value in (10, 20, 30):
        stack.push(value)
    assert stack.peek() == 30 and stack.size() == 3
    assert [stack.pop(), stack.pop(), stack.pop()] == [30, 20, 10]
    assert stack.is_empty()
    for method in (stack.pop, stack.peek):
        try:
            method()
        except IndexError:
            pass
        else:
            raise AssertionError("Expected IndexError")
    print("Stack tests passed")
