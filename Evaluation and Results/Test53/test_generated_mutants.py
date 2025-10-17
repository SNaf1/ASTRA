import pytest
from source_to_mutate import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_positive_and_negative_numbers():
    assert add(2, -3) == -1

def test_add_zero():
    assert add(2, 0) == 2

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_add_max_int():
    import sys
    max_int = sys.maxsize
    assert add(max_int, 1) == max_int + 1

def test_add_min_int():
    import sys
    min_int = -sys.maxsize - 1
    assert add(min_int, -1) == min_int - 1