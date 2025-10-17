import pytest
from source_to_mutate import *

def test_empty_list():
    assert rolling_max([]) == []

def test_single_element_list():
    assert rolling_max([5]) == [5]

def test_increasing_sequence():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_decreasing_sequence():
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

def test_mixed_sequence():
    assert rolling_max([1, 3, 2, 4, 5, 3, 2]) == [1, 3, 3, 4, 5, 5, 5]

def test_duplicate_values():
    assert rolling_max([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]

def test_negative_numbers():
    assert rolling_max([-1, -2, -3, -4, -5]) == [-1, -1, -1, -1, -1]

def test_mixed_positive_and_negative():
    assert rolling_max([-1, 2, -3, 4, -5]) == [-1, 2, 2, 4, 4]

def test_zero_values():
    assert rolling_max([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

def test_large_numbers():
    assert rolling_max([1000, 500, 1500, 2000]) == [1000, 1000, 1500, 2000]

def test_decimal_numbers():
    assert rolling_max([1.5, 2.5, 1.0, 3.0]) == [1.5, 2.5, 2.5, 3.0]

def test_mixed_integer_and_decimal():
    assert rolling_max([1, 2.5, 3, 1.5]) == [1, 2.5, 3, 3]