import pytest
from source_to_mutate import poly, find_zero
import math

def test_poly_empty_list():
    assert poly([], 2.0) == 0.0

def test_poly_single_coefficient():
    assert poly([5.0], 2.0) == 5.0

def test_poly_two_coefficients():
    assert poly([1.0, 2.0], 2.0) == 5.0

def test_poly_three_coefficients():
    assert poly([1.0, 2.0, 1.0], 2.0) == 9.0

def test_poly_negative_x():
    assert poly([1.0, 2.0], -2.0) == -3.0

def test_poly_zero_x():
    assert poly([1.0, 2.0], 0.0) == 1.0

def test_poly_negative_coefficients():
    assert poly([-1.0, -2.0], 2.0) == -5.0

def test_poly_mixed_coefficients():
    assert poly([-1.0, 2.0, -1.0], 2.0) == -1.0

def test_poly_large_x():
    assert poly([1.0, 2.0], 10.0) == 21.0

def test_poly_large_coefficients():
    assert poly([100.0, 200.0], 2.0) == 500.0

def test_poly_decimal_x():
    assert poly([1.0, 2.0], 0.5) == 2.0

def test_poly_decimal_coefficients():
    assert poly([0.5, 1.5], 2.0) == 3.5

def test_find_zero_linear():
    assert round(find_zero([1, 2]), 10) == -0.5000000001

def test_find_zero_cubic():
    assert round(find_zero([-6, 11, -6, 1]), 10) == 0.9999999999

def test_find_zero_linear_negative_coefficients():
    assert round(find_zero([-1, -2]), 10) == -0.5000000001

def test_find_zero_linear_zero_constant():
    assert round(find_zero([0, 2]), 10) == -1e-10

def test_find_zero_cubic_negative_constant():
    assert round(find_zero([6, -11, 6, -1]), 10) == 0.9999999999

def test_find_zero_cubic_large_coefficients():
    assert round(find_zero([-6000, 11000, -6000, 1000]), 10) == 0.9999999999

def test_find_zero_cubic_decimal_coefficients():
    assert round(find_zero([-6.0, 11.0, -6.0, 1.0]), 10) == 0.9999999999

def test_find_zero_linear_decimal_coefficients():
    assert round(find_zero([1.5, 2.5]), 10) == -0.6

def test_find_zero_linear_large_coefficients():
    assert round(find_zero([1000, 2000]), 10) == -0.5000000001

def test_find_zero_cubic_with_zero_coefficient():
    assert round(find_zero([0, 0, 0, 1]), 10) == -1e-10