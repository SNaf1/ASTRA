import pytest
from source_to_mutate import search

def test_empty_list():
    assert search([1]) == 1

def test_example_1():
    assert search([4, 1, 2, 2, 3, 1]) == 2

def test_example_2():
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3

def test_example_3():
    assert search([5, 5, 4, 4, 4]) == -1

def test_single_element_list():
    assert search([1]) == 1

def test_all_same_elements():
    assert search([3, 3, 3]) == 3

def test_no_suitable_element():
    assert search([2, 1, 1]) == 1

def test_large_numbers():
    assert search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10

def test_mixed_numbers():
    assert search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10

def test_boundary_condition_equal():
    assert search([1, 2, 2, 3, 3, 3]) == 3

def test_boundary_condition_greater():
    assert search([1, 2, 2, 3, 3, 3, 3]) == 3

def test_no_element_meets_criteria():
    assert search([5, 1, 1, 1, 1]) == 1

def test_sorted_list():
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4

def test_reverse_sorted_list():
    assert search([4, 4, 4, 4, 3, 3, 3, 2, 2, 1]) == 4

def test_duplicate_max_value():
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]) == 4

def test_max_value_not_present():
    assert search([1, 2, 2, 3, 3, 3]) == 3

def test_max_value_present_once():
    assert search([1, 2, 2, 3, 3, 3, 4]) == 3

def test_all_numbers_less_than_frequency():
    assert search([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5

def test_all_numbers_greater_than_frequency():
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == 5