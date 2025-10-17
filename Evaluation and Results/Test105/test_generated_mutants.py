import pytest
from source_to_mutate import by_length

def test_empty_array():
    arr = []
    expected = []
    assert by_length(arr) == expected

def test_example_array():
    arr = [2, 1, 1, 4, 5, 8, 2, 3]
    expected = ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    assert by_length(arr) == expected

def test_array_with_strange_numbers():
    arr = [1, -1, 55]
    expected = ['One']
    assert by_length(arr) == expected

def test_array_with_only_strange_numbers():
    arr = [-1, 55, 10]
    expected = []
    assert by_length(arr) == expected

def test_array_with_duplicates():
    arr = [1, 1, 1, 1, 1]
    expected = ['One', 'One', 'One', 'One', 'One']
    assert by_length(arr) == expected

def test_array_with_all_numbers_1_to_9():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
    assert by_length(arr) == expected

def test_array_with_mixed_numbers():
    arr = [1, 5, 10, 3, -2, 7]
    expected = ['Seven', 'Five', 'Three', 'One']
    assert by_length(arr) == expected

def test_array_with_zero():
    arr = [0, 1, 2]
    expected = ['Two', 'One']
    assert by_length(arr) == expected

def test_array_with_large_numbers_and_valid_numbers():
    arr = [100, 5, 200, 1, 9]
    expected = ['Nine', 'Five', 'One']
    assert by_length(arr) == expected

def test_array_with_negative_and_valid_numbers():
    arr = [-5, 3, 1, -10, 8]
    expected = ['Eight', 'Three', 'One']
    assert by_length(arr) == expected

def test_array_with_only_one_valid_number():
    arr = [10, 11, 5]
    expected = ['Five']
    assert by_length(arr) == expected

def test_array_with_only_one_number():
    arr = [7]
    expected = ['Seven']
    assert by_length(arr) == expected

def test_array_with_same_number_multiple_times_and_invalid_numbers():
    arr = [1, 1, 1, 10, -5, 1]
    expected = ['One', 'One', 'One', 'One']
    assert by_length(arr) == expected