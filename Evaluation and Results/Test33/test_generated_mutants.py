import pytest
from source_to_mutate import sort_third

def test_empty_list():
    assert sort_third([]) == []

def test_single_element_list():
    assert sort_third([1]) == [1]

def test_list_with_one_element_divisible_by_three():
    assert sort_third([3]) == [3]

def test_list_with_multiple_elements_no_change():
    assert sort_third([1, 2, 3]) == [1, 2, 3]

def test_list_with_multiple_elements_with_change():
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

def test_list_with_all_elements_divisible_by_three():
    assert sort_third([9, 6, 3]) == [9, 6, 3]

def test_list_with_negative_numbers():
    assert sort_third([-1, -2, -3, -4, -5, -6]) == [-4, -2, -3, -1, -5, -6]

def test_list_with_mixed_positive_and_negative_numbers():
    assert sort_third([-1, 2, 3, 4, -5, 6]) == [-1, 2, 3, 4, -5, 6]

def test_list_with_duplicate_numbers():
    assert sort_third([1, 2, 1, 4, 5, 1]) == [1, 2, 1, 4, 5, 1]

def test_list_with_duplicate_numbers_divisible_by_three():
    assert sort_third([3, 2, 3, 4, 5, 3]) == [3, 2, 3, 4, 5, 3]

def test_longer_list():
    assert sort_third([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

def test_list_with_zeros():
    assert sort_third([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]

def test_list_with_only_zeros_divisible_by_three():
    assert sort_third([0, 1, 2, 0, 4, 5, 0]) == [0, 1, 2, 0, 4, 5, 0]

def test_list_with_mixed_zeros_and_numbers():
    assert sort_third([0, 1, 3, 4, 0, 6]) == [0, 1, 3, 4, 0, 6]

def test_list_with_large_numbers():
    assert sort_third([1000, 2, 3000, 4, 5000, 6]) == [4, 2, 3000, 1000, 5000, 6]

def test_list_with_identical_numbers_at_divisible_indices():
    assert sort_third([5, 1, 5, 7, 2, 5]) == [5, 1, 5, 7, 2, 5]