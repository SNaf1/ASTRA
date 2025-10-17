import pytest
from source_to_mutate import max_element

def test_empty_list():
    with pytest.raises(IndexError):
        max_element([])

def test_single_element():
    assert max_element([5]) == 5

def test_positive_numbers():
    assert max_element([1, 2, 3]) == 3

def test_negative_numbers():
    assert max_element([-1, -2, -3]) == -1

def test_mixed_numbers():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

def test_duplicate_max():
    assert max_element([1, 5, 2, 5, 3]) == 5

def test_all_same():
    assert max_element([7, 7, 7, 7]) == 7

def test_large_numbers():
    assert max_element([1000000, 2000000, 500000]) == 2000000

def test_negative_and_zero():
    assert max_element([-1, -2, 0]) == 0

def test_zero_only():
    assert max_element([0, 0, 0]) == 0