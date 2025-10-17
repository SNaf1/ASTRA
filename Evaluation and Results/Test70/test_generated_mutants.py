import pytest
from source_to_mutate import strange_sort_list

def test_empty_list():
    assert strange_sort_list([]) == []

def test_single_element_list():
    assert strange_sort_list([5]) == [5]

def test_example_1():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]

def test_example_2():
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

def test_list_with_duplicates():
    assert strange_sort_list([1, 2, 2, 3, 4, 4]) == [1, 4, 2, 4, 2, 3]

def test_list_with_negative_numbers():
    assert strange_sort_list([-1, -2, -3, -4]) == [-4, -1, -3, -2]

def test_list_with_mixed_positive_and_negative_numbers():
    assert strange_sort_list([-1, 2, -3, 4]) == [-3, 4, -1, 2]

def test_list_with_zero():
    assert strange_sort_list([0, 1, 2, 3]) == [0, 3, 1, 2]

def test_list_with_large_numbers():
    assert strange_sort_list([1000, 2000, 3000, 4000]) == [1000, 4000, 2000, 3000]

def test_list_with_same_min_and_max():
    assert strange_sort_list([1, 1, 2, 2]) == [1, 2, 1, 2]

def test_list_already_sorted():
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]

def test_list_reverse_sorted():
    assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]