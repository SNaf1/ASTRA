import pytest
from source_to_mutate import count_nums

def test_empty_array():
    assert count_nums([]) == 0

def test_positive_numbers():
    assert count_nums([1, 1, 2]) == 3

def test_negative_numbers():
    assert count_nums([-1, -1, -2]) == 0

def test_mixed_numbers():
    assert count_nums([-1, 11, -11]) == 1

def test_zero():
    assert count_nums([0]) == 0

def test_large_numbers():
    assert count_nums([12345, 67890]) == 2

def test_negative_large_numbers():
    assert count_nums([-12345, -67890]) == 2

def test_mixed_large_numbers():
    assert count_nums([12345, -67890, 9876]) == 3

def test_single_element_positive():
    assert count_nums([5]) == 1

def test_single_element_negative():
    assert count_nums([-5]) == 0

def test_single_element_zero():
    assert count_nums([0]) == 0

def test_all_zeros():
    assert count_nums([0, 0, 0]) == 0

def test_negative_and_positive_zeros():
    assert count_nums([0, -0, 0]) == 0

def test_duplicate_numbers():
    assert count_nums([1, 1, 1, 1]) == 4

def test_duplicate_negative_numbers():
    assert count_nums([-1, -1, -1, -1]) == 0

def test_duplicate_mixed_numbers():
    assert count_nums([1, -1, 1, -1]) == 2

def test_numbers_with_zero_sum():
    assert count_nums([1, -10]) == 1

def test_numbers_with_positive_sum():
    assert count_nums([1, 10]) == 2

def test_numbers_with_negative_sum():
    assert count_nums([-1, -10]) == 0

def test_large_number_with_negative_digit():
    assert count_nums([-91]) == 0

def test_large_number_with_positive_digit():
    assert count_nums([91]) == 1

def test_mix_large_and_small():
    assert count_nums([1, 1000000]) == 2

def test_mix_large_and_small_negative():
    assert count_nums([-1, -1000000]) == 0

def test_mix_large_and_small_mixed():
    assert count_nums([1, -1000000, 100]) == 2