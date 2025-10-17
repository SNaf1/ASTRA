import pytest
from source_to_mutate import maximum

def test_maximum_empty_array():
    arr = []
    k = 0
    assert maximum(arr, k) == []

def test_maximum_k_0():
    arr = [1, 2, 3]
    k = 0
    assert maximum(arr, k) == []

def test_maximum_k_equals_length():
    arr = [1, 2, 3]
    k = 3
    assert maximum(arr, k) == [1, 2, 3]

def test_maximum_k_less_than_length():
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    k = 3
    assert maximum(arr, k) == [5, 6, 9]

def test_maximum_negative_numbers():
    arr = [-3, -4, 5]
    k = 3
    assert maximum(arr, k) == [-4, -3, 5]

def test_maximum_duplicate_numbers():
    arr = [4, -4, 4]
    k = 2
    assert maximum(arr, k) == [4, 4]

def test_maximum_mixed_numbers():
    arr = [-3, 2, 1, 2, -1, -2, 1]
    k = 1
    assert maximum(arr, k) == [2]

def test_maximum_single_element():
    arr = [5]
    k = 1
    assert maximum(arr, k) == [5]

def test_maximum_single_element_k_0():
    arr = [5]
    k = 0
    assert maximum(arr, k) == []

def test_maximum_all_same_numbers():
    arr = [7, 7, 7, 7]
    k = 2
    assert maximum(arr, k) == [7, 7]

def test_maximum_large_array():
    arr = list(range(-500, 500))
    k = 10
    assert maximum(arr, k) == list(range(490, 500))

def test_maximum_k_1():
    arr = [1, 5, 2, 8, 3]
    k = 1
    assert maximum(arr, k) == [8]

def test_maximum_k_equals_len_minus_1():
    arr = [1, 5, 2, 8, 3]
    k = 4
    assert maximum(arr, k) == [2, 3, 5, 8]