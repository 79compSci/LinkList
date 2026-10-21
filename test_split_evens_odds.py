import unittest
from singly_linked_list import _check_invariants, _node_ids
from split_evens_odds import SplitEvensOdds

class TestSplitEvensOdds(unittest.TestCase):
    def verify_split(self, values):
        source = SplitEvensOdds()
        source.build_list_forward(values)
        original_ids = _node_ids(source)
        even, odd = source.split_even_odd()
        self.assertEqual(list(even), [v for v in values if v % 2 == 0])
        self.assertEqual(list(odd), [v for v in values if v % 2])
        self.assertTrue(source.is_empty())
        result_ids = _node_ids(even) + _node_ids(odd)
        self.assertCountEqual(result_ids, original_ids)
        self.assertEqual(len(set(result_ids)), len(values))
        self.assertEqual(len(even) + len(odd), len(values))
        for item in (source, even, odd):
            _check_invariants(item)

    def test_mixed(self):
        self.verify_split([1, 2, 3, 4, 5, 6, 7, 8])

    def test_all_even(self):
        self.verify_split([2, 4, 6])

    def test_all_odd(self):
        self.verify_split([1, 3, 5])

    def test_single_even(self):
        self.verify_split([2])

    def test_single_odd(self):
        self.verify_split([3])

    def test_negative_and_zero(self):
        self.verify_split([0, -1, -2, 7])

    def test_empty_error(self):
        with self.assertRaises(ValueError):
            SplitEvensOdds().split_even_odd()

    def test_invalid_integer_input_preserves_source(self):
        source = SplitEvensOdds()
        source.build_list_forward([2, "bad", 3])
        with self.assertRaises(ValueError):
            source.split_even_odd()
        self.assertEqual(list(source), [2, "bad", 3])
        _check_invariants(source)

    def test_inherited_operations(self):
        source = SplitEvensOdds()
        source.append(2)
        source.prepend(1)
        source.insert_after(2, 3)
        self.assertEqual(list(source), [1, 2, 3])
        _check_invariants(source)

if __name__ == "__main__":
    unittest.main()
