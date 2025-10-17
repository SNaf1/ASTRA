import pytest
from source_to_mutate import specialFilter

def test_empty_array():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_no_numbers_with_odd_first_and_last_digits():
    assert specialFilter([12, 24, 36, 48, 60]) == 0

def test_single_number_greater_than_10_with_odd_digits():
    assert specialFilter([11]) == 1

def test_single_number_greater_than_10_with_even_digits():
    assert specialFilter([22]) == 0

def test_multiple_numbers_greater_than_10_with_odd_digits():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_multiple_numbers_greater_than_10_with_mixed_digits():
    assert specialFilter([11, 22, 33, 44, 55]) == 3

def test_mixed_numbers_greater_and_less_than_10_with_mixed_digits():
    assert specialFilter([5, 11, 15, 22, 33]) == 3

def test_negative_numbers():
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_mixed_positive_and_negative_numbers():
    assert specialFilter([11, -33, 55, -77, 99]) == 3

def test_large_numbers():
    assert specialFilter([11111, 33333, 55555, 77777, 99999]) == 5

def test_numbers_with_leading_zeros():
    assert specialFilter([101, 303, 505, 707, 909]) == 5

def test_numbers_with_different_lengths():
    assert specialFilter([11, 111, 1111, 11111, 111111]) == 5

def test_numbers_with_zero_as_first_or_last_digit():
    assert specialFilter([10, 101, 110, 111]) == 2

def test_example_1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_example_2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_number_with_same_first_and_last_digit():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_number_close_to_10():
    assert specialFilter([9, 10, 11]) == 1

def test_number_with_zero_in_the_middle():
    assert specialFilter([101, 303, 505]) == 3

def test_number_with_repeating_digits():
    assert specialFilter([111, 333, 555]) == 3

def test_number_with_different_odd_digits():
    assert specialFilter([13, 35, 57, 79, 91]) == 5

def test_number_with_even_first_and_odd_last_digit():
    assert specialFilter([21, 43, 65, 87]) == 0

def test_number_with_odd_first_and_even_last_digit():
    assert specialFilter([12, 34, 56, 78]) == 0

def test_number_with_only_one_digit():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_number_with_zero():
    assert specialFilter([0]) == 0

def test_number_with_negative_and_odd_digits():
    assert specialFilter([-11, -33, -55]) == 0

def test_number_with_negative_and_even_digits():
    assert specialFilter([-22, -44, -66]) == 0

def test_number_with_negative_and_mixed_digits():
    assert specialFilter([-12, -34, -56]) == 0

def test_number_with_negative_and_zero():
    assert specialFilter([-0]) == 0

def test_number_with_large_negative_number():
    assert specialFilter([-123456789]) == 0

def test_number_with_large_positive_number():
    assert specialFilter([123456789]) == 1

def test_number_with_same_digits():
    assert specialFilter([111111111]) == 1

def test_number_with_different_digits():
    assert specialFilter([123456789]) == 1

def test_number_with_mixed_positive_and_negative_and_zero():
    assert specialFilter([11, -33, 0, 55, -77, 99]) == 3