import pytest
from source_to_mutate import order_by_points

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]

def test_mixed_numbers():
    assert order_by_points([1, -2, 3, -4, 5]) == [-4, -2, 1, 3, 5]

def test_same_digit_sum():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_different_digit_sums():
    assert order_by_points([12, 21, 1, 111]) == [1, 12, 21, 111]

def test_negative_and_positive_same_digit_sum():
    assert order_by_points([1, -1, 10, -10]) == [-1, -10, 1, 10]

def test_example_1():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_large_numbers():
    assert order_by_points([12345, 54321, 1, 10]) == [1, 10, 12345, 54321]

def test_negative_large_numbers():
    assert order_by_points([-12345, -54321, -1, -10]) == [-1, -10, -54321, -12345]

def test_mixed_large_numbers():
    assert order_by_points([12345, -54321, 1, -10]) == [-10, 1, -54321, 12345]

def test_zero():
    assert order_by_points([0, 1, -1]) == [-1, 0, 1]

def test_multiple_zeros():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_complex_example():
    assert order_by_points([12, -12, 1, -1, 123, -123, 1234, -1234]) == [-1, -12, 1, 12, -123, 123, -1234, 1234]