import pytest
from source_to_mutate import is_equal_to_sum_even

def test_is_equal_to_sum_even_less_than_8():
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(6) == False

def test_is_equal_to_sum_even_equal_to_8():
    assert is_equal_to_sum_even(8) == True

def test_is_equal_to_sum_even_greater_than_8_even():
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(12) == True
    assert is_equal_to_sum_even(100) == True

def test_is_equal_to_sum_even_odd():
    assert is_equal_to_sum_even(9) == False
    assert is_equal_to_sum_even(11) == False
    assert is_equal_to_sum_even(99) == False

def test_is_equal_to_sum_even_zero():
    assert is_equal_to_sum_even(0) == False

def test_is_equal_to_sum_even_negative():
    assert is_equal_to_sum_even(-2) == False
    assert is_equal_to_sum_even(-8) == False
    assert is_equal_to_sum_even(-10) == False