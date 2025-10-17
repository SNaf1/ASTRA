import pytest
from source_to_mutate import smallest_change

def test_empty_array():
    assert smallest_change([]) == 0

def test_single_element_array():
    assert smallest_change([1]) == 0

def test_palindrome_array():
    assert smallest_change([1, 2, 3, 2, 1]) == 0

def test_non_palindrome_array():
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4

def test_non_palindrome_array_2():
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1

def test_even_length_palindrome():
    assert smallest_change([1, 2, 2, 1]) == 0

def test_even_length_non_palindrome():
    assert smallest_change([1, 2, 3, 4]) == 2

def test_odd_length_non_palindrome():
    assert smallest_change([1, 2, 3, 4, 5]) == 2

def test_array_with_duplicates():
    assert smallest_change([1, 2, 2, 2, 1]) == 0

def test_array_with_all_same_elements():
    assert smallest_change([1, 1, 1, 1, 1]) == 0

def test_array_with_two_elements_different():
    assert smallest_change([1, 2]) == 1

def test_array_with_three_elements_non_palindrome():
    assert smallest_change([1, 2, 3]) == 1

def test_array_with_three_elements_palindrome():
    assert smallest_change([1, 2, 1]) == 0

def test_array_with_negative_numbers():
    assert smallest_change([-1, -2, -3, -2, -1]) == 0

def test_array_with_mixed_numbers():
    assert smallest_change([1, -2, 3, -2, 1]) == 0

def test_array_with_large_numbers():
    assert smallest_change([1000, 2000, 3000, 2000, 1000]) == 0

def test_array_with_large_numbers_non_palindrome():
    assert smallest_change([1000, 2000, 3000, 4000, 5000]) == 2

def test_array_with_zeroes():
    assert smallest_change([0, 0, 0, 0, 0]) == 0

def test_array_with_zeroes_non_palindrome():
    assert smallest_change([0, 1, 0, 1, 0]) == 0