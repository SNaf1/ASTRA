import pytest
from source_to_mutate import double_the_difference, check

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_and_even():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_negative_numbers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_positive_and_negative():
    assert double_the_difference([9, -2]) == 81

def test_zero():
    assert double_the_difference([0]) == 0

def test_mixed_positive_negative_and_zero():
    assert double_the_difference([-1, -2, 8]) == 0

def test_float_and_integers():
    assert double_the_difference([0.2, 3, 5]) == 34

def test_large_list_odd_numbers():
    lst = list(range(-99, 100, 2))
    odd_sum = sum([i**2 for i in lst if i > 0])
    assert double_the_difference(lst) == odd_sum

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_only_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_odd_and_even_positive_and_negative():
    assert double_the_difference([-1, 2, 3, -4, 5]) == 34

def test_floats_only():
    assert double_the_difference([1.5, 2.5, 3.5]) == 0

def test_string_input():
    with pytest.raises(TypeError):
        double_the_difference(["1", "2", "3"])

def test_mixed_string_and_int():
    with pytest.raises(TypeError):
        double_the_difference([1, "2", 3])

def test_large_numbers():
    assert double_the_difference([1000, 1001]) == 1001**2

def test_duplicate_numbers():
    assert double_the_difference([1, 1, 1]) == 3

def test_negative_odd_numbers():
    assert double_the_difference([-1, -3, -5]) == 0