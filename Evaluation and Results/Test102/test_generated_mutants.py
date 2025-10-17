import pytest
from source_to_mutate import choose_num

def test_choose_num_x_greater_than_y():
    assert choose_num(13, 12) == -1

def test_choose_num_y_is_even():
    assert choose_num(12, 15) == 14

def test_choose_num_y_is_odd():
    assert choose_num(1, 5) == 4

def test_choose_num_x_equals_y_and_even():
    assert choose_num(4, 4) == 4

def test_choose_num_x_equals_y_and_odd():
    assert choose_num(5, 5) == -1

def test_choose_num_no_even_number_in_range():
    assert choose_num(1, 1) == -1

def test_choose_num_small_range_with_even():
    assert choose_num(2, 3) == 2

def test_choose_num_small_range_no_even():
    assert choose_num(3, 3) == -1

def test_choose_num_large_range():
    assert choose_num(100, 200) == 200

def test_choose_num_x_is_even_y_is_odd():
    assert choose_num(2, 5) == 4

def test_choose_num_x_is_odd_y_is_even():
    assert choose_num(3, 6) == 6

def test_choose_num_x_close_to_y_even():
    assert choose_num(5, 6) == 6

def test_choose_num_x_close_to_y_odd():
    assert choose_num(4, 5) == 4

def test_choose_num_negative_x_positive_y():
    assert choose_num(-2, 5) == 4

def test_choose_num_negative_x_negative_y():
    assert choose_num(-5, -2) == -2

def test_choose_num_zero_x_positive_y():
    assert choose_num(0, 5) == 4

def test_choose_num_zero_x_zero_y():
    assert choose_num(0, 0) == 0

def test_choose_num_x_is_zero_y_is_one():
    assert choose_num(0, 1) == 0

def test_choose_num_x_is_one_y_is_zero():
    assert choose_num(1, 0) == -1