import pytest
from source_to_mutate import sort_array

def test_empty_array():
    assert sort_array([]) == []

def test_single_element_array():
    assert sort_array([5]) == [5]

def test_ascending_sort():
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

def test_descending_sort():
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

def test_array_with_same_elements_ascending():
    assert sort_array([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_array_with_same_elements_descending():
    assert sort_array([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]

def test_array_already_sorted_ascending():
    assert sort_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

def test_array_already_sorted_descending():
    assert sort_array([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]

def test_array_with_zeros_ascending():
    assert sort_array([0, 2, 4, 1, 3]) == [0, 1, 2, 3, 4]

def test_array_with_zeros_descending():
    assert sort_array([0, 2, 4, 1, 3, 5]) == [0, 1, 2, 3, 4, 5]

def test_array_with_negative_numbers_ascending():
    assert sort_array([1, 2, 3, 4, -1]) == [4, 3, 2, 1, -1]

def test_array_with_negative_numbers_descending():
    assert sort_array([1, 2, 3, 4, -2]) == [-2, 1, 2, 3, 4]

def test_array_with_mixed_positive_and_negative_numbers_ascending():
    assert sort_array([-2, 1, -1, 0, 2]) == [2, 1, 0, -1, -2]

def test_array_with_mixed_positive_and_negative_numbers_descending():
    assert sort_array([-2, 1, -1, 0, 2, 3]) == [-2, -1, 0, 1, 2, 3]

def test_array_with_large_numbers_ascending():
    assert sort_array([1000, 1, 500, 2, 750]) == [1000, 750, 500, 2, 1]

def test_array_with_large_numbers_descending():
    assert sort_array([1000, 1, 500, 2, 750, 3]) == [1, 2, 3, 500, 750, 1000]

def test_array_with_duplicate_values_ascending():
    assert sort_array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

def test_array_with_duplicate_values_descending():
    assert sort_array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0]) == [0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]