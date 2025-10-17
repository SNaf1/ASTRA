import pytest
from source_to_mutate import remove_duplicates

def test_empty_list():
    assert remove_duplicates([]) == []

def test_no_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_all_duplicates():
    assert remove_duplicates([1, 1, 1, 1, 1]) == []

def test_single_duplicate():
    assert remove_duplicates([1, 2, 1]) == [2]

def test_multiple_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [3, 4, 5]

def test_duplicates_at_start():
    assert remove_duplicates([1, 1, 2, 3, 4]) == [2, 3, 4]

def test_duplicates_at_end():
    assert remove_duplicates([1, 2, 3, 4, 4]) == [1, 2, 3]

def test_duplicates_scattered():
    assert remove_duplicates([1, 2, 1, 3, 2, 4, 5]) == [3, 4, 5]

def test_negative_numbers():
    assert remove_duplicates([-1, -2, -1, 0, 1, -2]) == [0, 1]

def test_mixed_positive_and_negative():
    assert remove_duplicates([-1, 1, -1, 1, 0]) == [0]

def test_zeroes():
    assert remove_duplicates([0, 0, 0, 1, 2, 0]) == [1, 2]

def test_large_numbers():
    assert remove_duplicates([1000, 2000, 1000, 3000]) == [2000, 3000]

def test_duplicate_zero():
    assert remove_duplicates([0, 1, 0]) == [1]

def test_long_list_with_duplicates():
    numbers = [i % 10 for i in range(100)]
    expected = []
    assert remove_duplicates(numbers) == expected