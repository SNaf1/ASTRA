import pytest
from source_to_mutate import largest_smallest_integers

def test_empty_list():
    assert largest_smallest_integers([]) == (None, None)

def test_no_positive_integers():
    assert largest_smallest_integers([-2, -4, -1, -3, -5, -7]) == (-1, None)

def test_no_negative_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)

def test_mixed_integers():
    assert largest_smallest_integers([2, -4, 1, -3, 5, -7]) == (-3, 1)

def test_only_zero():
    assert largest_smallest_integers([0]) == (None, None)

def test_mixed_with_zero():
    assert largest_smallest_integers([2, -4, 0, -3, 5, -7]) == (-3, 2)

def test_all_negative():
    assert largest_smallest_integers([-1, -2, -3]) == (-1, None)

def test_all_positive():
    assert largest_smallest_integers([1, 2, 3]) == (None, 1)

def test_single_positive():
    assert largest_smallest_integers([1]) == (None, 1)

def test_single_negative():
    assert largest_smallest_integers([-1]) == (-1, None)

def test_duplicate_positive():
    assert largest_smallest_integers([1, 1, 1]) == (None, 1)

def test_duplicate_negative():
    assert largest_smallest_integers([-1, -1, -1]) == (-1, None)

def test_large_numbers():
    assert largest_smallest_integers([1000, -1000, 500, -500]) == (-500, 500)

def test_negative_zero_positive():
    assert largest_smallest_integers([-1, 0, 1]) == (-1, 1)

def test_multiple_negatives_and_positives():
    assert largest_smallest_integers([-5, 2, -1, 4, -8, 1]) == (-1, 1)

def test_same_magnitude_positive_negative():
    assert largest_smallest_integers([-5, 5]) == (-5, 5)

def test_large_list_mixed():
    test_list = list(range(-100, 101))
    assert largest_smallest_integers(test_list) == (-1, 1)