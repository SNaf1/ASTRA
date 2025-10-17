import pytest
from source_to_mutate import triangle_area

def test_triangle_area_positive():
    assert triangle_area(5, 3) == 7.5

def test_triangle_area_zero_base():
    assert triangle_area(0, 5) == 0.0

def test_triangle_area_zero_height():
    assert triangle_area(5, 0) == 0.0

def test_triangle_area_large_numbers():
    assert triangle_area(1000, 500) == 250000.0

def test_triangle_area_decimal_values():
    assert triangle_area(2.5, 3.5) == 4.375

def test_triangle_area_negative_base():
    assert triangle_area(-5, 3) == -7.5

def test_triangle_area_negative_height():
    assert triangle_area(5, -3) == -7.5

def test_triangle_area_negative_both():
    assert triangle_area(-5, -3) == 7.5