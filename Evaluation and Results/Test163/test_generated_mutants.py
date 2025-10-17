import pytest
from source_to_mutate import generate_integers

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_same_number_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_same_number_odd():
    assert generate_integers(5, 5) == []

def test_generate_integers_one_even_one_odd_ascending():
    assert generate_integers(3, 6) == [4, 6]

def test_generate_integers_one_even_one_odd_descending():
    assert generate_integers(6, 3) == [4, 6]

def test_generate_integers_lower_than_2():
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_greater_than_8():
    assert generate_integers(5, 9) == [6, 8]

def test_generate_integers_both_greater_than_8():
    assert generate_integers(10, 12) == []

def test_generate_integers_both_less_than_2():
    assert generate_integers(0, 1) == []

def test_generate_integers_negative_numbers():
    assert generate_integers(-5, -1) == []

def test_generate_integers_one_negative_one_positive():
    assert generate_integers(-2, 4) == [2, 4]

def test_generate_integers_large_range():
    assert generate_integers(1, 100) == [2, 4, 6, 8]

def test_generate_integers_a_equals_2():
    assert generate_integers(2, 5) == [2, 4]

def test_generate_integers_b_equals_8():
    assert generate_integers(5, 8) == [6, 8]

def test_generate_integers_a_equals_8():
    assert generate_integers(8, 5) == [6, 8]

def test_generate_integers_b_equals_2():
    assert generate_integers(5, 2) == [2, 4]