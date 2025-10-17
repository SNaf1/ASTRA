import pytest
from source_to_mutate import pluck

def test_empty_array():
    assert pluck([]) == []

def test_no_even_numbers():
    assert pluck([1, 3, 5]) == []

def test_single_even_number():
    assert pluck([2]) == [2, 0]

def test_multiple_even_numbers():
    assert pluck([4, 2, 6]) == [2, 1]

def test_even_and_odd_numbers():
    assert pluck([1, 2, 3, 4, 5]) == [2, 1]

def test_smallest_even_at_start():
    assert pluck([2, 4, 6]) == [2, 0]

def test_smallest_even_at_end():
    assert pluck([4, 6, 2]) == [2, 2]

def test_multiple_smallest_even_numbers():
    assert pluck([0, 2, 0, 4]) == [0, 0]

def test_zero_as_smallest_even():
    assert pluck([1, 0, 3, 2]) == [0, 1]

def test_large_array_with_even_numbers():
    assert pluck([1, 3, 5, 2, 4, 6, 8, 0]) == [0, 7]

def test_large_array_no_even_numbers():
    assert pluck([1, 3, 5, 7, 9, 11, 13]) == []

def test_duplicate_even_numbers_smallest_index():
    assert pluck([4, 2, 3, 2]) == [2, 1]

def test_all_same_even_numbers():
    assert pluck([2, 2, 2, 2]) == [2, 0]

def test_negative_numbers():
    assert pluck([-2, -4, -6]) == [-6, 2]

def test_zero_only():
    assert pluck([0]) == [0, 0]

def test_zero_multiple():
    assert pluck([0, 0, 0]) == [0, 0]

def test_zero_and_other_even():
    assert pluck([2, 0, 4]) == [0, 1]

def test_zero_and_other_even_reverse():
    assert pluck([4, 0, 2]) == [0, 1]

def test_zero_and_odd():
    assert pluck([1, 0, 3]) == [0, 1]

def test_even_at_end_with_zero():
    assert pluck([1, 3, 0, 2]) == [0, 2]

def test_even_at_start_with_zero():
    assert pluck([2, 0, 1, 3]) == [0, 1]