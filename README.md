# CSC 223 Linked List Programming Project

Two-part Python project implementing a singly linked list ADT and a `SplitEvensOdds` subclass that moves **existing nodes** into stable even/odd lists.

## Files

- `singly_linked_list.py`: `Node`, `SinglyLinkedList`, core operations, list builders, `remove_all`, and nonrecursive reverse display.
- `split_evens_odds.py`: `SplitEvensOdds`, reference-only splitting, and identity/invariant tests.
- `stack.py`: reused from the earlier Stack project; reverse display imports this class.
- `main.py`: integrated demonstration and expected error messages.

## Running tests

Run with Python 3 in PyCharm or a terminal:

```bash
python stack.py
python singly_linked_list.py
python split_evens_odds.py
python main.py
```

The tests cover list order, insertion and removal, duplicates, missing-value errors, reverse display without mutation, all-even/all-odd/mixed/singleton/empty splits, preserved node identity, and head/tail/count invariants.

## Design notes

`append` and `prepend` take O(1) time. Searching and removing are O(n). `split_even_odd` is O(n) time and O(1) extra working space (excluding the two result-list objects). The split validates all values before modifying links, ensuring invalid input does not leave a partially split list.

No private information or credentials are used in tests. The project avoids unsafe evaluation of user input.
