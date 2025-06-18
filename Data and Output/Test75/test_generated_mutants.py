import pytest
from source_to_mutate import is_multiply_prime

def test_is_multiply_prime_true():
    assert is_multiply_prime(30) == True

def test_is_multiply_prime_false():
    assert is_multiply_prime(2) == False

def test_is_multiply_prime_large_number():
    assert is_multiply_prime(99) == True

def test_is_multiply_prime_prime_number():
    assert is_multiply_prime(7) == False

def test_is_multiply_prime_one():
    assert is_multiply_prime(1) == False

def test_is_multiply_prime_zero():
    assert is_multiply_prime(0) == False

def test_is_multiply_prime_negative():
    assert is_multiply_prime(-30) == False

def test_is_multiply_prime_8():
    assert is_multiply_prime(8) == True

def test_is_multiply_prime_10():
    assert is_multiply_prime(10) == False

def test_is_multiply_prime_42():
    assert is_multiply_prime(42) == True

def test_is_multiply_prime_66():
    assert is_multiply_prime(66) == True

def test_is_multiply_prime_70():
    assert is_multiply_prime(70) == True

def test_is_multiply_prime_78():
    assert is_multiply_prime(78) == True

def test_is_multiply_prime_105():
    assert is_multiply_prime(105) == True

def test_is_multiply_prime_130():
    assert is_multiply_prime(130) == True

def test_is_multiply_prime_110():
    assert is_multiply_prime(110) == True

def test_is_multiply_prime_114():
    assert is_multiply_prime(114) == True

def test_is_multiply_prime_154():
    assert is_multiply_prime(154) == True