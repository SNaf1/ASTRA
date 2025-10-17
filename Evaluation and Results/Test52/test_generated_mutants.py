import pytest
from source_to_mutate import below_threshold

def test_empty_list():
    assert below_threshold([], 10) == True

def test_all_below():
    assert below_threshold([1, 2, 3], 4) == True

def test_one_equal():
    assert below_threshold([1, 2, 3], 3) == False

def test_one_above():
    assert below_threshold([1, 2, 3], 2) == False

def test_all_equal():
    assert below_threshold([5, 5, 5], 5) == False

def test_negative_numbers():
    assert below_threshold([-1, -2, -3], 0) == True

def test_mixed_positive_negative():
    assert below_threshold([-1, 2, -3], 1) == False

def test_large_numbers():
    assert below_threshold([1000, 2000, 3000], 4000) == True

def test_large_threshold():
    assert below_threshold([1, 2, 3], 1000) == True

def test_zero_threshold():
    assert below_threshold([1, 2, 3], 0) == False

def test_zero_in_list():
    assert below_threshold([0, 1, 2], 1) == False

def test_negative_threshold():
    assert below_threshold([1, 2, 3], -1) == False

def test_negative_numbers_and_threshold():
    assert below_threshold([-1, -2, -3], -1) == False

def test_duplicate_numbers():
    assert below_threshold([1, 2, 2, 3], 3) == False

def test_duplicate_numbers_above_threshold():
    assert below_threshold([1, 2, 2, 3], 2) == False