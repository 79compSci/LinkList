"""Split a singly linked list by relinking existing nodes only."""
from singly_linked_list import SinglyLinkedList, _check_invariants, _node_ids

class SplitEvensOdds(SinglyLinkedList):
    """Linked list with a stable, destructive parity split."""

    def split_even_odd(self):
        """Return (even, odd) lists containing original nodes; empty source.

        Raise ValueError for an empty list or non-integer values.
        """
        if self.is_empty():
            raise ValueError("cannot split an empty source list")
        if not all(type(value) is int for value in self):
            raise ValueError("split requires integer values")
        evens, odds = SinglyLinkedList(), SinglyLinkedList()
        current = self._head
        while current is not None:
            following = current.next
            current.next = None
            target = evens if current.data % 2 == 0 else odds
            if target._tail is None:
                target._head = current
            else:
                target._tail.next = current
            target._tail = current
            target._count += 1
            current = following
        self._head = self._tail = None
        self._count = 0
        return evens, odds

def module_tests():
    cases = ([1, 2, 3, 4, 5, 6, 7, 8], [2, 4, 6], [1, 3, 5],
             [2], [3], [0, -1, -2, 7])
    for values in cases:
        source = SplitEvensOdds()
        source.build_list_forward(list(values))
        original_ids = _node_ids(source)
        even, odd = source.split_even_odd()
        assert list(even) == [v for v in values if v % 2 == 0]
        assert list(odd) == [v for v in values if v % 2 != 0]
        assert set(_node_ids(even)) | set(_node_ids(odd)) == set(original_ids)
        assert set(_node_ids(even)).isdisjoint(_node_ids(odd))
        assert len(even) + len(odd) == len(original_ids)
        for item in (source, even, odd):
            _check_invariants(item)
        assert source.is_empty()
    try:
        SplitEvensOdds().split_even_odd()
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for empty list")
    invalid = SplitEvensOdds()
    invalid.build_list_forward([2, "oops", 3])
    try:
        invalid.split_even_odd()
    except ValueError:
        assert list(invalid) == [2, "oops", 3]
    else:
        raise AssertionError("Expected ValueError for non-integer")
    print("Split evens/odds tests passed")

if __name__ == "__main__":
    module_tests()
