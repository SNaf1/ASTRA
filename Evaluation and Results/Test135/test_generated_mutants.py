import pytest
from source_to_mutate import can_arrange

def test_empty_array():
    assert can_arrange([]) == -1

def test_single_element_array():
    assert can_arrange([5]) == -1

def test_sorted_array():
    assert can_arrange([1, 2, 3, 4, 5]) == -1

def test_reverse_sorted_array():
    assert can_arrange([5, 4, 3, 2, 1]) == 4

def test_example_1():
    assert can_arrange([1, 2, 4, 3, 5]) == 3

def test_example_2():
    assert can_arrange([1, 2, 3]) == -1

def test_decreasing_then_increasing():
    assert can_arrange([5, 4, 3, 6, 7]) == 2

def test_increasing_then_decreasing():
    assert can_arrange([1, 2, 3, 2, 1]) == 4

def test_all_equal():
    assert can_arrange([2, 2, 2, 2, 2]) == -1

def test_negative_numbers():
    assert can_arrange([-1, -2, -3]) == 2

def test_mixed_positive_and_negative():
    assert can_arrange([-1, 2, -3, 4]) == 2

def test_large_numbers():
    assert can_arrange([1000, 2000, 500, 3000]) == 2

def test_first_element_is_largest():
    assert can_arrange([5, 1, 2, 3, 4]) == 1

def test_last_element_is_smallest():
    assert can_arrange([1, 2, 3, 4, 0]) == 4

def test_almost_sorted():
    assert can_arrange([1, 2, 3, 5, 4]) == 4

def test_two_elements_unsorted():
    assert can_arrange([2, 1]) == 1

def test_long_array_with_one_unsorted_element():
    assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == 20