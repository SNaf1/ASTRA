import pytest
from source_to_mutate import fruit_distribution

def test_fruit_distribution_example_1():
    assert fruit_distribution('5 apples and 6 oranges', 19) == 8

def test_fruit_distribution_example_2():
    assert fruit_distribution('0 apples and 1 oranges', 3) == 2

def test_fruit_distribution_example_3():
    assert fruit_distribution('2 apples and 3 oranges', 100) == 95

def test_fruit_distribution_example_4():
    assert fruit_distribution('100 apples and 1 oranges', 120) == 19

def test_fruit_distribution_zero_apples_oranges():
    assert fruit_distribution('0 apples and 0 oranges', 5) == 5

def test_fruit_distribution_large_numbers():
    assert fruit_distribution('1000 apples and 2000 oranges', 5000) == 2000

def test_fruit_distribution_same_number_apples_oranges():
    assert fruit_distribution('5 apples and 5 oranges', 15) == 5

def test_fruit_distribution_only_apples():
    assert fruit_distribution('5 apples and 0 oranges', 10) == 5

def test_fruit_distribution_only_oranges():
    assert fruit_distribution('0 apples and 5 oranges', 10) == 5

def test_fruit_distribution_no_apples_oranges_mentioned():
    assert fruit_distribution('apples and oranges', 10) == 10

def test_fruit_distribution_multiple_spaces():
    assert fruit_distribution('5  apples  and  6  oranges', 19) == 8

def test_fruit_distribution_numbers_at_start_and_end():
    assert fruit_distribution('1 apples and 2 oranges', 10) == 7

def test_fruit_distribution_negative_total_fruits():
    assert fruit_distribution('5 apples and 6 oranges', -19) == -30

def test_fruit_distribution_decimal_numbers_in_string():
    assert fruit_distribution('5.5 apples and 6.5 oranges', 19) == 19

def test_fruit_distribution_non_integer_total_fruits():
    assert fruit_distribution('5 apples and 6 oranges', 19.5) == 8.5