import pytest
from source_to_mutate import multiply

def test_multiply_positive_numbers():
    assert multiply(148, 412) == 16

def test_multiply_positive_numbers_2():
    assert multiply(19, 28) == 72

def test_multiply_zero():
    assert multiply(2020, 1851) == 0

def test_multiply_one_negative():
    assert multiply(14, -15) == 20

def test_multiply_both_negative():
    assert multiply(-14, -15) == 30

def test_multiply_single_digit_positive():
    assert multiply(7, 8) == 56

def test_multiply_single_digit_negative():
    assert multiply(-7, -8) == 6

def test_multiply_one_single_digit_positive():
    assert multiply(123, 7) == 21

def test_multiply_one_single_digit_negative():
    assert multiply(123, -7) == 9

def test_multiply_large_numbers():
    assert multiply(123456789, 987654321) == 9

def test_multiply_one_number_zero():
    assert multiply(123, 0) == 0

def test_multiply_both_numbers_zero():
    assert multiply(0, 0) == 0

def test_multiply_negative_and_zero():
    assert multiply(-123, 0) == 0

def test_multiply_zero_and_negative():
    assert multiply(0, -123) == 0

def test_multiply_negative_large_numbers():
    assert multiply(-123456789, -987654321) == 9

def test_multiply_negative_and_positive_large_numbers():
    assert multiply(-123456789, 987654321) == 1

def test_multiply_positive_and_negative_large_numbers():
    assert multiply(123456789, -987654321) == 81

def test_multiply_same_numbers():
    assert multiply(123, 123) == 9