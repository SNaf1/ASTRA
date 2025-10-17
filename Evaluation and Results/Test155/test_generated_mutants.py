import pytest
from source_to_mutate import even_odd_count

def test_positive_number():
    assert even_odd_count(12345) == (2, 3)

def test_negative_number():
    assert even_odd_count(-1234) == (2, 2)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_single_even_digit():
    assert even_odd_count(2) == (1, 0)

def test_single_odd_digit():
    assert even_odd_count(1) == (0, 1)

def test_all_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits():
    assert even_odd_count(13579) == (0, 5)

def test_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_large_number():
    assert even_odd_count(-9876543210) == (5, 5)

def test_number_with_leading_zeros():
    assert even_odd_count(2004) == (4, 0)

def test_negative_number_with_leading_zeros():
    assert even_odd_count(-2004) == (4, 0)

def test_number_with_repeating_digits():
    assert even_odd_count(112233) == (2, 4)