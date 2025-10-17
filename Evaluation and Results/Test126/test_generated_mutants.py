import pytest
from source_to_mutate import is_sorted

def test_single_element():
    assert is_sorted([5]) == True

def test_ascending_order():
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_not_sorted():
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_longer_sorted_list():
    assert is_sorted([1, 2, 3, 4, 5, 6]) == True

def test_even_longer_sorted_list():
    assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True

def test_longer_not_sorted_list():
    assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == False

def test_duplicates_less_than_three():
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True

def test_duplicates_more_than_two():
    assert is_sorted([1, 2, 2, 2, 3, 4]) == False

def test_empty_list():
    assert is_sorted([]) == True

def test_duplicates_at_start():
    assert is_sorted([2, 2, 1, 3, 4]) == False

def test_duplicates_at_end():
    assert is_sorted([1, 2, 3, 4, 4, 4]) == False

def test_duplicates_mixed():
    assert is_sorted([1, 2, 2, 3, 3, 3, 4]) == False

def test_large_numbers():
    assert is_sorted([100, 200, 300, 400]) == True

def test_large_numbers_not_sorted():
    assert is_sorted([100, 300, 200, 400]) == False

def test_same_number_multiple_times():
    assert is_sorted([5, 5, 5]) == False

def test_two_elements_sorted():
    assert is_sorted([1, 2]) == True

def test_two_elements_not_sorted():
    assert is_sorted([2, 1]) == False

def test_three_elements_sorted():
    assert is_sorted([1, 2, 3]) == True

def test_three_elements_not_sorted():
    assert is_sorted([1, 3, 2]) == False