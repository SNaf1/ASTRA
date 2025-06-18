import pytest
from source_to_mutate import add

def test_add_empty_list():
    assert add([]) == 0

def test_add_single_element():
    assert add([4]) == 0

def test_add_example_1():
    assert add([4, 2, 6, 7]) == 2

def test_add_all_even_at_odd_indices():
    assert add([1, 2, 3, 4, 5, 6]) == 12

def test_add_no_even_at_odd_indices():
    assert add([1, 1, 3, 1, 5, 1]) == 0

def test_add_all_odd_at_odd_indices():
    assert add([1, 3, 3, 5, 5, 7]) == 0

def test_add_even_at_even_indices():
    assert add([2, 1, 4, 3, 6, 5]) == 0

def test_add_negative_numbers():
    assert add([-1, -2, -3, -4]) == -6

def test_add_mixed_positive_and_negative():
    assert add([1, -2, 3, 4, -5, -6]) == -4

def test_add_large_numbers():
    assert add([1, 2000000000, 3, 4000000000]) == 6000000000