import pytest
from source_to_mutate import is_prime

def test_is_prime_6():
    assert is_prime(6) == False

def test_is_prime_101():
    assert is_prime(101) == True

def test_is_prime_11():
    assert is_prime(11) == True

def test_is_prime_13441():
    assert is_prime(13441) == True

def test_is_prime_61():
    assert is_prime(61) == True

def test_is_prime_4():
    assert is_prime(4) == False

def test_is_prime_1():
    assert is_prime(1) == False

def test_is_prime_2():
    assert is_prime(2) == True

def test_is_prime_3():
    assert is_prime(3) == True

def test_is_prime_0():
    assert is_prime(0) == False

def test_is_prime_negative():
    assert is_prime(-1) == False

def test_is_prime_large_prime():
    assert is_prime(997) == True

def test_is_prime_large_composite():
    assert is_prime(999) == False