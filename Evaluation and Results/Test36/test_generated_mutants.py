import pytest
from source_to_mutate import fizz_buzz

def test_fizz_buzz_50():
    assert fizz_buzz(50) == 0

def test_fizz_buzz_78():
    assert fizz_buzz(78) == 2

def test_fizz_buzz_79():
    assert fizz_buzz(79) == 3

def test_fizz_buzz_0():
    assert fizz_buzz(0) == 0

def test_fizz_buzz_1():
    assert fizz_buzz(1) == 0

def test_fizz_buzz_11():
    assert fizz_buzz(11) == 0

def test_fizz_buzz_13():
    assert fizz_buzz(13) == 0

def test_fizz_buzz_14():
    assert fizz_buzz(14) == 0

def test_fizz_buzz_22():
    assert fizz_buzz(22) == 0

def test_fizz_buzz_26():
    assert fizz_buzz(26) == 0

def test_fizz_buzz_77():
    assert fizz_buzz(77) == 0

def test_fizz_buzz_91():
    assert fizz_buzz(91) == 3

def test_fizz_buzz_100():
    assert fizz_buzz(100) == 3

def test_fizz_buzz_143():
    assert fizz_buzz(143) == 4

def test_fizz_buzz_200():
    assert fizz_buzz(200) == 6

def test_fizz_buzz_70():
    assert fizz_buzz(70) == 0