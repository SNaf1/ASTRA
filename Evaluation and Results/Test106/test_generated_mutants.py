import pytest
from source_to_mutate import f

def test_f_empty():
    assert f(0) == []

def test_f_one():
    assert f(1) == [1]

def test_f_two():
    assert f(2) == [1, 2]

def test_f_three():
    assert f(3) == [1, 2, 6]

def test_f_four():
    assert f(4) == [1, 2, 6, 24]

def test_f_five():
    assert f(5) == [1, 2, 6, 24, 15]

def test_f_six():
    assert f(6) == [1, 2, 6, 24, 15, 720]

def test_f_seven():
    assert f(7) == [1, 2, 6, 24, 15, 720, 28]

def test_f_ten():
    assert f(10) == [1, 2, 6, 24, 15, 720, 28, 40320, 45, 3628800]