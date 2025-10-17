import pytest
from source_to_mutate import fib4

def test_fib4_0():
    assert fib4(0) == 0

def test_fib4_1():
    assert fib4(1) == 0

def test_fib4_2():
    assert fib4(2) == 2

def test_fib4_3():
    assert fib4(3) == 0

def test_fib4_5():
    assert fib4(5) == 4

def test_fib4_6():
    assert fib4(6) == 8

def test_fib4_7():
    assert fib4(7) == 14

def test_fib4_8():
    assert fib4(8) == 28

def test_fib4_9():
    assert fib4(9) == 54

def test_fib4_10():
    assert fib4(10) == 104

def test_fib4_11():
    assert fib4(11) == 200

def test_fib4_12():
    assert fib4(12) == 386

def test_fib4_13():
    assert fib4(13) == 744

def test_fib4_14():
    assert fib4(14) == 1434

def test_fib4_15():
    assert fib4(15) == 2764