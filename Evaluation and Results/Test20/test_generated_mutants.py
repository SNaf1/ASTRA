import pytest
from source_to_mutate import find_closest_elements
from typing import List, Tuple

def test_basic_example():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

def test_same_numbers():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

def test_negative_numbers():
    assert find_closest_elements([-1.0, -2.0, -3.0, -4.0, -5.0, -2.2]) == (-2.2, -2.0)

def test_mixed_numbers():
    assert find_closest_elements([-1.0, 2.0, -3.0, 4.0, -5.0, 2.2]) == (2.0, 2.2)

def test_large_numbers():
    assert find_closest_elements([1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 2000.2]) == (2000.0, 2000.2)

def test_small_numbers():
    assert find_closest_elements([0.001, 0.002, 0.003, 0.004, 0.005, 0.0022]) == (0.002, 0.0022)

def test_two_numbers():
    assert find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

def test_three_numbers():
    assert find_closest_elements([1.0, 2.0, 1.1]) == (1.0, 1.1)

def test_duplicate_closest():
    assert find_closest_elements([1.0, 2.0, 2.0, 3.0]) == (2.0, 2.0)

def test_all_same():
    assert find_closest_elements([2.0, 2.0, 2.0, 2.0]) == (2.0, 2.0)

def test_negative_and_positive():
    assert find_closest_elements([-1.0, 1.0, 2.0]) == (1.0, 2.0)

def test_zero_values():
    assert find_closest_elements([0.0, 1.0, 0.1]) == (0.0, 0.1)

def test_large_and_small():
    assert find_closest_elements([1000.0, 0.001, 1000.1]) == (1000.0, 1000.1)

def test_identical_numbers():
    assert find_closest_elements([5.0, 5.0]) == (5.0, 5.0)