import pytest
from source_to_mutate import make_a_pile, check

def test_make_a_pile_3():
    assert make_a_pile(3) == [3, 5, 7]

def test_make_a_pile_4():
    assert make_a_pile(4) == [4, 6, 8, 10]

def test_make_a_pile_5():
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

def test_make_a_pile_6():
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]

def test_make_a_pile_8():
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]

def test_make_a_pile_1():
    assert make_a_pile(1) == [1]

def test_make_a_pile_2():
    assert make_a_pile(2) == [2, 4]

def test_make_a_pile_7():
    assert make_a_pile(7) == [7, 9, 11, 13, 15, 17, 19]

def test_make_a_pile_9():
    assert make_a_pile(9) == [9, 11, 13, 15, 17, 19, 21, 23, 25]

def test_make_a_pile_10():
    assert make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]