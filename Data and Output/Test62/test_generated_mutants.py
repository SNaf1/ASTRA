import pytest
from source_to_mutate import derivative, METADATA


def test_derivative_empty_list():
    assert derivative([]) == []


def test_derivative_single_element():
    assert derivative([5]) == []


def test_derivative_example_1():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]


def test_derivative_example_2():
    assert derivative([1, 2, 3]) == [2, 6]


def test_derivative_all_zeros():
    assert derivative([0, 0, 0, 0]) == [0, 0, 0]


def test_derivative_negative_coefficients():
    assert derivative([1, -2, 3, -4]) == [-2, 6, -12]


def test_derivative_mixed_coefficients():
    assert derivative([-1, 2, -3, 4, -5]) == [2, -6, 12, -20]


def test_derivative_large_coefficients():
    assert derivative([100, 200, 300, 400]) == [200, 600, 1200]


def test_derivative_float_coefficients():
    assert derivative([1.0, 2.0, 3.0]) == [2.0, 6.0]


def test_derivative_mixed_int_float():
    assert derivative([1, 2.0, 3]) == [2.0, 6]