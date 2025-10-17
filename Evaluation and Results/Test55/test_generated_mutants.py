import pytest
from source_to_mutate import fib, METADATA

def test_fib_0():
    assert fib(0) == 0

def test_fib_1():
    assert fib(1) == 1

def test_fib_2():
    assert fib(2) == 1

def test_fib_3():
    assert fib(3) == 2

def test_fib_4():
    assert fib(4) == 3

def test_fib_5():
    assert fib(5) == 5

def test_fib_6():
    assert fib(6) == 8

def test_fib_7():
    assert fib(7) == 13

def test_fib_8():
    assert fib(8) == 21

def test_fib_9():
    assert fib(9) == 34

def test_fib_10():
    assert fib(10) == 55

def test_fib_11():
    assert fib(11) == 89

def test_fib_12():
    assert fib(12) == 144

def test_fib_13():
    assert fib(13) == 233

def test_fib_14():
    assert fib(14) == 377

def test_fib_15():
    assert fib(15) == 610

def test_fib_negative():
    with pytest.raises(RecursionError):
        fib(-1)