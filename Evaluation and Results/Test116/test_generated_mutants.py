import pytest
from source_to_mutate import sort_array

def test_empty_array():
    assert sort_array([]) == []

def test_single_element_array():
    assert sort_array([5]) == [5]

def test_positive_integers():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

def test_negative_integers():
    assert sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

def test_mixed_positive_and_negative_integers():
    assert sort_array([1, -2, 3, -4, 5]) == [-4, -2, 1, 3, 5]

def test_zero_and_positive_integers():
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]

def test_duplicate_integers():
    assert sort_array([1, 5, 2, 3, 4, 1, 2]) == [1, 1, 2, 2, 4, 3, 5]

def test_integers_with_same_number_of_ones():
    assert sort_array([3, 5, 7]) == [3, 5, 7]

def test_integers_with_different_number_of_ones():
    assert sort_array([1, 2, 4, 8]) == [1, 2, 4, 8]

def test_large_integers():
    assert sort_array([1023, 1024, 1025]) == [1024, 1025, 1023]

def test_negative_and_zero():
    assert sort_array([-1, 0]) == [0, -1]

def test_negative_with_same_number_of_ones():
    assert sort_array([-3, -5, -6]) == [-6, -5, -3]

def test_mixed_positive_negative_and_zero():
    assert sort_array([1, -1, 0]) == [0, -1, 1]

def test_all_zeros():
    assert sort_array([0, 0, 0]) == [0, 0, 0]

def test_large_negative_numbers():
    assert sort_array([-1023, -1024, -1025]) == [-1024, -1025, -1023]