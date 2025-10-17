import pytest
from source_to_mutate import prod_signs

def test_empty_array():
    assert prod_signs([]) is None

def test_positive_numbers():
    assert prod_signs([1, 2, 3]) == 6

def test_negative_numbers():
    assert prod_signs([-1, -2, -3]) == -6

def test_mixed_numbers():
    assert prod_signs([1, -2, 3]) == -6

def test_zero_in_array():
    assert prod_signs([0, 1, 2]) == 0

def test_multiple_zeros():
    assert prod_signs([0, 0, 0]) == 0

def test_large_numbers():
    assert prod_signs([100, 200, 300]) == 600

def test_large_negative_numbers():
    assert prod_signs([-100, -200, -300]) == -600

def test_mixed_large_numbers():
    assert prod_signs([100, -200, 300]) == -600

def test_single_positive_number():
    assert prod_signs([5]) == 5

def test_single_negative_number():
    assert prod_signs([-5]) == -5

def test_single_zero():
    assert prod_signs([0]) == 0

def test_mixed_with_zero():
    assert prod_signs([1, -2, 0, 3]) == 0

def test_all_same_positive():
    assert prod_signs([2, 2, 2]) == 6

def test_all_same_negative():
    assert prod_signs([-2, -2, -2]) == -6

def test_even_number_of_negatives():
    assert prod_signs([-1, -1, 1]) == 3

def test_odd_number_of_negatives():
    assert prod_signs([-1, 1, 1]) == -3

def test_mixed_with_large_and_small():
    assert prod_signs([1, -100, 2]) == -103

def test_only_negatives_and_zero():
    assert prod_signs([-1, -2, 0]) == 0