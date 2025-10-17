import pytest
from source_to_mutate import greatest_common_divisor

def test_gcd_positive_numbers_no_common_divisor():
    assert greatest_common_divisor(3, 5) == 1

def test_gcd_positive_numbers_with_common_divisor():
    assert greatest_common_divisor(25, 15) == 5

def test_gcd_one_number_is_zero():
    assert greatest_common_divisor(0, 5) == 5

def test_gcd_both_numbers_are_zero():
    assert greatest_common_divisor(0, 0) == 0

def test_gcd_one_number_is_one():
    assert greatest_common_divisor(1, 5) == 1

def test_gcd_both_numbers_are_one():
    assert greatest_common_divisor(1, 1) == 1

def test_gcd_large_numbers():
    assert greatest_common_divisor(1071, 462) == 21

def test_gcd_equal_numbers():
    assert greatest_common_divisor(10, 10) == 10

def test_gcd_one_number_is_multiple_of_other():
    assert greatest_common_divisor(10, 5) == 5

def test_gcd_prime_numbers():
    assert greatest_common_divisor(7, 11) == 1

def test_gcd_negative_numbers():
    assert greatest_common_divisor(-12, -18) == -6