"""Demonstrate linked-list operations and inherited even/odd splitting."""
from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds

def main():
    linked = SinglyLinkedList()
    linked.build_list_forward([10, 20, 30, 40, 50])
    print("Forward:", linked)
    linked.display_reverse_nr()
    linked.build_list_backward([10, 20, 30, 40, 50])
    print("Backward:", linked)
    linked.insert_after(30, 35)
    linked.remove(50)
    print("After insertion/removal:", linked)
    linked.build_list_forward([2, 2, 3, 2, 4, 2, 5, 2])
    print("Removed:", linked.remove_all(2), "Remaining:", linked)
    try:
        linked.remove(99)
    except ValueError as exc:
        print("Expected error:", exc)

    source = SplitEvensOdds()
    source.build_list_forward([1, 2, 3, 4, 5, 6, 7, 8])
    print("Before split:", source)
    evens, odds = source.split_even_odd()
    print("Evens:", evens)
    print("Odds:", odds)
    print("Original:", source)
    evens.append(10)
    print("Evens after inherited append:", evens)
    try:
        source.split_even_odd()
    except ValueError as exc:
        print("Expected error:", exc)

if __name__ == "__main__":
    main()
