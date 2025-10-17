import pytest
from source_to_mutate import *

def test_empty_list():
    assert incr_list([]) == []

def test_single_element_list():
    assert incr_list([5]) == [6]

def test_multiple_elements_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

def test_list_with_negative_numbers():
    assert incr_list([-1, 0, 1]) == [0, 1, 2]

def test_list_with_large_numbers():
    assert incr_list([1000, 2000, 3000]) == [1001, 2001, 3001]

def test_list_with_mixed_numbers():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

def test_list_with_duplicate_numbers():
    assert incr_list([1, 1, 1, 1]) == [2, 2, 2, 2]

def test_list_with_zero():
    assert incr_list([0]) == [1]