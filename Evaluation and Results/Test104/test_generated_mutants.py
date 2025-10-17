import pytest
from source_to_mutate import unique_digits

def test_empty_list():
    assert unique_digits([]) == []

def test_no_odd_digit_elements():
    assert unique_digits([2, 4, 6, 8, 20]) == []

def test_all_odd_digit_elements():
    assert unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

def test_mixed_odd_and_even_digit_elements():
    assert unique_digits([1, 2, 3, 4, 5]) == [1, 3, 5]

def test_multiple_digit_numbers():
    assert unique_digits([11, 22, 33, 44, 55]) == [11, 33, 55]

def test_mixed_multiple_digit_numbers():
    assert unique_digits([11, 22, 33, 44, 55, 12, 34, 56]) == [11, 33, 55]

def test_example_1():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

def test_example_2():
    assert unique_digits([152, 323, 1422, 10]) == []

def test_large_numbers():
    assert unique_digits([13579, 24680, 11111, 33333]) == [11111, 13579, 33333]

def test_duplicate_numbers():
    assert unique_digits([1, 1, 1, 3, 3, 5]) == [1, 1, 1, 3, 3, 5]

def test_numbers_with_leading_zeros_represented_as_integers():
    assert unique_digits([1, 3, 5, 20, 111, 333, 123]) == [1, 3, 5, 111, 333]

def test_negative_numbers():
    with pytest.raises(ValueError):
        unique_digits([-1, -3, -5, -7, -9])

def test_zero():
    assert unique_digits([0]) == []

def test_mixed_positive_and_negative_numbers():
    with pytest.raises(ValueError):
        unique_digits([1, -2, 3, -4, 5])

def test_numbers_with_zero_as_a_digit():
    assert unique_digits([10, 30, 50, 101, 303, 505]) == []

def test_large_input_list():
    input_list = list(range(1, 100))
    expected_output = [i for i in input_list if all((int(d) % 2 == 1 for d in str(i)))]
    assert unique_digits(input_list) == expected_output