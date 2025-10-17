import pytest
from source_to_mutate import add_elements

def test_add_elements_empty_array():
    arr = []
    k = 0
    assert add_elements(arr, k) == 0

def test_add_elements_k_greater_than_array_length():
    arr = [1, 2, 3]
    k = 4
    assert add_elements(arr, k) == 6

def test_add_elements_k_equals_array_length():
    arr = [1, 2, 3]
    k = 3
    assert add_elements(arr, k) == 6

def test_add_elements_k_less_than_array_length():
    arr = [1, 2, 3, 4, 5]
    k = 2
    assert add_elements(arr, k) == 3

def test_add_elements_no_two_digit_elements():
    arr = [100, 1000, 10000]
    k = 3
    assert add_elements(arr, k) == 0

def test_add_elements_all_two_digit_elements():
    arr = [10, 20, 30]
    k = 3
    assert add_elements(arr, k) == 60

def test_add_elements_mixed_elements():
    arr = [1, 10, 100, 1000]
    k = 4
    assert add_elements(arr, k) == 11

def test_add_elements_negative_numbers():
    arr = [-1, -10, -100]
    k = 3
    assert add_elements(arr, k) == -1

def test_add_elements_zero():
    arr = [0, 10, 100]
    k = 3
    assert add_elements(arr, k) == 10

def test_add_elements_large_numbers():
    arr = [99, 100, 999]
    k = 3
    assert add_elements(arr, k) == 99

def test_add_elements_single_element_two_digits():
    arr = [55]
    k = 1
    assert add_elements(arr, k) == 55

def test_add_elements_single_element_three_digits():
    arr = [555]
    k = 1
    assert add_elements(arr, k) == 0

def test_add_elements_single_element_one_digit():
    arr = [5]
    k = 1
    assert add_elements(arr, k) == 5

def test_add_elements_k_is_one():
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 1
    assert add_elements(arr, k) == 0

def test_add_elements_example():
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 4
    assert add_elements(arr, k) == 24

def test_add_elements_all_single_digit():
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert add_elements(arr, k) == 15

def test_add_elements_all_same_number():
    arr = [11, 11, 11, 11, 11]
    k = 5
    assert add_elements(arr, k) == 55

def test_add_elements_mixed_positive_and_negative():
    arr = [1, -10, 100, -1000, 20]
    k = 5
    assert add_elements(arr, k) == 21