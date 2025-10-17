import pytest
from source_to_mutate import median

def test_median_odd_length():
    assert median([3, 1, 2, 4, 5]) == 3

def test_median_even_length():
    assert median([-10, 4, 6, 1000, 10, 20]) == 8.0

def test_median_empty_list():
    with pytest.raises(IndexError):
        median([])

def test_median_single_element():
    assert median([7]) == 7

def test_median_two_elements():
    assert median([1, 2]) == 1.5

def test_median_duplicate_elements():
    assert median([1, 2, 2, 3]) == 2.0

def test_median_negative_numbers():
    assert median([-5, -3, -1, -2, -4]) == -3

def test_median_mixed_positive_negative():
    assert median([-1, 0, 1]) == 0

def test_median_large_numbers():
    assert median([1000, 2000, 3000]) == 2000

def test_median_floats():
    assert median([1.0, 2.0, 3.0, 4.0]) == 2.5

def test_median_unsorted_list():
    assert median([5, 2, 1, 4, 3]) == 3

def test_median_already_sorted():
    assert median([1, 2, 3, 4, 5]) == 3

def test_median_all_same_elements():
    assert median([5, 5, 5, 5, 5]) == 5

def test_median_large_even_list():
    l = list(range(1, 1001))
    assert median(l) == 500.5