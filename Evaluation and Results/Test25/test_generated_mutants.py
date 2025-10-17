import pytest
from source_to_mutate import factorize

def test_factorize_8():
    assert factorize(8) == [2, 2, 2]

def test_factorize_25():
    assert factorize(25) == [5, 5]

def test_factorize_70():
    assert factorize(70) == [2, 5, 7]

def test_factorize_1():
    assert factorize(1) == []

def test_factorize_2():
    assert factorize(2) == [2]

def test_factorize_3():
    assert factorize(3) == [3]

def test_factorize_4():
    assert factorize(4) == [2, 2]

def test_factorize_9():
    assert factorize(9) == [3, 3]

def test_factorize_16():
    assert factorize(16) == [2, 2, 2, 2]

def test_factorize_27():
    assert factorize(27) == [3, 3, 3]

def test_factorize_32():
    assert factorize(32) == [2, 2, 2, 2, 2]

def test_factorize_64():
    assert factorize(64) == [2, 2, 2, 2, 2, 2]

def test_factorize_100():
    assert factorize(100) == [2, 2, 5, 5]

def test_factorize_121():
    assert factorize(121) == [11, 11]

def test_factorize_144():
    assert factorize(144) == [2, 2, 2, 2, 3, 3]

def test_factorize_169():
    assert factorize(169) == [13, 13]

def test_factorize_196():
    assert factorize(196) == [2, 2, 7, 7]

def test_factorize_225():
    assert factorize(225) == [3, 3, 5, 5]

def test_factorize_360():
    assert factorize(360) == [2, 2, 2, 3, 3, 5]

def test_factorize_large_prime():
    assert factorize(997) == [997]

def test_factorize_large_composite():
    assert factorize(1319500) == [2, 2, 5, 5, 5, 7, 13, 29]