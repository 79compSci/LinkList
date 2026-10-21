import unittest
from io import StringIO
from contextlib import redirect_stdout
from singly_linked_list import SinglyLinkedList, _check_invariants

class TestSinglyLinkedList(unittest.TestCase):
    def test_append_prepend(self):
        a = SinglyLinkedList()
        self.assertTrue(a.is_empty())
        a.append(2)
        a.prepend(1)
        a.append(3)
        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(len(a), 3)
        self.assertTrue(a.contains(2))
        self.assertFalse(a.contains(9))
        _check_invariants(a)

    def test_build_forward_backward(self):
        original = [10, 20, 30, 40, 50]
        a = SinglyLinkedList()
        a.build_list_forward(original)
        self.assertEqual(list(a), original)
        _check_invariants(a)
        a.build_list_backward(original)
        self.assertEqual(list(a), original[::-1])
        self.assertEqual(original, [10, 20, 30, 40, 50])
        _check_invariants(a)

    def test_insert_after(self):
        a = SinglyLinkedList()
        a.build_list_forward([1, 3])
        a.insert_after(1, 2)
        a.insert_after(3, 4)
        self.assertEqual(list(a), [1, 2, 3, 4])
        _check_invariants(a)
        with self.assertRaises(ValueError):
            a.insert_after(99, 5)

    def test_remove_positions(self):
        a = SinglyLinkedList()
        a.build_list_forward([1, 2, 3, 4])
        a.remove(1)
        a.remove(3)
        a.remove(4)
        self.assertEqual(list(a), [2])
        _check_invariants(a)
        a.remove(2)
        self.assertTrue(a.is_empty())
        _check_invariants(a)
        with self.assertRaises(ValueError):
            a.remove(9)

    def test_remove_all(self):
        a = SinglyLinkedList()
        a.build_list_forward([5, 5, 1, 5, 2, 5, 5])
        self.assertEqual(a.remove_all(5), 5)
        self.assertEqual(list(a), [1, 2])
        self.assertEqual(a.remove_all(9), 0)
        _check_invariants(a)

    def test_reverse_display_preserves_nodes(self):
        a = SinglyLinkedList()
        a.build_list_forward([10, 20, 30])
        before = a._head
        output = StringIO()
        with redirect_stdout(output):
            a.display_reverse_nr()
        self.assertEqual(output.getvalue().strip(), "Head -> 30 -> 20 -> 10 -> None")
        self.assertIs(a._head, before)
        self.assertEqual(list(a), [10, 20, 30])
        _check_invariants(a)

if __name__ == "__main__":
    unittest.main()
