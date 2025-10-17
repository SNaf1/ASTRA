import pytest
from source_to_mutate import sum_squares

def test_empty_list():
    assert sum_squares([]) == 0

def test_list_with_one_element_index_0():
    assert sum_squares([1]) == 1

def test_list_with_one_element_index_not_0():
    assert sum_squares([1, 2]) == 3

def test_list_with_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 6

def test_list_with_multiple_of_4():
    assert sum_squares([1, 2, 3, 4, 5]) == 147

def test_list_with_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1062

def test_list_with_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_with_zeros():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_list_with_mixed_positive_and_negative_numbers():
    assert sum_squares([1, -2, 3, -4, 5, -6, 7, -8, 9]) == 907

def test_list_with_large_numbers():
    assert sum_squares([10, 20, 30, 40, 50]) == 126750

def test_list_with_all_same_numbers():
    assert sum_squares([2, 2, 2, 2, 2, 2]) == 22

def test_list_with_only_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 153

def test_list_with_only_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 210

def test_list_with_multiples_of_3_and_4_and_others():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1231