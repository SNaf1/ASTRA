import pytest
from source_to_mutate import sum_squares

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_positive_integers():
    assert sum_squares([1, 2, 3]) == 14

def test_sum_squares_positive_integers_2():
    assert sum_squares([1, 4, 9]) == 98

def test_sum_squares_positive_integers_3():
    assert sum_squares([1, 3, 5, 7]) == 84

def test_sum_squares_positive_floats():
    assert sum_squares([1.4, 4.2, 0]) == 29

def test_sum_squares_negative_floats_and_integers():
    assert sum_squares([-2.4, 1, 1]) == 6

def test_sum_squares_mixed_positive_and_negative_integers():
    assert sum_squares([-1, 2, -3]) == 14

def test_sum_squares_mixed_positive_and_negative_floats():
    assert sum_squares([-1.5, 2.5, -3.5]) == 19

def test_sum_squares_zeroes():
    assert sum_squares([0, 0, 0]) == 0

def test_sum_squares_large_numbers():
    assert sum_squares([100, 200, 300]) == 140000

def test_sum_squares_negative_integers():
    assert sum_squares([-1, -2, -3]) == 14

def test_sum_squares_single_element():
    assert sum_squares([5]) == 25

def test_sum_squares_single_float():
    assert sum_squares([5.5]) == 36

def test_sum_squares_single_negative_integer():
    assert sum_squares([-5]) == 25

def test_sum_squares_single_negative_float():
    assert sum_squares([-5.5]) == 25

def test_sum_squares_all_negative_floats():
    assert sum_squares([-1.1, -2.2, -3.3]) == 14

def test_sum_squares_all_positive_floats():
    assert sum_squares([1.1, 2.2, 3.3]) == 29

def test_sum_squares_large_floats():
    assert sum_squares([100.5, 200.5, 300.5]) == 141203