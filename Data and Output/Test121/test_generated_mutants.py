import pytest
from source_to_mutate import solution

def test_empty_list():
    assert solution([]) == 0

def test_single_element_odd_at_even_index():
    assert solution([5]) == 5

def test_single_element_even_at_even_index():
    assert solution([4]) == 0

def test_odd_at_even_indices():
    assert solution([5, 8, 7, 1]) == 12

def test_all_odd_elements_at_even_indices():
    assert solution([3, 3, 3, 3, 3]) == 9

def test_even_at_even_indices():
    assert solution([30, 13, 24, 321]) == 0

def test_mixed_odd_and_even_at_even_indices():
    assert solution([3, 4, 5, 6, 7, 8]) == 15

def test_long_list():
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25

def test_negative_numbers():
    assert solution([-1, 2, -3, 4, -5, 6]) == -9

def test_zero_in_list():
    assert solution([0, 1, 0, 1, 0, 1]) == 0

def test_large_numbers():
    assert solution([1001, 2, 3003, 4]) == 4004

def test_all_even_length_2():
    assert solution([2,4]) == 0

def test_all_odd_length_2():
    assert solution([1,3]) == 1

def test_mixed_length_2():
    assert solution([1,4]) == 1