import pytest
from source_to_mutate import x_or_y

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_one():
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_two():
    assert x_or_y(2, 5, 10) == 5

def test_x_or_y_three():
    assert x_or_y(3, 5, 10) == 5

def test_x_or_y_four():
    assert x_or_y(4, 5, 10) == 10

def test_x_or_y_large_prime():
    assert x_or_y(101, 1, 0) == 1

def test_x_or_y_large_not_prime():
    assert x_or_y(100, 1, 0) == 0

def test_x_or_y_zero():
    assert x_or_y(0, 1, 2) == 1