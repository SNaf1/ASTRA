import pytest
from source_to_mutate import any_int

def test_positive_sum():
    assert any_int(5, 2, 7) == True

def test_negative_sum():
    assert any_int(3, -2, 1) == True

def test_no_sum():
    assert any_int(3, 2, 2) == False

def test_float_input():
    assert any_int(3.6, -2.2, 2) == False

def test_zero_sum():
    assert any_int(0, 0, 0) == True

def test_one_zero():
    assert any_int(1, 0, 1) == True

def test_two_zeros():
    assert any_int(0, 0, 5) == False

def test_large_numbers():
    assert any_int(1000, 2000, 3000) == True

def test_negative_numbers():
    assert any_int(-5, -2, -7) == True

def test_mixed_positive_negative():
    assert any_int(5, -2, 3) == True

def test_all_negative_no_sum():
    assert any_int(-1, -2, -4) == False

def test_one_positive_two_negative_no_sum():
    assert any_int(1, -2, -4) == False

def test_zero_and_negatives():
    assert any_int(0, -5, 5) == True

def test_zero_and_positives():
    assert any_int(0, 5, -5) == True

def test_same_numbers_sum():
    assert any_int(2, 2, 4) == True

def test_same_numbers_no_sum():
    assert any_int(2, 2, 2) == False

def test_one_is_sum_of_other_two_negative():
    assert any_int(-2, -3, -5) == True

def test_one_is_sum_of_other_two_mixed():
    assert any_int(2, -3, -1) == True

def test_one_is_sum_of_other_two_positive():
    assert any_int(2, 3, 5) == True

def test_non_integer_input_x():
    assert any_int(2.5, 3, 5) == False

def test_non_integer_input_y():
    assert any_int(2, 3.5, 5) == False

def test_non_integer_input_z():
    assert any_int(2, 3, 5.5) == False

def test_non_integer_input_all():
    assert any_int(2.5, 3.5, 5.5) == False