import pytest
from source_to_mutate import monotonic, METADATA

def test_monotonic_increasing():
    assert monotonic([1, 2, 4, 20]) == True

def test_monotonic_decreasing():
    assert monotonic([4, 1, 0, -10]) == True

def test_monotonic_non_monotonic():
    assert monotonic([1, 20, 4, 10]) == False

def test_monotonic_empty_list():
    assert monotonic([]) == True

def test_monotonic_single_element():
    assert monotonic([5]) == True

def test_monotonic_equal_elements_increasing():
    assert monotonic([1, 1, 1, 1]) == True

def test_monotonic_equal_elements_decreasing():
    assert monotonic([5, 5, 5, 5]) == True

def test_monotonic_mixed_equal_and_increasing():
    assert monotonic([1, 1, 2, 3]) == True

def test_monotonic_mixed_equal_and_decreasing():
    assert monotonic([5, 5, 4, 3]) == True

def test_monotonic_negative_numbers_increasing():
    assert monotonic([-5, -4, -3, -2]) == True

def test_monotonic_negative_numbers_decreasing():
    assert monotonic([-2, -3, -4, -5]) == True

def test_monotonic_mixed_positive_and_negative_increasing():
    assert monotonic([-5, -2, 0, 3]) == True

def test_monotonic_mixed_positive_and_negative_decreasing():
    assert monotonic([3, 0, -2, -5]) == True

def test_monotonic_floats_increasing():
    assert monotonic([1.0, 2.5, 3.7, 4.2]) == True

def test_monotonic_floats_decreasing():
    assert monotonic([4.2, 3.7, 2.5, 1.0]) == True

def test_monotonic_mixed_floats_and_integers_increasing():
    assert monotonic([1, 2.5, 4, 5.5]) == True

def test_monotonic_mixed_floats_and_integers_decreasing():
    assert monotonic([5.5, 4, 2.5, 1]) == True

def test_monotonic_list_with_same_first_and_last_element_increasing():
    assert monotonic([1, 2, 3, 1]) == False

def test_monotonic_list_with_same_first_and_last_element_decreasing():
    assert monotonic([5, 4, 3, 5]) == False

def test_monotonic_long_increasing_list():
    assert monotonic(list(range(100))) == True

def test_monotonic_long_decreasing_list():
    assert monotonic(list(range(99, -1, -1))) == True

def test_monotonic_long_non_monotonic_list():
    l = list(range(100))
    l[50] = 0
    assert monotonic(l) == False