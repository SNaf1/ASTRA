import pytest
from source_to_mutate import get_odd_collatz

def test_get_odd_collatz_1():
    assert get_odd_collatz(1) == [1]

def test_get_odd_collatz_5():
    assert get_odd_collatz(5) == [1, 5]

def test_get_odd_collatz_6():
    assert get_odd_collatz(6) == [1, 3, 5]

def test_get_odd_collatz_7():
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]

def test_get_odd_collatz_8():
    assert get_odd_collatz(8) == [1]

def test_get_odd_collatz_9():
    assert get_odd_collatz(9) == [1, 5, 7, 9, 11, 13, 17]

def test_get_odd_collatz_10():
    assert get_odd_collatz(10) == [1, 5]

def test_get_odd_collatz_11():
    assert get_odd_collatz(11) == [1, 5, 11, 13, 17]

def test_get_odd_collatz_12():
    assert get_odd_collatz(12) == [1, 3, 5]

def test_get_odd_collatz_13():
    assert get_odd_collatz(13) == [1, 5, 13]

def test_get_odd_collatz_14():
    assert get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]

def test_get_odd_collatz_15():
    assert get_odd_collatz(15) == [1, 5, 15, 23, 35, 53]

def test_get_odd_collatz_16():
    assert get_odd_collatz(16) == [1]

def test_get_odd_collatz_17():
    assert get_odd_collatz(17) == [1, 5, 13, 17]

def test_get_odd_collatz_18():
    assert get_odd_collatz(18) == [1, 5, 7, 9, 11, 13, 17]

def test_get_odd_collatz_19():
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]

def test_get_odd_collatz_20():
    assert get_odd_collatz(20) == [1, 5]