import pytest
from source_to_mutate import move_one_ball

def test_empty_array():
    assert move_one_ball([]) == True

def test_already_sorted():
    assert move_one_ball([1, 2, 3, 4, 5]) == True

def test_one_shift_needed():
    assert move_one_ball([5, 1, 2, 3, 4]) == True

def test_multiple_shifts_needed():
    assert move_one_ball([3, 4, 5, 1, 2]) == True

def test_not_sortable():
    assert move_one_ball([3, 5, 4, 1, 2]) == False

def test_single_element():
    assert move_one_ball([7]) == True

def test_two_elements_sorted():
    assert move_one_ball([1, 2]) == True

def test_two_elements_unsorted_but_shiftable():
    assert move_one_ball([2, 1]) == True

def test_negative_numbers():
    assert move_one_ball([-2, -1, 0, 1, 2]) == True

def test_negative_numbers_shift_needed():
    assert move_one_ball([1, 2, -2, -1, 0]) == True

def test_negative_numbers_not_sortable():
    assert move_one_ball([1, 2, -2, 0, -1]) == False

def test_mixed_positive_and_negative_numbers():
    assert move_one_ball([-1, 0, 1, 2, -2]) == True

def test_mixed_positive_and_negative_numbers_not_sortable():
    assert move_one_ball([-1, 0, 2, 1, -2]) == False

def test_large_numbers():
    assert move_one_ball([1000, 2000, 3000, 4000, 5000]) == True

def test_large_numbers_shift_needed():
    assert move_one_ball([4000, 5000, 1000, 2000, 3000]) == True

def test_large_numbers_not_sortable():
    assert move_one_ball([4000, 5000, 1000, 3000, 2000]) == False

def test_duplicate_min_value():
    assert move_one_ball([2, 1, 3, 1, 4]) == False

def test_all_same_elements():
    assert move_one_ball([5, 5, 5, 5, 5]) == True

def test_almost_sorted():
    assert move_one_ball([1, 2, 3, 5, 4]) == False

def test_longer_array():
    assert move_one_ball([7, 8, 9, 1, 2, 3, 4, 5, 6]) == True

def test_longer_array_not_sortable():
    assert move_one_ball([7, 8, 9, 1, 2, 3, 5, 4, 6]) == False