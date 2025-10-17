import pytest
from source_to_mutate import largest_divisor

def test_largest_divisor_15():
    assert largest_divisor(15) == 5

def test_largest_divisor_7():
    assert largest_divisor(7) == 1

def test_largest_divisor_2():
    assert largest_divisor(2) == 1

def test_largest_divisor_4():
    assert largest_divisor(4) == 2

def test_largest_divisor_100():
    assert largest_divisor(100) == 50

def test_largest_divisor_1():
    with pytest.raises(ZeroDivisionError):
        largest_divisor(1)