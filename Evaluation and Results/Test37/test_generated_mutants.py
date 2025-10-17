import pytest
from source_to_mutate import sort_even

def test_empty_list():
    assert sort_even([]) == []

def test_single_element_list():
    assert sort_even([1]) == [1]

def test_two_element_list():
    assert sort_even([1, 2]) == [1, 2]

def test_three_element_list():
    assert sort_even([1, 2, 3]) == [1, 2, 3]

def test_four_element_list():
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

def test_five_element_list():
    assert sort_even([5, 6, 3, 4, 1]) == [1, 6, 3, 4, 5]

def test_already_sorted():
    assert sort_even([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    assert sort_even([5, 4, 3, 2, 1]) == [1, 4, 3, 2, 5]

def test_duplicate_even_numbers():
    assert sort_even([2, 1, 2, 3, 2]) == [2, 1, 2, 3, 2]

def test_duplicate_odd_numbers():
    assert sort_even([1, 2, 1, 2, 1]) == [1, 2, 1, 2, 1]

def test_negative_numbers():
    assert sort_even([-1, 2, -3, 4, -5]) == [-5, 2, -3, 4, -1]

def test_mixed_positive_negative_numbers():
    assert sort_even([1, -2, -3, 4, 5]) == [-3, -2, 1, 4, 5]

def test_zero_in_list():
    assert sort_even([0, 1, 2, 3, 4]) == [0, 1, 2, 3, 4]

def test_all_even_indices_same():
    assert sort_even([2, 1, 2, 3, 2]) == [2, 1, 2, 3, 2]

def test_all_odd_indices_same():
    assert sort_even([1, 2, 3, 2, 5]) == [1, 2, 3, 2, 5]

def test_long_list():
    assert sort_even([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def test_list_with_floats():
    assert sort_even([1.0, 2, 3.0, 4]) == [1.0, 2, 3.0, 4]

def test_list_with_mixed_types():
    assert sort_even([1, 'a', 3, 'b']) == [1, 'a', 3, 'b']

def test_list_with_only_even_indices():
    assert sort_even([1, 3, 5]) == [1, 3, 5]