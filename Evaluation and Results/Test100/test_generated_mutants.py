import pytest
from source_to_mutate import make_a_pile

def test_make_a_pile_positive_odd():
    assert make_a_pile(3) == [3, 5, 7]

def test_make_a_pile_positive_even():
    assert make_a_pile(4) == [4, 6, 8, 10]

def test_make_a_pile_one():
    assert make_a_pile(1) == [1]

def test_make_a_pile_large_number():
    assert make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

def test_make_a_pile_zero():
    assert make_a_pile(0) == []