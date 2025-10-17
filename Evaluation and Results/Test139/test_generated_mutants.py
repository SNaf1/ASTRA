import pytest
from source_to_mutate import special_factorial

def test_special_factorial_1():
    assert special_factorial(1) == 1

def test_special_factorial_2():
    assert special_factorial(2) == 2

def test_special_factorial_3():
    assert special_factorial(3) == 12

def test_special_factorial_4():
    assert special_factorial(4) == 288

def test_special_factorial_5():
    assert special_factorial(5) == 34560

def test_special_factorial_6():
    assert special_factorial(6) == 24883200