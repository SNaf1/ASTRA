import pytest
from source_to_mutate import digits

def test_digits_single_odd():
    assert digits(1) == 1

def test_digits_single_even():
    assert digits(4) == 0

def test_digits_multiple_odd():
    assert digits(235) == 15

def test_digits_all_even():
    assert digits(2468) == 0

def test_digits_mixed_odd_even():
    assert digits(12345) == 15

def test_digits_large_number():
    assert digits(1357913579) == 893025

def test_digits_number_with_zero():
    assert digits(103) == 3

def test_digits_number_with_repeated_odd_digits():
    assert digits(11111) == 1

def test_digits_number_starting_with_zero():
    assert digits(204) == 0

def test_digits_number_ending_with_zero():
    assert digits(1350) == 15

def test_digits_number_with_only_one_odd_digit_at_the_end():
    assert digits(24681) == 1

def test_digits_number_with_only_one_odd_digit_at_the_beginning():
    assert digits(12468) == 1

def test_digits_number_with_multiple_zeros():
    assert digits(100030005) == 15