import pytest
from source_to_mutate import get_positive

def test_empty_list():
    assert get_positive([]) == []

def test_all_positive():
    assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_all_negative():
    assert get_positive([-1, -2, -3, -4, -5]) == []

def test_mixed_positive_negative():
    assert get_positive([-1, 2, -3, 4, -5]) == [2, 4]

def test_with_zero():
    assert get_positive([-1, 0, 1, 2, -2]) == [1, 2]

def test_duplicate_positive_numbers():
    assert get_positive([1, 2, 2, 3, 3, 3]) == [1, 2, 2, 3, 3, 3]

def test_duplicate_negative_numbers():
    assert get_positive([-1, -2, -2, -3, -3, -3]) == []

def test_large_positive_numbers():
    assert get_positive([1000, 2000, 3000]) == [1000, 2000, 3000]

def test_large_negative_numbers():
    assert get_positive([-1000, -2000, -3000]) == []

def test_mixed_large_and_small_numbers():
    assert get_positive([-1000, 1, -2, 2000]) == [1, 2000]

def test_positive_at_start():
    assert get_positive([5, -1, -2]) == [5]

def test_positive_at_end():
    assert get_positive([-1, -2, 5]) == [5]

def test_positive_in_middle():
    assert get_positive([-1, 5, -2]) == [5]