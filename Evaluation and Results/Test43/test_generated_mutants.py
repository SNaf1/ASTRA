import pytest
from source_to_mutate import pairs_sum_to_zero

def test_empty_list():
    assert pairs_sum_to_zero([]) == False

def test_single_element_list():
    assert pairs_sum_to_zero([1]) == False

def test_no_zero_sum_pair():
    assert pairs_sum_to_zero([1, 2, 3, 4, 5]) == False

def test_zero_sum_pair_exists():
    assert pairs_sum_to_zero([1, 2, -2, 4, 5]) == True

def test_multiple_zero_sum_pairs():
    assert pairs_sum_to_zero([1, -1, 2, -2, 3, -3]) == True

def test_zero_in_list_no_pair():
    assert pairs_sum_to_zero([1, 2, 3, 0]) == False

def test_zero_in_list_with_pair():
    assert pairs_sum_to_zero([1, 2, 0, -2]) == True

def test_duplicate_numbers_no_zero_sum():
    assert pairs_sum_to_zero([1, 1, 2, 2, 3, 3]) == False

def test_duplicate_numbers_with_zero_sum():
    assert pairs_sum_to_zero([1, 1, -1, 2, 2]) == True

def test_negative_numbers_no_zero_sum():
    assert pairs_sum_to_zero([-1, -2, -3, -4, -5]) == False

def test_all_zeros():
    assert pairs_sum_to_zero([0, 0, 0, 0]) == True

def test_large_numbers():
    assert pairs_sum_to_zero([1000, -1000]) == True

def test_large_list_no_zero_sum():
    assert pairs_sum_to_zero(list(range(1, 100))) == False

def test_large_list_with_zero_sum():
    l = list(range(1, 100))
    l.append(-50)
    assert pairs_sum_to_zero(l) == True

def test_same_number_twice_no_zero_sum():
    assert pairs_sum_to_zero([5,5]) == False

def test_same_number_twice_zero_sum():
    assert pairs_sum_to_zero([-5,5]) == True