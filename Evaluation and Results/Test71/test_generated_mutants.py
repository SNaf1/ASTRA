import pytest
from source_to_mutate import triangle_area

def test_valid_triangle():
    assert triangle_area(3, 4, 5) == 6.0

def test_invalid_triangle_sum_less_than():
    assert triangle_area(1, 2, 10) == -1

def test_invalid_triangle_sum_equal_to():
    assert triangle_area(1, 2, 3) == -1

def test_equilateral_triangle():
    assert triangle_area(5, 5, 5) == 10.83

def test_isosceles_triangle():
    assert triangle_area(5, 5, 6) == 12.0

def test_large_numbers():
    assert triangle_area(100, 100, 100) == 4330.13

def test_zero_input():
    assert triangle_area(0, 1, 2) == -1

def test_negative_input():
    assert triangle_area(-1, 2, 3) == -1

def test_float_input():
    assert triangle_area(3.5, 4.5, 5.5) == 7.85

def test_near_zero_input():
    assert triangle_area(0.001, 0.001, 0.001) == 0.0

def test_large_float_input():
    assert triangle_area(1000.5, 1000.5, 1000.5) == 433445.82

def test_invalid_triangle_with_large_numbers():
    assert triangle_area(1000, 1, 1) == -1

def test_invalid_triangle_with_equal_sides():
    assert triangle_area(10, 1, 1) == -1

def test_valid_triangle_with_close_sides():
    assert triangle_area(10, 9, 8) == 34.2

def test_valid_triangle_with_small_sides():
    assert triangle_area(0.1, 0.2, 0.25) == 0.01