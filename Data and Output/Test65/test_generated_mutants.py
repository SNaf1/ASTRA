import pytest
from source_to_mutate import circular_shift

def test_circular_shift_positive_shift_less_than_length():
    assert circular_shift(12, 1) == '21'

def test_circular_shift_positive_shift_equal_to_length():
    assert circular_shift(12, 2) == '12'

def test_circular_shift_positive_shift_greater_than_length():
    assert circular_shift(12, 3) == '21'

def test_circular_shift_zero_shift():
    assert circular_shift(12, 0) == '12'

def test_circular_shift_single_digit():
    assert circular_shift(1, 1) == '1'

def test_circular_shift_large_number_small_shift():
    assert circular_shift(123456789, 2) == '891234567'

def test_circular_shift_large_number_large_shift():
    assert circular_shift(123456789, 10) == '987654321'

def test_circular_shift_negative_number():
    assert circular_shift(-12, 1) == '2-1'

def test_circular_shift_negative_number_large_shift():
    assert circular_shift(-12, 3) == '-12'

def test_circular_shift_zero():
    assert circular_shift(0, 1) == '0'

def test_circular_shift_zero_large_shift():
    assert circular_shift(0, 5) == '0'

def test_circular_shift_number_with_leading_zeros():
    assert circular_shift(102, 1) == '210'

def test_circular_shift_number_with_leading_zeros_large_shift():
    assert circular_shift(102, 4) == '201'

def test_circular_shift_number_with_repeated_digits():
    assert circular_shift(111, 1) == '111'

def test_circular_shift_number_with_repeated_digits_large_shift():
    assert circular_shift(111, 4) == '111'