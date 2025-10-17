import pytest
from source_to_mutate import unique

def test_empty_list():
    assert unique([]) == []

def test_single_element_list():
    assert unique([5]) == [5]

def test_multiple_elements_list():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

def test_list_with_duplicates():
    assert unique([1, 2, 2, 3, 3, 3]) == [1, 2, 3]

def test_list_with_negative_numbers():
    assert unique([-1, 0, 1, -1, 0]) == [-1, 0, 1]

def test_list_with_mixed_numbers():
    assert unique([-5, 0, 5, -10, 10]) == [-10, -5, 0, 5, 10]

def test_list_with_same_element():
    assert unique([7, 7, 7, 7, 7]) == [7]

def test_list_already_sorted():
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_list_reverse_sorted():
    assert unique([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_list_with_zero():
    assert unique([0, 0, 0, 0]) == [0]

def test_list_with_large_numbers():
    assert unique([1000, 2000, 1000, 3000]) == [1000, 2000, 3000]