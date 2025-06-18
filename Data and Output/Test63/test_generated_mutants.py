import pytest
from source_to_mutate import fibfib, METADATA

def test_fibfib_0():
    assert fibfib(0) == 0

def test_fibfib_1():
    assert fibfib(1) == 0

def test_fibfib_2():
    assert fibfib(2) == 1

def test_fibfib_3():
    assert fibfib(3) == 1

def test_fibfib_4():
    assert fibfib(4) == 2

def test_fibfib_5():
    assert fibfib(5) == 4

def test_fibfib_6():
    assert fibfib(6) == 7

def test_fibfib_7():
    assert fibfib(7) == 13

def test_fibfib_8():
    assert fibfib(8) == 24

def test_fibfib_9():
    assert fibfib(9) == 44

def test_fibfib_10():
    assert fibfib(10) == 81