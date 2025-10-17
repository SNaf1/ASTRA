import pytest
from source_to_mutate import modp

def test_modp_3_5():
    assert modp(3, 5) == 3

def test_modp_1101_101():
    assert modp(1101, 101) == 2

def test_modp_0_101():
    assert modp(0, 101) == 1

def test_modp_3_11():
    assert modp(3, 11) == 8

def test_modp_100_101():
    assert modp(100, 101) == 1

def test_modp_1_2():
    assert modp(1, 2) == 0

def test_modp_2_2():
    assert modp(2, 2) == 0

def test_modp_10_3():
    assert modp(10, 3) == 1

def test_modp_10_1024():
    assert modp(10, 1024) == 0

def test_modp_1024_1024():
    assert modp(1024, 1024) == 0

def test_modp_1_1():
    assert modp(1, 1) == 0

def test_modp_0_1():
    assert modp(0, 1) == 1

def test_modp_2_1():
    assert modp(2, 1) == 0

def test_modp_1000_10000():
    assert modp(1000, 10000) == 9376

def test_modp_1000_1001():
    assert modp(1000, 1001) == 562