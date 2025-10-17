import pytest
from source_to_mutate import will_it_fly

def test_will_it_fly_unbalanced_and_heavy():
    assert will_it_fly([1, 2], 5) == False

def test_will_it_fly_balanced_but_heavy():
    assert will_it_fly([3, 2, 3], 1) == False

def test_will_it_fly_balanced_and_light():
    assert will_it_fly([3, 2, 3], 9) == True

def test_will_it_fly_single_element_light():
    assert will_it_fly([3], 5) == True

def test_will_it_fly_empty_list():
    assert will_it_fly([], 0) == True

def test_will_it_fly_empty_list_with_weight():
    assert will_it_fly([], 5) == True

def test_will_it_fly_single_element_heavy():
    assert will_it_fly([5], 1) == False

def test_will_it_fly_two_elements_balanced_light():
    assert will_it_fly([1, 1], 3) == True

def test_will_it_fly_two_elements_balanced_heavy():
    assert will_it_fly([2, 2], 3) == False

def test_will_it_fly_two_elements_unbalanced_light():
    assert will_it_fly([1, 2], 3) == False

def test_will_it_fly_long_balanced_light():
    assert will_it_fly([1, 2, 3, 4, 5, 4, 3, 2, 1], 30) == True

def test_will_it_fly_long_balanced_heavy():
    assert will_it_fly([1, 2, 3, 4, 5, 4, 3, 2, 1], 20) == False

def test_will_it_fly_long_unbalanced_light():
    assert will_it_fly([1, 2, 3, 4, 5, 4, 3, 2, 2], 30) == False

def test_will_it_fly_negative_numbers_balanced_light():
    assert will_it_fly([-1, -2, -1], -3) == True

def test_will_it_fly_negative_numbers_balanced_heavy():
    assert will_it_fly([-1, -2, -1], -5) == False

def test_will_it_fly_mixed_numbers_balanced_light():
    assert will_it_fly([-1, 2, -1], 1) == True

def test_will_it_fly_mixed_numbers_balanced_heavy():
    assert will_it_fly([-1, 2, -1], -1) == False

def test_will_it_fly_zero_weight():
    assert will_it_fly([1, 2, 1], 0) == False

def test_will_it_fly_zero_list_elements():
    assert will_it_fly([0, 0, 0], 1) == True

def test_will_it_fly_large_numbers_balanced_light():
    assert will_it_fly([100, 200, 100], 400) == True

def test_will_it_fly_large_numbers_balanced_heavy():
    assert will_it_fly([100, 200, 100], 300) == False

def test_will_it_fly_same_numbers_balanced_light():
    assert will_it_fly([5, 5, 5, 5, 5], 25) == True

def test_will_it_fly_same_numbers_balanced_heavy():
    assert will_it_fly([5, 5, 5, 5, 5], 20) == False

def test_will_it_fly_single_zero():
    assert will_it_fly([0], 0) == True

def test_will_it_fly_single_negative():
    assert will_it_fly([-1], -1) == True

def test_will_it_fly_single_negative_heavy():
    assert will_it_fly([-1], -2) == False

def test_will_it_fly_single_negative_light():
    assert will_it_fly([-1], 0) == True