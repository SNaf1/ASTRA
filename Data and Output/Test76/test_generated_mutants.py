import pytest
from source_to_mutate import is_simple_power

def test_is_simple_power_1_4():
    assert is_simple_power(1, 4) == True

def test_is_simple_power_2_2():
    assert is_simple_power(2, 2) == True

def test_is_simple_power_8_2():
    assert is_simple_power(8, 2) == True

def test_is_simple_power_3_2():
    assert is_simple_power(3, 2) == False

def test_is_simple_power_3_1():
    assert is_simple_power(3, 1) == False

def test_is_simple_power_5_3():
    assert is_simple_power(5, 3) == False

def test_is_simple_power_9_3():
    assert is_simple_power(9, 3) == True

def test_is_simple_power_27_3():
    assert is_simple_power(27, 3) == True

def test_is_simple_power_1_1():
    assert is_simple_power(1, 1) == True

def test_is_simple_power_0_2():
    assert is_simple_power(0, 2) == False

def test_is_simple_power_16_2():
    assert is_simple_power(16, 2) == True

def test_is_simple_power_25_5():
    assert is_simple_power(25, 5) == True

def test_is_simple_power_125_5():
    assert is_simple_power(125, 5) == True

def test_is_simple_power_1_5():
    assert is_simple_power(1, 5) == True

def test_is_simple_power_minus_1_2():
    assert is_simple_power(-1, 2) == False

def test_is_simple_power_minus_8_minus_2():
    assert is_simple_power(-8, -2) == False

def test_is_simple_power_4_minus_2():
    assert is_simple_power(4, -2) == True

def test_is_simple_power_10_10():
    assert is_simple_power(10, 10) == True

def test_is_simple_power_100_10():
    assert is_simple_power(100, 10) == True

def test_is_simple_power_1000_10():
    assert is_simple_power(1000, 10) == True

def test_is_simple_power_10000_10():
    assert is_simple_power(10000, 10) == True

def test_is_simple_power_100000_10():
    assert is_simple_power(100000, 10) == True

def test_is_simple_power_1000000_10():
    assert is_simple_power(1000000, 10) == True

def test_is_simple_power_10000000_10():
    assert is_simple_power(10000000, 10) == True

def test_is_simple_power_100000000_10():
    assert is_simple_power(100000000, 10) == True

def test_is_simple_power_1000000000_10():
    assert is_simple_power(1000000000, 10) == True

def test_is_simple_power_10000000000_10():
    assert is_simple_power(10000000000, 10) == True

def test_is_simple_power_100000000000_10():
    assert is_simple_power(100000000000, 10) == True