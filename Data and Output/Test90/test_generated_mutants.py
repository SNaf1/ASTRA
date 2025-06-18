import pytest
from source_to_mutate import next_smallest

def test_empty_list():
    assert next_smallest([]) is None

def test_single_element_list():
    assert next_smallest([1]) is None

def test_two_distinct_elements():
    assert next_smallest([1, 2]) == 2

def test_two_identical_elements():
    assert next_smallest([1, 1]) is None

def test_multiple_distinct_elements():
    assert next_smallest([1, 2, 3, 4, 5]) == 2

def test_multiple_elements_unsorted():
    assert next_smallest([5, 1, 4, 3, 2]) == 2

def test_multiple_elements_with_duplicates():
    assert next_smallest([1, 2, 2, 3, 4, 5]) == 2

def test_multiple_elements_with_multiple_duplicates():
    assert next_smallest([1, 2, 2, 3, 3, 3, 4, 5]) == 2

def test_negative_numbers():
    assert next_smallest([-1, -2, -3, -4, -5]) == -4

def test_mixed_positive_and_negative_numbers():
    assert next_smallest([-1, 2, -3, 4, -5]) == -3

def test_zero_in_list():
    assert next_smallest([0, 1, 2, 3]) == 1

def test_all_zeros():
    assert next_smallest([0, 0, 0]) is None

def test_large_numbers():
    assert next_smallest([1000, 2000, 3000]) == 2000

def test_duplicate_smallest_number():
    assert next_smallest([1, 1, 2, 3]) == 2

def test_duplicate_second_smallest_number():
    assert next_smallest([1, 2, 2, 3]) == 2

def test_list_with_same_number():
    assert next_smallest([5, 5, 5, 5]) is None