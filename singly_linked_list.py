"""Singly linked list ADT with stack-based reverse display."""
from stack import Stack

class Node:
    """Store a value and next-node reference."""
    def __init__(self, data, next=None):
        self.data, self.next = data, next

class SinglyLinkedList:
    """Maintain head, tail, count, and forward links."""
    def __init__(self):
        self._head = self._tail = None
        self._count = 0

    def append(self, value):
        """Add a new tail in O(1)."""
        node = Node(value)
        if self._tail is None:
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._count += 1

    def prepend(self, value):
        """Add a new head in O(1)."""
        self._head = Node(value, self._head)
        if self._tail is None:
            self._tail = self._head
        self._count += 1

    def insert_after(self, existing_value, new_value):
        """Insert after first match; ValueError if missing."""
        current = self._head
        while current is not None and current.data != existing_value:
            current = current.next
        if current is None:
            raise ValueError(f"value not found: {existing_value!r}")
        new_node = Node(new_value, current.next)
        current.next = new_node
        if self._tail is current:
            self._tail = new_node
        self._count += 1

    def remove(self, value):
        """Remove first matching node; ValueError if missing."""
        previous, current = None, self._head
        while current is not None and current.data != value:
            previous, current = current, current.next
        if current is None:
            raise ValueError(f"value not found: {value!r}")
        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next
        if current is self._tail:
            self._tail = previous
        current.next = None
        self._count -= 1

    def contains(self, value):
        """Return whether value is present."""
        return any(item == value for item in self)

    def is_empty(self):
        return self._count == 0

    def __len__(self):
        return self._count

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self):
        return "Head -> " + (" -> ".join(map(str, self)) + " -> " if self._count else "") + "None"

    def _clear(self):
        self._head = self._tail = None
        self._count = 0

    def build_list_forward(self, values):
        """Replace list using append without changing input list."""
        if not isinstance(values, list):
            raise TypeError("values must be a Python list")
        self._clear()
        for value in values:
            self.append(value)

    def build_list_backward(self, values):
        """Replace list using prepend without changing input list."""
        if not isinstance(values, list):
            raise TypeError("values must be a Python list")
        self._clear()
        for value in values:
            self.prepend(value)

    def remove_all(self, value):
        """Remove all matching nodes and return removed count."""
        previous, current, removed = None, self._head, 0
        while current is not None:
            following = current.next
            if current.data == value:
                if previous is None:
                    self._head = following
                else:
                    previous.next = following
                if current is self._tail:
                    self._tail = previous
                current.next = None
                self._count -= 1
                removed += 1
            else:
                previous = current
            current = following
        return removed

    def display_reverse_nr(self):
        """Display values in reverse with imported Stack, preserving nodes."""
        stack = Stack()
        for value in self:
            stack.push(value)
        values = []
        while not stack.is_empty():
            values.append(str(stack.pop()))
        print("Head -> " + (" -> ".join(values) + " -> " if values else "") + "None")

def _node_ids(linked_list):
    result = []
    current = linked_list._head
    while current is not None:
        result.append(id(current))
        current = current.next
    return result

def _check_invariants(linked_list):
    ids = _node_ids(linked_list)
    assert len(ids) == len(linked_list)
    if not ids:
        assert linked_list._head is None and linked_list._tail is None
    else:
        assert linked_list._head is not None and linked_list._tail is not None
        assert linked_list._tail.next is None
        assert ids[-1] == id(linked_list._tail)

def module_tests():
    from contextlib import redirect_stdout
    from io import StringIO
    values = [10, 20, 30, 40, 50]
    linked = SinglyLinkedList()
    linked.build_list_forward(values)
    assert list(linked) == values and values == [10, 20, 30, 40, 50]
    linked.remove(10)
    linked.remove(50)
    linked.remove(30)
    assert list(linked) == [20, 40]
    linked.insert_after(40, 60)
    linked.prepend(5)
    linked.append(70)
    assert linked.contains(60) and not linked.contains(100)
    _check_invariants(linked)
    linked.build_list_backward(values)
    assert list(linked) == [50, 40, 30, 20, 10] and values == [10, 20, 30, 40, 50]
    ids = _node_ids(linked)
    output = StringIO()
    with redirect_stdout(output):
        linked.display_reverse_nr()
    assert output.getvalue().strip() == "Head -> 10 -> 20 -> 30 -> 40 -> 50 -> None"
    assert _node_ids(linked) == ids
    linked.build_list_forward([2, 2, 3, 2, 4, 2, 2])
    assert linked.remove_all(2) == 5 and list(linked) == [3, 4]
    assert linked.remove_all(99) == 0
    _check_invariants(linked)
    for operation in (lambda: linked.remove(99), lambda: linked.insert_after(99, 1)):
        try:
            operation()
        except ValueError:
            pass
        else:
            raise AssertionError("Expected ValueError")
    linked.build_list_forward([1])
    linked.remove(1)
    _check_invariants(linked)
    print("Singly linked list tests passed")

if __name__ == "__main__":
    module_tests()
